import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html_new = """<div id="omamori-nav" class="omamori-nav">
    <div class="omamori-overlay" onclick="toggleOmamoriNav()"></div>
    <div class="omamori-container">
      <div class="omamori-string-horizontal"></div>
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
  </div>"""

html = re.sub(r'<div id="omamori-nav" class="omamori-nav">.*?</nav>\s*</div>', html_new, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_new = """/* Omamori Navigation */
.omamori-nav {
  position: fixed;
  top: 80px;
  right: 0;
  z-index: 2000;
  pointer-events: none;
}

.omamori-nav.open {
  pointer-events: auto;
}

.omamori-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.1);
  z-index: 1999;
  display: none;
  opacity: 0;
  transition: opacity 0.2s;
  pointer-events: auto;
}

.omamori-nav.open .omamori-overlay {
  display: block;
  opacity: 1;
}

.omamori-container {
  position: absolute;
  top: 0;
  right: 0;
  width: 240px;
  transform: translateX(100%);
  transition: transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 2001;
  pointer-events: auto;
}

.omamori-nav.open .omamori-container {
  transform: translateX(0);
}

.omamori-tray {
  width: 100%;
  background: #FDFBF7;
  border: 2px solid #17252A;
  border-right: none;
  border-radius: 12px 0 0 12px;
  padding: 40px 16px 20px 16px;
  box-shadow: -4px 4px 0 rgba(23, 37, 42, 0.2);
}

.omamori-string-horizontal {
  position: absolute;
  top: 24px;
  left: -24px;
  width: 24px;
  height: 4px;
  background-color: #d13030;
  border-top: 1px solid #17252A;
  border-bottom: 1px solid #17252A;
  z-index: 2002;
}

.omamori-tag {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  position: absolute;
  top: 26px;
  left: -42px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2003;
  transform-origin: top center;
  transition: transform 0.2s;
}

.omamori-nav.open .omamori-tag {
  animation: swingOpen 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.omamori-nav:not(.open) .omamori-tag {
  animation: swingClose 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.omamori-tag:hover {
  transform: rotate(-15deg) !important;
  animation: none !important;
}

@keyframes swingOpen {
  0% { transform: rotate(0deg); }
  30% { transform: rotate(25deg); }
  60% { transform: rotate(-10deg); }
  80% { transform: rotate(5deg); }
  100% { transform: rotate(0deg); }
}

@keyframes swingClose {
  0% { transform: rotate(0deg); }
  30% { transform: rotate(-25deg); }
  60% { transform: rotate(10deg); }
  80% { transform: rotate(-5deg); }
  100% { transform: rotate(0deg); }
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

@media (prefers-reduced-motion: reduce) {
  .omamori-container {
    transition: transform 0.2s ease-out;
  }
  .omamori-nav.open .omamori-tag, .omamori-nav:not(.open) .omamori-tag {
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
}"""

css = re.sub(r'/\* Omamori Navigation \*/.*?\.omamori-tray::after \{[^}]*\}', css_new, css, flags=re.DOTALL)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v81', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
