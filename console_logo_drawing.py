import os

# Console-based Silixus logo sketch
# This draws a text-style logo in the terminal, no PNG output.

WIDTH = 120
HEIGHT = 32

# Create empty canvas
canvas = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Helper to draw lines

def put(x, y, ch='█'):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[y][x] = ch


def draw_hline(y, x1, x2, ch='─'):
    for x in range(x1, x2 + 1):
        put(x, y, ch)


def draw_vline(x, y1, y2, ch='│'):
    for y in range(y1, y2 + 1):
        put(x, y, ch)


def draw_rect(x1, y1, x2, y2, fill=' '):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if x in (x1, x2) or y in (y1, y2):
                put(x, y, '│' if x in (x1, x2) and y not in (y1, y2) else '─' if y in (y1, y2) and x not in (x1, x2) else '┼')
            else:
                put(x, y, fill)


def draw_s_monogram(cx, cy):
    # stylized S using block characters
    points = [
        (cx + 6, cy - 12), (cx + 2, cy - 10), (cx - 3, cy - 5), (cx - 4, cy + 1),
        (cx + 1, cy + 6), (cx + 9, cy + 9), (cx + 15, cy + 12), (cx + 15, cy + 18),
        (cx + 9, cy + 21), (cx + 2, cy + 22), (cx - 3, cy + 18), (cx - 2, cy + 12),
        (cx + 5, cy + 9), (cx + 12, cy + 7), (cx + 14, cy + 1), (cx + 11, cy - 4),
        (cx + 6, cy - 7), (cx + 4, cy - 12)
    ]
    for x, y in points:
        put(x, y, '█')

    # internal stroke for clarity
    for y in range(cy - 10, cy + 20):
        if y % 4 == 0:
            put(cx + 5, y, '▓')


def draw_wordmark(x_start=45, y=16):
    text = "SILIXUS"
    for i, ch in enumerate(text):
        put(x_start + i * 2, y, '█')

    # subtitle line
    subtitle = "AI • DEVOPS • SOFTWARE"
    for i, ch in enumerate(subtitle):
        put(40 + i, y + 2, '░')


def draw_logo():
    # background halo using dots
    for y in range(4, 28):
        for x in range(18, 100):
            if (x - 55) ** 2 + (y - 17) ** 2 < 650:
                if (x + y) % 7 == 0:
                    put(x, y, '.')

    # panel
    for y in range(5, 27):
        for x in range(13, 107):
            if x in (13, 106) or y in (5, 26):
                put(x, y, '═' if y in (5, 26) else '║')

    # icon square
    for y in range(8, 23):
        for x in range(20, 42):
            if x in (20, 41) or y in (8, 22):
                put(x, y, '█')

    # accent glow inside square
    for y in range(10, 21):
        for x in range(23, 38):
            if (x + y) % 5 == 0:
                put(x, y, '▓')

    # draw S monogram inside icon square
    draw_s_monogram(30, 15)

    # draw wordmark
    draw_wordmark(46, 15)

    # draw small underline
    for x in range(46, 96):
        if x % 8 == 0:
            put(x, 19, '─')


draw_logo()

# print in terminal with clean formatting
for row in canvas:
    print(''.join(row).rstrip())
