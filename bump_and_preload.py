import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

preload_tags = '''<link rel="preload" as="image" href="bg_lesson_1.jpg">
  <link rel="preload" as="image" href="bg_lesson_2.jpg">
  <link rel="preload" as="image" href="bg_lesson_3.jpg">'''

if "bg_lesson_1.jpg" not in html:
    html = html.replace('<link rel="preload" as="image" href="bg_practice.jpg">', '<link rel="preload" as="image" href="bg_practice.jpg">\n  ' + preload_tags)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v43', sw)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
