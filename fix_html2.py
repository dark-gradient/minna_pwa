with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
# Completely wipe out welcomeView and homeView from html
pattern = re.compile(r'<section id="welcomeView".*?</section>\s*<section id="homeView".*?</section>', re.DOTALL)

new_views = '''
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

    <section id="homeView" class="view active">
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
    </section>
'''

html = pattern.sub(new_views.strip(), html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
