import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove footer
html = re.sub(r'<footer>.*?</footer>', '', html, flags=re.DOTALL)

# Update Bottom Nav icons
new_nav = '''  <nav class="bottom-nav">
    <button data-view="home" class="nav-btn active">
      <div class="nav-icon">🏠</div>
      <span>Home</span>
    </button>
    <button data-view="lessons" class="nav-btn">
      <div class="nav-icon">📖</div>
      <span>Learn</span>
    </button>
    <button data-view="practiceSetup" class="nav-btn">
      <div class="nav-icon">📊</div>
      <span>Practice</span>
    </button>
    <button data-view="mockTest" class="nav-btn">
      <div class="nav-icon">☑️</div>
      <span>Mock Test</span>
    </button>
    <button data-view="more" class="nav-btn">
      <div class="nav-icon">⊞</div>
      <span>More</span>
    </button>
  </nav>'''

html = re.sub(r'<nav class="bottom-nav">.*?</nav>', new_nav, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
