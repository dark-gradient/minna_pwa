with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

lines = css.split('\n')
for i, line in enumerate(lines):
    if '.panel {' in line or '.panel.setup {' in line:
        for j in range(i, i+15):
            print(lines[j])
            if '}' in lines[j]: break
