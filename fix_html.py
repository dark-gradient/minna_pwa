import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_nav = """  <div id="omamori-nav" class="omamori-nav">
    <div class="omamori-overlay" onclick="toggleOmamoriNav()"></div>
    <div class="omamori-container">
      <button id="omamori-tag" class="omamori-tag" aria-expanded="false" aria-label="Toggle Navigation" onclick="toggleOmamoriNav()">
        <div class="omamori-cord">
          <div class="omamori-knot">🎀</div>
          <div class="omamori-bell">🔔</div>
        </div>
        <div class="omamori-body">🌸</div>
      </button>
      <nav id="omamori-tray" class="omamori-tray" aria-hidden="true">
        <div class="omamori-header">
          <span class="omamori-header-title">MINNA KOTOBA</span>
        </div>
        <ul class="omamori-menu">
          <li>
            <button class="omamori-btn" data-view="home" onclick="showView('home'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_home.png" class="omamori-icon" alt="Home"></div>
              <div class="omamori-label">
                <span class="jp">ホーム</span>
                <span class="en">HOME</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="lessons" onclick="showView('lessons'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_lessons.png" class="omamori-icon" alt="Lessons"></div>
              <div class="omamori-label">
                <span class="jp">レッスン</span>
                <span class="en">LESSONS</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="vocabulary" onclick="showView('vocabulary'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_vocabulary.png" class="omamori-icon" alt="Vocabulary"></div>
              <div class="omamori-label">
                <span class="jp">語彙</span>
                <span class="en">VOCABULARY</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="grammar" onclick="showView('grammar'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_grammar.png" class="omamori-icon" alt="Grammar"></div>
              <div class="omamori-label">
                <span class="jp">文法</span>
                <span class="en">GRAMMAR</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="kanji" onclick="showView('kanji'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_kanji.png" class="omamori-icon" alt="Kanji"></div>
              <div class="omamori-label">
                <span class="jp">漢字</span>
                <span class="en">KANJI</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="listening" onclick="showView('listening'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_listening.png" class="omamori-icon" alt="Listening"></div>
              <div class="omamori-label">
                <span class="jp">聴解</span>
                <span class="en">LISTENING</span>
              </div>
            </button>
          </li>
          <li>
            <button class="omamori-btn" data-view="mockTest" onclick="showView('mockTest'); toggleOmamoriNav();">
              <div class="omamori-icon-wrapper"><img src="assets/images/icons/icon_mocktest.png" class="omamori-icon" alt="Mock Tests"></div>
              <div class="omamori-label">
                <span class="jp">模擬試験</span>
                <span class="en">MOCK TESTS</span>
              </div>
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </div>"""

pattern = re.compile(r'<div id="omamori-nav" class="omamori-nav">.*?</ul>\s*</nav>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_nav, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
