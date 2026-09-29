import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_nav = '''.bottom-nav {
    background: rgba(247, 241, 231, 0.95) !important; /* Slightly transparent solid color, NOT glass */
}'''
new_nav = '''.bottom-nav {
    background: rgba(247, 241, 231, 0.6) !important;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-top: 1px solid rgba(247, 241, 231, 0.8);
}'''

if old_nav in css:
    css = css.replace(old_nav, new_nav)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
