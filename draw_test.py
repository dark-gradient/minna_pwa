import numpy as np
from PIL import Image, ImageDraw

img = Image.open('bg_pixel_cinema_wide.jpg').convert('RGB')
draw = ImageDraw.Draw(img)

W, H = img.size

# Let's adjust based on visual.
w = W * 0.556
h = w * (9/16)
x = (W - w) / 2
y = H * 0.354  # tweak top

draw.rectangle([x, y, x+w, y+h], outline="red", width=5)

img.save('C:/Users/sathy/.gemini/antigravity-ide/brain/74148e4e-a10a-4bf5-94ad-8f8399e35a7a/bg_test_bounds_2.jpg')
print(f"Test 2 saved. x: {x/W*100:.2f}%, y: {y/H*100:.2f}%, w: {w/W*100:.2f}%, h: {h/H*100:.2f}%")
