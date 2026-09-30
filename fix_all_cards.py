import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix bottom-nav: remove the display:none override and ensure translucent
css = css.replace(
    '.bottom-nav {\n    display: none !important;\n}',
    '/* bottom-nav display controlled by media query */'
)

# 2. quiz-card - make translucent
css = css.replace(
    '.quiz-card {\n    max-width: 820px;\n    margin: 0 auto;\n    background: var(--surface);\n    border: 1px solid var(--border);\n    border-radius: 25px;\n    box-shadow: var(--shadow);\n    min-height: 450px;\n    padding: 42px;\n    display: flex;\n    flex-direction: column;\n    align-items: center;\n    justify-content: center;\n    text-align: center\n}',
    '.quiz-card {\n    max-width: 820px;\n    margin: 0 auto;\n    background: rgba(253, 251, 247, 0.65);\n    border: 2px solid var(--border);\n    border-radius: 25px;\n    box-shadow: var(--shadow);\n    min-height: 450px;\n    padding: 42px;\n    display: flex;\n    flex-direction: column;\n    align-items: center;\n    justify-content: center;\n    text-align: center\n}'
)

# 3. lesson-card - make translucent + pink/yellow text
css = css.replace(
    '.lesson-card {\n    color: var(--text-primary);\n    border: 1px solid var(--border);\n    background: var(--surface);\n    border-radius: 18px;\n    padding: 20px;\n    cursor: pointer;\n    text-align: left;\n    transition: .18s\n}',
    '.lesson-card {\n    color: var(--text-primary);\n    border: 2px solid var(--border);\n    background: rgba(253, 251, 247, 0.65);\n    border-radius: 18px;\n    padding: 20px;\n    cursor: pointer;\n    text-align: left;\n    transition: .18s;\n    box-shadow: 3px 3px 0 var(--text-primary);\n}'
)

# 4. progress-card (N5 progress) - translucent
css = css.replace(
    '.progress-card {\n    background: var(--surface);\n    border: 2px solid var(--border-strong);\n    border-radius: 20px;\n    padding: 24px;\n    box-shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);\n}',
    '.progress-card {\n    background: rgba(253, 251, 247, 0.65);\n    border: 2px solid var(--border-strong);\n    border-radius: 20px;\n    padding: 24px;\n    box-shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);\n}'
)

# 5. bottom-nav first definition - ensure translucent
css = css.replace(
    '.bottom-nav {\n    position: fixed;\n    bottom: 0;\n    left: 0;\n    right: 0;\n    height: 80px;\n    background: var(--bg-primary);\n    border-top: 2px solid var(--border-strong);\n    display: flex;\n    justify-content: space-around;\n    align-items: flex-start;\n    padding-top: 10px;\n    padding-bottom: env(safe-area-inset-bottom, 10px);\n    z-index: 1000;\n}',
    '.bottom-nav {\n    position: fixed;\n    bottom: 0;\n    left: 0;\n    right: 0;\n    height: 80px;\n    background: rgba(253, 251, 247, 0.75) !important;\n    border-top: 2px solid var(--border-strong);\n    display: flex;\n    justify-content: space-around;\n    align-items: flex-start;\n    padding-top: 10px;\n    padding-bottom: env(safe-area-inset-bottom, 10px);\n    z-index: 1000;\n}'
)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v69', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
