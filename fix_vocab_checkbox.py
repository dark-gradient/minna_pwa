import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_checkbox = '''.vocab-checkbox {
    width: 22px;
    height: 22px;
    border: 2px solid var(--text-secondary);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 12px;
    background: var(--surface);
}'''
new_checkbox = '''.vocab-checkbox {
    width: 24px;
    height: 24px;
    border: 2px solid var(--text-primary) !important;
    border-radius: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 12px;
    background: var(--yellow) !important;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
}'''

if old_checkbox in css:
    css = css.replace(old_checkbox, new_checkbox)

old_checkbox_selected = '''.vocab-row.selected .vocab-checkbox {
    background: var(--pink);
    border-color: var(--pink);
}
.vocab-row.selected .vocab-checkbox::after {
    content: "🌸";
    font-size: 14px;
}'''
new_checkbox_selected = '''.vocab-row.selected .vocab-checkbox {
    background: var(--pink) !important;
    border-color: var(--text-primary) !important;
}
.vocab-row.selected .vocab-checkbox::after {
    content: "X";
    color: var(--yellow) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 18px;
    font-weight: 900;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
}'''

if old_checkbox_selected in css:
    css = css.replace(old_checkbox_selected, new_checkbox_selected)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
