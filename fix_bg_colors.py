import re
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the card background colors translucent
old_colors = '''.bg-green { background-color: var(--green-soft); }
.bg-pink { background-color: var(--pink); }
.bg-blue { background-color: var(--blue); }
.bg-yellow { background-color: var(--yellow); }'''
new_colors = '''.bg-green { background-color: #C9DCC7D9; }
.bg-pink { background-color: #F4A6A6D9; }
.bg-blue { background-color: #C9DCE4D9; }
.bg-yellow { background-color: #F3D99BD9; }'''

if old_colors in css:
    css = css.replace(old_colors, new_colors)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
