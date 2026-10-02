import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix opacity in styles.css
old_opacity = '''    background: rgba(253, 251, 247, 0.7) !important;'''
new_opacity = '''    background: rgba(253, 251, 247, 0.35) !important;'''
if old_opacity in css:
    css = css.replace(old_opacity, new_opacity)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix text in app.js
# The script output showed a  because of the • character (bullet) not matching ASCII. We use regex to match it.
js = re.sub(r'<p>\$\{VOCAB\[n\]\.length\} vocabulary entries .*? separate from Kaiwa\.</p>',
           r'<p> vocabulary entries</p>', js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
