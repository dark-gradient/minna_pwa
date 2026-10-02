import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .vocab-en and .vocab-jp text colors
old_vocab_text = '''.vocab-row .vocab-en {
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
}'''

new_vocab_text = '''.vocab-row .vocab-en {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    font-size: 15px;
    text-align: right;
    line-height: 1.3;
    letter-spacing: 1px;
}
.vocab-row .vocab-jp {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
}'''

if old_vocab_text in css:
    css = css.replace(old_vocab_text, new_vocab_text)

# 2. Add custom styling for the checkboxes!
css += '''
/* Custom Checkboxes */
.vocab-row input[type="checkbox"] {
    appearance: none;
    -webkit-appearance: none;
    width: 24px;
    height: 24px;
    background: var(--yellow);
    border: 2px solid var(--text-primary);
    border-radius: 4px;
    cursor: pointer;
    position: relative;
    box-shadow: 2px 2px 0 var(--text-primary);
    margin-right: 12px;
}
.vocab-row input[type="checkbox"]:checked {
    background: var(--pink);
}
.vocab-row input[type="checkbox"]:checked::after {
    content: 'X';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: var(--yellow);
    font-family: 'DotGothic16', sans-serif;
    font-size: 18px;
    font-weight: 900;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary);
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
