import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_welcome = '''    <section id="welcomeView" class="view">
      <div class="welcome-container" style="display: flex; flex-direction: column; height: 100vh; background: var(--bg-primary); overflow: hidden; padding-bottom: 40px;">
        
        <div style="text-align: center; margin-top: 80px; position: relative;">
          <h1 style="font-family: 'Courier New', monospace; font-weight: 900; font-size: 52px; line-height: 1; margin: 0; color: var(--text-primary); text-transform: uppercase;">
            Minna<br>Kotoba
            <span style="position: absolute; right: 20%; top: 0; font-size: 30px;">🌸</span>
          </h1>
          <div style="font-weight: 800; font-size: 14px; margin-top: 12px; color: var(--text-primary);">みんなのことば</div>
          <p style="font-family: 'Courier New', monospace; font-size: 13px; font-weight: 700; margin-top: 24px; color: var(--text-primary);">Learn Japanese.<br>Step by step. Together.</p>
        </div>

        <div style="flex: 1; display: flex; align-items: center; justify-content: center; position: relative; margin: 20px 0;">
          <img src="fuji.jpg" alt="Mount Fuji Pixel Art" style="width: 100%; max-width: 400px; object-fit: contain;">
        </div>

        <div style="padding: 0 40px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 12px;">
          <button class="primary-btn" onclick="showView('home')" style="width: 100%; max-width: 300px; background: var(--pink); color: var(--text-primary); border: 3px solid var(--text-primary); border-radius: 12px; padding: 16px; font-size: 24px; font-weight: 800; box-shadow: 4px 4px 0px var(--text-primary); display: flex; justify-content: space-between; align-items: center;">
            <span style="flex: 1; text-align: center;">はじめる</span>
            <span>→</span>
          </button>
          <div style="font-family: 'Courier New', monospace; font-size: 11px; font-weight: 700; letter-spacing: 2px; color: var(--text-primary);">GET STARTED</div>
          
          <div style="display: flex; gap: 8px; margin-top: 24px;">
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--pink);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
            <div style="width: 8px; height: 8px; border-radius: 50%; background: var(--border-strong);"></div>
          </div>
        </div>
      </div>
    </section>'''

html = re.sub(r'<section id="welcomeView" class="view">.*?</section>', new_welcome, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
