import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove bell and cat emoji
html = re.sub(r'<div class=\"home-actions\">.*?</div>', '', html, flags=re.DOTALL)

# Turn Reading into Kanji
html = html.replace('<div class="card-jp">読解</div>', '<div class="card-jp">漢字</div>')
html = html.replace('<div class="card-en">Reading</div>', '<div class="card-en">Kanji</div>')

# Make the N5 progress clickable
html = html.replace('<div class="progress-card">', '<div class="progress-card" style="cursor:pointer;" onclick="showView(\'lessons\')">')

# Give IDs to elements we need to update with real data
html = html.replace('<p>🔥 You\'re on a 7 day streak</p>', '<p id="streakText">🔥 You\'re on a 0 day streak</p>')
html = html.replace('<span class="progress-percent">38%</span>', '<span class="progress-percent" id="n5Percent">0%</span>')
html = html.replace('<span class="progress-topics">48/125<br>Topics</span>', '<span class="progress-topics" id="n5Topics">0/0<br>Words</span>')
html = html.replace('<div class="progress-fill-large" style="width: 38%;"></div>', '<div class="progress-fill-large" id="n5ProgressBar" style="width: 0%;"></div>')

# For the 4 cards
html = html.replace('<span class="progress-text">12/20</span>', '<span class="progress-text" id="statVocab">0/0</span>')
html = html.replace('<span class="progress-text">8/15</span>', '<span class="progress-text" id="statGrammar">0/0</span>')
html = html.replace('<span class="progress-text">6/15</span>', '<span class="progress-text" id="statListening">0/0</span>')
html = html.replace('<span class="progress-text">4/10</span>', '<span class="progress-text" id="statKanji">0/0</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
