with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = -1
for i, line in enumerate(lines, 1):
    if 'practiceSetupView' in line:
        start = i
        break

if start != -1:
    for i in range(start, min(start + 30, len(lines))):
        print(f'{i}: {lines[i-1].strip()}')
