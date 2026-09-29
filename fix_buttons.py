import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix select box ("normal" text) to be a pink card
old_select = '''#lessonDetailView select {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px) !important;
    border: 2px solid var(--text-primary) !important;
    color: var(--yellow) !important;'''
new_select = '''#lessonDetailView select {
    background: var(--pink) !important;
    backdrop-filter: none !important;
    border: 2px solid var(--text-primary) !important;
    color: var(--yellow) !important;'''
if old_select in css:
    css = css.replace(old_select, new_select)

# Fix Select All / Clear Selection buttons to be translucent cards
old_buttons = '''#lessonDetailView label, #lessonSelectionControls button {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    font-size: 16px !important;
    opacity: 1 !important;
}
#lessonSelectionControls button:hover {
    color: var(--yellow) !important;
}'''

new_buttons = '''#lessonDetailView label {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    font-size: 16px !important;
    opacity: 1 !important;
}

#lessonSelectionControls button {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    border: 2px solid var(--text-primary) !important;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
    border-radius: 4px;
    padding: 6px 12px !important;
    margin-right: 8px;
    margin-bottom: 8px;
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    font-size: 14px !important;
    opacity: 1 !important;
}
#lessonSelectionControls button:hover {
    background: var(--yellow) !important;
    color: var(--pink) !important;
}'''

if old_buttons in css:
    css = css.replace(old_buttons, new_buttons)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
