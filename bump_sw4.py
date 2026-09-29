import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()

sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v31', sw)

with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
