import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '<section id="homeView"' in html:
    print('homeView exists')
else:
    print('homeView missing')

print(f"File length: {len(html)}")
