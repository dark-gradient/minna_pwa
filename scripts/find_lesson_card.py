with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'lesson-card' in line:
        print(f'{i}: {repr(line[:80])}')
