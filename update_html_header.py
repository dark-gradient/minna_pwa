import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add decorative element under MINNA KOTOBA if it doesn't exist
if 'omamori-header-decor' not in html:
    html = html.replace(
        '<span class="omamori-header-title">MINNA KOTOBA</span>',
        '<span class="omamori-header-title">MINNA KOTOBA</span>\n          <div class="omamori-header-decor">✿</div>'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
