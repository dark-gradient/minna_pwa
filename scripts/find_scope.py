with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'scopeMode' in line or 'focus' in line:
        if 'focus' in line and 'renderFocus' not in line and 'focusView' not in line:
            pass # just checking focus logic
        print(f'{i}: {line.strip()}')
