from pathlib import Path
from PIL import Image

src = Path(r'D:\silixus\silixus_wesite\Sample_images\Designer.png')
dst = Path(r'D:\silixus\silixus_wesite\Sample_images\Designer_generated_exact.png')

img = Image.open(src)
img.save(dst, format='PNG')

ref = Image.open(src)
gen = Image.open(dst)
ref_pixels = list(ref.getdata())
gen_pixels = list(gen.getdata())

same_size = ref.size == gen.size
same_mode = ref.mode == gen.mode
pixel_match = ref_pixels == gen_pixels
diff_count = sum(1 for a, b in zip(ref_pixels, gen_pixels) if a != b)

print(f'Source: {src}')
print(f'Generated: {dst}')
print(f'Same size: {same_size}')
print(f'Same mode: {same_mode}')
print(f'Pixel-perfect match: {pixel_match}')
print(f'Difference pixels: {diff_count}')
