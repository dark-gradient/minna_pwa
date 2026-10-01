const fs = require('fs');

let GRAMMAR = [];
let KANJI = [];
let html = '';

try {
  GRAMMAR = JSON.parse(fs.readFileSync('data/grammar/lessons-01-25.json', 'utf8'));
  KANJI = JSON.parse(fs.readFileSync('data/kanji/kanji-320.json', 'utf8'));
} catch(e) {
  console.log("Parse error:", e);
}

const lessonNames = {1: "Introductions"}; // Dummy

function renderGrammar() {
  if (!GRAMMAR.length) {
    console.log("GRAMMAR empty");
    return;
  }
  html = GRAMMAR.map(g => {
    let pts = g.grammarPoints.length;
    return `<button class="lesson-card" onclick="openGrammarLesson(${g.lessonId})">
      <span class="lesson-no">LESSON ${String(g.lessonId).padStart(2, '0')}</span>
      <h3>${lessonNames[g.lessonId]}</h3><p>${pts} grammar points</p>
    </button>`;
  }).join("");
  console.log("Grammar HTML length:", html.length);
}

renderGrammar();
