with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix Topbar display
import re
css = re.sub(r'/\* Topbar Hide \(Mobile First\) \*/\s*\.topbar\s*\{\s*display:\s*none;\s*\}', 
'''/* Topbar Redesign */
.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 20px;
    background: var(--bg-primary);
    border-bottom: 2px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 100;
}
.brand { display: flex; align-items: center; cursor: pointer; }
.brand-jp { font-size: 16px; font-weight: 800; color: var(--text-primary); font-family: 'Noto Sans JP'; }
.brand-en { font-size: 10px; font-weight: 700; color: var(--text-secondary); letter-spacing: 1px; }
.header-actions { display: flex; align-items: center; }
.icon-btn { background: none; border: none; font-size: 24px; cursor: pointer; color: var(--text-primary); }
''', css)

# 2. Fix Nav Btn Active Color (Black on pink)
css = css.replace('.nav-btn.active {\n    color: var(--text-primary);\n    background: var(--pink);\n}', 
'''.nav-btn.active {
    color: #17252A; /* Black on pink even in dark mode */
    background: var(--pink);
}''')

# 3. Fix Test Badge Color (Black on pink)
css = css.replace('.test-badge {\n    display: inline-block;\n    background: var(--pink);\n    color: var(--text-primary);',
'''.test-badge {
    display: inline-block;
    background: var(--pink);
    color: #17252A;''')


with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
