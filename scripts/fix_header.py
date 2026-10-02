import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the topbar html
topbar_pattern = re.compile(r'<header class="topbar">.*?</header>', re.DOTALL)
new_topbar = '''
  <header class="topbar">
    <div class="brand" onclick="showView('home')">
      <div class="brand-text">
        <div class="brand-jp">みんなのことば</div>
        <div class="brand-en">N5 JOURNEY</div>
      </div>
    </div>
    <div class="header-actions">
      <button id="themeBtn" class="icon-btn" aria-label="Toggle theme" onclick="toggleTheme()">\U0001F317</button>
    </div>
  </header>
'''
html = topbar_pattern.sub(new_topbar.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
