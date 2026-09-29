import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Minna with hand-kerned spans
old_minna = '''Minna<br>Kotoba'''
new_minna = '''<span style="letter-spacing: -6px;">M</span><span style="letter-spacing: 0px;">I</span><span style="letter-spacing: 6px;">N</span><span style="letter-spacing: 4px;">N</span>A<br>KOTOBA'''
html = html.replace(old_minna, new_minna)

# Remove the pagination dots
dots = '''<div style="display: flex; gap: 8px; margin-top: 24px;">
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--pink);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
          </div>'''
html = html.replace(dots, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
