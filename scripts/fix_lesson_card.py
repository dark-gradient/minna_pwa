import re
with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    # Only target the first .lesson-card block (line 527)
    if line.strip() == '.lesson-card {' and i < 540:
        new_lines.append('.lesson-card {\n')
        new_lines.append('    color: var(--text-primary);\n')
        new_lines.append('    border: 2px solid var(--text-primary) !important;\n')
        new_lines.append('    background: rgba(244, 166, 166, 0.35) !important;\n')
        new_lines.append('    border-radius: 18px;\n')
        new_lines.append('    padding: 20px;\n')
        new_lines.append('    cursor: pointer;\n')
        new_lines.append('    text-align: left;\n')
        new_lines.append('    transition: .18s;\n')
        new_lines.append('    box-shadow: 3px 3px 0 var(--text-primary) !important;\n')
        new_lines.append('}\n')
        # Skip original block
        i += 1
        while i < len(lines) and lines[i].strip() != '}':
            i += 1
        i += 1  # skip closing brace
    else:
        new_lines.append(line)
        i += 1

with open('styles.css', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v73', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
