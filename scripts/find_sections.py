with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'section' in line.lower() or 'panel' in line.lower() or 'mock' in line.lower() or 'practice' in line.lower():
            print(f'{i}: {line}', end='')
