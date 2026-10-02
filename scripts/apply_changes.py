import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Opacity from 0.75 -> 0.65
css = css.replace('rgba(253, 251, 247, 0.75)', 'rgba(253, 251, 247, 0.65)')

# 2. Focus badge -> bright pink
old_badge = '''.focus-badge {
    font-size: 10px;
    background: var(--yellow);
    color: var(--bg-primary);
    padding: 3px 7px;
    border-radius: 6px;
    font-weight: 800;
    text-transform: uppercase;
    margin-left: 8px;
    display: inline-block;
    vertical-align: middle;
}'''
new_badge = '''.focus-badge {
    font-size: 10px;
    background: #ff2d78;
    color: #fff;
    border: 2px solid #fff;
    padding: 3px 7px;
    border-radius: 6px;
    font-weight: 800;
    text-transform: uppercase;
    margin-left: 8px;
    display: inline-block;
    vertical-align: middle;
    text-shadow: 0 1px 2px rgba(0,0,0,0.5);
}'''
css = css.replace(old_badge, new_badge)

# Remove the duplicate .focus-badge override
css = re.sub(r'\.focus-badge \{\s*color: #171a1d;\s*\}', '', css)

# 3. vocab-en -> pink with text-shadow for legibility
old_en = '''.vocab-en {
    color: var(--text-secondary);
    font-size: 13px;
    text-align: right
}'''
new_en = '''.vocab-en {
    color: #ff2d78;
    font-size: 13px;
    text-align: right;
    font-weight: 700;
    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
}'''
css = css.replace(old_en, new_en)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Bump SW
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v57', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
