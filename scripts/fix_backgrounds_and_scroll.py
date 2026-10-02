import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Apply backgrounds to BODY instead of .app-shell
old_bgs = '''/* Page Backgrounds */
.app-shell {
    transition: background-image 0.3s ease;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
}
body.welcome-active .app-shell { background-image: url('fuji_wide.jpg') !important; }
body.home-active .app-shell { background-image: url('bg_home.jpg') !important; }
body.lessons-active .app-shell { background-image: url('bg_learn.jpg') !important; }
body.practiceSetup-active .app-shell { background-image: url('bg_practice.jpg') !important; }
body.mockTest-active .app-shell { background-image: url('bg_practice.jpg') !important; }
body.more-active .app-shell { background-image: url('bg_more.jpg') !important; }
body.quiz-active .app-shell { background-image: url('bg_practice.jpg') !important; }'''

new_bgs = '''/* Page Backgrounds */
body {
    transition: background-image 0.3s ease;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}
body.welcome-active { background-image: url('fuji_wide.jpg') !important; }
body.home-active { background-image: url('bg_home.jpg') !important; }
body.lessons-active { background-image: url('bg_learn.jpg') !important; }
body.practiceSetup-active { background-image: url('bg_practice.jpg') !important; }
body.mockTest-active { background-image: url('bg_practice.jpg') !important; }
body.more-active { background-image: url('bg_more.jpg') !important; }
body.quiz-active { background-image: url('bg_practice.jpg') !important; }

/* Make App Shell completely transparent to show body background */
.app-shell { background: transparent !important; }
'''

if old_bgs in css:
    css = css.replace(old_bgs, new_bgs)

# 2. Fix the scrollbars. Let body handle scrolling, don't restrict app-shell height.
old_appshell = '''    body, .app-shell {
        display: block !important;
        width: 100vw !important;
        height: 100vh !important;
        margin: 0 !important;
        padding: 0 5vw 90px 5vw !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        max-width: 100% !important;
        max-height: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
    }
    body.welcome-active, body.welcome-active .app-shell {
        overflow: hidden !important;
        padding: 0 !important;
    }'''

new_appshell = '''    body {
        width: 100vw !important;
        height: 100vh !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
    }
    .app-shell {
        display: block !important;
        width: 100% !important;
        min-height: 100vh !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 5vw 90px 5vw !important;
        overflow: visible !important;
        max-width: 100% !important;
        border-radius: 0 !important;
        border: none !important;
        box-shadow: none !important;
        box-sizing: border-box !important;
    }
    body.welcome-active {
        overflow: hidden !important;
    }
    body.welcome-active .app-shell {
        overflow: hidden !important;
        padding: 0 !important;
        height: 100vh !important;
    }'''

if old_appshell in css:
    css = css.replace(old_appshell, new_appshell)

# 3. Make cards translucent
old_lesson_card = '''.lesson-card {
    background: var(--surface);'''
new_lesson_card = '''.lesson-card {
    background: rgba(253, 251, 247, 0.85); /* Translucent surface */
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);'''
if old_lesson_card in css:
    css = css.replace(old_lesson_card, new_lesson_card)

# also make practice cards translucent
old_practice_card = '''.practice-card {
    background: var(--surface);'''
new_practice_card = '''.practice-card {
    background: rgba(253, 251, 247, 0.85);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);'''
if old_practice_card in css:
    css = css.replace(old_practice_card, new_practice_card)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
