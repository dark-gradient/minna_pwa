from PIL import Image
import glob

names = ['home', 'lessons', 'vocabulary', 'grammar', 'kanji', 'listening', 'mocktest']

for name in names:
    try:
        img = Image.open(f'nav_icon_{name}.png')
        w, h = img.size
        # The icon is at the top. The width is roughly the size of the square icon.
        # We want to crop it to be a square (w x w) from the top.
        square_h = w
        # Just to be safe, we'll crop a square starting from the top.
        cropped = img.crop((0, 0, w, square_h))
        cropped.save(f'nav_icon_{name}.png')
        print(f'Cropped {name}: {w}x{h} -> {w}x{square_h}')
    except Exception as e:
        print(f"Error on {name}: {e}")
