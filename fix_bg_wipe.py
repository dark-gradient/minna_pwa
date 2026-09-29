import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_show_view = '''  document.body.className = '';
  document.body.style.removeProperty('background-image');
  document.body.classList.add(view + '-active');'''

new_show_view = '''  document.body.className = '';
  if (view !== 'lessonDetail') {
      document.body.style.removeProperty('background-image');
  }
  document.body.classList.add(view + '-active');'''

if old_show_view in js:
    js = js.replace(old_show_view, new_show_view)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
