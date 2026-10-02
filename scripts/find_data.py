with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
if 'const VOCAB =' in js: print('VOCAB exists')
if 'const GRAMMAR =' in js: print('GRAMMAR exists')
if 'const KANJI =' in js: print('KANJI exists')

