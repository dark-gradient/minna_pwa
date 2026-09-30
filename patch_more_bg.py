import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change more background
css = css.replace(
    "body.more-active { background-image: url('bg_more.jpg') !important; }",
    "body.more-active { background-image: url('bg_more_new.jpg') !important; }"
)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add preload for the new image
html = html.replace(
    '<link rel="preload" as="image" href="bg_more.jpg">',
    '<link rel="preload" as="image" href="bg_more.jpg">\n  <link rel="preload" as="image" href="bg_more_new.jpg">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v79', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
