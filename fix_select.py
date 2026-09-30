import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find and print around controls-grid select
idx = css.find('controls-grid select')
if idx >= 0:
    print('Found at:', idx)
    print(repr(css[idx-5:idx+200]))
else:
    print('NOT FOUND')
    # show all select rules
    for m in re.finditer(r'select\s*\{[^}]*\}', css):
        print(m.group(0)[:100])
        print('---')
