with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the duplicate closing section tag
html = html.replace('      </div>\n    </section>\n     </section>', '      </div>\n    </section>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import re
with open('sw.js', 'r', encoding='utf-8') as f:
    sw = f.read()
sw = re.sub(r'minna-kotoba-v\d+', 'minna-kotoba-v66', sw)
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw)
print('Done')
