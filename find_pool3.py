with open('app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(275, min(300, len(lines))):
    print(lines[i-1].strip())
