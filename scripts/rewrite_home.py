import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace homeView
new_home_view = '''<section id="homeView" class="view">
      <div class="topbar-home">
        <div class="home-title">
          <h1>Minna Kotoba</h1>
          <span class="subtitle">N5 JOURNEY</span>
        </div>
        <div class="home-actions">
          <button class="icon-btn" aria-label="Notifications">\U0001F514</button>
          <button class="icon-btn" aria-label="Profile">\U0001F431</button>
        </div>
      </div>
      
      <div class="dashboard-scroll">
        <!-- Streak Card -->
        <div class="streak-card">
          <div class="streak-content">
            <h2>Keep going!</h2>
            <p>\U0001F525 You're on a 7 day streak</p>
          </div>
          <div class="streak-mascot">
             <!-- Placeholder for pixel cat -->
             <div class="pixel-cat-placeholder"></div>
          </div>
        </div>

        <!-- Today's Practice Section -->
        <div class="section-header">
          <h2>Today's Practice</h2>
          <span class="chevron">›</span>
        </div>
        
        <div class="practice-grid">
          <div class="practice-card bg-green">
            <div class="card-icon">\U0001F4D6</div>
            <div class="card-jp">\u8a9e\u5f59</div>
            <div class="card-en">Vocabulary</div>
            <div class="card-progress">
              <div class="progress-bar"><div class="progress-fill" style="width: 60%;"></div></div>
              <span class="progress-text">12/20</span>
            </div>
          </div>
          <div class="practice-card bg-pink">
            <div class="card-icon">\U0001F4C4</div>
            <div class="card-jp">\u6587\u6cd5</div>
            <div class="card-en">Grammar</div>
            <div class="card-progress">
              <div class="progress-bar"><div class="progress-fill" style="width: 53%;"></div></div>
              <span class="progress-text">8/15</span>
            </div>
          </div>
          <div class="practice-card bg-blue">
            <div class="card-icon">\U0001F3A7</div>
            <div class="card-jp">\u8074\u89e3</div>
            <div class="card-en">Listening</div>
            <div class="card-progress">
              <div class="progress-bar"><div class="progress-fill" style="width: 40%;"></div></div>
              <span class="progress-text">6/15</span>
            </div>
          </div>
          <div class="practice-card bg-yellow">
            <div class="card-icon">\U0001F4AC</div>
            <div class="card-jp">\u8aad\u89e3</div>
            <div class="card-en">Reading</div>
            <div class="card-progress">
              <div class="progress-bar"><div class="progress-fill" style="width: 40%;"></div></div>
              <span class="progress-text">4/10</span>
            </div>
          </div>
        </div>

        <!-- N5 Progress -->
        <div class="section-header" style="margin-top: 24px;">
          <h2>N5 Progress</h2>
          <span class="chevron">›</span>
        </div>
        <div class="progress-card">
          <div class="progress-row">
            <span class="progress-percent">38%</span>
            <div class="progress-bar-large"><div class="progress-fill-large" style="width: 38%;"></div></div>
            <span class="progress-topics">48/125<br>Topics</span>
          </div>
        </div>
      </div>
    </section>'''

html = re.sub(r'<section id="homeView".*?</section>', new_home_view, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
