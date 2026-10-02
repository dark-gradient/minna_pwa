import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root
root_pattern = re.compile(r':root\s*\{.*?\}(?=\s*\[data-theme=dark\])', re.DOTALL)
new_root = r'''
:root {
    --bg-primary: #F7F1E7;
    --surface: #FCF8EF;
    --surface-soft: #F3EBDD;

    --text-primary: #17252A;
    --text-secondary: #66706D;
    --text-muted: #8A918C;

    --green: #21483D;
    --green-soft: #C9DCC7;

    --pink: #F4A6A6;
    --peach: #F6D9B8;
    --blue: #C9DCE4;
    --yellow: #F3D99B;

    --border: #D8D0C3;
    --border-strong: #BDB3A6;

    --success: #6E9D78;
    --warning: #D39A4A;
    --error: #C96B63;
    
    --shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);
    --radius: 8px;
}'''

css = root_pattern.sub(new_root.strip() + '\n', css)

# Replace dark mode
dark_pattern = re.compile(r'\[data-theme=dark\]\s*\{.*?\}(?=\s*body\s*\{)', re.DOTALL)
new_dark = r'''
[data-theme=dark] {
    --bg-primary: #17211F;
    --surface: #20302C;
    --surface-soft: #283833;

    --text-primary: #F7F1E7;
    --text-secondary: #C2CBC5;
    --text-muted: #909C95;

    --green: #9FC4A9;
    --green-soft: #334B41;

    --pink: #F4A6A6;
    --peach: #D8B58E;
    --blue: #A9C4CE;
    --yellow: #D8BA70;

    --border: #40514B;
    --border-strong: #566760;

    --success: #6E9D78;
    --warning: #D39A4A;
    --error: #C96B63;

    --shadow: 4px 4px 0px rgba(0, 0, 0, 0.25);
    --radius: 8px;
}'''

css = dark_pattern.sub(new_dark.strip() + '\n', css)

# Fix var names across the file
css = css.replace('var(--bg)', 'var(--bg-primary)')
css = css.replace('var(--ink)', 'var(--text-primary)')
css = css.replace('var(--muted)', 'var(--text-secondary)')
css = css.replace('var(--line)', 'var(--border)')
css = css.replace('var(--surface2)', 'var(--surface-soft)')
css = css.replace('var(--red)', 'var(--pink)')
css = css.replace('var(--red2)', 'var(--peach)')
css = css.replace('var(--gold)', 'var(--yellow)')
css = css.replace('var(--indigo)', 'var(--blue)')

# Body update
body_pattern = re.compile(r'body\s*\{.*?font-family:.*?;.*?\}', re.DOTALL)
def body_repl(m):
    return m.group(0).replace('\"DM Sans\"', '\"Quicksand\"')
css = body_pattern.sub(body_repl, css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
