from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

WIDTH, HEIGHT = 1600, 500
img = Image.new('RGBA', (WIDTH, HEIGHT), (248, 250, 252, 255))
draw = ImageDraw.Draw(img)

# dark navy square icon
icon_x, icon_y, icon_size = 70, 90, 220
icon = Image.new('RGBA', (icon_size, icon_size), (0, 0, 0, 0))
icon_draw = ImageDraw.Draw(icon)
icon_draw.rounded_rectangle((0, 0, icon_size, icon_size), radius=42, fill=(15, 23, 42, 255))
img.alpha_composite(icon, (icon_x, icon_y))

# make a soft blue gradient background behind the icon
for x in range(40, 330):
    for y in range(70, 360):
        r = min(255, 20 + int((x - 40) * 0.35))
        g = min(255, 90 + int((x - 40) * 0.25))
        b = min(255, 180 + int((x - 40) * 0.22))
        if x < 250 and y < 300:
            img.putpixel((x, y), (r, g, b, 255))

# stylized S line
s_points = [
    (170, 138), (150, 120), (110, 116), (88, 122), (72, 136), (72, 150),
    (88, 166), (120, 174), (150, 170), (168, 152), (170, 132), (152, 118),
    (120, 116), (90, 122), (74, 140), (74, 154), (86, 168), (130, 171),
    (158, 166), (177, 152)
]
for i in range(len(s_points)-1):
    x1, y1 = s_points[i]
    x2, y2 = s_points[i+1]
    draw.line((x1 + 5, y1 + 5, x2 + 5, y2 + 5), fill=(255, 255, 255, 255), width=10)

# accent points
for px, py in [(120, 102), (162, 170)]:
    draw.ellipse((px, py, px + 18, py + 18), fill=(224, 242, 254, 255))
    draw.line((px + 9, py + 9, px + 38, py + 42), fill=(224, 242, 254, 255), width=3)

# text
font_candidates = [
    'C:/Windows/Fonts/arialbd.ttf',
    'C:/Windows/Fonts/segoeui.ttf',
    'C:/Windows/Fonts/calibrib.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf',
]

main_font = None
for f in font_candidates:
    try:
        main_font = ImageFont.truetype(f, 82)
        break
    except Exception:
        pass
if main_font is None:
    main_font = ImageFont.load_default()

sub_font = None
for f in font_candidates:
    try:
        sub_font = ImageFont.truetype(f, 20)
        break
    except Exception:
        pass
if sub_font is None:
    sub_font = ImageFont.load_default()

text_color = (15, 23, 42, 255)
draw.text((410, 146), 'SILIXUS', font=main_font, fill=text_color)

subtitle = 'SOFTWARE • AI • DEVOPS'
char_x = 415
for ch in subtitle:
    draw.text((char_x, 212), ch, font=sub_font, fill=(71, 85, 105, 255))
    char_x += sub_font.getbbox(ch)[2] + 7

# accent line under text
draw.rounded_rectangle((410, 242, 780, 248), radius=3, fill=(79, 70, 229, 255))

# convert to RGB for saving as PNG
rgb_img = img.convert('RGB')
output = Path(__file__).resolve().parent / 'silixus_logo.png'
rgb_img.save(output)
print(f'PNG logo generated: {output}')
