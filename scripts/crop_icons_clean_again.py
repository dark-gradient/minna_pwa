import numpy as np
from PIL import Image
import glob

for filepath in glob.glob("icon_*.png"):
    try:
        img = Image.open(filepath).convert("RGBA")
        data = np.array(img)
        alpha = data[:, :, 3]
        rows = np.any(alpha, axis=1)
        
        # Find the first solid block
        start_row = None
        for i in range(len(rows)):
            if rows[i]:
                start_row = i
                break
        
        if start_row is None:
            continue
            
        # Find the gap after the solid block
        end_row = None
        # Start looking for a gap after 50 pixels to ignore small artifacts
        for i in range(start_row + 50, len(rows)):
            if not rows[i]:
                end_row = i
                break
                
        if end_row is not None:
            # Crop to [0:end_row] to remove everything below the gap
            # Also get bbox of just the top part to trim edges perfectly
            top_data = data[:end_row, :, :]
            top_img = Image.fromarray(top_data)
            bbox = top_img.getbbox()
            if bbox:
                final_img = top_img.crop(bbox)
                final_img.save(filepath)
                print(f"Cropped {filepath} to {final_img.size}")
        else:
            print(f"No gap found for {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")
