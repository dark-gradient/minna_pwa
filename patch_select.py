with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if '.controls-grid select {' in line:
        # Replace the whole block
        new_lines.append('.controls-grid select {\n')
        new_lines.append('    height: 44px;\n')
        new_lines.append('    border: 2px solid var(--text-primary) !important;\n')
        new_lines.append('    border-radius: 8px;\n')
        new_lines.append('    padding: 0 12px;\n')
        new_lines.append('    background: var(--yellow) !important;\n')
        new_lines.append('    color: var(--text-primary) !important;\n')
        new_lines.append("    font-family: 'DotGothic16', sans-serif !important;\n")
        new_lines.append('    font-weight: 800 !important;\n')
        new_lines.append('    outline: none;\n')
        new_lines.append('    box-shadow: 2px 2px 0 var(--text-primary) !important;\n')
        new_lines.append('}\n')
        # Skip original block lines until closing brace
        i += 1
        while i < len(lines) and '}' not in lines[i]:
            i += 1
        i += 1  # skip the closing brace line
    elif 'select option {' in line:
        new_lines.append('select option {\n')
        new_lines.append('    background: #F3D99B !important;\n')
        new_lines.append('    color: #17252A !important;\n')
        new_lines.append("    font-family: 'DotGothic16', sans-serif !important;\n")
        new_lines.append('    font-weight: 700 !important;\n')
        new_lines.append('}\n')
        i += 1
        while i < len(lines) and '}' not in lines[i]:
            i += 1
        i += 1
    else:
        new_lines.append(line)
        i += 1

with open('styles.css', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v72', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
