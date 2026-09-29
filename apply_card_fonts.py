import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hide .topbar
css += "\n.topbar { display: none !important; }\n"

# 2. Page Head Title colors
css += '''
.page-head h1 {
    color: var(--pink) !important;
    -webkit-text-stroke: 2px var(--text-primary);
    text-shadow: 4px 4px 0px var(--text-primary);
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 42px !important;
}
.page-head .eyebrow {
    color: var(--yellow) !important;
    font-weight: 800;
    -webkit-text-stroke: 1px var(--text-primary);
    font-size: 18px !important;
    letter-spacing: 2px;
}
.page-head {
    padding-top: 24px !important;
}
'''

# 3. Make cards more translucent (from 0.85 to 0.55)
# 0.85 opacity was rgba(253, 251, 247, 0.85)
css = css.replace('rgba(253, 251, 247, 0.85)', 'rgba(253, 251, 247, 0.55)')
# hex colors: D9 was 85%. 55% is 8C.
css = css.replace('#C9DCC7D9', '#C9DCC78C')
css = css.replace('#F4A6A6D9', '#F4A6A68C')
css = css.replace('#C9DCE4D9', '#C9DCE48C')
css = css.replace('#F3D99BD9', '#F3D99B8C')

# 4. Pixel font for text inside cards
css += '''
.lesson-card, .lesson-card *, .practice-card, .practice-card * {
    font-family: 'DotGothic16', sans-serif !important;
}
.lesson-card h3 {
    font-size: 24px !important;
    font-weight: 800 !important;
    color: var(--text-primary) !important;
}
.lesson-card .meta {
    font-size: 16px !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
