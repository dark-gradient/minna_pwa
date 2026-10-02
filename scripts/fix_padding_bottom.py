import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_str = "padding: 0 5vw !important;"
new_str = "padding: 0 5vw 90px 5vw !important;"

if old_str in css:
    css = css.replace(old_str, new_str)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
