import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
.omamori-tray {
  width: 100%;
  height: auto;
  max-height: calc(100vh - 40px);
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  background-color: #F7F1E7;
  border: 3px solid #21483D;
  border-right: none;
  border-radius: 16px 0 0 16px;
  padding: 32px 16px 32px 24px;
  box-shadow: -4px 4px 0 rgba(244, 166, 166, 0.4), -4px 4px 0 2px rgba(33, 72, 61, 0.2) inset;
  overflow-y: auto;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.omamori-tray::-webkit-scrollbar {
  display: none;
}

.omamori-header {
  padding-bottom: 24px;
  text-align: center;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.omamori-header-title {
  font-family: 'DotGothic16', sans-serif;
  font-size: 16px;
  letter-spacing: 3px;
  color: #21483D;
  font-weight: bold;
}

.omamori-header-decor {
  font-size: 14px;
  color: #F4A6A6;
}

.omamori-string-horizontal {
  position: absolute;
  top: 24px;
  left: -24px;
  width: 24px;
  height: 4px;
  background-color: #d13030;
  border-top: 1px solid #17252A;
  border-bottom: 1px solid #17252A;
  z-index: 2002;
}

.omamori-tag {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  position: absolute;
  top: 26px;
  left: -42px;
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 2003;
  transform-origin: top center;
  transition: transform 0.2s;
}

.omamori-nav.open .omamori-tag {
  animation: swingOpen 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.omamori-nav:not(.open) .omamori-tag {
  animation: swingClose 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

.omamori-tag:hover {
  transform: rotate(5deg) !important;
  animation: none !important;
}

@keyframes swingOpen {
  0% { transform: rotate(0deg); }
  30% { transform: rotate(25deg); }
  60% { transform: rotate(-10deg); }
  80% { transform: rotate(5deg); }
  100% { transform: rotate(0deg); }
}

@keyframes swingClose {
  0% { transform: rotate(0deg); }
  30% { transform: rotate(-25deg); }
  60% { transform: rotate(10deg); }
  80% { transform: rotate(-5deg); }
  100% { transform: rotate(0deg); }
}

.omamori-cord {
  position: relative;
  font-size: 28px;
  line-height: 1;
  z-index: 2;
  margin-bottom: -10px;
  filter: drop-shadow(1px 1px 0 #17252A) drop-shadow(-1px -1px 0 #17252A);
}

.omamori-bell {
  position: absolute;
  bottom: -4px;
  right: -12px;
  font-size: 18px;
}

.omamori-body {
  width: 36px;
  height: 60px;
  background: var(--pink);
  border: 2px solid #17252A;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 2px 2px 0 rgba(23, 37, 42, 0.2);
  color: #fff;
  text-shadow: 1px 1px 0 #17252A;
}

@media (prefers-reduced-motion: reduce) {
  .omamori-container {
    transition: transform 0.2s ease-out;
  }
  .omamori-nav.open .omamori-tag, .omamori-nav:not(.open) .omamori-tag {
    animation: none;
  }
}

.omamori-menu {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 24px;
  flex: 1;
}

.omamori-btn {
  width: 100%;
  background: transparent;
  border: none;
  padding: 12px 12px;
  border-radius: 8px;
  display: grid;
  grid-template-columns: 72px 1fr;
  align-items: center;
  gap: 16px;
  font-family: 'DotGothic16', sans-serif;
  cursor: pointer;
  transition: all 0.2s ease;
  text-align: left;
  position: relative;
}

.omamori-btn:hover, .omamori-btn:focus-visible {
  background: rgba(246, 217, 184, 0.4);
  transform: translateX(-4px);
  outline: none;
}

.omamori-btn.active {
  background: rgba(244, 166, 166, 0.15);
}

.omamori-btn.active::before {
  content: "✿";
  position: absolute;
  left: -12px;
  color: #F4A6A6;
  font-size: 14px;
}

.omamori-icon-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 72px;
  height: 72px;
}

.omamori-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  image-rendering: pixelated;
  filter: drop-shadow(2px 2px 0px rgba(0,0,0,0.1));
}

.omamori-label {
  display: flex;
  flex-direction: column;
  justify-content: center;
  white-space: nowrap;
}

.omamori-label .jp {
  font-size: 20px;
  font-weight: 700;
  color: #21483D;
  line-height: 1.2;
}

.omamori-label .en {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: rgba(23, 37, 42, 0.6);
  line-height: 1.2;
  margin-top: 2px;
}
"""

pattern = re.compile(r'\.omamori-tray\s*{.*?\.omamori-label\s*\.en\s*{[^}]*}', re.DOTALL)
css = pattern.sub(new_css.strip(), css)

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
