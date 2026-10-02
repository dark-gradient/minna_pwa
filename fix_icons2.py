import os
from PIL import Image
import glob

files = ["assets/images/icons/icon_home.png"]
for f in files:
    img = Image.open(f).convert("RGBA")
    data = img.load()
    width, height = img.size
    
    rows = []
    for y in range(height):
        row_is_empty = True
        for x in range(width):
            if data[x, y][3] > 10: # threshold alpha
                row_is_empty = False
                break
        rows.append(not row_is_empty)
    
    # Print the pattern of rows
    pattern = ""
    for r in rows:
        pattern += "1" if r else "0"
    print(f"{f}:\n{pattern}\n")
