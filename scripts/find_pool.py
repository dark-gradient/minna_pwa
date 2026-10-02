with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
start = -1
for i, line in enumerate(lines, 1):
    if 'function getPracticePool()' in line:
        start = i
        break
if start != -1:
    for i in range(start, min(start + 25, len(lines))):
        print(lines[i-1].strip())
