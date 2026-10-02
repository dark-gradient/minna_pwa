import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<nav class="bottom-nav">[\s\S]*?</nav>', html)
if m: print(m.group(0))
