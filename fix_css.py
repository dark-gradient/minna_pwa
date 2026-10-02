import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Omamori Navigation */
.omamori-nav {
  position: fixed;
  top: env(safe-area-inset-top, 80px);
  right: 0;
  z-index: 2000;
  pointer-events: none;
}

.omamori-nav.open {
  pointer-events: auto;
}

.omamori-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.2);
  z-index: 1999;
  display: none;
  opacity: 0;
  transition: opacity 0.2s;
  pointer-events: auto;
}

.omamori-nav.open .omamori-overlay {
  display: block;
  opacity: 1;
}

.omamori-container {
  position: absolute;
  top: 0;
  right: 0;
  width: min(320px, calc(100vw - 24px));
  transform: translateX(100%);
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 2001;
  pointer-events: auto;
}

.omamori-nav.open .omamori-container {
  transform: translateX(0);
}

.omamori-tray {
  width: 100%;
  height: auto;
  max-height: calc(100vh - 100px);
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  background-color: var(--pink);
  background-image: radial-gradient(rgba(243, 217, 155, 0.6) 15%, transparent 16%), radial-gradient(rgba(243, 217, 155, 0.6) 15%, transparent 16%);
  background-size: 20px 20px;
  background-position: 0 0, 10px 10px;
  border: 3px solid #17252A;
  border-right: none;
  border-radius: 16px 0 0 16px;
  padding: 24px 16px;
  box-shadow: -6px 6px 0 rgba(243, 217, 155, 1), -6px 6px 0 3px #17252A inset;
  overflow-y: auto;
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.omamori-tray::-webkit-scrollbar {
  display: none;
}

.omamori-header {
  padding-bottom: 12px;
  margin-bottom: 12px;
  border-bottom: 2px dashed rgba(23, 37, 42, 0.2);
  text-align: center;
  flex-shrink: 0;
}

.omamori-header-title {
  font-family: 'DotGothic16', sans-serif;
  font-size: 16px;
  letter-spacing: 2px;
  color: #17252A;
  font-weight: bold;
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
  gap: 8px;
  flex: 1;
}

.omamori-btn {
  width: 100%;
  background: transparent;
  border: 2px solid transparent;
  border-bottom: 2px dashed rgba(23, 37, 42, 0.15);
  border-radius: 8px;
  padding: 8px 12px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 16px;
  font-family: 'DotGothic16', sans-serif;
  color: #17252A;
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}

.omamori-btn:hover, .omamori-btn:focus-visible {
  background: rgba(243, 217, 155, 0.95);
  border-color: #17252A;
  box-shadow: 2px 2px 0 #17252A;
  transform: translateX(-4px);
  outline: none;
}

.omamori-btn.active {
  background: var(--yellow);
  border-color: #17252A;
  box-shadow: 4px 4px 0 #17252A;
  transform: translateX(-8px);
  color: #17252A;
}

.omamori-icon-wrapper {
  flex: 0 0 52px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.omamori-icon {
  width: 52px;
  height: 52px;
  object-fit: contain;
  image-rendering: pixelated;
  filter: drop-shadow(2px 2px 0px rgba(0,0,0,0.15));
}

.omamori-label {
  display: flex;
  flex-direction: column;
  justify-content: center;
  white-space: nowrap;
}

.omamori-label .jp {
  font-size: 18px;
  font-weight: 700;
  line-height: 1.2;
}

.omamori-label .en {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1px;
  color: rgba(23, 37, 42, 0.7);
  line-height: 1.2;
}
"""

# Replace from /* Omamori Navigation */ down to the end of .omamori-icon block (before the next main block)
pattern = re.compile(r'/\* Omamori Navigation \*/.*?\.omamori-icon\s*{[^}]*}', re.DOTALL)
css = pattern.sub(new_css.strip(), css)

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
