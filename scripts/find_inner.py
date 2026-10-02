import numpy as np
from PIL import Image

img = Image.open('bg_pixel_cinema_wide.jpg').convert('RGB')
data = np.array(img)
H, W = data.shape[:2]

# The screen is bright, the border is very dark (#000000 to #142E27).
# Let's crop to center and find the bounding box of the non-dark area.
r, g, b = data.T
brightness = (r.astype(int) + g.astype(int) + b.astype(int)) / 3

is_bright = brightness > 50
mask = is_bright.T

cy_start, cy_end = int(H*0.25), int(H*0.75)
cx_start, cx_end = int(W*0.2), int(W*0.8)

center_mask = mask[cy_start:cy_end, cx_start:cx_end]
rows = np.any(center_mask, axis=1)
cols = np.any(center_mask, axis=0)

ymin, ymax = np.where(rows)[0][[0, -1]]
xmin, xmax = np.where(cols)[0][[0, -1]]

ymin += cy_start
ymax += cy_start
xmin += cx_start
xmax += cx_start

w = xmax - xmin
h = ymax - ymin

print(f"Inner screen: x={xmin/W*100:.2f}%, y={ymin/H*100:.2f}%, w={w/W*100:.2f}%, h={h/H*100:.2f}%")
print(f"Aspect ratio: {w/h:.2f}")
