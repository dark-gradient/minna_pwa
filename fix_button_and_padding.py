import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix .app-shell padding to avoid text getting cut on the left, and enable scrolling
old_appshell = '''    body, .app-shell {
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        max-width: 100% !important;
        max-height: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
    }'''
new_appshell = '''    body, .app-shell {
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 5vw !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        max-width: 100% !important;
        max-height: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
    }
    body.welcome-active, body.welcome-active .app-shell {
        overflow: hidden !important;
        padding: 0 !important;
    }'''
if old_appshell in css:
    css = css.replace(old_appshell, new_appshell)
else:
    # try the current state which might already have overflow-y: auto
    old_appshell2 = '''    body, .app-shell {
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        max-width: 100% !important;
        max-height: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
    }'''
    if old_appshell2 in css:
        css = css.replace(old_appshell2, new_appshell)

# 2. Fix the primary button theme globally
old_btn = '''.primary-btn {
    background: var(--pink);
    color: white;
    box-shadow: 0 8px 18px #b7433630
}'''
new_btn = '''.primary-btn {
    background: var(--pink) !important;
    color: var(--text-primary) !important;
    border: 3px solid var(--text-primary) !important;
    border-radius: 12px !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    box-shadow: 4px 4px 0px var(--text-primary) !important;
}'''

if old_btn in css:
    css = css.replace(old_btn, new_btn)

old_btn_hover = '''.primary-btn:hover {
    background: var(--peach);
    transform: translateY(-1px)
}'''
new_btn_hover = '''.primary-btn:hover {
    background: var(--yellow) !important;
    color: var(--text-primary) !important;
    transform: translate(2px, 2px) !important;
    box-shadow: 2px 2px 0px var(--text-primary) !important;
}'''
if old_btn_hover in css:
    css = css.replace(old_btn_hover, new_btn_hover)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
