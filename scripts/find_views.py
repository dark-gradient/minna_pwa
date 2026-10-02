with open('old_index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
views = re.findall(r'<section id="(.*?)"', html)
print("Views:", views)
