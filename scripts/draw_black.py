import numpy as np
from PIL import Image, ImageDraw

img = Image.open('bg_pixel_cinema_wide.jpg').convert('RGB')
draw = ImageDraw.Draw(img)

W, H = img.size

# Coordinates found
xp = 21.0
yp = 33.0
wp = 58.0
hp = 34.0

x = W * xp / 100
y = H * yp / 100
w = W * wp / 100
h = H * hp / 100

draw.rectangle([x, y, x+w, y+h], fill="black")

img.save('C:/Users/sathy/.gemini/antigravity-ide/brain/74148e4e-a10a-4bf5-94ad-8f8399e35a7a/bg_black_screen.jpg')
