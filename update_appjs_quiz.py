import re

with open('app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

# Add startKanjiTest and startGrammarTest
new_functions = """
function startKanjiTest(type) {
  state.testMode = "kanji";
  let kanjiItems = KANJI;
  if (type === 'quick') kanjiItems = shuffle(KANJI).slice(0, 10);
  else if (type === 'n5') kanjiItems = KANJI;
  else kanjiItems = shuffle(KANJI).slice(0, 20); // mixed
  
  let qQueue = [];
  kanjiItems.forEach(k => {
     let isKtoR = Math.random() < 0.5;
     let correctOpt = isKtoR ? (k.kunReadings[0] || k.onReadings[0] || k.meanings[0]) : k.character;
     let qText = isKtoR ? k.character : (k.kunReadings[0] || k.onReadings[0] || k.meanings[0]);
     
     let distractors = [];
     let attempts = 0;
     while(distractors.length < 3 && attempts < 100) {
         attempts++;
         let r = KANJI[Math.floor(Math.random() * KANJI.length)];
         if (r.kanjiNumber === k.kanjiNumber) continue;
         let opt = isKtoR ? (r.kunReadings[0] || r.onReadings[0] || r.meanings[0]) : r.character;
         if (opt && !distractors.includes(opt) && opt !== correctOpt) distractors.push(opt);
     }
     let options = shuffle([correctOpt, ...distractors]);
     
     qQueue.push({
         id: 'k' + k.kanjiNumber,
         lesson: 'Kanji ' + k.kanjiNumber,
         dir: isKtoR ? 'Kanji → Reading/Meaning' : 'Reading/Meaning → Kanji',
         questionText: qText,
         options: options.map(o => ({ text: o, isCorrect: o === correctOpt })),
         correctText: correctOpt,
     });
  });
  
  state.queue = shuffle(qQueue).slice(0, (type === 'quick' ? 10 : (type === 'mixed' ? 20 : qQueue.length)));
  state.index = 0;
  state.score = 0;
  state.history = [];
  $("quizScope").textContent = type === 'quick' ? "Quick Kanji" : (type === 'n5' ? "N5 Challenge" : "Mixed Kanji");
  showView("quiz");
  nextQuestion();
}

function startGrammarTest(type) {
  state.testMode = "grammar";
  let grammarPoints = [];
  GRAMMAR.forEach(lesson => {
      lesson.grammarPoints.forEach(p => {
          grammarPoints.push({ ...p, lessonId: lesson.lessonId });
      });
  });
  let selected = grammarPoints;
  if (type === 'quick') selected = shuffle(grammarPoints).slice(0, 10);
  else if (type === 'mixed') selected = shuffle(grammarPoints).slice(0, 20);
  
  let qQueue = [];
  selected.forEach(g => {
      // Create a fill-in-the-blank question using the example sentence
      if (!g.exampleSentence) return;
      let qText = g.exampleSentence;
      // Mask out a particle or part of the pattern if possible, else just ask for meaning
      let correctOpt = g.pattern.split(" ")[0] || "です"; // Fallback dummy logic
      
      // Since generating perfect grammar MCQs dynamically is hard, we'll ask for English meaning!
      qText = g.exampleSentence;
      correctOpt = g.meaning;
      let distractors = [];
      while(distractors.length < 3) {
          let r = grammarPoints[Math.floor(Math.random() * grammarPoints.length)];
          if (r.id === g.id) continue;
          if (!distractors.includes(r.meaning) && r.meaning !== correctOpt) distractors.push(r.meaning);
      }
      let options = shuffle([correctOpt, ...distractors]);
      
      qQueue.push({
         id: 'g' + g.id,
         lesson: 'Lesson ' + g.lessonId,
         dir: 'Grammar Context',
         questionText: qText,
         options: options.map(o => ({ text: o, isCorrect: o === correctOpt })),
         correctText: correctOpt,
      });
  });
  
  state.queue = shuffle(qQueue).slice(0, (type === 'quick' ? 10 : (type === 'mixed' ? 20 : qQueue.length)));
  if (state.queue.length === 0) {
      alert("Not enough grammar data!");
      return;
  }
  state.index = 0;
  state.score = 0;
  state.history = [];
  $("quizScope").textContent = type === 'quick' ? "Quick Grammar" : "Mixed Grammar";
  showView("quiz");
  nextQuestion();
}

function selectOptionGeneric(idx) {
  if (state.answered) return;
  state.answered = true;
  const selected = state.currentOptions[idx];
  state.lastSelectedObj = selected;
  const isCorrect = selected.isCorrect;
  state.lastCorrect = isCorrect;
  state.currentOptions.forEach((opt, i) => {
    const btn = $("opt" + i);
    btn.disabled = true;
    if (opt.isCorrect) btn.classList.add("correct");
    else if (i === idx && !isCorrect) btn.classList.add("incorrect");
  });
  $("nextAction").classList.remove("hidden");
}

function gradeGeneric() {
  if (state.lastCorrect) {
    state.score++;
    // markCorrect for grammar/kanji? 
    // let's leave it out or add dummy for now
  } else {
    // markWrong
  }
  
  state.history.push({
    id: state.current.id,
    lesson: state.current.lesson,
    dir: state.current.dir,
    questionText: state.current.questionText,
    selectedAnswer: state.lastSelectedObj ? state.lastSelectedObj.text : "Timeout",
    correctAnswer: state.current.correctText,
    known: state.lastCorrect,
  });

  state.index++;
  nextQuestion();
}

"""

# Append to app.js
if "function startKanjiTest" not in app_js:
    app_js += "\n" + new_functions

# Now modify nextQuestion to intercept
next_q_start = app_js.find('function nextQuestion() {')
if next_q_start != -1:
    insertion = """
  if (state.testMode === "kanji" || state.testMode === "grammar") {
      state.current = state.queue[state.index];
      $("question").textContent = state.current.questionText;
      state.currentOptions = state.current.options;
      state.answered = false;
      $("mcqGrid").innerHTML = state.currentOptions.map((opt, i) => {
          return `<button class="mcq-option" id="opt${i}" onclick="selectOptionGeneric(${i})">${escapeHtml(opt.text)}</button>`;
      }).join("");
      $("mcqGrid").classList.remove("hidden");
      $("nextAction").classList.add("hidden");
      $("lessonTag").textContent = state.current.lesson;
      $("quizDirection").textContent = state.current.dir;
      $("quizProgress").textContent = `${state.index + 1} / ${state.queue.length}`;
      $("progressBar").style.width = `${(state.index / state.queue.length) * 100}%`;
      return;
  }
"""
    # Insert right after `if (state.index >= state.queue.length) { finishQuiz(); return; }`
    target_idx = app_js.find('state.current = state.queue[state.index];', next_q_start)
    if target_idx != -1:
        app_js = app_js[:target_idx] + insertion + app_js[target_idx:]

# Modify selectOption to reset testMode in startPractice
start_p_idx = app_js.find('function startPractice() {')
if start_p_idx != -1:
    app_js = app_js[:start_p_idx+26] + '\n  state.testMode = "vocab";' + app_js[start_p_idx+26:]

# Modify grade to branch
grade_idx = app_js.find('function grade() {')
if grade_idx != -1:
    app_js = app_js[:grade_idx+18] + '\n  if (state.testMode === "kanji" || state.testMode === "grammar") return gradeGeneric();\n' + app_js[grade_idx+18:]

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(app_js)

print("app.js updated successfully!")
