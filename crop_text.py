import os
from PIL import Image
import glob

files = glob.glob("assets/images/icons/icon_*.png")
for f in files:
    try:
        img = Image.open(f).convert("RGBA")
        width, height = img.size
        
        # If the image is taller than 86px, it probably has text at the bottom.
        # Let's crop it to 86px height from the top.
        if height > 88:
            print(f"{f}: Height is {height}. Cropping to 86px.")
            # crop (left, top, right, bottom)
            box = (0, 0, width, 86)
            cropped = img.crop(box)
            # Find the new bounding box to trim transparent edges
            bbox = cropped.getbbox()
            if bbox:
                final = cropped.crop(bbox)
                final.save(f)
                print(f"Saved {f} with new size {final.size}")
        else:
            print(f"{f}: Height is {height}. No need to crop.")
    except Exception as e:
        print(f"Error on {f}: {e}")
