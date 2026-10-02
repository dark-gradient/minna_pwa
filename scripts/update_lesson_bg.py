import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I want to add logic to load a specific background image for the lesson
old_open_lesson = '''function openLesson(n) {
  currentLessonId = n;
  lessonSelection.clear();
  currentLessonWords = VOCAB[n] || [];'''
new_open_lesson = '''function openLesson(n) {
  currentLessonId = n;
  
  // Set custom background image for the lesson, or fallback to the learn background
  const imgUrl = (n >= 1 && n <= 3) ? 'bg_lesson_' + n + '.jpg' : 'bg_learn.jpg';
  document.body.style.setProperty('background-image', 'url(' + imgUrl + ')', 'important');
  
  lessonSelection.clear();
  currentLessonWords = VOCAB[n] || [];'''

if old_open_lesson in js:
    js = js.replace(old_open_lesson, new_open_lesson)

# Also need to clear it in showView so it doesn't get stuck!
old_show_view = '''  document.body.className = '';
  document.body.classList.add(view + '-active');
  if (view === 'welcomeView') {
      document.body.classList.add('welcome-active');
  }'''
new_show_view = '''  document.body.className = '';
  document.body.style.removeProperty('background-image');
  document.body.classList.add(view + '-active');
  if (view === 'welcomeView') {
      document.body.classList.add('welcome-active');
  }'''

if old_show_view in js:
    js = js.replace(old_show_view, new_show_view)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
