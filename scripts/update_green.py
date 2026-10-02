with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the --green in dark mode
# Find [data-theme=dark] block and replace --green
import re
dark_block = re.search(r'\[data-theme=dark\]\s*\{.*?\}', css, re.DOTALL)
if dark_block:
    new_dark_block = dark_block.group(0).replace('--green: #9FC4A9;', '--green: #81c995;')
    css = css.replace(dark_block.group(0), new_dark_block)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
