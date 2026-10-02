import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the current welcome-active toggling with a generic class name toggler
old_logic = '''    if(viewId === 'welcomeView') {
        document.body.classList.add('welcome-active');
    } else {
        document.body.classList.remove('welcome-active');
    }'''
new_logic = '''    // Clear all previous view classes
    document.body.className = '';
    // Add new view class for backgrounds
    let baseName = viewId.replace('View', '');
    document.body.classList.add(baseName + '-active');'''

if old_logic in js:
    js = js.replace(old_logic, new_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
