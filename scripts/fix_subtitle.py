import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_subtitle = '''.detail-header p {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-family: 'DotGothic16', sans-serif !important;
    letter-spacing: 1px;
}'''

new_subtitle = '''.detail-header p {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-family: 'DotGothic16', sans-serif !important;
    letter-spacing: 1px;
    background: rgba(253, 251, 247, 0.7) !important;
    backdrop-filter: blur(4px) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    display: inline-block;
    padding: 6px 12px;
    border-radius: 4px;
    border: 2px solid var(--text-primary) !important;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
    margin-top: 8px !important;
}'''

if old_subtitle in css:
    css = css.replace(old_subtitle, new_subtitle)
else:
    print("Could not find exact old_subtitle")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
