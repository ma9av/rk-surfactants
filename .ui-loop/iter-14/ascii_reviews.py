from pathlib import Path

for name in ["art_director.json", "systems_designer.json", "typographer.json"]:
    p = Path(".ui-loop/iter-14/reviews") / name
    t = p.read_text(encoding="utf-8")
    t = (
        t.replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2014", "--")
        .replace("\u2013", "-")
        .replace("\u00b7", "-")
        .replace("\u2026", "...")
    )
    p.write_text(t, encoding="ascii", errors="replace")
    p.read_text()  # default encoding check
    print(name, "ok")
