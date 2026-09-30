with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
m = re.search(r'function showView\(.*?\).*?}', js, re.DOTALL)
if m:
    print(m.group(0))
