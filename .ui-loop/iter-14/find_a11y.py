from playwright.sync_api import sync_playwright
import json

JS = r"""
() => {
  const isVisible = (el) => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || parseFloat(cs.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const named = (el) => {
    if (el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || el.getAttribute('title')) return true;
    if (el.textContent.trim().length > 0) return true;
    if (el.querySelector('img[alt]:not([alt=""])')) return true;
    if (el.tagName === 'INPUT' && (el.labels && el.labels.length || el.placeholder)) return true;
    return false;
  };
  const inter = Array.from(document.querySelectorAll('a[href], button, input, select, textarea, [role=button]')).filter(isVisible);
  const unnamed = inter.filter(e => !named(e)).map(el => ({
    tag: el.tagName, id: el.id, name: el.name, type: el.type, cls: el.className,
    html: el.outerHTML.slice(0, 220), labels: el.labels && el.labels.length
  }));
  const tiny = [];
  for (const el of inter) {
    const cs = getComputedStyle(el);
    if (el.tagName === 'A' && cs.display === 'inline' && el.closest('p, li')) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 24 || r.height < 24) tiny.push({
      tag: el.tagName, id: el.id, cls: el.className, w: r.width, h: r.height,
      html: el.outerHTML.slice(0, 180)
    });
  }
  return {unnamed, tiny, inter: inter.length};
}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_context(viewport={"width": 1440, "height": 900}).new_page()
    page = b.new_context(viewport={"width": 375, "height": 812}).new_page()
    page.goto("http://127.0.0.1:8765/contact.html", wait_until="networkidle")
    page.wait_for_timeout(600)
    print(json.dumps(page.evaluate(JS), indent=2))
    b.close()
