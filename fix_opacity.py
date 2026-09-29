import re
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('rgba(253, 251, 247, 0.45)', 'rgba(253, 251, 247, 0.35)')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v53', sw)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
