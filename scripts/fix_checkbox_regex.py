import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .vocab-checkbox
css = re.sub(r'\.vocab-checkbox\s*\{[^}]*\}', 
'''.vocab-checkbox {
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
}''', css)

# Replace .vocab-row.selected .vocab-checkbox
css = re.sub(r'\.vocab-row\.selected \.vocab-checkbox\s*\{[^}]*\}',
'''.vocab-row.selected .vocab-checkbox {
    background: var(--pink) !important;
    border-color: var(--text-primary) !important;
}''', css)

# Replace .vocab-row.selected .vocab-checkbox::after
css = re.sub(r'\.vocab-row\.selected \.vocab-checkbox::after\s*\{[^}]*\}',
'''.vocab-row.selected .vocab-checkbox::after {
    content: "X";
    color: var(--yellow) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 18px;
    font-weight: 900;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
}''', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
