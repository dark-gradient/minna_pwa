with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    if '<section ' in line:
        print(line.strip())
