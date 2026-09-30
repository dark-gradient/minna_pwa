with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'showView' in line:
        print(f'{i}: {line.strip()}')
