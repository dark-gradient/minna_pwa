import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

dashboard_func = '''
function updateDashboardStats() {
    const vocabTotal = 855;
    const grammarTotal = 120;
    const listeningTotal = 50;
    const kanjiTotal = 110;
    
    let completedVocab = 0;
    try {
        let fw = JSON.parse(localStorage.getItem("minna_focus_words")) || {};
        completedVocab = Object.keys(fw).length;
    } catch(e) {}
    
    const updateBar = (id, current, total) => {
        const bar = document.getElementById(id);
        const text = document.getElementById(id.replace('bar', 'stat'));
        if (bar && text) {
            let pct = total > 0 ? Math.round((current / total) * 100) : 0;
            if (pct > 100) pct = 100;
            bar.style.width = pct + '%';
            text.innerText = current + '/' + total;
        }
    };
    
    updateBar('barVocab', completedVocab, vocabTotal);
    updateBar('barGrammar', 0, grammarTotal);
    updateBar('barListening', 0, listeningTotal);
    updateBar('barKanji', 0, kanjiTotal);
    
    const totalN5 = vocabTotal + grammarTotal + listeningTotal + kanjiTotal;
    const currentN5 = completedVocab;
    let n5Pct = totalN5 > 0 ? Math.round((currentN5 / totalN5) * 100) : 0;
    
    let n5Bar = document.getElementById('n5ProgressBar');
    let n5PercentText = document.getElementById('n5Percent');
    let n5TopicsText = document.getElementById('n5Topics');
    if (n5Bar) n5Bar.style.width = n5Pct + '%';
    if (n5PercentText) n5PercentText.innerText = n5Pct + '%';
    if (n5TopicsText) n5TopicsText.innerHTML = currentN5 + '/' + totalN5 + '<br>Items';
}
'''

# insert it before unction showView
js = js.replace('function showView(view)', dashboard_func + '\nfunction showView(view)')

# add a call to updateDashboardStats inside showView if view is homeView
call_logic = '''
    if (view === 'home' || view === 'homeView') {
        updateDashboardStats();
    }
'''
js = js.replace('document.body.classList.add(baseName + \'-active\');', 'document.body.classList.add(baseName + \'-active\');\n' + call_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
