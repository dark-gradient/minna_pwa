import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v30', sw)

# Add new backgrounds to cache
if '"bg_home.jpg"' not in sw:
    sw = sw.replace('"fuji.jpg",', '"fuji.jpg",\n  "bg_home.jpg",\n  "bg_learn.jpg",\n  "bg_practice.jpg",\n  "bg_more.jpg",')

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
