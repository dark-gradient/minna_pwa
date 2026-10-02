import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_en = '''.vocab-en {
    color: var(--pink);
    font-size: 13px;
    text-align: right;
    font-weight: 700;
    text-shadow: 0 1px 2px rgba(0,0,0,0.18);
}'''

new_en = '''.vocab-en {
    color: var(--yellow);
    background: var(--pink);
    font-size: 13px;
    text-align: right;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 5px;
    display: inline-block;
}'''

css = css.replace(old_en, new_en)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v59', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
