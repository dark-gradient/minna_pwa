import numpy as np
from PIL import Image, ImageDraw

img = Image.open('bg_pixel_cinema.jpg').convert('RGB')
draw = ImageDraw.Draw(img)

W, H = img.size
xp, yp, wp, hp = 27.54, 22.40, 44.84, 44.92

x = W * xp / 100
y = H * yp / 100
w = W * wp / 100
h = H * hp / 100

draw.rectangle([x, y, x+w, y+h], outline="red", width=5)

img.save('C:/Users/sathy/.gemini/antigravity-ide/brain/74148e4e-a10a-4bf5-94ad-8f8399e35a7a/bg_massive_bounds.jpg')
