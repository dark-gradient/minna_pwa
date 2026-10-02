import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hardcoded #ff2d78 with the UI pink variable
css = css.replace('background: #ff2d78;', 'background: var(--pink);')
css = css.replace('color: #ff2d78;', 'color: var(--pink);')
# Remove the white text-shadow outline on vocab-en (not needed for softer pink)
css = css.replace(
    '    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;',
    '    text-shadow: 0 1px 2px rgba(0,0,0,0.18);'
)
# focus-badge: dark text on soft pink background looks better
css = css.replace('    color: #fff;\n    border: 2px solid #fff;\n', '    color: #17252A;\n    border: 2px solid #17252A;\n')
css = css.replace('    text-shadow: 0 1px 2px rgba(0,0,0,0.5);', '    text-shadow: none;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v58', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
