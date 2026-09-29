import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove the white line under the detail header
old_detail_header = '''.detail-header {
    padding: 18px 0 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 20px
}'''
new_detail_header = '''.detail-header {
    padding: 18px 0 24px;
    border-bottom: none !important;
    margin-bottom: 20px
}'''
if old_detail_header in css:
    css = css.replace(old_detail_header, new_detail_header)

# 2. Style the english subtext inside detail header
css += '''
.detail-header p {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-family: 'DotGothic16', sans-serif !important;
    letter-spacing: 1px;
}
'''

# 3. Fix back button, Select All / Clear Selection buttons, Pronunciation label, select box, Play button
css += '''
#lessonDetailView .back-btn {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
}
#lessonDetailView .back-btn:hover {
    color: var(--yellow) !important;
}

#lessonDetailView select {
    background: rgba(253, 251, 247, 0.35) !important;
    backdrop-filter: blur(4px) !important;
    border: 2px solid var(--text-primary) !important;
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    border-radius: 4px;
    padding: 4px 8px;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
}

#lessonDetailView label, #lessonSelectionControls button {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: 1px;
    font-size: 16px !important;
    opacity: 1 !important;
}
#lessonSelectionControls button:hover {
    color: var(--yellow) !important;
}

#lessonDetailView .secondary-btn {
    background: var(--pink) !important;
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-weight: 800 !important;
    border: 2px solid var(--text-primary) !important;
    box-shadow: 2px 2px 0 var(--text-primary) !important;
    font-size: 16px !important;
}
#lessonDetailView .secondary-btn:hover {
    background: var(--yellow) !important;
    color: var(--pink) !important;
}
'''

# 4. English text inside Practice cards (Home page)
css += '''
.practice-card .card-en {
    color: var(--pink) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-family: 'DotGothic16', sans-serif !important;
    opacity: 1 !important;
    font-size: 15px !important;
    letter-spacing: 1px;
}
.practice-card .card-jp {
    color: var(--yellow) !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary) !important;
    font-weight: 800 !important;
    font-family: 'DotGothic16', sans-serif !important;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
