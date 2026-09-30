with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'mock' in line.lower():
        print(f'{i}: {repr(line[:120])}')
