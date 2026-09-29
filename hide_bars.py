import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''
body.welcome-active .topbar,
body.welcome-active .bottom-nav {
    display: none !important;
}
body.welcome-active {
    padding-bottom: 0 !important;
}
'''
css += new_css

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
