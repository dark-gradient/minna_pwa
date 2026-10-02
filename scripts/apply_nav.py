import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

omamori_html = """
  <div id="omamori-nav" class="omamori-nav">
    <div class="omamori-overlay" onclick="toggleOmamoriNav()"></div>
    <button id="omamori-tag" class="omamori-tag" aria-expanded="false" aria-label="Toggle Navigation" onclick="toggleOmamoriNav()">
      <div class="omamori-cord">
        <div class="omamori-knot">🎀</div>
        <div class="omamori-bell">🔔</div>
      </div>
      <div class="omamori-body">🌸</div>
    </button>
    <nav id="omamori-tray" class="omamori-tray" aria-hidden="true">
      <ul class="omamori-menu">
        <li><button class="omamori-btn" data-view="lessons" onclick="showView('lessons'); toggleOmamoriNav();"><span class="omamori-icon">📜</span> <span>Lessons</span></button></li>
        <li><button class="omamori-btn" data-view="focus" onclick="showView('focus'); toggleOmamoriNav();"><span class="omamori-icon">🎴</span> <span>Vocabulary</span></button></li>
        <li><button class="omamori-btn" data-view="kaiwa" onclick="showView('kaiwa'); toggleOmamoriNav();"><span class="omamori-icon">📝</span> <span>Grammar</span></button></li>
        <li><button class="omamori-btn" data-view="practiceSetup" onclick="showView('practiceSetup'); toggleOmamoriNav();"><span class="omamori-icon">🖌️</span> <span>Kanji</span></button></li>
        <li><button class="omamori-btn" data-view="home" onclick="showView('home'); toggleOmamoriNav();"><span class="omamori-icon">🎧</span> <span>Listening</span></button></li>
        <li><button class="omamori-btn" data-view="mockTest" onclick="showView('mockTest'); toggleOmamoriNav();"><span class="omamori-icon">💮</span> <span>Mock Tests</span></button></li>
        <li><button class="omamori-btn" data-view="review" onclick="showView('review'); toggleOmamoriNav();"><span class="omamori-icon">⭐</span> <span>Review</span></button></li>
      </ul>
    </nav>
  </div>
"""

# Insert before </main> if possible, or before </div> <script src="app.js">
if '  </main>' in html:
    html = html.replace('  </main>', omamori_html + '\n  </main>')
else:
    html = html.replace('<script src="app.js"></script>', omamori_html + '\n<script src="app.js"></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

omamori_css = """
/* Omamori Navigation */
.omamori-nav {
  position: fixed;
  top: 80px;
  right: 0;
  z-index: 2000;
}

.omamori-tag {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  position: absolute;
  top: 0;
  right: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2002;
  transition: transform 0.2s;
}

.omamori-tag:hover {
  transform: translateY(-2px);
}

.omamori-cord {
  position: relative;
  font-size: 28px;
  line-height: 1;
  z-index: 2;
  margin-bottom: -10px;
  filter: drop-shadow(1px 1px 0 #17252A) drop-shadow(-1px -1px 0 #17252A);
}

.omamori-bell {
  position: absolute;
  bottom: -4px;
  right: -12px;
  font-size: 18px;
}

.omamori-body {
  width: 36px;
  height: 60px;
  background: var(--pink);
  border: 2px solid #17252A;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 2px 2px 0 rgba(23, 37, 42, 0.2);
  color: #fff;
  text-shadow: 1px 1px 0 #17252A;
}

.omamori-tray {
  position: absolute;
  top: -20px;
  right: -260px;
  width: 240px;
  background: #FDFBF7;
  border: 2px solid #17252A;
  border-right: none;
  border-radius: 12px 0 0 12px;
  padding: 40px 16px 20px 16px;
  box-shadow: -4px 4px 0 rgba(23, 37, 42, 0.2);
  transition: right 0.2s ease-in;
  z-index: 2001;
}

.omamori-nav.open .omamori-tray {
  right: 0;
  animation: trayJiggle 0.45s ease-out forwards;
}

.omamori-nav.open .omamori-tag {
  animation: tagJiggle 0.45s ease-out forwards;
}

@keyframes trayJiggle {
  0% { right: -260px; }
  60% { right: 12px; }
  80% { right: -4px; }
  100% { right: 0; }
}

@keyframes tagJiggle {
  0% { right: 16px; }
  60% { right: 28px; }
  80% { right: 12px; }
  100% { right: 16px; }
}

@media (prefers-reduced-motion: reduce) {
  .omamori-nav.open .omamori-tray {
    animation: none;
    right: 0;
    transition: right 0.2s ease-out;
  }
  .omamori-nav.open .omamori-tag {
    animation: none;
  }
}

.omamori-menu {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.omamori-btn {
  width: 100%;
  background: transparent;
  border: 2px solid transparent;
  border-radius: 8px;
  padding: 12px 12px;
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: 'DotGothic16', sans-serif;
  font-size: 16px;
  font-weight: 700;
  color: #17252A;
  cursor: pointer;
  text-align: left;
  transition: all 0.2s;
}

.omamori-btn:hover, .omamori-btn:focus-visible {
  background: rgba(244, 166, 166, 0.2);
  border-color: rgba(244, 166, 166, 0.5);
  outline: none;
}

.omamori-btn.active {
  background: rgba(244, 166, 166, 0.4);
  border-color: #17252A;
  box-shadow: 2px 2px 0 #17252A;
  color: #17252A;
}

.omamori-icon {
  font-size: 20px;
  filter: drop-shadow(1px 1px 0 #fff) drop-shadow(-1px -1px 0 #fff);
}

.omamori-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.1);
  z-index: 1999;
  display: none;
  opacity: 0;
  transition: opacity 0.2s;
}

.omamori-nav.open .omamori-overlay {
  display: block;
  opacity: 1;
}

.omamori-tray::before {
  content: '🌸';
  position: absolute;
  top: 10px;
  left: 10px;
  font-size: 24px;
  opacity: 0.8;
}
.omamori-tray::after {
  content: '🌸';
  position: absolute;
  bottom: 10px;
  right: 10px;
  font-size: 24px;
  opacity: 0.8;
}
"""

if 'omamori-nav' not in css:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write('\n' + omamori_css)


# 3. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update querySelectorAll(".nav-btn") to include .omamori-btn
js = js.replace('querySelectorAll(".nav-btn")', 'querySelectorAll(".nav-btn, .omamori-btn")')

omamori_js = """
// Omamori Nav logic
function toggleOmamoriNav() {
  const nav = document.getElementById('omamori-nav');
  const tag = document.getElementById('omamori-tag');
  const tray = document.getElementById('omamori-tray');
  if (!nav) return;
  const isOpen = nav.classList.contains('open');
  if (isOpen) {
    nav.classList.remove('open');
    if (tag) tag.setAttribute('aria-expanded', 'false');
    if (tray) tray.setAttribute('aria-hidden', 'true');
  } else {
    nav.classList.add('open');
    if (tag) tag.setAttribute('aria-expanded', 'true');
    if (tray) tray.setAttribute('aria-hidden', 'false');
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const nav = document.getElementById('omamori-nav');
    if (nav && nav.classList.contains('open')) toggleOmamoriNav();
  }
});
window.toggleOmamoriNav = toggleOmamoriNav;
"""

if 'toggleOmamoriNav' not in js:
    with open('app.js', 'a', encoding='utf-8') as f:
        f.write('\n' + omamori_js)

# Update Service Worker
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v80', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
