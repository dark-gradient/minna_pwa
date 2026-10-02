import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.page-head {\n    padding-top: 24px !important;\n}', '.page-head {\n    padding-top: 12px !important;\n}')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
