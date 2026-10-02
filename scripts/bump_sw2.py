import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v29', sw)
# Also add fuji.jpg to cache list
if '"fuji.jpg"' not in sw:
    sw = sw.replace('"app.js",', '"app.js",\n  "fuji.jpg",')

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
