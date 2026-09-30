import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace function showView(view) { with the wrapper
wrapper = """function showView(view) {
  if (!document.startViewTransition) {
    _showView(view);
    return;
  }
  // Try to use view transition
  document.startViewTransition(() => {
    _showView(view);
  });
}

function _showView(view) {"""

js = js.replace("function showView(view) {", wrapper, 1)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
