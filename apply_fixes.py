import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove bottom-nav completely
html = re.sub(r'<nav class="bottom-nav">.*?</nav>', '', html, flags=re.DOTALL)

# Remove review from omamori menu
html = re.sub(r'<li><button class="omamori-btn" data-view="review".*?</li>', '', html, flags=re.DOTALL)

# Add review to scopeMode
if '<option value="review">Review</option>' not in html:
    html = html.replace('<option value="focus">Focus Words</option>', '<option value="focus">Focus Words</option>\n<option value="review">Review</option>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Background position for more-active
css = css.replace("body.more-active { background-image: url('bg_more_new.jpg') !important; }", "body.more-active { background-image: url('bg_more_new.jpg') !important; background-position: bottom right !important; background-size: cover !important; }")
css = css.replace("body.more-active { background-image: url('bg_more.jpg') !important; }", "body.more-active { background-image: url('bg_more_new.jpg') !important; background-position: bottom right !important; background-size: cover !important; }")

# Fix hover glitch
css = css.replace('transform: rotate(-15deg) !important;', 'transform: rotate(5deg) !important;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Update app.js
with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

pool_logic = """if (mode === "focus") {
let all = [];
for (let l in VOCAB) {
VOCAB[l].forEach((v, i) => {
let id = +l + "-" + i;
if (focusWords[id]) all.push({ ...v, lesson: +l, id });
});
}
return all;
}
if (mode === "review") {
let wrong = getWrongData();
let all = [];
for (let l in VOCAB) {
VOCAB[l].forEach((v, i) => {
let id = +l + "-" + i;
if (wrong[id]) all.push({ ...v, lesson: +l, id });
});
}
return all;
}"""

old_logic = """if (mode === "focus") {
let all = [];
for (let l in VOCAB) {
VOCAB[l].forEach((v, i) => {
let id = +l + "-" + i;
if (focusWords[id]) all.push({ ...v, lesson: +l, id });
});
}
return all;
}"""

js = js.replace(old_logic, pool_logic)

js = js.replace('mode === "all" || mode === "focus"', 'mode === "all" || mode === "focus" || mode === "review"')

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update Service Worker
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v82', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)

print('Done')
