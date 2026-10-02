with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

lines = js.splitlines()[-50:]
for i, line in enumerate(lines):
    print(f'{i}: {line}')
