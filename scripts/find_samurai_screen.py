import numpy as np
from PIL import Image

img = Image.open('bg_pixel_cinema_wide.jpg').convert('RGB')
data = np.array(img)

r, g, b = data.T
# The screen is mostly grayscale (samurai movie) with a slight blue tint, while the rest of the image is very warm (red/yellow) or dark green.
# Let's find pixels that are somewhat bright and desaturated.
brightness = (r.astype(int) + g.astype(int) + b.astype(int)) / 3
color_diff = np.abs(r.astype(int) - g.astype(int)) + np.abs(g.astype(int) - b.astype(int))

# High brightness, low color saturation (grayscale)
is_screen = (brightness > 100) & (color_diff < 40)
mask = is_screen.T.astype(np.uint8) * 255

H, W = mask.shape
cy_start, cy_end = int(H*0.2), int(H*0.7)
cx_start, cx_end = int(W*0.2), int(W*0.8)

center_mask = mask[cy_start:cy_end, cx_start:cx_end]
rows = np.any(center_mask, axis=1)
cols = np.any(center_mask, axis=0)

if np.any(rows) and np.any(cols):
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    
    ymin += cy_start
    ymax += cy_start
    xmin += cx_start
    xmax += cx_start
    
    w = xmax - xmin
    h = ymax - ymin
    
    xp = (xmin / W) * 100
    yp = (ymin / H) * 100
    wp = (w / W) * 100
    hp = (h / H) * 100
    
    print(f"Screen found at X: {xp:.2f}%, Y: {yp:.2f}%, W: {wp:.2f}%, H: {hp:.2f}%")
else:
    print("No screen found")
