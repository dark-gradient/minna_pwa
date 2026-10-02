import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace fonts with DotGothic16
css = re.sub(r'--font-main:.*?\;', '--font-main: \'DotGothic16\', sans-serif;', css)
css = re.sub(r'--font-jp:.*?\;', '--font-jp: \'DotGothic16\', sans-serif;', css)

# Add desktop frame and background images
new_css = '''
/* --- GLOBAL BACKGROUNDS & DESKTOP FRAME --- */
@import url('https://fonts.googleapis.com/css2?family=DotGothic16&display=swap');

body {
    font-family: 'DotGothic16', sans-serif !important;
    background-color: #1a1a1a;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

/* On desktop, confine the app to a mobile-sized frame */
@media (min-width: 768px) {
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .app-shell {
        width: 400px;
        height: 100vh;
        max-height: 850px;
        border-radius: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        overflow: hidden !important;
        position: relative;
        border: 4px solid #000;
    }
    main {
        overflow: hidden !important; /* No scrolling on desktop */
    }
}

/* Page Backgrounds */
.app-shell {
    transition: background 0.3s ease;
}
body.welcome-active .app-shell { background: url('fuji.jpg') center/cover no-repeat !important; }
body.home-active .app-shell { background: url('bg_home.jpg') center/cover no-repeat !important; }
body.lessons-active .app-shell { background: url('bg_learn.jpg') center/cover no-repeat !important; }
body.practiceSetup-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }
body.mockTest-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }
body.more-active .app-shell { background: url('bg_more.jpg') center/cover no-repeat !important; }
body.quiz-active .app-shell { background: url('bg_practice.jpg') center/cover no-repeat !important; }

/* Ensure views are transparent so background shows */
.view, main, #homeView {
    background: transparent !important;
}
.bottom-nav {
    background: rgba(247, 241, 231, 0.95) !important; /* Slightly transparent solid color, NOT glass */
}

/* Make text readable against backgrounds */
.home-title h1, .home-title .subtitle, .section-header h2, .section-header .chevron {
    text-shadow: 2px 2px 0px rgba(247, 241, 231, 1), -1px -1px 0px rgba(247, 241, 231, 1), 1px -1px 0px rgba(247, 241, 231, 1), -1px 1px 0px rgba(247, 241, 231, 1), 1px 1px 0px rgba(247, 241, 231, 1);
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(new_css + '\n' + css)
