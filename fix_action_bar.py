import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the original focus-action-bar CSS
old_action_bar = r'\.focus-action-bar\s*\{[^}]*\}'
old_visible = r'\.focus-action-bar\.visible\s*\{[^}]*\}'

new_action_bar = '''\.focus-action-bar {
    position: fixed;
    bottom: -150px;
    left: 16px;
    right: 16px;
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px) !important;
    -webkit-backdrop-filter: blur(4px) !important;
    border: 2px solid var(--text-primary) !important;
    border-radius: 8px !important;
    padding: 12px 16px !important;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
    z-index: 100;
    transition: bottom 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
}
.focus-action-bar .primary-btn {
    background: var(--pink) !important;
    color: var(--yellow) !important;
    border: 2px solid var(--text-primary) !important;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
}
.focus-action-bar .primary-btn:hover {
    background: var(--yellow) !important;
    color: var(--pink) !important;
}'''

new_visible = '''.focus-action-bar.visible {
    bottom: 96px;
}'''

css = re.sub(old_action_bar, new_action_bar, css, count=1)
css = re.sub(old_visible, new_visible, css)

# There is a duplicate definition in styles.css:
# .focus-action-bar { box-shadow: 0 -10px 25px rgba(0,0,0,0.5); }
# I'll just remove it entirely
css = re.sub(r'\.focus-action-bar\s*\{\s*box-shadow:[^}]*\}\n', '', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
