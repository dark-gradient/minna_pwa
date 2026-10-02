with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
m = re.search(r'<div id="omamori-nav" class="omamori-nav">.*?</nav>\s*</div>', html, re.DOTALL)
if m:
    print('Found HTML')
else:
    print('HTML not found')

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
m2 = re.search(r'/\* Omamori Navigation \*/.*?\.omamori-tray::after \{[^}]*\}', css, re.DOTALL)
if m2:
    print('Found CSS')
else:
    print('CSS not found')
