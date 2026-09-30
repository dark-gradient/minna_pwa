import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace omamori menu items for focus/kaiwa/practiceSetup
new_menu_items = """<li><button class="omamori-btn" data-view="vocabulary" onclick="showView('vocabulary'); toggleOmamoriNav();"><span class="omamori-icon">🎴</span> <span>Vocabulary</span></button></li>
          <li><button class="omamori-btn" data-view="grammar" onclick="showView('grammar'); toggleOmamoriNav();"><span class="omamori-icon">📝</span> <span>Grammar</span></button></li>
          <li><button class="omamori-btn" data-view="kanji" onclick="showView('kanji'); toggleOmamoriNav();"><span class="omamori-icon">🖌️</span> <span>Kanji</span></button></li>"""

html = re.sub(
    r'<li><button class="omamori-btn" data-view="focus".*?</li>\s*<li><button class="omamori-btn" data-view="kaiwa".*?</li>\s*<li><button class="omamori-btn" data-view="practiceSetup".*?</li>',
    new_menu_items,
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_map = """  const map = {
    welcomeView: "welcomeView",
    home: "homeView",
    quiz: "quizView",
    lessons: "lessonsView",
    lessonDetail: "lessonDetailView",
    kaiwa: "kaiwaView",
    review: "reviewView",
    resultsView: "resultsView",
    focus: "focusView",
    practiceSetup: "practiceSetupView",
    mockTest: "mockTestView",
    more: "moreView"
  };
  Object.values(map).forEach((id) => {
    const el = ;
    if (el) el.classList.remove("active");
  });
  const target = ;
  if (target) target.classList.add("active");"""

new_map = """  const map = {
    welcomeView: "welcomeView",
    home: "homeView",
    quiz: "quizView",
    lessons: "lessonsView",
    lessonDetail: "lessonDetailView",
    kaiwa: "kaiwaView",
    review: "reviewView",
    resultsView: "resultsView",
    focus: "focusView",
    practiceSetup: "practiceSetupView",
    vocabulary: "practiceSetupView",
    grammar: "practiceSetupView",
    kanji: "practiceSetupView",
    mockTest: "mockTestView",
    more: "moreView"
  };
  Object.values(map).forEach((id) => {
    const el = ;
    if (el) el.classList.remove("active");
  });
  const target = ;
  if (target) target.classList.add("active");
  
  if (view === 'vocabulary' || view === 'grammar' || view === 'kanji' || view === 'practiceSetup') {
    let title = 'Practice Setup';
    let eyebrowText = 'CUSTOM PRACTICE';
    if (view === 'vocabulary') { title = 'Vocabulary Practice'; eyebrowText = 'VOCABULARY SETUP'; }
    if (view === 'grammar') { title = 'Grammar Practice'; eyebrowText = 'GRAMMAR SETUP'; }
    if (view === 'kanji') { title = 'Kanji Practice'; eyebrowText = 'KANJI SETUP'; }
    const header = document.querySelector('#practiceSetupView h1');
    const eyebrow = document.querySelector('#practiceSetupView .eyebrow');
    if (header) header.textContent = title;
    if (eyebrow) eyebrow.textContent = eyebrowText;
  }"""

js = js.replace(old_map, new_map)

# Update querySelectorAll(".nav-btn, .omamori-btn") to work with duplicate mappings?
# No need, it just checks b.dataset.view === view

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add bg images for vocabulary, grammar, kanji
if 'body.vocabulary-active' not in css:
    css = css.replace("body.practiceSetup-active { background-image: url('bg_practice_new.jpg') !important; }", 
                      "body.practiceSetup-active { background-image: url('bg_practice_new.jpg') !important; }\nbody.vocabulary-active { background-image: url('bg_practice_new.jpg') !important; }\nbody.grammar-active { background-image: url('bg_practice_new.jpg') !important; }\nbody.kanji-active { background-image: url('bg_practice_new.jpg') !important; }")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update Service Worker
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v83', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
