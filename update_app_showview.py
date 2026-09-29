import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_logic = '''  document.body.classList.toggle("quiz-active", view === "quiz");
  document.body.classList.toggle("home-active", view === "home");
  document.body.classList.toggle("welcome-active", view === "welcomeView");'''

new_logic = '''  document.body.className = '';
  document.body.classList.add(view + '-active');
  if (view === 'welcomeView') {
      document.body.classList.add('welcome-active');
  }'''

if old_logic in js:
    js = js.replace(old_logic, new_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
