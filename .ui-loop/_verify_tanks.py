from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path(".ui-loop/verify-tanks")
out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto("http://127.0.0.1:8765/manufacturing.html", wait_until="networkidle", timeout=20000)
    page.wait_for_timeout(800)
    page.screenshot(path=str(out / "mfg_fold.png"))
    page.evaluate("window.scrollTo(0, 420)")
    page.wait_for_timeout(400)
    page.screenshot(path=str(out / "mfg_tanks.png"))
    page.goto("http://127.0.0.1:8765/index.html", wait_until="networkidle", timeout=20000)
    page.wait_for_timeout(600)
    page.evaluate("document.getElementById('plant').scrollIntoView()")
    page.wait_for_timeout(500)
    page.screenshot(path=str(out / "index_plant.png"))
    ctx.close()
    b.close()
print("ok")
