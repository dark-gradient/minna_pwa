with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

for line in css.split('\n'):
    if 'background-image' in line or 'bg_' in line or '-active' in line:
        print(line.strip())
