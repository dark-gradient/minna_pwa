import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v33', sw)

# Ensure fuji_wide.jpg is cached
if '"fuji_wide.jpg"' not in sw:
    sw = sw.replace('"fuji.jpg",', '"fuji_wide.jpg",\n  "fuji.jpg",')

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
