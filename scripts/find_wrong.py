with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'wrongList' in line or 'renderWrong' in line or 'renderReview' in line or 'wrong-list' in line:
        print(f'{i}: {repr(line[:120])}')
