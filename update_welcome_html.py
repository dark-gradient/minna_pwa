import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the img wrapper div from welcomeView
html = re.sub(r'<div style="flex: 1; display: flex; align-items: center; justify-content: center; position: relative; margin: 20px 0;">\s*<img src="fuji.jpg".*?>\s*</div>', '<div style="flex: 1;"></div>', html, flags=re.DOTALL)

# Make welcome-container background transparent
html = html.replace('background: var(--bg-primary); overflow: hidden; padding-bottom: 40px;"', 'background: transparent; overflow: hidden; padding-bottom: 40px;"')

# Ensure the title has text-shadow to be readable against Mount Fuji
html = html.replace('<h1 style="font-family: \'Courier New\', monospace; font-weight: 900; font-size: 52px; line-height: 1; margin: 0; color: var(--text-primary); text-transform: uppercase;">', '<h1 style="font-family: \'DotGothic16\', sans-serif; font-weight: 900; font-size: 52px; line-height: 1; margin: 0; color: var(--text-primary); text-transform: uppercase; text-shadow: 2px 2px 0px #F7F1E7, -1px -1px 0px #F7F1E7, 1px -1px 0px #F7F1E7, -1px 1px 0px #F7F1E7, 1px 1px 0px #F7F1E7;">')

# Ensure subtitles also have text-shadow
html = html.replace('<div style="font-weight: 800; font-size: 14px; margin-top: 12px; color: var(--text-primary);">', '<div style="font-family: \'DotGothic16\', sans-serif; font-weight: 800; font-size: 14px; margin-top: 12px; color: var(--text-primary); text-shadow: 2px 2px 0px #F7F1E7, -1px -1px 0px #F7F1E7, 1px -1px 0px #F7F1E7, -1px 1px 0px #F7F1E7, 1px 1px 0px #F7F1E7;">')
html = html.replace('<p style="font-family: \'Courier New\', monospace; font-size: 13px; font-weight: 700; margin-top: 24px; color: var(--text-primary);">', '<p style="font-family: \'DotGothic16\', sans-serif; font-size: 13px; font-weight: 700; margin-top: 24px; color: var(--text-primary); text-shadow: 2px 2px 0px #F7F1E7, -1px -1px 0px #F7F1E7, 1px -1px 0px #F7F1E7, -1px 1px 0px #F7F1E7, 1px 1px 0px #F7F1E7;">')

# Replace Courier New in button
html = html.replace('font-family: \'Courier New\'', 'font-family: \'DotGothic16\'')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
