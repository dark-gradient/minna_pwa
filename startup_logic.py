import re
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# I will append this to the end of init()
append_logic = '''
  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  if (currentStreak === 0 && !localStorage.getItem('minna_last_active')) {
    showView('welcomeView');
  } else {
    showView('home');
  }
'''

# Find end of init()
m = re.search(r'function init\(\).*?if \(saved\) document\.documentElement\.dataset\.theme = saved;\n\}', js, re.DOTALL)
if m:
    init_func = m.group(0)
    new_init = init_func[:-1] + append_logic + '}\n'
    js = js.replace(init_func, new_init)
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("Startup logic added")
else:
    print("Could not find init()")
