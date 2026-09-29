import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix text shadows causing split letters. 
# Remove 3px 3px / 4px 4px offsets from headings
css = css.replace(', 4px 4px 0px var(--text-primary)', '')
css = css.replace(', 3px 3px 0px var(--text-primary)', '')
css = css.replace(', 2px 2px 0px var(--text-primary)', '')

# Add letter-spacing to .big-number to prevent overlap
old_bignum = '''.big-number {
    font-size: 34px !important;'''
new_bignum = '''.big-number {
    letter-spacing: 2px !important;
    font-size: 34px !important;'''
if old_bignum in css:
    css = css.replace(old_bignum, new_bignum)

# 2. Make vocab rows translucent
old_vocab = '''.vocab-row {
    background: var(--surface);'''
new_vocab = '''.vocab-row {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    border: 2px solid var(--border) !important;'''
if old_vocab in css:
    css = css.replace(old_vocab, new_vocab)

# .vocab-row text color
old_vocab_text = '''.vocab-row .vocab-en {
    color: var(--text-secondary);
    font-size: 13px;
    text-align: right;
    line-height: 1.3
}'''
new_vocab_text = '''.vocab-row .vocab-en {
    color: var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px;
    text-align: right;
    line-height: 1.3
}
.vocab-row .vocab-jp {
    color: var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
}
'''
if old_vocab_text in css:
    css = css.replace(old_vocab_text, new_vocab_text)

# Also style #detailHeader h1 and eyebrow to match the pink/yellow guidelines
css += '''
.detail-header h1 {
    color: var(--pink) !important;
    -webkit-text-stroke: 0px !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 42px !important;
    margin: 12px 0 !important;
}
.detail-header .eyebrow {
    color: var(--yellow) !important;
    font-weight: 800;
    -webkit-text-stroke: 0px !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-size: 18px !important;
    letter-spacing: 2px;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
