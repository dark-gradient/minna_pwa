import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change practice and quiz backgrounds
css = css.replace(
    "body.practiceSetup-active { background-image: url('bg_practice.jpg') !important; }",
    "body.practiceSetup-active { background-image: url('bg_practice_new.jpg') !important; }"
)
css = css.replace(
    "body.quiz-active { background-image: url('bg_practice.jpg') !important; }",
    "body.quiz-active { background-image: url('bg_practice_new.jpg') !important; }"
)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add preload for the new image
html = html.replace(
    '<link rel="preload" as="image" href="bg_practice.jpg">',
    '<link rel="preload" as="image" href="bg_practice.jpg">\n  <link rel="preload" as="image" href="bg_practice_new.jpg">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v78', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
