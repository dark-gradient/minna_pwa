import numpy as np
from PIL import Image

img_path = r'C:\Users\sathy\.gemini\antigravity-ide\brain\74148e4e-a10a-4bf5-94ad-8f8399e35a7a\.user_uploaded\media_1790781653964.png'
img = Image.open(img_path).convert('RGBA')

data = np.array(img)
# If background is white or near white, make it transparent
r, g, b, a = data.T
white_areas = (r > 240) & (g > 240) & (b > 240)
data[..., :][white_areas.T] = (255, 255, 255, 0)

# The image has 3 rows: Main Icons, Active State, Nav Bar Icons (Small).
# The bottom ~20% of the image contains the Nav Bar Icons.
H, W, _ = data.shape
bottom_y = int(H * 0.75)
bottom_section = data[bottom_y:H, :, :]

# Split horizontally into 7 sections
section_w = W // 7
names = ['home', 'lessons', 'vocabulary', 'grammar', 'kanji', 'listening', 'mocktest']

for i in range(7):
    x_start = i * section_w
    x_end = (i + 1) * section_w
    
    icon_data = bottom_section[:, x_start:x_end, :]
    out_img = Image.fromarray(icon_data)
    
    # Get bounding box of non-transparent parts
    bbox = out_img.getbbox()
    if bbox:
        # crop to bounding box
        out_img = out_img.crop(bbox)
        # Add 4px padding
        padded = Image.new('RGBA', (out_img.width + 8, out_img.height + 8), (0,0,0,0))
        padded.paste(out_img, (4, 4))
        padded.save(f'icon_{names[i]}.png')
    else:
        out_img.save(f'icon_{names[i]}.png')

print("Extraction complete.")
