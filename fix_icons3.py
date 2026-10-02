import os
from PIL import Image
import glob

files = glob.glob("assets/images/icons/icon_*.png")
for f in files:
    try:
        img = Image.open(f).convert("RGBA")
        data = img.load()
        width, height = img.size
        
        rows = []
        for y in range(height):
            row_is_empty = True
            for x in range(width):
                if data[x, y][3] > 10:
                    row_is_empty = False
                    break
            rows.append(not row_is_empty)
            
        gap_start = -1
        consecutive_zeros = 0
        for y in range(height):
            if rows[y]:
                consecutive_zeros = 0
            else:
                if consecutive_zeros == 0:
                    gap_start = y
                consecutive_zeros += 1
                
                if consecutive_zeros >= 15:
                    break
                    
        if consecutive_zeros >= 15 and gap_start != -1:
            print(f"{f}: Found large gap starting at row {gap_start}")
            # crop from gap_start to height
            box = (0, gap_start, width, height)
            cropped = img.crop(box)
            bbox = cropped.getbbox()
            if bbox:
                final = cropped.crop(bbox)
                final.save(f)
                print(f"Saved {f} with new size {final.size}")
        else:
            print(f"{f}: No large gap found. Keeping original.")
    except Exception as e:
        print(f"Error on {f}: {e}")
