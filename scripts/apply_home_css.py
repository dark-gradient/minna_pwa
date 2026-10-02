import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will append the new CSS for the Home Screen to the end
new_css = '''

/* === NEW HOME SCREEN EXACT STYLING === */
#homeView {
    padding: 0 20px 100px 20px;
}

/* Home Header */
.topbar-home {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-top: 20px;
    margin-bottom: 24px;
}
.home-title h1 {
    font-size: 26px;
    font-weight: 800;
    margin: 0;
    color: var(--text-primary);
    line-height: 1.2;
}
.home-title .subtitle {
    font-size: 11px;
    font-weight: 800;
    color: var(--text-secondary);
    letter-spacing: 1px;
    text-transform: uppercase;
}
.home-actions {
    display: flex;
    gap: 12px;
}
.home-actions .icon-btn {
    width: 36px;
    height: 36px;
    border-radius: 12px;
    background: transparent;
    border: none;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}
.home-actions .icon-btn:last-child {
    background: var(--surface);
    border: 2px solid var(--border-strong);
}

/* Streak Card */
.streak-card {
    background: var(--pink);
    border: 2px solid var(--border-strong);
    border-radius: 20px;
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    box-shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);
}
.streak-content h2 {
    font-size: 20px;
    font-weight: 800;
    margin: 0 0 8px 0;
    color: var(--text-primary);
}
.streak-content p {
    font-size: 12px;
    font-weight: 700;
    margin: 0;
    color: var(--text-primary);
}
.streak-mascot {
    width: 60px;
    height: 60px;
    background: url('https://cdn-icons-png.flaticon.com/512/1864/1864514.png') center/contain no-repeat; /* Temp placeholder */
}

/* Section Header */
.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
}
.section-header h2 {
    font-size: 18px;
    font-weight: 800;
    color: var(--text-primary);
    margin: 0;
}
.section-header .chevron {
    font-size: 20px;
    font-weight: 800;
    color: var(--text-primary);
}

/* Practice Grid */
.practice-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 30px;
}
.practice-card {
    border-radius: 20px;
    padding: 16px;
    border: 2px solid var(--border-strong);
    box-shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
.practice-card.bg-green { background-color: var(--green-soft); }
.practice-card.bg-pink { background-color: var(--pink); }
.practice-card.bg-blue { background-color: var(--blue); }
.practice-card.bg-yellow { background-color: var(--yellow); }

.card-icon {
    font-size: 32px;
    margin-bottom: 12px;
}
.card-jp {
    font-size: 20px;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 2px;
    font-family: 'Noto Sans JP', sans-serif;
}
.card-en {
    font-size: 12px;
    font-weight: 700;
    color: var(--text-secondary);
    margin-bottom: 16px;
}
.card-progress {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 8px;
}
.card-progress .progress-bar {
    flex: 1;
    height: 6px;
    background: rgba(255,255,255,0.4);
    border-radius: 3px;
    border: 1px solid var(--border-strong);
    overflow: hidden;
}
.card-progress .progress-fill {
    height: 100%;
    background: var(--green);
}
.card-progress .progress-text {
    font-size: 10px;
    font-weight: 800;
    color: var(--text-primary);
}

/* Progress Card */
.progress-card {
    background: var(--surface);
    border: 2px solid var(--border-strong);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 4px 4px 0px rgba(29, 45, 58, 0.1);
}
.progress-row {
    display: flex;
    align-items: center;
    gap: 16px;
}
.progress-percent {
    font-size: 24px;
    font-weight: 800;
    color: var(--text-primary);
}
.progress-bar-large {
    flex: 1;
    height: 12px;
    background: var(--surface-soft);
    border-radius: 6px;
    border: 1px solid var(--border-strong);
    overflow: hidden;
}
.progress-fill-large {
    height: 100%;
    background: var(--green);
    border-radius: 6px;
}
.progress-topics {
    font-size: 10px;
    font-weight: 700;
    color: var(--text-secondary);
    text-align: right;
    line-height: 1.2;
}

/* Hide global topbar when in home */
body.home-active .topbar {
    display: none !important;
}

/* Ensure Bottom Nav has exact styling from image */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 80px;
    background: var(--bg-primary);
    border-top: 2px solid var(--border-strong);
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    padding-top: 10px;
    padding-bottom: env(safe-area-inset-bottom, 10px);
    z-index: 1000;
}
.nav-btn {
    background: none;
    border: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    color: var(--text-primary);
    font-family: inherit;
    cursor: pointer;
}
.nav-icon {
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    font-size: 24px;
}
.nav-btn.active .nav-icon {
    background: var(--pink);
    border: 2px solid var(--border-strong);
}
.nav-btn span {
    font-size: 10px;
    font-weight: 800;
}
'''

# We will remove the old .streak-card and .bottom-nav definitions to avoid conflicts
css = re.sub(r'\.streak-card\s*\{.*?\}', '', css, flags=re.DOTALL)
css = re.sub(r'\.bottom-nav\s*\{.*?\}', '', css, flags=re.DOTALL)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + new_css)
