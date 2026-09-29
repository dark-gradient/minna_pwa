const jsdom = require('jsdom');
const { JSDOM } = jsdom;
const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');
const js = fs.readFileSync('app.js', 'utf8');

const dom = new JSDOM(html, { runScripts: 'dangerously' });
const window = dom.window;
const document = window.document;

// We need to inject the JS and run it
const script = document.createElement('script');
script.textContent = js;
document.body.appendChild(script);

// Set up mock state
window.currentLessonId = 1;
window.VOCAB = {
    1: [
        { jp: "Word1", en: "English1" },
        { jp: "Word2", en: "English2" }
    ]
};
window.currentLessonWords = window.VOCAB[1];
window.lessonNames = { 1: "Lesson 1" };

try {
    window.openLesson(1);
    console.log("Opened lesson, rows rendered:", document.querySelectorAll('.vocab-row').length);
    window.selectAllInLesson();
    console.log("Selected all, selected rows:", document.querySelectorAll('.selected').length);
    window.clearLessonSelection();
    console.log("Cleared selection, selected rows:", document.querySelectorAll('.selected').length);
    console.log("Success! No crashes.");
} catch (e) {
    console.error("Crash!", e);
}
