import os
from PIL import Image
import glob

files = glob.glob("assets/images/icons/icon_*.png")
for f in files:
    try:
        img = Image.open(f).convert("RGBA")
        data = img.load()
        width, height = img.size
        
        in_first_block = False
        gap_row = -1
        for y in range(height):
            row_is_empty = True
            for x in range(width):
                if data[x, y][3] > 0: # Alpha > 0
                    row_is_empty = False
                    break
            
            if not row_is_empty:
                in_first_block = True
            elif in_first_block and row_is_empty:
                gap_row = y
                break
                
        if gap_row != -1:
            print(f"{f}: Found gap at row {gap_row}")
            box = (0, gap_row, width, height)
            cropped = img.crop(box)
            bbox = cropped.getbbox()
            if bbox:
                final = cropped.crop(bbox)
                final.save(f)
                print(f"Saved {f} with new size {final.size}")
        else:
            print(f"{f}: No gap found. Keeping original.")
    except Exception as e:
        print(f"Error on {f}: {e}")
