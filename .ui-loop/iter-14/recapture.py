from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

out = Path(".ui-loop/iter-14/shots")
out.mkdir(parents=True, exist_ok=True)
sections = out / "sections"
sections.mkdir(exist_ok=True)


def settle(page):
    h = page.evaluate("document.documentElement.scrollHeight")
    vh = page.evaluate("window.innerHeight")
    y = 0
    while y < h:
        page.evaluate(f"window.scrollTo(0, {y})")
        page.wait_for_timeout(200)
        y += max(vh // 2, 300)
        h = page.evaluate("document.documentElement.scrollHeight")
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1500)


def slice_image(src, out_dir, height=1100):
    im = Image.open(src)
    w, h = im.size
    n = 0
    y = 0
    while y < h and n < 20:
        n += 1
        im.crop((0, y, w, min(y + height, h))).save(out_dir / f"desktop_s{n:02d}.png")
        y += height


with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto("http://127.0.0.1:8765/contact.html", wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(800)
    page.screenshot(path=str(out / "desktop_fold.png"))
    settle(page)
    page.locator(".place-map").first.scroll_into_view_if_needed()
    page.wait_for_timeout(2500)
    page.locator(".place-map").first.screenshot(path=str(out / "factory_map.png"))
    page.locator(".place-map").nth(1).screenshot(path=str(out / "office_map.png"))
    page.locator(".enquiry .note").first.screenshot(path=str(out / "disclaimer.png"))
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(400)
    page.screenshot(path=str(out / "desktop_full.png"), full_page=True)
    btn = page.locator(".nav a.btn").first
    box = btn.bounding_box()
    btn.hover()
    page.wait_for_timeout(350)
    page.screenshot(
        path=str(out / "hover.png"),
        clip={
            "x": max(box["x"] - 40, 0),
            "y": max(box["y"] - 40, 0),
            "width": min(box["width"] + 80, 400),
            "height": box["height"] + 80,
        },
    )
    page.keyboard.press("Tab")
    page.wait_for_timeout(250)
    page.screenshot(
        path=str(out / "focus.png"),
        clip={
            "x": max(box["x"] - 40, 0),
            "y": max(box["y"] - 40, 0),
            "width": min(box["width"] + 80, 400),
            "height": box["height"] + 80,
        },
    )
    ctx.close()

    for name, w, h in (("tablet", 768, 1024), ("mobile", 375, 812)):
        c = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1)
        pg = c.new_page()
        pg.goto("http://127.0.0.1:8765/contact.html", wait_until="networkidle", timeout=30000)
        settle(pg)
        pg.wait_for_timeout(1500)
        pg.screenshot(path=str(out / f"{name}_full.png"), full_page=True)
        c.close()
    b.close()

slice_image(out / "desktop_full.png", sections)
print("recapture ok")
