from pathlib import Path
import re

p = Path(__file__).with_name("index.html")
t = p.read_text(encoding="utf-8")
t2, n = re.subn(
    r"\n\s*<div class=\"reel-nav\">.*?</div>\n",
    "\n",
    t,
    count=1,
    flags=re.S,
)
if n != 1:
    raise SystemExit(f"reel-nav replace failed: {n}")
t2 = t2.replace("styles.css?v=20261115e", "styles.css?v=20261115f")
t2 = t2.replace("main.js?v=20261115e", "main.js?v=20261115f")
p.write_text(t2, encoding="utf-8")
print("index patched")
