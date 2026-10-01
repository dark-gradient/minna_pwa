import numpy as np
from PIL import Image

def get_top_component(img_data):
    # Find all rows that have at least one non-transparent pixel
    alpha_rows = np.any(img_data[:,:,3] > 0, axis=1)
    
    # We want to find the first continuous block of True
    in_block = False
    start_row = -1
    end_row = -1
    
    for i, val in enumerate(alpha_rows):
        if val and not in_block:
            in_block = True
            start_row = i
        elif not val and in_block:
            # Reached end of first block. Check if this gap is large enough to be text separation.
            # Usually > 2 pixels
            # Let's say any gap stops it.
            end_row = i
            break
            
    if end_row == -1 and in_block:
        end_row = len(alpha_rows)
        
    return img_data[start_row:end_row, :, :]

img_path = r'C:\Users\sathy\.gemini\antigravity-ide\brain\74148e4e-a10a-4bf5-94ad-8f8399e35a7a\.user_uploaded\media_1790781653964.png'
img = Image.open(img_path).convert('RGBA')
data = np.array(img)

# Make white background transparent
r, g, b, a = data.T
white_areas = (r > 240) & (g > 240) & (b > 240)
data[..., :][white_areas.T] = (255, 255, 255, 0)

H, W, _ = data.shape
section_w = W // 7
names = ['home', 'lessons', 'vocabulary', 'grammar', 'kanji', 'listening', 'mocktest']

for i in range(7):
    x_start = i * section_w
    x_end = (i + 1) * section_w
    
    # Let's use the TOP row, which is the first 40%
    icon_data = data[0:int(H*0.4), x_start:x_end, :]
    
    out_img = Image.fromarray(icon_data)
    bbox = out_img.getbbox()
    if bbox:
        out_img = out_img.crop(bbox)
        
        # Now find the first contiguous vertical block
        # Convert back to array
        cropped_data = np.array(out_img)
        alpha_rows = np.any(cropped_data[:,:,3] > 0, axis=1)
        
        # We need to handle small gaps (e.g., in pixel art) by finding a gap of at least 5 pixels
        end_idx = len(alpha_rows)
        gap_count = 0
        for r_idx in range(len(alpha_rows)):
            if not alpha_rows[r_idx]:
                gap_count += 1
                if gap_count >= 5:
                    end_idx = r_idx - gap_count + 1
                    break
            else:
                gap_count = 0
                
        final_data = cropped_data[0:end_idx, :, :]
        final_img = Image.fromarray(final_data)
        
        # Crop tight again
        bbox2 = final_img.getbbox()
        if bbox2:
            final_img = final_img.crop(bbox2)
        
        final_img.save(f'nav_icon_{names[i]}.png')

print("Icons perfectly cropped without text!")
