import numpy as np
from PIL import Image

img_path = r'C:\Users\sathy\.gemini\antigravity-ide\brain\74148e4e-a10a-4bf5-94ad-8f8399e35a7a\.user_uploaded\media_1790781653964.png'
img = Image.open(img_path).convert('RGBA')
data = np.array(img)

# Make white background transparent
r, g, b, a = data.T
white_areas = (r > 240) & (g > 240) & (b > 240)
data[..., :][white_areas.T] = (255, 255, 255, 0)

H, W, _ = data.shape
print(f"Original size: {W}x{H}")

# Split horizontally into 7 sections
section_w = W // 7
names = ['home', 'lessons', 'vocabulary', 'grammar', 'kanji', 'listening', 'mocktest']

for i in range(7):
    x_start = i * section_w
    x_end = (i + 1) * section_w
    
    # Try the top row (Main Icons)
    top_y = 0
    bottom_y = int(H * 0.45) # Take top 45%
    icon_data = data[top_y:bottom_y, x_start:x_end, :]
    
    out_img = Image.fromarray(icon_data)
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        # We need to aggressively crop out the text if it's there
        # Let's crop the bottom 25% of the bounding box if the text is at the bottom
        # Let's assume the icon is the top 75% of the bounding box
        ib_w, ib_h = out_img.size
        # The text is usually separated by some blank space. We can find the gap!
        # Or just take top 75% for now:
        # Actually, let's just use the first row. Maybe it doesn't have text.
        out_img.save(f'nav_icon_{names[i]}.png')
        print(f"Saved nav_icon_{names[i]}.png")

print("Icons extracted from Top Row!")
