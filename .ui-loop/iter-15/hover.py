from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path(".ui-loop/iter-15/shots")
with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1).new_page()
    page.goto("http://127.0.0.1:5500/labsa-90.html", wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(400)
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
    page.locator("#faq").scroll_into_view_if_needed()
    page.wait_for_timeout(200)
    page.locator(".faq details").first.locator("summary").click()
    page.wait_for_timeout(200)
    page.locator(".faq").first.screenshot(path=str(out / "faq_open.png"))
    page.locator(".apps").first.screenshot(path=str(out / "apps.png"))
    page.locator(".traits").first.screenshot(path=str(out / "traits.png"))
    b.close()
print("hover ok")
