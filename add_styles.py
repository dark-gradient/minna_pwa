with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('''

/* =========================================
   NEW RETRO UI STYLES
   ========================================= */

/* Topbar Hide (Mobile First) */
.topbar { display: none; } /* We will hide it or re-purpose it */

/* Bottom Navigation */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 64px;
    background: var(--bg-primary);
    border-top: 2px solid var(--border);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding-bottom: env(safe-area-inset-bottom);
    z-index: 100;
}
.nav-btn {
    background: none;
    border: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 700;
    gap: 4px;
    border-radius: 8px;
    padding: 6px 12px;
    transition: 0.2s;
}
.nav-btn.active {
    color: var(--text-primary);
    background: var(--pink);
}
.nav-icon {
    font-size: 20px;
}

/* Page Spacing for Bottom Nav */
.app-shell {
    padding-bottom: 90px; 
}

/* Welcome Screen */
.welcome-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
    text-align: center;
}
.welcome-logo {
    font-family: 'Noto Sans JP';
    font-size: 24px;
    font-weight: 800;
    color: var(--pink);
    margin-bottom: 12px;
}
.welcome-title {
    font-size: 32px;
    letter-spacing: 2px;
    margin: 0 0 16px 0;
}
.welcome-subtitle {
    font-size: 18px;
    color: var(--text-secondary);
    margin-bottom: 40px;
}
.welcome-start-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 16px 32px;
    border-radius: 12px;
}
.welcome-start-btn .jp-text { font-size: 20px; font-weight: 700; }
.welcome-start-btn .en-text { font-size: 11px; letter-spacing: 2px; opacity: 0.8; }

/* Dashboard Cards */
.dashboard {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.streak-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: var(--shadow);
}
.streak-icon {
    font-size: 32px;
}
.streak-text strong {
    display: block;
    font-size: 18px;
    color: var(--text-primary);
}
.streak-text div {
    font-size: 14px;
    color: var(--text-secondary);
}
.dashboard-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}
.dash-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 16px;
    text-align: center;
    box-shadow: var(--shadow);
    cursor: pointer;
}
.dash-card:active { transform: translateY(2px); box-shadow: none; }
.dash-card-jp {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 4px;
}
.dash-card-en {
    font-size: 12px;
    color: var(--text-secondary);
    margin-bottom: 12px;
}
.dash-progress {
    font-size: 14px;
    font-weight: bold;
    color: var(--green);
}
.progress-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: var(--shadow);
}
.progress-bar-container {
    flex: 1;
    height: 12px;
    background: var(--bg-primary);
    border: 2px solid var(--border);
    border-radius: 6px;
    overflow: hidden;
}
.progress-bar-fill {
    height: 100%;
    background: var(--green);
}
.progress-text {
    font-weight: 700;
}

/* Mock Test */
.test-header {
    margin-bottom: 20px;
}
.test-badge {
    display: inline-block;
    background: var(--pink);
    color: var(--text-primary);
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 8px;
}
.test-header h2 { margin: 0 0 4px 0; font-size: 20px; }
.test-header p { margin: 0; color: var(--text-secondary); }
.test-meta {
    display: flex;
    gap: 16px;
    font-size: 14px;
    font-weight: bold;
    color: var(--green);
}
.empty-state {
    text-align: center;
    padding: 40px 20px;
    background: var(--surface);
    border: 2px dashed var(--border);
    border-radius: var(--radius);
    color: var(--text-muted);
}

/* More Menu */
.more-menu {
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.more-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 20px;
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
    font-size: 16px;
    font-weight: 600;
}
.more-item:active { transform: translateY(2px); box-shadow: none; }

/* Global components override */
.primary-btn {
    background: var(--text-primary);
    color: var(--bg-primary);
    border: 2px solid var(--text-primary);
    border-radius: var(--radius);
    box-shadow: 4px 4px 0px var(--pink);
}
.primary-btn:active { transform: translateY(4px) translateX(4px); box-shadow: 0px 0px 0px var(--pink); }

.secondary-btn {
    background: var(--surface);
    color: var(--text-primary);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    box-shadow: 2px 2px 0px var(--border-strong);
}
.secondary-btn:active { transform: translateY(2px) translateX(2px); box-shadow: 0px 0px 0px var(--border-strong); }

.panel, .quiz-card, .lesson-card {
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
}
''')
