from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

FONT_CANDIDATES = [
    'C:/Windows/Fonts/arialbd.ttf',
    'C:/Windows/Fonts/segoeui.ttf',
    'C:/Windows/Fonts/calibrib.ttf',
    'C:/Windows/Fonts/tahomabd.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]


def load_font(size, fallback='bold'):
    for font_path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(font_path, size)
        except Exception:
            pass
    if fallback == 'bold':
        return ImageFont.load_default()
    return ImageFont.load_default()


def build_s_monogram(base_color=(255, 255, 255), accent_color=(110, 180, 255)):
    points = [
        (120, 20), (75, 30), (42, 54), (34, 86), (52, 118),
        (96, 126), (137, 148), (145, 181), (124, 213), (78, 220),
        (40, 206), (60, 172), (98, 168), (129, 160), (146, 144), (148, 110)
    ]
    overlay = Image.new('RGBA', (220, 220), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.line(points, fill=base_color + (255,), width=18)
    d.ellipse((18, 105, 36, 123), fill=accent_color + (255,))
    d.ellipse((133, 180, 151, 198), fill=accent_color + (255,))
    return overlay


def build_logo_variant(name, width, height, bg_color, panel_color, text_color, accent_color, show_wordmark=True, icon_only=False):
    img = Image.new('RGBA', (width, height), bg_color + (255,))
    draw = ImageDraw.Draw(img)

    # soft background glow
    for cx, cy, r, color in [
        (width * 0.32, height * 0.38, width * 0.18, (*accent_color[:3], 60)),
        (width * 0.76, height * 0.68, width * 0.22, (*accent_color[:3], 45)),
    ]:
        glow = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(*accent_color[:3], 60))
        img.alpha_composite(glow, (0, 0))

    if not icon_only:
        panel = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        p = ImageDraw.Draw(panel)
        p.rounded_rectangle((70, 80, width - 70, height - 80), radius=36, fill=panel_color + (255,))
        img.alpha_composite(panel, (0, 0))

    # icon
    icon_size = 260
    icon_x = 200
    icon_y = 240 if not icon_only else 150
    icon_bg = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))
    icon_draw = ImageDraw.Draw(icon_bg)
    icon_draw.rounded_rectangle((0, 0, icon_size, icon_size), radius=56, fill=(19, 32, 54, 255))
    img.alpha_composite(icon_bg, (icon_x, icon_y))

    # gradient fill for icon area
    for yy in range(icon_y, icon_y + icon_size):
        for xx in range(icon_x, icon_x + icon_size):
            if xx < icon_x + 50 or xx > icon_x + icon_size - 50:
                continue
            v = (xx - icon_x) / icon_size
            r = int(18 + v * 120)
            g = int(50 + v * 120)
            b = int(110 + v * 150)
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            img.putpixel((xx, yy), (r, g, b, 255))

    monogram = build_s_monogram(base_color=(255, 255, 255), accent_color=accent_color)
    img.alpha_composite(monogram, (icon_x + 30, icon_y + 25))

    if show_wordmark:
        main_font = load_font(96)
        sub_font = load_font(28)
        word_x = 560
        word_y = 330 if not icon_only else 260
        draw.text((word_x, word_y), 'SILIXUS', font=main_font, fill=text_color + (255,))
        draw.text((word_x + 4, word_y + 88), 'SOFTWARE • AI • DEVOPS', font=sub_font, fill=(88, 101, 120, 255))
        for x in range(word_x, word_x + 500, 10):
            alpha = 200 if x % 20 == 0 else 110
            draw.line((x, word_y + 150, x + 8, word_y + 150), fill=(*accent_color[:3], alpha), width=3)

    if icon_only:
        output_name = f'{name}.png'
    else:
        output_name = f'{name}.png'

    output = Path(__file__).resolve().parent / output_name
    img = img.convert('RGB')
    img.save(output)
    print(f'Generated: {output}')


if __name__ == '__main__':
    variants = [
        ('silixus_enterprise_logo', 1600, 900, (244, 247, 251), (13, 20, 34), (15, 23, 42), (76, 110, 245), True, False),
        ('silixus_minimal_logo', 1600, 900, (250, 252, 255), (240, 245, 250), (21, 31, 48), (44, 132, 255), True, False),
        ('silixus_badge_logo', 1200, 1200, (10, 18, 30), (17, 30, 52), (235, 240, 255), (65, 180, 255), False, False),
        ('silixus_icon_logo', 1000, 1000, (246, 249, 255), (255, 255, 255), (12, 20, 38), (61, 130, 255), False, True),
    ]

    for name, width, height, bg_color, panel_color, text_color, accent_color, show_wordmark, icon_only in variants:
        build_logo_variant(name, width, height, bg_color, panel_color, text_color, accent_color, show_wordmark, icon_only)
