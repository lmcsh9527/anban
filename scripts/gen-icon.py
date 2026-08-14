#!/usr/bin/env python3
"""Generate Anban (案板) brand icons: build/icon.png, build/icon.icns, build/icon.ico.

Design: warm dark rounded square (stove/stone), a wooden chopping board (案板)
with a tilted cleaver (菜刀) and rising steam — "什么都能下锅的创作台".
Requires: Pillow (PIL); macOS `iconutil` for .icns output.
Run: python3 scripts/gen-icon.py
"""
from PIL import Image, ImageDraw, ImageFilter
import os
import shutil
import subprocess
import tempfile

S = 1024
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")


def make_canvas():
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=195, fill=(44, 33, 24, 255))
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle([0, 0, S - 1, S - 1], radius=195, fill=(255, 145, 70, 42))
    img = Image.alpha_composite(img, glow)
    return img


def draw_board(img):
    d = ImageDraw.Draw(img)
    bx0, by0, bx1, by1 = 175, 350, 849, 705
    d.rounded_rectangle([bx0, by0, bx1, by1], radius=44, fill=(203, 157, 110, 255))
    for y in range(by0 + 60, by1, 55):
        d.line([bx0 + 46, y, bx1 - 46, y], fill=(184, 138, 95, 255), width=9)
    d.rounded_rectangle([bx0, by0, bx1, by0 + 26], radius=13, fill=(222, 182, 142, 255))
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.rounded_rectangle([bx0 + 10, by1 - 10, bx1 - 10, by1 + 20], radius=16, fill=(0, 0, 0, 90))
    return Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(12)))


def draw_cleaver(img):
    w, h = 350, 138
    t = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    td = ImageDraw.Draw(t)
    td.rounded_rectangle([6, 16, w - 92, h - 18], radius=48, fill=(212, 218, 226, 255))
    td.rounded_rectangle([6, h - 34, w - 92, h - 18], radius=10, fill=(238, 243, 248, 255))
    td.rounded_rectangle([w - 82, 34, w - 6, h - 36], radius=14, fill=(58, 50, 42, 255))
    td.rounded_rectangle([w - 82, 34, w - 6, 58], radius=10, fill=(92, 80, 68, 255))
    t = t.rotate(-32, expand=True, resample=Image.BICUBIC)
    img.paste(t, (248, 430), t)
    return img


def draw_steam(img):
    d = ImageDraw.Draw(img)
    for cx, cy, wdt in [(470, 300, 9), (588, 258, 10), (700, 300, 9)]:
        for k in range(4):
            y0 = cy - k * 46
            x0 = cx + k * 20
            d.arc([x0 - 36, y0 - 46, x0 + 36, y0 + 46], 200, 340, fill=(246, 238, 224, 165), width=wdt)
            d.arc([x0 - 36, y0 - 46, x0 + 36, y0 + 46], 20, 160, fill=(246, 238, 224, 140), width=max(wdt - 2, 3))
    return img


def main():
    os.makedirs(BUILD, exist_ok=True)
    img = make_canvas()
    img = draw_board(img)
    img = draw_steam(img)
    img = draw_cleaver(img)

    png = os.path.join(BUILD, "icon.png")
    img.save(png, "PNG")
    print("wrote", png, img.size)

    ico = os.path.join(BUILD, "icon.ico")
    img.save(ico, "ICO", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("wrote", ico)

    icns = os.path.join(BUILD, "icon.icns")
    with tempfile.TemporaryDirectory() as td:
        iconset = os.path.join(td, "icon.iconset")
        os.makedirs(iconset)
        # iconutil is picky about PIL-encoded PNG chunks; re-encode each
        # size through `sips` (macOS native) before building the .icns.
        for size in (16, 32, 128, 256, 512):
            out1 = os.path.join(iconset, "icon_{0}x{0}.png".format(size))
            out2 = os.path.join(iconset, "icon_{0}x{0}@2x.png".format(size))
            subprocess.run(
                ["sips", "-z", str(size), str(size), png, "--out", out1],
                check=True, capture_output=True,
            )
            subprocess.run(
                ["sips", "-z", str(size * 2), str(size * 2), png, "--out", out2],
                check=True, capture_output=True,
            )
        # iconutil cannot write its output to external volumes (fails with
        # "Failed to generate ICNS"); build in a local temp dir, then move.
        tmp_icns = os.path.join(td, "icon.icns")
        subprocess.run(["iconutil", "-c", "icns", iconset, "-o", tmp_icns], check=True)
        shutil.move(tmp_icns, icns)
    print("wrote", icns)


if __name__ == "__main__":
    main()
