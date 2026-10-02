import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .page-head h1
old_h1 = '''.page-head h1 {
    color: var(--pink) !important;
    -webkit-text-stroke: 2px var(--text-primary);
    text-shadow: 4px 4px 0px var(--text-primary);
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 42px !important;
}'''
new_h1 = '''.page-head h1 {
    color: var(--pink) !important;
    -webkit-text-stroke: 0px !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary), 4px 4px 0px var(--text-primary) !important;
    font-family: 'DotGothic16', sans-serif !important;
    font-size: 42px !important;
}'''
if old_h1 in css:
    css = css.replace(old_h1, new_h1)

# 2. Update .eyebrow
old_eyebrow = '''.page-head .eyebrow {
    color: var(--yellow) !important;
    font-weight: 800;
    -webkit-text-stroke: 1px var(--text-primary);
    font-size: 18px !important;
    letter-spacing: 2px;
}'''
new_eyebrow = '''.page-head .eyebrow {
    color: var(--yellow) !important;
    font-weight: 800;
    -webkit-text-stroke: 0px !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary), 2px 2px 0px var(--text-primary) !important;
    font-size: 18px !important;
    letter-spacing: 2px;
}'''
if old_eyebrow in css:
    css = css.replace(old_eyebrow, new_eyebrow)

# 3. Update .big-number
old_bignum = '''.big-number {
    font-size: 34px;
    font-weight: 800;
    color: var(--pink)
}'''
new_bignum = '''.big-number {
    font-size: 34px !important;
    font-weight: 800 !important;
    color: var(--pink) !important;
    font-family: 'DotGothic16', sans-serif !important;
    -webkit-text-stroke: 0px !important;
    text-shadow: -1px -1px 0 var(--text-primary), 1px -1px 0 var(--text-primary), -1px 1px 0 var(--text-primary), 1px 1px 0 var(--text-primary), 3px 3px 0px var(--text-primary) !important;
}'''
if old_bignum in css:
    css = css.replace(old_bignum, new_bignum)

# 4. Decrease opacity from 55% (0.55 / 8C) to 35% (0.35 / 59)
css = css.replace('rgba(253, 251, 247, 0.55)', 'rgba(253, 251, 247, 0.35)')
css = css.replace('#C9DCC78C', '#C9DCC759')
css = css.replace('#F4A6A68C', '#F4A6A659')
css = css.replace('#C9DCE48C', '#C9DCE459')
css = css.replace('#F3D99B8C', '#F3D99B59')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
