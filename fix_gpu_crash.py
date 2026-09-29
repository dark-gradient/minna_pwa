import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove backdrop-filter from vocab-row
css = re.sub(r'backdrop-filter:\s*blur\([^)]+\)\s*!important;\n\s*-webkit-backdrop-filter:\s*blur\([^)]+\)\s*!important;', '', css)
css = re.sub(r'backdrop-filter:\s*blur\([^)]+\);\n\s*-webkit-backdrop-filter:\s*blur\([^)]+\);', '', css)

# Wait, let's be more precise
old_vocab_row = '''\.vocab-row {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    border: 2px solid var(--border) !important;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 13px 15px;
    display: flex;
    justify-content: space-between;
    gap: 18px
}'''
new_vocab_row = '''.vocab-row {
    background: rgba(253, 251, 247, 0.65) !important;
    border: 2px solid var(--border) !important;
    border-radius: 12px;
    padding: 13px 15px;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    transform: translateZ(0); /* Hardware acceleration */
}'''

if old_vocab_row in css:
    print("Failed to replace old_vocab_row directly (regex needed)")
    
css = re.sub(r'\.vocab-row\s*\{[^}]*\}', new_vocab_row, css, count=1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
