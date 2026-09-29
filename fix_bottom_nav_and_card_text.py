import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Bottom nav transparency
old_nav = '''.bottom-nav {
    background: rgba(247, 241, 231, 0.6) !important;
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-top: 1px solid rgba(247, 241, 231, 0.8);
}'''
new_nav = '''.bottom-nav {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    border-top: 2px solid var(--border-strong) !important;
}'''
if old_nav in css:
    css = css.replace(old_nav, new_nav)

# 2. Pink and yellow styling inside .lesson-card
old_card_meta = '''.lesson-card .meta {
    font-size: 16px !important;
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}'''
# Actually, wait, .meta isn't the <p> tag?
# In app.js: <span class="lesson-no">LESSON ...</span> ... <p> vocabulary entries</p>
css += '''
/* Pink and yellow text inside lesson and practice cards */
.lesson-card .lesson-no {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-size: 14px !important;
}
.lesson-card p {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-size: 14px !important;
}
.practice-card h2 {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
}
.practice-card p {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
