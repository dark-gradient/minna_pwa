with open('app.js', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'vocab-row' in line or 'vocab-en' in line or 'focusWords' in line:
            print(f'{i}: {line}', end='')
