import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I will add updateDashboardStats() and call it inside showView('home')
new_func = '''
function updateDashboardStats() {
  let streak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  let streakText = document.getElementById('streakText');
  if (streakText) streakText.innerHTML = '\U0001F525 You\\'re on a ' + streak + ' day streak';
  
  // Calculate vocab stats
  let totalVocab = allVocab.length || 800; // fallback if not loaded
  
  // We don't have grammar/listening/kanji data yet, so we just show 0
  let statVocab = document.getElementById('statVocab');
  if (statVocab) statVocab.innerText = '0/' + totalVocab;
  
  let statGrammar = document.getElementById('statGrammar');
  if (statGrammar) statGrammar.innerText = '0/0';
  
  let statListening = document.getElementById('statListening');
  if (statListening) statListening.innerText = '0/0';
  
  let statKanji = document.getElementById('statKanji');
  if (statKanji) statKanji.innerText = '0/0';
  
  let n5Percent = document.getElementById('n5Percent');
  let n5Topics = document.getElementById('n5Topics');
  let n5ProgressBar = document.getElementById('n5ProgressBar');
  if (n5Percent) n5Percent.innerText = '0%';
  if (n5Topics) n5Topics.innerHTML = '0/' + totalVocab + '<br>Words';
  if (n5ProgressBar) n5ProgressBar.style.width = '0%';
}
'''

# insert function
js += '\n' + new_func

# call in showView
js = js.replace('document.body.classList.toggle("home-active", view === "home");',
                'document.body.classList.toggle("home-active", view === "home");\n  if (view === "home") updateDashboardStats();')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
