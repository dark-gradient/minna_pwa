import re

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

images_to_add = '''  "bg_lesson_1.jpg",
  "bg_lesson_2.jpg",
  "bg_lesson_3.jpg",'''

if "bg_lesson_1.jpg" not in sw:
    sw = sw.replace('"bg_more.jpg",', '"bg_more.jpg",\n' + images_to_add)

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v42', sw)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
