import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the shorthand backgrounds with explicit backgrounds to guarantee covering
old_bg_block = '''/* Page Backgrounds */
.app-shell {
    transition: background 0.3s ease;
}
body.welcome-active .app-shell { background: url('fuji_wide.jpg') center/cover no-repeat !important; }
body.home-active .app-shell { background: url('bg_home.jpg') center/cover no-repeat !important; }
body.lessons-active .app-shell { background: url('bg_learn.jpg') center/cover no-repeat !important; }
body.practiceSetup-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }
body.mockTest-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }
body.more-active .app-shell { background: url('bg_more.jpg') center/cover no-repeat !important; }
body.quiz-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }'''

new_bg_block = '''/* Page Backgrounds */
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

if old_bg_block in css:
    css = css.replace(old_bg_block, new_bg_block)
else:
    # try regex
    css = re.sub(r'body\.welcome-active \.app-shell \{ background: url\(\'fuji_wide\.jpg\'\) center/cover no-repeat !important; \}', 'body.welcome-active .app-shell { background-image: url(\'fuji_wide.jpg\') !important; background-size: cover !important; background-position: center !important; background-repeat: no-repeat !important; }', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
