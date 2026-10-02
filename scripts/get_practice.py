with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines, 1):
    if '<section id="practiceSetupView"' in line:
        start = i
        break
for i in range(start, start+40):
    if '</section>' in lines[i-1]:
        print(lines[i-1].strip())
        break
    print(lines[i-1].strip())
