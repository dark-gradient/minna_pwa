import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update font
html = html.replace('family=DM+Sans:wght@400;500;600;700', 'family=Quicksand:wght@400;500;600;700')

# 2. Add Welcome View
welcome_view = '''
    <section id="welcomeView" class="view">
      <div class="welcome-container">
        <div class="welcome-logo">みんなのことば</div>
        <h1 class="welcome-title">MINNA KOTOBA</h1>
        <p class="welcome-subtitle">Learn Japanese.<br>Step by step. Together.</p>
        <button class="primary-btn welcome-start-btn" onclick="showView('home')">
          <span class="jp-text">はじめる</span>
          <span class="en-text">GET STARTED</span>
        </button>
      </div>
    </section>
'''

if 'id="welcomeView"' not in html:
    html = html.replace('<main>', '<main>\n' + welcome_view)

# 3. Create Bottom Navigation
bottom_nav = '''
  <nav class="bottom-nav">
    <button data-view="home" class="nav-btn active">
      <div class="nav-icon">\u2302</div>
      <span>Home</span>
    </button>
    <button data-view="lessons" class="nav-btn">
      <div class="nav-icon">\U0001F4DA</div>
      <span>Learn</span>
    </button>
    <button data-view="practiceSetup" class="nav-btn">
      <div class="nav-icon">\U0001F3AE</div>
      <span>Practice</span>
    </button>
    <button data-view="mockTest" class="nav-btn">
      <div class="nav-icon">\U0001F4DD</div>
      <span>Mock Test</span>
    </button>
    <button data-view="more" class="nav-btn">
      <div class="nav-icon">\u22EF</div>
      <span>More</span>
    </button>
  </nav>
'''
if '<nav class="bottom-nav">' not in html:
    html = html.replace('</footer>', '</footer>\n' + bottom_nav)

# 4. Remove old top nav
old_nav_pattern = re.compile(r'<nav>.*?</nav>', re.DOTALL)
html = old_nav_pattern.sub('', html)

# 5. Extract practice setup from homeView and make it a separate view
setup_panel_pattern = re.compile(r'<div class="panel setup">.*?<button id="startBtn".*?</button>\s*</div>', re.DOTALL)
setup_panel_match = setup_panel_pattern.search(html)

if setup_panel_match and 'id="practiceSetupView"' not in html:
    setup_html = setup_panel_match.group(0)
    html = html.replace(setup_html, '')
    
    practice_setup_view = f'''
    <section id="practiceSetupView" class="view">
      <div class="page-head"><div><div class="eyebrow">CUSTOM PRACTICE</div><h1>Practice Setup</h1></div></div>
      {setup_html}
    </section>
    '''
    html = html.replace('</main>', practice_setup_view + '\n  </main>')

# 6. Add Dashboard structure to homeView
dashboard_html = '''
      <div class="dashboard">
        <div class="streak-card">
          <div class="streak-icon">\U0001F525</div>
          <div class="streak-text">
            <strong><span id="streakDays">0</span> DAY STREAK</strong>
            <div>Keep going!</div>
          </div>
        </div>
        
        <div class="section-head"><span class="kicker">TODAY\\'S PRACTICE</span></div>
        <div class="dashboard-grid">
          <div class="dash-card" onclick="showView('lessons')">
            <div class="dash-card-jp">\u8a9e\u5f59</div>
            <div class="dash-card-en">Vocabulary</div>
            <div class="dash-progress" id="vocabProgress">--%</div>
          </div>
          <div class="dash-card" onclick="showView('kaiwa')">
            <div class="dash-card-jp">\u4f1a\u8a71</div>
            <div class="dash-card-en">Kaiwa</div>
            <div class="dash-progress" id="kaiwaProgress">--%</div>
          </div>
        </div>
        
        <div class="section-head" style="margin-top:20px;"><span class="kicker">N5 PROGRESS</span></div>
        <div class="progress-card">
          <div class="progress-bar-container">
            <div class="progress-bar-fill" id="n5ProgressBar" style="width:0%"></div>
          </div>
          <div class="progress-text"><span id="n5ProgressText">0</span>%</div>
        </div>
      </div>
'''
if '<div class="dashboard">' not in html:
    html = html.replace('<div class="hero">', '<div class="hero" style="display:none;">') # Hide old hero for now
    html = html.replace('</section>', dashboard_html + '\n    </section>', 1) # Insert into homeView

# 7. Add Mock Test View
mock_test_view = '''
    <section id="mockTestView" class="view">
      <div class="page-head"><div><div class="eyebrow">MOCK TEST</div><h1>N5 Practice Exam</h1></div></div>
      <div class="panel">
        <div class="test-header">
          <div class="test-badge">N5</div>
          <h2>Try a full N5 mock test</h2>
          <p>Real format \u2022 Timed</p>
        </div>
        <div class="test-meta">
          <span>\u23f1 60 min</span>
          <span>\U0001F4DD 50 questions</span>
        </div>
        <button id="startMockTestBtn" class="primary-btn" style="width:100%; margin-top:16px;" onclick="startMockTest()">START MOCK TEST \u2192</button>
      </div>
      
      <div class="section-head" style="margin-top: 30px;"><span class="kicker">PAST RESULTS</span></div>
      <div id="mockTestResults">
        <div class="empty-state">No mock tests yet.<br><br>Take your first N5 mock test \u2192</div>
      </div>
    </section>
'''
if 'id="mockTestView"' not in html:
    html = html.replace('</main>', mock_test_view + '\n  </main>')

# 8. Add More View
more_view = '''
    <section id="moreView" class="view">
      <div class="page-head"><div><h1>More</h1></div></div>
      <div class="more-menu">
        <button class="more-item" onclick="showView('review')">
          <span>\u274c Wrong Answers</span>
          <span>\u2192</span>
        </button>
        <button class="more-item" onclick="showView('focus')">
          <span>\U0001F3AF Focus Words</span>
          <span>\u2192</span>
        </button>
        <button class="more-item" onclick="toggleTheme()">
          <span>\U0001F317 Toggle Dark Mode</span>
          <span>\u2192</span>
        </button>
      </div>
    </section>
'''
if 'id="moreView"' not in html:
    html = html.replace('</main>', more_view + '\n  </main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
