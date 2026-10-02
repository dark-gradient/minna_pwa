import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will find the top-level block I added and add !important to ensure it overrides the 1180px later in the file.
old_str = '''    body, .app-shell {
        display: block;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden !important;
        max-width: 100%;
        max-height: 100%;
        border-radius: 0;
        border: none;
        box-shadow: none;
    }'''
new_str = '''    body, .app-shell {
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        max-width: 100% !important;
        max-height: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
    }'''

if old_str in css:
    css = css.replace(old_str, new_str)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
