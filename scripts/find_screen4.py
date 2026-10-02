import numpy as np
from PIL import Image

img = Image.open('bg_pixel_cinema.jpg').convert('RGB')
data = np.array(img)

r, g, b = data.T
bright = (r > 240) & (g > 240) & (b > 240)
mask = bright.T.astype(np.uint8) * 255

H, W = mask.shape
cy_start, cy_end = int(H*0.15), int(H*0.85)
cx_start, cx_end = int(W*0.1), int(W*0.9)

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
    print(f"Aspect ratio: {w/h:.2f}")
else:
    print("No screen found")
