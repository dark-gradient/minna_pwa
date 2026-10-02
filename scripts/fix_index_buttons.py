import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('background: rgba(253, 251, 247, 0.65) !important;', 'background: rgba(253, 251, 247, 0.45) !important;')
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<button class="nav-btn compact" onclick="selectAllInLesson()">', '<button type="button" class="nav-btn compact" onclick="selectAllInLesson()">')
html = html.replace('<button class="nav-btn compact" onclick="clearLessonSelection()">', '<button type="button" class="nav-btn compact" onclick="clearLessonSelection()">')
html = html.replace('<button class="primary-btn compact" onclick="addSelectionToFocus()">', '<button type="button" class="primary-btn compact" onclick="addSelectionToFocus()">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
