with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'controls-grid select' in line or ('select' in line and 'bg-primary' in line):
        print(f'{i}: {repr(line)}')
