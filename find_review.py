with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if 'renderReview' in line or 'review' in line:
        pass

start = -1
for i, line in enumerate(lines, 1):
    if 'function renderReview' in line:
        start = i
        break

if start != -1:
    for i in range(start, min(start + 20, len(lines))):
        print(lines[i-1].strip())
