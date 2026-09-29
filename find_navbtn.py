import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for m in re.finditer(r'class="[^"]*nav-btn[^"]*"', html):
    start = max(0, m.start() - 50)
    end = min(len(html), m.end() + 50)
    print(html[start:end])
