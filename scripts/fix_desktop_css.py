import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find the block starting with @media (min-width: 768px) and containing .app-shell up to the end of the media query
# Wait, I know exactly what I added in apply_global_bg.py, so let me just replace that exact string.
old_str = '''@media (min-width: 768px) {
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
}'''

new_str = '''@media (min-width: 768px) {
    body, .app-shell {
        display: block;
        width: 100vw;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden !important;
        max-width: 100%;
        max-height: 100%;
        border-radius: 0;
        border: none;
        box-shadow: none;
    }
    main {
        overflow: hidden !important; /* No scrolling on desktop */
        height: 100%;
        width: 100%;
    }
    
    /* Make content horizontally centered and reasonably sized on desktop */
    #homeView { max-width: 600px; margin: 0 auto; }
    #welcomeView .welcome-container { max-width: 800px; margin: 0 auto; }
}'''

if old_str in css:
    css = css.replace(old_str, new_str)
    print("Replaced successfully")
else:
    print("Could not find old_str")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
