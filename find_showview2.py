with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines, 1):
    if 'function showView(view)' in line:
        start = i
        break
for i in range(start, start + 30):
    print(lines[i-1].strip())
