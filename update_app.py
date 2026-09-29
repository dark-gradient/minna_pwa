import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# 1. Hook up bottom nav buttons
nav_script = '''
document.querySelectorAll('.bottom-nav .nav-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.bottom-nav .nav-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    showView(btn.dataset.view);
  });
});
'''
if 'bottom-nav' not in app_js:
    app_js = app_js.replace('// --- Start Application ---', nav_script + '\n// --- Start Application ---')

# 2. Update toggleTheme() to use the new icon or at least to work
theme_func = '''
function toggleTheme() {
  const dark = document.documentElement.dataset.theme === "dark";
  document.documentElement.dataset.theme = dark ? "" : "dark";
  localStorage.setItem("mnn-theme", dark ? "" : "dark");
}
'''
if 'function toggleTheme()' not in app_js:
    app_js += '\n' + theme_func

# 3. Add Streak Logic
streak_script = '''
function updateStreakAndDashboard() {
  const today = new Date().toDateString();
  let lastActive = localStorage.getItem('minna_last_active');
  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  
  // Dashboard updates
  const elStreak = document.getElementById('streakDays');
  if (elStreak) elStreak.textContent = currentStreak;
  
  // Calculate N5 Progress
  const total = allVocab.length;
  let learnedCount = Object.keys(getWrongData()).length; // rough estimate based on wrong/correct history
  // Since we don't have a real 'learned' array, let's just use total focus words and wrong words + some constant for now
  // Actually, we can just say progress is based on how many words we have answered at least once
  let n5Percent = total > 0 ? Math.round((learnedCount / total) * 100) : 0;
  if(n5Percent > 100) n5Percent = 100;
  
  const elProgress = document.getElementById('n5ProgressBar');
  const elProgressText = document.getElementById('n5ProgressText');
  if (elProgress) elProgress.style.width = n5Percent + '%';
  if (elProgressText) elProgressText.textContent = n5Percent;
  
  // Update Vocab / Kaiwa progress bars
  const elVocab = document.getElementById('vocabProgress');
  if(elVocab) elVocab.textContent = Math.round(n5Percent) + '%';
  const elKaiwa = document.getElementById('kaiwaProgress');
  if(elKaiwa) elKaiwa.textContent = '100%';
}

function recordActivity() {
  const today = new Date().toDateString();
  let lastActive = localStorage.getItem('minna_last_active');
  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  
  if (lastActive !== today) {
    let yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    if (lastActive === yesterday.toDateString()) {
      currentStreak++;
    } else {
      currentStreak = 1;
    }
    localStorage.setItem('minna_last_active', today);
    localStorage.setItem('minna_streak', currentStreak);
    updateStreakAndDashboard();
  }
}
'''
if 'function recordActivity()' not in app_js:
    app_js += '\n' + streak_script

# 4. Inject recordActivity() into end of quiz
app_js = app_js.replace('function finishQuiz() {', 'function finishQuiz() {\n  recordActivity();\n')

# 5. Initialize dashboard on load
if 'updateStreakAndDashboard();' not in app_js:
    app_js = app_js.replace('showView("home");', 'updateStreakAndDashboard();\n  showView("welcomeView");')
    # Change starting view to welcomeView

# 6. Start Mock Test function
mock_script = '''
function startMockTest() {
  // Set scope to All, mixed direction, 50 questions
  document.getElementById("scopeMode").value = "all";
  document.getElementById("direction").value = "mixed";
  document.getElementById("sessionSize").value = "50";
  
  // Update state and pool
  updateScopeUI(); 
  
  // Wait for pool to update then start
  setTimeout(() => {
    if(state.pool.length > 0) {
      document.getElementById('startBtn').click();
    } else {
      alert("No questions available for Mock Test yet.");
    }
  }, 100);
}
'''
if 'function startMockTest()' not in app_js:
    app_js += '\n' + mock_script


with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)
