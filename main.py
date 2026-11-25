#!/usr/bin/env python3
"""Render 'The World Today' front page for Tuesday 24 November 2026.

Deterministic: fixed strings, fixed fonts, no network, no clock, no
randomness. Running this file twice produces a byte-identical PNG.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (18, 18, 18)
RED = (158, 27, 27)
GREY = (96, 90, 80)
LIGHT_RULE = (190, 182, 168)
GREEN = (38, 110, 58)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, max_w, text, fnt, leading, fill=INK):
    """Draw a wrapped paragraph; return the y after the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def story(draw, x, y, w, kicker, head, head_size, body, body_size=15):
    """Kicker + bold headline + body paragraph. Returns bottom y."""
    kf = font(SANS_B, 14)
    hf = font(SERIF_B, head_size)
    bf = font(SERIF, body_size)
    draw.text((x, y), kicker, font=kf, fill=RED)
    y += 22
    y = para(draw, x, y, w, head, hf, head_size + 6)
    y += 4
    y = para(draw, x, y, w, body, bf, body_size + 6)
    return y


def chip_illustration(draw, x, y, w, h):
    """Stylised green processor chip on a dark board (drawn, no photo)."""
    draw.rectangle([x, y, x + w, y + h], fill=(24, 30, 26))
    for i in range(5):
        yy = y + 14 + i * ((h - 28) // 4)
        draw.line([(x + 10, yy), (x + w - 10, yy)], fill=(52, 84, 62), width=1)
    cx, cy = x + w // 2, y + h // 2 - 8
    chip = 118
    for i in range(5):
        off = -44 + i * 22
        draw.line([(cx + off, cy - chip // 2 - 13), (cx + off, cy - chip // 2)], fill=(180, 190, 170), width=3)
        draw.line([(cx + off, cy + chip // 2), (cx + off, cy + chip // 2 + 13)], fill=(180, 190, 170), width=3)
        draw.line([(cx - chip // 2 - 13, cy + off), (cx - chip // 2, cy + off)], fill=(180, 190, 170), width=3)
        draw.line([(cx + chip // 2, cy + off), (cx + chip // 2 + 13, cy + off)], fill=(180, 190, 170), width=3)
    draw.rectangle([cx - chip // 2, cy - chip // 2, cx + chip // 2, cy + chip // 2],
                   fill=GREEN, outline=(210, 225, 200), width=3)
    draw.rectangle([cx - 40, cy - 40, cx + 40, cy + 40], outline=(210, 225, 200), width=2)
    eye = font(SERIF_B, 26)
    label = "NVDA"
    tw = draw.textlength(label, font=eye)
    draw.text((cx - tw / 2, cy - 14), label, font=eye, fill=(235, 240, 225))
    cap = font(SANS, 13)
    caption = "Nvidia's Jensen Huang returns as chief executive."
    tw = draw.textlength(caption, font=cap)
    draw.text((x + (w - tw) / 2, y + h - 22), caption, font=cap, fill=(200, 205, 190))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 46
    R = W - M

    # ---- masthead ---------------------------------------------------
    rule(d, M, 28, R, 4)
    rule(d, M, 36, R, 1)
    mast = font(SERIF_B, 62)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 46), title, font=mast, fill=INK)
    rule(d, M, 124, R, 1)
    meta = font(SANS_B, 16)
    left = "TUESDAY 24 NOVEMBER 2026"
    right = "ONE WORLD  •  ONE PAGE  •  FREE"
    d.text((M, 134), left, font=meta, fill=INK)
    tw = d.textlength(right, font=meta)
    d.text((R - tw, 134), right, font=meta, fill=INK)
    rule(d, M, 160, R, 3)

    # ---- lead story -------------------------------------------------
    y = 176
    kf = font(SANS_B, 16)
    d.text((M, y), "TECH  •  THE COMEBACK", font=kf, fill=RED)
    y += 26
    y = para(d, M, y, R - M, "Huang is back: Nvidia reinstates its chief",
             font(SERIF_B, 44), 50)
    y += 10
    ill_w, ill_h = 470, 180
    chip_illustration(d, M, y, ill_w, ill_h)
    bx = M + ill_w + 26
    bw = R - bx
    by = y
    by = para(d, bx, by, bw,
              "Jensen Huang was reinstated as chief executive of Nvidia on "
              "Monday, less than two weeks after he stepped down. Vice "
              "President JD Vance lobbied the board at President Trump's "
              "behest, and Mr Trump said he convinced the company to bring "
              "its founder back.",
              font(SERIF, 17), 23)
    by += 8
    by = para(d, bx, by, bw,
              "Shares jumped on the news, adding as much as $15 million to "
              "Mr Trump's own Nvidia holding.",
              font(SERIF, 17), 23)
    y = y + ill_h + 12
    rule(d, M, y, R, 2)
    y += 12

    # ---- second row: three columns ----------------------------------
    col_w = (R - M - 2 * 28) // 3
    tops = []
    x0 = M
    tops.append(story(
        d, x0, y, col_w,
        "IRAN  •  STANDOFF",
        "Tehran vows to fight US naval blockade",
        22,
        "Iran will use 'all its tools' against the US naval blockade, its "
        "foreign ministry said, as Vance and Rubio met Qatar's prime "
        "minister."))
    x0 += col_w + 28
    tops.append(story(
        d, x0, y, col_w,
        "GAZA  •  CEASEFIRE UNDER STRAIN",
        "Israeli strike kills Hamas security chief",
        22,
        "Naeem Abu Nahal, director of Hamas' internal security apparatus, "
        "was among seven people killed in Israeli strikes on Gaza City, "
        "despite a ceasefire in place since last year."))
    x0 += col_w + 28
    tops.append(story(
        d, x0, y, col_w,
        "UKRAINE  •  WAR",
        "Two killed as Russian strike hits flats",
        22,
        "An overnight Russian attack on Zaporizhzhia killed two and "
        "wounded 40, including four children, after striking an apartment "
        "building."))
    y = max(tops) + 10
    rule(d, M, y, R, 1, fill=LIGHT_RULE)
    y += 10

    # ---- third row: two wider stories -------------------------------
    half = (R - M - 28) // 2
    t1 = story(
        d, M, y, half,
        "SPACE  •  NATO",
        "NATO vows to defend space after nuclear satellite reports",
        20,
        "Alliance chief Mark Rutte said NATO would defend against any "
        "threat in space, after reports Russia could launch a nuclear-armed "
        "satellite before the end of the year.")
    t2 = story(
        d, M + half + 28, y, half,
        "KOREA  •  AIRSPACE",
        "North Korean aircraft breaches South's airspace",
        20,
        "Seoul said a suspected North Korean aircraft crossed into its "
        "airspace near the island of Ulleung, prompting residents to "
        "shelter.")
    y = max(t1, t2) + 10
    rule(d, M, y, R, 2)
    y += 10

    # ---- in brief strip ---------------------------------------------
    bf = font(SERIF, 16)
    sf = font(SANS_B, 14)
    d.text((M, y), "IN BRIEF", font=sf, fill=RED)
    y += 22
    briefs = [
        "Trump awards Rudy Giuliani the Medal of Freedom.",
        "US, Mexico, Costa Rica and Jamaica to host the 2031 Women's World Cup.",
        "Honda recalls 810,000 vehicles in the US; a 5.4 quake hits Nepal.",
    ]
    for b in briefs:
        d.text((M, y), "•", font=bf, fill=RED)
        y = para(d, M + 22, y, R - M - 22, b, bf, 21)
        y += 1
    y += 4
    rule(d, M, y, R, 1, fill=LIGHT_RULE)
    y += 8
    foot = font(SANS, 12)
    ftext = "The World Today — a one-page summary of Tuesday 24 November 2026."
    tw = d.textlength(ftext, font=foot)
    d.text(((W - tw) / 2, y), ftext, font=foot, fill=GREY)

    img.save(OUT, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
