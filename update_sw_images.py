import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

# I will add the images to the PRECACHE_URLS array
images_to_add = '''  "bg_home.jpg",
  "bg_learn.jpg",
  "bg_practice.jpg",
  "bg_more.jpg",'''

if "bg_home.jpg" not in sw:
    sw = sw.replace('"fuji_wide.jpg",', '"fuji_wide.jpg",\n' + images_to_add)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
