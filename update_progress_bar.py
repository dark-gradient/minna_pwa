import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
.progress-card {
    background: transparent;
    border: none;
    padding: 8px 0;
    box-shadow: none;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s;
    width: 100%;
}
.progress-card:hover {
    transform: translateY(-2px);
}

.progress-row {
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px;
    width: 100%;
    box-sizing: border-box;
}
.progress-percent {
    font-size: 26px;
    font-weight: 900;
    color: var(--pink);
    font-family: 'Noto Sans JP', sans-serif;
    text-shadow: 2px 2px 0 var(--text-primary);
    min-width: 60px;
}
.progress-bar-large {
    flex: 1;
    height: 14px;
    background: rgba(23, 37, 42, 0.4);
    border: 2px solid var(--text-primary);
    border-radius: 8px;
    box-shadow: inset 2px 2px 0 rgba(0,0,0,0.3);
    position: relative;
    overflow: hidden;
}
.progress-fill-large {
    height: 100%;
    background: var(--pink);
    border-right: 2px solid var(--text-primary);
    transition: width 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.progress-topics {
    font-size: 14px;
    font-weight: 800;
    color: var(--text-primary);
    text-shadow: 1px 1px 0 rgba(255,255,255,0.6);
    text-align: right;
    line-height: 1.2;
    text-transform: uppercase;
    font-family: 'DotGothic16', sans-serif;
    min-width: 60px;
}
"""

# Replace the specific block starting from .progress-card at around line 1361
# to the end of .progress-topics.
# We have to be careful since .progress-card is defined twice in styles.css.
# The first one is around 1094. The second one is around 1361.
# Let's just find the second occurrence.

# Split by ".progress-card {"
parts = css.split('.progress-card {')
if len(parts) >= 3:
    # parts[2] is the second .progress-card definition
    # Let's find where .progress-topics ends in parts[2]
    match = re.search(r'\.progress-topics\s*{[^}]*}', parts[2])
    if match:
        end_idx = match.end()
        # The text to replace is from the beginning of parts[2] up to end_idx
        # But we need to stitch it back carefully.
        # It's easier to use a regex on the whole file that targets the block with progress-fill-large inside it.
        pass

# Better approach: target the exact sequence of classes.
pattern = re.compile(r'\.progress-card\s*{[^}]*}\s*\.progress-card:hover\s*{[^}]*}\s*\.progress-row\s*{[^}]*}\s*\.progress-percent\s*{[^}]*}\s*\.progress-bar-large\s*{[^}]*}\s*\.progress-fill-large\s*{[^}]*}\s*\.progress-topics\s*{[^}]*}', re.DOTALL)

css = pattern.sub(new_css.strip(), css)

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
