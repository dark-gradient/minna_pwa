with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'section id=' in line or 'controls-grid' in line or 'past' in line.lower() or 'mock' in line.lower():
        try:
            print(f'{i}: {repr(line[:120])}')
        except:
            pass
