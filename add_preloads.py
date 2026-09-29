import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

preloads = '''
  <link rel="preload" as="image" href="fuji_wide.jpg">
  <link rel="preload" as="image" href="bg_home.jpg">
  <link rel="preload" as="image" href="bg_learn.jpg">
  <link rel="preload" as="image" href="bg_practice.jpg">
  <link rel="preload" as="image" href="bg_more.jpg">
</head>'''

if 'bg_home.jpg' not in html:
    html = html.replace('</head>', preloads)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
