"""Brand colour grade for site photography.

Run from the project root:  python .ui-loop/grade_photos.py
Originals are kept in .ui-loop/img-originals and every run grades from them,
so the script is safe to re-run after tweaking the parameters.
"""
import os, re, shutil, glob
import numpy as np
from PIL import Image, ImageOps

IMG = 'assets/img'
ORIG = '.ui-loop/img-originals'

# per-photo overrides: target mean luma, white-balance strength, shadow tint strength
SETS = {
    'tank-labsa':        dict(),
    'tank-red':          dict(),
    'tanker-rkspl':      dict(),
    'plant-team':        dict(wb=.45),
    'plant-wide':        dict(),
    'lab':               dict(target=.55),
    'process-tanks':     dict(target=.47, wb=.3, src='process-tanks.jpg'),
    'labsa-sample-tube': dict(target=.70, tint=.35, sat=.9, src='labsa-sample-tube.jpg'),
}

LUMA = np.array([.2126, .7152, .0722], np.float32)
SHADOW_TINT = np.array([-.035, -.004, .05], np.float32)  # toward --deep navy
HIGH_TINT = np.array([.006, .004, -.004], np.float32)    # keep highlights clean, a touch warm


def grade(im, target=.5, wb=.5, tint=1.0, sat=.84, contrast=.16):
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    means = a.reshape(-1, 3).mean(0)
    corr = np.clip(means.mean() / means, .88, 1.12)
    a = np.clip(a * (1 + wb * (corr - 1)), 0, 1)

    m = float((a @ LUMA).mean())
    g = np.log(target) / np.log(max(m, 1e-3))
    g = float(np.clip(1 + .65 * (g - 1), .72, 1.35))
    a = a ** g

    s = a * a * (3 - 2 * a)
    a = a + contrast * (s - a)

    l = (a @ LUMA)[..., None]
    a = l + sat * (a - l)

    l = (a @ LUMA)[..., None]
    a = a + tint * ((1 - l) ** 2 * SHADOW_TINT + l ** 3 * HIGH_TINT)
    return Image.fromarray((np.clip(a, 0, 1) * 255 + .5).astype(np.uint8))


def main():
    os.makedirs(ORIG, exist_ok=True)
    for name, opt in SETS.items():
        variants = sorted(glob.glob(f'{IMG}/{name}-[0-9]*.webp'))
        variants = [v for v in variants if re.fullmatch(rf'{re.escape(name)}-\d+\.webp', os.path.basename(v))]
        for v in variants + ([f"{IMG}/{opt['src']}"] if 'src' in opt else []):
            dst = os.path.join(ORIG, os.path.basename(v))
            if not os.path.exists(dst):
                shutil.copy2(v, dst)
        sizes = {v: Image.open(os.path.join(ORIG, os.path.basename(v))).size for v in variants}
        master_path = os.path.join(ORIG, opt['src']) if 'src' in opt else os.path.join(ORIG, os.path.basename(max(sizes, key=lambda k: sizes[k][0])))
        master = ImageOps.exif_transpose(Image.open(master_path)).convert('RGB')
        kw = {k: opt[k] for k in ('target', 'wb', 'tint', 'sat') if k in opt}
        graded = grade(master, **kw)
        for v, (w, h) in sizes.items():
            out = graded if graded.size == (w, h) else graded.resize((w, h), Image.LANCZOS)
            out.save(v, 'WEBP', quality=82, method=6)
            print(f'{v:40s} {w}x{h} {os.path.getsize(v):>7d} B')


if __name__ == '__main__':
    main()
