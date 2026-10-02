import numpy as np
from PIL import Image

img = Image.open('bg_cinema.jpg').convert('RGB')
data = np.array(img)

r, g, b = data.T
# Screen is bright cream, high RGB values.
bright = (r > 200) & (g > 200) & (b > 180)
mask = bright.T.astype(np.uint8) * 255

# Find bounding box of the bright area in the center
H, W = mask.shape
# Crop the search to the center 60% to avoid lights on the walls
cy_start, cy_end = int(H*0.2), int(H*0.8)
cx_start, cx_end = int(W*0.2), int(W*0.8)

center_mask = mask[cy_start:cy_end, cx_start:cx_end]
rows = np.any(center_mask, axis=1)
cols = np.any(center_mask, axis=0)

if np.any(rows) and np.any(cols):
    ymin, ymax = np.where(rows)[0][[0, -1]]
    xmin, xmax = np.where(cols)[0][[0, -1]]
    
    # Adjust for center crop
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
