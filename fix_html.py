import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract dashboard from welcomeView
dashboard_pattern = re.compile(r'\s*<div class="dashboard">.*?</div>\s*</div>\s*', re.DOTALL)
match = dashboard_pattern.search(html)

if match:
    dashboard_html = match.group(0)
    # Remove it from where it is
    html = html.replace(dashboard_html, '\n')
    
    # Insert it into homeView right after the hidden hero
    hero_pattern = r'<div class="hero".*?</div>\s*</div>'
    hero_match = re.search(hero_pattern, html, re.DOTALL)
    if hero_match:
        html = html.replace(hero_match.group(0), hero_match.group(0) + '\n' + dashboard_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
