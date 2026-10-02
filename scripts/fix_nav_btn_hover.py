import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css += '''
.nav-btn.active, .nav-btn:hover {
    background: rgba(253, 251, 247, 0.25) !important;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
