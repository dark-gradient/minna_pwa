with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
for m in re.finditer(r'<section id="([^"]+)"[^>]*class="([^"]+)"', html):
    if 'active' in m.group(2):
        print(f'{m.group(1)} is active')
