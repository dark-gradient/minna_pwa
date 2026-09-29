let VOCAB = {},
  KAIWA = {};
let focusWords = JSON.parse(localStorage.getItem("minna_focus_words")) || {};
function saveFocusWords() { localStorage.setItem("minna_focus_words", JSON.stringify(focusWords)); }
let lessonSelection = new Set();
let currentLessonId = null;
let state = {
  view: "home",
  pool: [],
  queue: [],
  index: 0,
  score: 0,
  current: null,
  history: [],
};
let ambiguousEnJpIds = new Set();
let allVocab = [];

function normalizeStr(str) {
  if (!str) return "";
  let s = String(str).toLowerCase().trim();
  s = s.replace(/^(to\s+)/, "");
  s = s.replace(/[.,/#!$%^&*;:{}=\-_`~()]/g, "");
  s = s.replace(/[。、]/g, "");
  s = s.replace(/\s+/g, " ").trim();
  return s;
}

function getSemanticKeys(vocabItem, isEn) {
  if (isEn) {
    return vocabItem.en.split("/").map(normalizeStr).filter(Boolean);
  } else {
    let res = [normalizeStr(vocabItem.jp)];
    if (vocabItem.kanji && vocabItem.kanji !== "—") {
      res.push(normalizeStr(vocabItem.kanji));
    }
    return res;
  }
}

function isDistractorValid(correctItem, distractorItem) {
  if (correctItem.id === distractorItem.id) return false;
  
  if (distractorItem.en === correctItem.en) return false;
  if (distractorItem.jp === correctItem.jp) return false;
  if (distractorItem.kanji !== "—" && distractorItem.kanji === correctItem.kanji) return false;

  const enKeys1 = getSemanticKeys(correctItem, true);
  const enKeys2 = getSemanticKeys(distractorItem, true);
  if (enKeys1.some(k => enKeys2.includes(k))) return false;
  
  const jpKeys1 = getSemanticKeys(correctItem, false);
  const jpKeys2 = getSemanticKeys(distractorItem, false);
  if (jpKeys1.some(k => jpKeys2.includes(k))) return false;
  
  return true;
}

function initAmbiguousSet() {
  allVocab = lessons.flatMap(n=>(VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`})));
  ambiguousEnJpIds.clear();
  let enPromptGroups = {};
  allVocab.forEach(item => {
    let p = normalizeStr(item.en);
    if (!enPromptGroups[p]) enPromptGroups[p] = [];
    enPromptGroups[p].push(item);
  });
  for (let p in enPromptGroups) {
    let group = enPromptGroups[p];
    let jpSet = new Set(group.map(g => normalizeStr(g.jp)));
    if (jpSet.size > 1) {
      group.forEach(g => ambiguousEnJpIds.add(g.id));
    }
  }
}

const $ = (id) => document.getElementById(id);
const lessons = Array.from({ length: 25 }, (_, i) => i + 1);
const lessonNames = {
  1: "Introductions",
  2: "Objects & ownership",
  3: "Places & shopping",
  4: "Time & schedules",
  5: "Travel & dates",
  6: "Food & activities",
  7: "Giving & receiving",
  8: "Adjectives & life",
  9: "Likes & abilities",
  10: "Places & positions",
  11: "Counters & quantities",
  12: "Seasons & comparison",
  13: "Plans & wants",
  14: "Requests & directions",
  15: "Permission & family",
  16: "Daily routines",
  17: "Health & problems",
  18: "Skills & hobbies",
  19: "Experiences",
  20: "Plain-style speech",
  21: "Opinions & events",
  22: "Clothing & apartments",
  23: "Directions & crossing",
  24: "Showing around & helping",
  25: "Conditions & moving",
};
async function loadData() {
  [VOCAB, KAIWA] = await Promise.all([
    fetch("vocab.json").then((r) => r.json()),
    fetch("kaiwa.json").then((r) => r.json()),
  ]);
  initAmbiguousSet();
  init();
}
function getWrongData() {
  return JSON.parse(localStorage.getItem("mnn-wrong-v2")) || {};
}
function saveWrongData(data) {
  localStorage.setItem("mnn-wrong-v2", JSON.stringify(data));
}
function clearWrongData() {
  if (confirm("Clear all saved wrong answers?")) {
    localStorage.removeItem("mnn-wrong-v2");
    renderReview();
    updateReviewPoolCount();
  }
}

function init() {
  const opts = lessons
    .map((n) => `<option value="${n}">Lesson ${n}</option>`)
    .join("");
  $("lessonFrom").innerHTML = opts;
  $("lessonTo").innerHTML = opts;
  $("lessonFrom").value = 1;
  $("lessonTo").value = 5;
  $("reviewLessonFrom").innerHTML = opts;
  $("reviewLessonTo").innerHTML = opts;
  $("reviewLessonFrom").value = 1;
  $("reviewLessonTo").value = 5;

  document
    .querySelectorAll(".nav-btn")
    .forEach((b) => (b.onclick = () => showView(b.dataset.view)));
  ["scopeMode", "lessonFrom", "lessonTo"].forEach((id) =>
    $(id).addEventListener("change", updatePoolCount),
  );
  ["reviewScopeMode", "reviewLessonFrom", "reviewLessonTo"].forEach((id) =>
    $(id).addEventListener("change", updateReviewPoolCount),
  );

  $("startBtn").onclick = startPractice;
  $("startReviewBtn").onclick = startReviewPractice;
  $("clearWrongBtn").onclick = clearWrongData;
  $("nextBtn").onclick = grade;
  $("themeBtn").onclick = toggleTheme;
  renderLessons();
  renderKaiwa();
  updatePoolCount();
  updateReviewPoolCount();
  const saved = localStorage.getItem("mnn-theme");
  if (saved) document.documentElement.dataset.theme = saved;

  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  if (currentStreak === 0 && !localStorage.getItem('minna_last_active')) {
    showView('welcomeView');
  } else {
    showView('home');
  }
}

function reviewWrongAnswers() {
  showView("review");
}

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

function showView(view) {
  const map = {
    welcomeView: "welcomeView",
    home: "homeView",
    quiz: "quizView",
    lessons: "lessonsView",
    lessonDetail: "lessonDetailView",
    kaiwa: "kaiwaView",
    review: "reviewView",
    resultsView: "resultsView",
    focus: "focusView",
    practiceSetup: "practiceSetupView",
    mockTest: "mockTestView",
    more: "moreView"
  };
  Object.values(map).forEach((id) => {
    const el = $(id);
    if (el) el.classList.remove("active");
  });
  const target = $(map[view]);
  if (target) target.classList.add("active");
  state.view = view;
  document
    .querySelectorAll(".nav-btn")
    .forEach((b) => b.classList.toggle("active", b.dataset.view === view));
  document.body.className = '';
  document.body.classList.add(view + '-active');
  if (view === 'welcomeView') {
      document.body.classList.add('welcome-active');
  }
  if (view === "home") updateDashboardStats();
  if (view === "review") renderReview();
  if (view === "focus") renderFocusView();
  if (view === "focus") renderFocusView();
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function poolForScope() {
  const mode = $("scopeMode").value;
  if (mode === "focus") {
    let all = [];
    for (let l in VOCAB) {
      VOCAB[l].forEach((v, i) => {
        let id = +l + "-" + i;
        if (focusWords[id]) all.push({ ...v, lesson: +l, id });
      });
    }
    return all;
  }
  let nums = [];
  if (mode === "lesson") nums = [$("lessonFrom").value];
  else if (mode === "range") {
    let a = +$("lessonFrom").value,
      b = +$("lessonTo").value;
    if (a > b) [a, b] = [b, a];
    for (let i = a; i <= b; i++) nums.push(i);
  } else nums = lessons;
  return nums.flatMap((n) =>
    (VOCAB[n] || []).map((v, i) => ({ ...v, lesson: +n, id: `${n}-${i}` })),
  );
}
function updatePoolCount() {
  const mode = $("scopeMode").value;
  $("lessonFromWrap").classList.toggle("hidden", mode === "all" || mode === "focus");
  $("lessonToWrap").classList.toggle("hidden", mode !== "range");
  $("poolCount").textContent = `${poolForScope().length} words`;
}
function shuffle(a) {
  return [...a].sort(() => Math.random() - 0.5);
}
function startPractice() {
  state.pool = poolForScope();
  if ($("direction").value === "en-jp") {
    state.pool = state.pool.filter(v => !ambiguousEnJpIds.has(v.id));
  }
  if (!state.pool.length) {
    alert("No valid words for this selection.");
    return;
  }
  const size =
    $("sessionSize").value === "all"
      ? state.pool.length
      : +$("sessionSize").value;
  state.queue = shuffle(state.pool).slice(0, size);
  state.index = 0;
  state.score = 0;
  state.history = [];
  $("quizScope").textContent = scopeLabel();
  showView("quiz");
  nextQuestion();
}
function scopeLabel() {
  const mode = $("scopeMode").value;
  if (mode === "lesson") return `Lesson ${$("lessonFrom").value}`;
  if (mode === "range")
    return `Lessons ${Math.min($("lessonFrom").value, $("lessonTo").value)}–${Math.max($("lessonFrom").value, $("lessonTo").value)}`;
  return "Lessons 1–25";
}
function nextQuestion() {
  if (state.index >= state.queue.length) {
    finishQuiz();
    return;
  }
  state.current = state.queue[state.index];
  const requestedDir = $("direction").value;
  let dir = requestedDir;
  if (requestedDir === "mixed") {
    const isAmb = ambiguousEnJpIds.has(state.current.id);
    dir = isAmb ? "jp-en" : (Math.random() < 0.5 ? "jp-en" : "en-jp");
  }
  state.current.dir = dir;
  const isJpEn = dir === "jp-en";
  $("question").textContent = isJpEn
    ? state.current.kanji && state.current.kanji !== "—"
      ? state.current.kanji + " (" + state.current.jp + ")"
      : state.current.jp
    : state.current.en;

  function getVisibleText(opt) {
    return isJpEn ? opt.en : (opt.kanji && opt.kanji !== "—" ? opt.kanji + " (" + opt.jp + ")" : opt.jp);
  }

  function validateQuestion(correctItem, opts, isJpEnFlag) {
    if (!opts || opts.length !== 4) return false;
    const correctCount = opts.filter(o => o.id === correctItem.id).length;
    if (correctCount !== 1) return false;
    const visibleTexts = opts.map(o => isJpEnFlag ? o.en : (o.kanji && o.kanji !== "—" ? o.kanji + " (" + o.jp + ")" : o.jp));
    if (new Set(visibleTexts).size !== 4) return false;
    for (let i = 0; i < opts.length; i++) {
      for (let j = i + 1; j < opts.length; j++) {
        if (!isDistractorValid(opts[i], opts[j])) return false;
      }
    }
    if (!isJpEnFlag && ambiguousEnJpIds.has(correctItem.id)) return false;
    return true;
  }

  let options = [];
  function isValidCandidate(candidate) {
    for (let opt of options) {
      if (!isDistractorValid(opt, candidate)) return false;
      if (getVisibleText(opt) === getVisibleText(candidate)) return false;
    }
    return true;
  }

  function fillOptions(sourcePool) {
    const shuffled = shuffle(sourcePool);
    for (let candidate of shuffled) {
      if (options.length >= 4) break;
      if (isValidCandidate(candidate)) {
        options.push(candidate);
      }
    }
  }

  function generateOptions() {
    for (let attempt = 0; attempt < 5; attempt++) {
      options = [state.current];
      fillOptions(state.pool.filter(v => v.lesson === state.current.lesson));
      if (options.length < 4) fillOptions(state.pool.filter(v => v.lesson !== state.current.lesson));
      if (options.length < 4) fillOptions(allVocab);
      
      if (validateQuestion(state.current, options, isJpEn)) {
        return options;
      }
    }
    return null;
  }

  let finalOptions = generateOptions();
  if (!finalOptions) {
    console.error("Failed to generate safe options for", state.current, "- skipping.");
    state.index++;
    return nextQuestion();
  }
  options = shuffle(finalOptions);
  state.currentOptions = options;
  state.answered = false;

  $("mcqGrid").innerHTML = options
    .map((opt, i) => {
      let text = isJpEn
        ? opt.en
        : opt.kanji && opt.kanji !== "—"
          ? opt.kanji + " (" + opt.jp + ")"
          : opt.jp;
      return `<button class="mcq-option" id="opt${i}" onclick="selectOption(${i})">${escapeHtml(text)}</button>`;
    })
    .join("");

  $("mcqGrid").classList.remove("hidden");
  $("nextAction").classList.add("hidden");

  $("lessonTag").textContent =
    `Lesson ${state.current.lesson} · ${lessonNames[state.current.lesson]}`;
  $("quizDirection").textContent = isJpEn
    ? "Japanese → English"
    : "English → Japanese";
  $("quizProgress").textContent = `${state.index + 1} / ${state.queue.length}`;
  $("progressBar").style.width = `${(state.index / state.queue.length) * 100}%`;
}
function selectOption(idx) {
  if (state.answered) return;
  state.answered = true;
  const selected = state.currentOptions[idx];
  state.lastSelectedObj = selected;
  const isCorrect = selected.id === state.current.id;
  state.lastCorrect = isCorrect;
  state.currentOptions.forEach((opt, i) => {
    const btn = $("opt" + i);
    btn.disabled = true;
    if (opt.id === state.current.id) btn.classList.add("correct");
    else if (i === idx && !isCorrect) btn.classList.add("incorrect");
  });
  $("nextAction").classList.remove("hidden");
}
function grade() {
  if (state.lastCorrect) {
    state.score++;
    markCorrect(state.current.id);
  } else {
    markWrong(state.current.id);
  }
  const isJpEn = state.current.dir === "jp-en";
  const qJp =
    state.current.kanji && state.current.kanji !== "—"
      ? state.current.kanji + " (" + state.current.jp + ")"
      : state.current.jp;
  const qEn = state.current.en;

  const selJp = state.lastSelectedObj
    ? state.lastSelectedObj.kanji && state.lastSelectedObj.kanji !== "—"
      ? state.lastSelectedObj.kanji + " (" + state.lastSelectedObj.jp + ")"
      : state.lastSelectedObj.jp
    : "";
  const selEn = state.lastSelectedObj ? state.lastSelectedObj.en : "";

  state.history.push({
    id: state.current.id,
    lesson: state.current.lesson,
    dir: state.current.dir,
    questionText: isJpEn ? qJp : qEn,
    selectedAnswer: state.lastSelectedObj
      ? isJpEn
        ? selEn
        : selJp
      : "Timeout",
    correctAnswer: isJpEn ? qEn : qJp,
    known: state.lastCorrect,
  });

  state.index++;
  nextQuestion();
}
function finishQuiz() {
  recordActivity();

  $("progressBar").style.width = "100%";
  $("quizProgress").textContent = "Done";
  showView("resultsView");
  const wrongList = state.history.filter((h) => !h.known);
  const wrongCount = wrongList.length;
  const acc = Math.round((state.score / state.queue.length) * 100);

  let html = `
    <div class="results-desktop-split">
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:22px; padding:30px; text-align:center; box-shadow:var(--shadow);">
        <div class="big-number">${state.score} / ${state.queue.length}</div>
        <div style="font-size: 24px; font-weight: 800; color: var(--muted); margin-bottom: 20px;">${acc}%</div>
        <div style="display:flex; justify-content:center; gap:20px; font-weight:700; font-size:14px;">
          <span style="color: var(--green);">✓ Correct &nbsp; ${state.score}</span>
          <span style="color: var(--red);">✕ Wrong &nbsp; ${wrongCount}</span>
        </div>
      </div>
  `;

  if (wrongCount === 0) {
    html += `
      <div style="flex:1; display:flex; align-items:center; justify-content:center;">
        <div style="color: var(--green); font-weight: 800; font-size:18px; text-align:center;">Perfect!<br><span style="font-size:14px; color: var(--muted);">All questions correct.</span></div>
      </div>
    </div>`;
    $("btnReviewWrong").style.display = "none";
  } else {
    html += `
      <div>
        <div class="eyebrow" style="margin-bottom: 15px; text-align:center;">WHAT YOU GOT WRONG</div>
        <div style="display:flex; flex-direction:column; gap:12px;">
    `;
    wrongList.forEach((w) => {
      html += `
        <div style="background:var(--surface2); border-radius:12px; padding:16px; border:1px solid var(--line); text-align:left;">
          <div style="font-size:18px; font-weight:800; font-family:'Noto Sans JP'; margin-bottom:8px;">${escapeHtml(w.questionText)}</div>
          <div style="font-size:13px; color:var(--red); font-weight:600; margin-bottom:4px;">Your: ${escapeHtml(w.selectedAnswer)}</div>
          <div style="font-size:13px; color:var(--green); font-weight:600; margin-bottom:8px;">Correct: ${escapeHtml(w.correctAnswer)}</div>
          <div class="lesson-tag" style="display:inline-block; padding: 4px 8px; font-size:10px;">Lesson ${w.lesson}</div>
        </div>
      `;
    });
    html += `</div></div></div>`;
    $("btnReviewWrong").style.display = "block";
  }

  $("resultsSummary").innerHTML = html;
}
function quickStart(n) {
  $("scopeMode").value = "lesson";
  $("lessonFrom").value = n;
  updatePoolCount();
  startPractice();
}
function renderLessons() {
  const total = lessons.reduce((a, n) => a + (VOCAB[n]?.length || 0), 0);
  $("totalVocab").textContent = `${total} entries`;
  $("lessonGrid").innerHTML = lessons
    .map(
      (n) => `
    <button class="lesson-card" onclick="openLesson(${n})">
      <span class="lesson-no">LESSON ${String(n).padStart(2, "0")}</span>
      <h3>${lessonNames[n]}</h3><p>${VOCAB[n].length} vocabulary entries</p>
    </button>`,
    )
    .join("");
}
let currentLessonWords = [];
function openLesson(n) {
  currentLessonId = n;
  lessonSelection.clear();
  currentLessonWords = VOCAB[n] || [];
  $("detailHeader").innerHTML =
    `<div class="eyebrow">LESSON ${String(n).padStart(2, "0")}</div><h1>${lessonNames[n]}</h1><p>${VOCAB[n].length} vocabulary entries • separate from Kaiwa.</p>`;
  renderLessonVocabRows();
  updateFocusSelectionUI();
  $("detailPractice").onclick = () => {
    $("scopeMode").value = "lesson";
    $("lessonFrom").value = n;
    updatePoolCount();
    startPractice();
  };
  showView("lessonDetail");
}

function renderLessonVocabRows() {
  $("vocabTable").innerHTML = currentLessonWords
    .map(
      (v, i) => {
        let id = currentLessonId + "-" + i;
        let isFocused = !!focusWords[id];
        let isSelected = lessonSelection.has(id);
        return `<div class="vocab-row selectable ${isSelected ? 'selected' : ''}" id="vocab-row-${i}" onclick="toggleVocabSelection('${id}')" style="align-items: center; transition: 0.2s;">
          <div style="display:flex; align-items:center; gap:0;">
            <div class="vocab-checkbox"></div>
            <button class="speaker-btn" aria-label="Pronounce ${escapeHtml(v.jp)}" onclick="event.stopPropagation(); pronounceWord('${escapeHtml(v.jp.replace(/'/g, "\\'"))}', this)" style="border:none;background:var(--surface2);border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;margin-right:12px;">🔊</button>
            <span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span>
            ${isFocused ? `<span class="focus-badge">✓ In Focus</span>` : ''}
          </div>
          <span class="vocab-en">${escapeHtml(v.en)}</span>
        </div>`;
      }
    )
    .join("");
}

function toggleVocabSelection(id) {
  if (lessonSelection.has(id)) lessonSelection.delete(id);
  else lessonSelection.add(id);
  let idx = id.split("-")[1];
  let row = $("vocab-row-" + idx);
  if (row) row.classList.toggle('selected', lessonSelection.has(id));
  updateFocusSelectionUI();
}

function selectAllInLesson() {
  currentLessonWords.forEach((v, i) => {
    let id = currentLessonId + "-" + i;
    lessonSelection.add(id);
    let row = $("vocab-row-" + i);
    if (row) row.classList.add('selected');
  });
  updateFocusSelectionUI();
}

function clearLessonSelection() {
  lessonSelection.clear();
  currentLessonWords.forEach((v, i) => {
    let row = $("vocab-row-" + i);
    if (row) row.classList.remove('selected');
  });
  updateFocusSelectionUI();
}

function updateFocusSelectionUI() {
  let count = lessonSelection.size;
  document.querySelectorAll('.sel-count').forEach(el => el.textContent = count);
  let mobileBar = $('mobileFocusActionBar');
  let desktopBar = $('desktopFocusAction');
  if (count > 0) {
    if (mobileBar) { mobileBar.classList.remove('hidden'); setTimeout(() => mobileBar.classList.add('visible'), 10); }
    if (desktopBar) desktopBar.classList.remove('hidden');
  } else {
    if (mobileBar) { mobileBar.classList.remove('visible'); setTimeout(() => mobileBar.classList.add('hidden'), 300); }
    if (desktopBar) desktopBar.classList.add('hidden');
  }
}

function addSelectionToFocus() {
  let added = 0;
  lessonSelection.forEach(id => {
    if (!focusWords[id]) {
      focusWords[id] = { vocabId: id, lesson: +id.split("-")[0], addedAt: Date.now() };
      added++;
    }
  });
  if (added > 0) saveFocusWords();
  clearLessonSelection();
  renderLessonVocabRows();
}

function renderFocusView() {
  let keys = Object.keys(focusWords);
  $("focusStats").textContent = keys.length;
  if (keys.length === 0) {
    $("focusListContainer").innerHTML = `
      <div class="quiz-card" style="min-height: auto; padding: 30px;">
        <div style="font-size: 24px; font-weight: 800; font-family: 'Noto Sans JP'; color: var(--muted);">まだありません</div>
        <p style="color: var(--muted);">No Focus Words yet. Select words you keep forgetting from any lesson and add them here.</p>
        <button class="secondary-btn" onclick="showView('lessons')" style="margin-top: 15px;">Go to Lessons</button>
      </div>`;
    return;
  }
  
  let html = "";
  let byLesson = {};
  keys.forEach(k => {
    let l = focusWords[k].lesson;
    if (!byLesson[l]) byLesson[l] = [];
    byLesson[l].push(k);
  });
  
  let sortedLessons = Object.keys(byLesson).map(Number).sort((a,b)=>a-b);
  sortedLessons.forEach(l => {
    html += `<div class="focus-list-header">LESSON ${String(l).padStart(2, "0")}</div>`;
    html += `<div class="vocab-table">`;
    byLesson[l].forEach(id => {
      let idx = id.split("-")[1];
      let v = VOCAB[l][idx];
      if (!v) return;
      html += `<div class="vocab-row" style="align-items: center;">
        <div style="display:flex; align-items:center; gap:12px;">
          <button class="speaker-btn" aria-label="Pronounce ${escapeHtml(v.jp)}" onclick="pronounceWord('${escapeHtml(v.jp.replace(/'/g, "\\'"))}', this)" style="border:none;background:var(--surface2);border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;">🔊</button>
          <span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span>
        </div>
        <div style="display:flex; flex-direction:column; align-items:flex-end; gap:8px;">
          <span class="vocab-en">${escapeHtml(v.en)}</span>
          <button class="secondary-btn compact" style="font-size:11px; padding:4px 8px; color:var(--red);" onclick="removeFromFocus('${id}')">Remove</button>
        </div>
      </div>`;
    });
    html += `</div>`;
  });
  $("focusListContainer").innerHTML = html;
}

function removeFromFocus(id) {
  delete focusWords[id];
  saveFocusWords();
  renderFocusView();
}

function confirmClearFocus() {
  if (Object.keys(focusWords).length === 0) return;
  if (confirm("Clear all Focus Words? This will remove all manually selected practice words.")) {
    focusWords = {};
    saveFocusWords();
    renderFocusView();
  }
}

function startFocusPractice() {
  if (Object.keys(focusWords).length === 0) return;
  $("scopeMode").value = "focus";
  $("sessionSize").value = "all";
  updatePoolCount();
  startPractice();
}
function renderKaiwa() {
  $("kaiwaGrid").innerHTML = lessons
    .map((n) => {
      const k = KAIWA[n];
      if (!k) return "";
      return `<article class="kaiwa-card"><div class="kaiwa-head"><strong>Lesson ${n} · ${escapeHtml(k.title)}</strong><span class="count-pill">${k.lines.length} lines</span></div><div class="dialogue">${k.lines.map((l) => `<div class="line"><span class="speaker">${escapeHtml(l.kanji && l.kanji !== "—" ? l.kanji + " (" + l.speaker + ")" : l.speaker)}</span><span>${escapeHtml(l.text)}</span></div>`).join("")}</div></article>`;
    })
    .join("");
}
function toggleTheme() {
  const dark = document.documentElement.dataset.theme === "dark";
  document.documentElement.dataset.theme = dark ? "" : "dark";
  localStorage.setItem("mnn-theme", dark ? "" : "dark");
}
function markWrong(id) {
  let data = getWrongData();
  if (!data[id]) data[id] = { wrongCount: 0, correctStreak: 0 };
  data[id].wrongCount++;
  data[id].correctStreak = 0;
  data[id].lastIncorrect = Date.now();
  data[id].lastPracticed = Date.now();
  saveWrongData(data);
}
function markCorrect(id) {
  let data = getWrongData();
  if (data[id]) {
    data[id].correctStreak++;
    data[id].lastPracticed = Date.now();
    if (data[id].correctStreak >= 2) {
      delete data[id];
    }
    saveWrongData(data);
  }
}
function poolForReviewScope() {
  const mode = $("reviewScopeMode").value;
  let nums = [];
  if (mode === "lesson") nums = [$("reviewLessonFrom").value];
  else if (mode === "range") {
    let a = +$("reviewLessonFrom").value,
      b = +$("reviewLessonTo").value;
    if (a > b) [a, b] = [b, a];
    for (let i = a; i <= b; i++) nums.push(i);
  } else nums = lessons;
  const wrongData = getWrongData();
  return nums
    .flatMap((n) =>
      (VOCAB[n] || []).map((v, i) => ({ ...v, lesson: +n, id: `${n}-${i}` })),
    )
    .filter((v) => wrongData[v.id]);
}
function updateReviewPoolCount() {
  const mode = $("reviewScopeMode").value;
  $("reviewLessonFromWrap").classList.toggle("hidden", mode === "all");
  $("reviewLessonToWrap").classList.toggle("hidden", mode !== "range");
  $("wrongPoolCount").textContent = `${poolForReviewScope().length} words`;
}
function startReviewPractice() {
  state.pool = poolForReviewScope();
  if ($("direction").value === "en-jp") {
    state.pool = state.pool.filter(v => !ambiguousEnJpIds.has(v.id));
  }
  if (!state.pool.length) {
    alert("No wrong answers for this selection!");
    return;
  }
  const size =
    $("sessionSize").value === "all"
      ? state.pool.length
      : +$("sessionSize").value;
  state.queue = shuffle(state.pool).slice(0, size);
  state.index = 0;
  state.score = 0;
  state.history = [];
  $("quizScope").textContent = "Reviewing Wrong Answers";
  showView("quiz");
  nextQuestion();
}
function renderReview() {
  const data = getWrongData();
  const ids = Object.keys(data);
  const total = ids.length;
  $("wrongStats").innerHTML =
    `<div style="font-size: 14px; color: var(--muted); line-height: 1.4;">${total} words<br>${new Set(ids.map((id) => id.split("-")[0])).size} lessons affected</div>`;
  if (total === 0) {
    $("wrongListContainer").innerHTML =
      `<div class="quiz-card" style="min-height: auto; padding: 30px;"><div style="font-size: 24px; font-weight: 800; font-family: 'Noto Sans JP'; color: var(--muted);">まだ間違いはありません</div><p style="color: var(--muted);">No wrong answers yet. Words you answer incorrectly will appear here for review.</p><button class="secondary-btn" onclick="showView('home')" style="margin-top: 15px;">Back to Practice</button></div>`;
    $("reviewSetupPanel").style.display = "none";
    return;
  }
  $("reviewSetupPanel").style.display = "block";
  let html = "";
  for (let n of lessons) {
    const wrongInLesson = (VOCAB[n] || [])
      .map((v, i) => ({ ...v, lesson: +n, id: `${n}-${i}` }))
      .filter((v) => data[v.id]);
    if (wrongInLesson.length > 0) {
      html += `<div style="margin-bottom: 30px;"><div class="eyebrow" style="margin-bottom: 10px;">Lesson ${n}</div>`;
      html +=
        `<div class="vocab-table">` +
        wrongInLesson
          .map(
            (v) =>
              `<div class="vocab-row"><div style="display:flex; flex-direction:column; gap:4px;"><span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span><span style="font-size:11px; color:var(--red); font-weight:700;">Wrong ${data[v.id].wrongCount}×${data[v.id].correctStreak > 0 ? ` (1 correct)` : ""}</span></div><span class="vocab-en">${escapeHtml(v.en)}</span></div>`,
          )
          .join("") +
        `</div></div>`;
    }
  }
  $("wrongListContainer").innerHTML = html;
}
function escapeHtml(s) {
  return String(s).replace(
    /[&<>"']/g,
    (c) =>
      ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;",
      })[c],
  );
}
// Speech Synthesis
let currentSpeakerBtn = null;
let lessonSpeechIndex = 0;
let lessonSpeechStage = "STOPPED"; // STOPPED, JAPANESE, PAUSE_AFTER_JAPANESE, ENGLISH, PAUSE_AFTER_ENGLISH
let playbackTimeout = null;

function getJpVoice() {
  const voices = speechSynthesis.getVoices();
  return voices.find((v) => v.lang === "ja-JP" || v.lang === "ja") || null;
}
function getEnVoice() {
  const voices = speechSynthesis.getVoices();
  return (
    voices.find(
      (v) =>
        v.lang === "en-US" || v.lang === "en-GB" || v.lang.startsWith("en"),
    ) || null
  );
}
function saveSpeechRate() {
  localStorage.setItem("mnn-speech-rate", $("speechRate").value);
}
function loadSpeechRate() {
  const r = localStorage.getItem("mnn-speech-rate");
  if (r && $("speechRate")) $("speechRate").value = r;
}
function resetSpeakerBtn() {
  if (currentSpeakerBtn) {
    currentSpeakerBtn.textContent = "🔊";
    currentSpeakerBtn = null;
  }
}
function pronounceWord(text, btn) {
  if (!window.speechSynthesis) {
    alert("Japanese pronunciation is unavailable on this device.");
    return;
  }
  stopLesson(); // Safely stop teacher mode
  speechSynthesis.cancel();
  resetSpeakerBtn();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "ja-JP";
  utterance.rate = parseFloat($("speechRate").value || "1.0");
  const voice = getJpVoice();
  if (voice) utterance.voice = voice;

  if (btn) {
    currentSpeakerBtn = btn;
    btn.textContent = "🔉";
    utterance.onend = resetSpeakerBtn;
    utterance.onerror = resetSpeakerBtn;
  }
  speechSynthesis.speak(utterance);
}

function playLesson() {
  if (!window.speechSynthesis) {
    alert("Japanese pronunciation is unavailable on this device.");
    return;
  }

  if (lessonSpeechStage.startsWith("PAUSED_")) {
    if (lessonSpeechStage === "PAUSED_JAPANESE") {
      lessonSpeechStage = "JAPANESE";
    } else {
      lessonSpeechStage = "ENGLISH";
    }
    togglePlaybackUI(true);
    executeTeacherStep();
    return;
  }

  if (lessonSpeechStage !== "STOPPED") return;

  speechSynthesis.cancel();
  resetSpeakerBtn();
  clearTimeout(playbackTimeout);
  lessonSpeechIndex = 0;
  lessonSpeechStage = "JAPANESE";
  togglePlaybackUI(true);
  executeTeacherStep();
}

function executeTeacherStep() {
  if (lessonSpeechIndex >= currentLessonWords.length) {
    finishTeacherPlayback();
    return;
  }
  const word = currentLessonWords[lessonSpeechIndex];
  highlightRow(lessonSpeechIndex);

  const rateMultiplier = parseFloat($("speechRate").value || "1.0");
  const isSlow = rateMultiplier < 0.9;

  if (lessonSpeechStage === "JAPANESE") {
    const utterance = new SpeechSynthesisUtterance(word.jp);
    utterance.lang = "ja-JP";
    utterance.rate = rateMultiplier;
    const voice = getJpVoice();
    if (voice) utterance.voice = voice;

    utterance.onend = () => {
      if (lessonSpeechStage !== "JAPANESE") return;
      lessonSpeechStage = "PAUSE_AFTER_JAPANESE";
      playbackTimeout = setTimeout(() => {
        if (lessonSpeechStage !== "PAUSE_AFTER_JAPANESE") return;
        lessonSpeechStage = "ENGLISH";
        executeTeacherStep();
      }, 700);
    };
    utterance.onerror = () => {
      if (
        lessonSpeechStage.startsWith("PAUSED") ||
        lessonSpeechStage === "STOPPED"
      )
        return;
      stopLesson();
    };
    speechSynthesis.speak(utterance);
  } else if (lessonSpeechStage === "ENGLISH") {
    const englishText = word.en.replace(/\s*\/\s*/g, " or ");
    const utterance = new SpeechSynthesisUtterance(englishText);
    utterance.lang = "en-US";
    utterance.rate = isSlow ? 0.8 : 1.0;
    const voice = getEnVoice();
    if (voice) utterance.voice = voice;

    utterance.onend = () => {
      if (lessonSpeechStage !== "ENGLISH") return;
      lessonSpeechStage = "PAUSE_AFTER_ENGLISH";
      playbackTimeout = setTimeout(() => {
        if (lessonSpeechStage !== "PAUSE_AFTER_ENGLISH") return;
        lessonSpeechIndex++;
        lessonSpeechStage = "JAPANESE";
        executeTeacherStep();
      }, 1100);
    };
    utterance.onerror = () => {
      if (
        lessonSpeechStage.startsWith("PAUSED") ||
        lessonSpeechStage === "STOPPED"
      )
        return;
      stopLesson();
    };
    speechSynthesis.speak(utterance);
  }
}

function pauseLesson() {
  clearTimeout(playbackTimeout);
  if (
    lessonSpeechStage === "JAPANESE" ||
    lessonSpeechStage === "PAUSE_AFTER_JAPANESE"
  ) {
    lessonSpeechStage = "PAUSED_JAPANESE";
  } else if (
    lessonSpeechStage === "ENGLISH" ||
    lessonSpeechStage === "PAUSE_AFTER_ENGLISH"
  ) {
    lessonSpeechStage = "PAUSED_ENGLISH";
  }
  if (window.speechSynthesis) speechSynthesis.cancel();
  togglePlaybackUI(false);
}

function stopLesson() {
  clearTimeout(playbackTimeout);
  lessonSpeechStage = "STOPPED";
  lessonSpeechIndex = 0;
  if (window.speechSynthesis) speechSynthesis.cancel();
  highlightRow(-1);
  togglePlaybackUI(false);
}

function finishTeacherPlayback() {
  stopLesson();
  const msg = $("lessonCompleteMsg");
  if (msg) {
    msg.style.display = "inline";
    setTimeout(() => {
      msg.style.display = "none";
    }, 3000);
  }
}

function togglePlaybackUI(isPlaying) {
  if (isPlaying) {
    $("btnPlayLesson").classList.add("hidden");
    $("btnPauseLesson").classList.remove("hidden");
    $("btnStopLesson").classList.remove("hidden");
  } else {
    $("btnPlayLesson").classList.remove("hidden");
    $("btnPauseLesson").classList.add("hidden");
    $("btnStopLesson").classList.add("hidden");
  }
}

function highlightRow(idx) {
  document
    .querySelectorAll(".vocab-row")
    .forEach((el) => el.classList.remove("active-row"));
  if (idx >= 0) {
    const el = $("vocab-row-" + idx);
    if (el) el.classList.add("active-row");
  }
}

if (window.speechSynthesis) {
  speechSynthesis.onvoiceschanged = () => {
    getJpVoice();
    getEnVoice();
  };
}
document.addEventListener("DOMContentLoaded", loadSpeechRate);

loadData();

window.auditQuizDataset = function() {
  console.log("=== COMPLETE DATASET AUDIT ===");
  console.log(`Total vocabulary entries: ${allVocab.length}`);
  
  let lessonCounts = {};
  allVocab.forEach(v => {
    lessonCounts[v.lesson] = (lessonCounts[v.lesson] || 0) + 1;
  });
  console.log("Entries per lesson:", lessonCounts);
  
  console.log(`Ambiguous En->Jp items (excluded from EN->JP mode): ${ambiguousEnJpIds.size}`);
  
  let ambiguousList = Array.from(ambiguousEnJpIds).map(id => {
    let v = allVocab.find(x => x.id === id);
    return `L${v.lesson}: ${v.en} -> ${v.jp}`;
  });
  if (ambiguousList.length > 0) {
    console.log("Ambiguous En->Jp Details:\n" + ambiguousList.join("\n"));
  }
  
  console.log("Running distractor test on Lesson 9 Jp->En...");
  let l9 = allVocab.filter(v => v.lesson === 9);
  let overlaps = 0;
  for (let i = 0; i < l9.length; i++) {
    for (let j = i+1; j < l9.length; j++) {
       if (!isDistractorValid(l9[i], l9[j])) {
          console.log(`Semantic overlap found: ${l9[i].jp} (${l9[i].en}) <==> ${l9[j].jp} (${l9[j].en})`);
          overlaps++;
       }
    }
  }
  console.log(`Lesson 9 overlaps (these will never appear together now): ${overlaps}`);
  
  return "Audit complete. Check console.";
};


function updateStreakAndDashboard() {
  const today = new Date().toDateString();
  let lastActive = localStorage.getItem('minna_last_active');
  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  
  // Dashboard updates
  const elStreak = document.getElementById('streakDays');
  if (elStreak) elStreak.textContent = currentStreak;
  
  // Calculate N5 Progress
  const total = allVocab.length;
  let learnedCount = Object.keys(getWrongData()).length; // rough estimate based on wrong/correct history
  // Since we don't have a real 'learned' array, let's just use total focus words and wrong words + some constant for now
  // Actually, we can just say progress is based on how many words we have answered at least once
  let n5Percent = total > 0 ? Math.round((learnedCount / total) * 100) : 0;
  if(n5Percent > 100) n5Percent = 100;
  
  const elProgress = document.getElementById('n5ProgressBar');
  const elProgressText = document.getElementById('n5ProgressText');
  if (elProgress) elProgress.style.width = n5Percent + '%';
  if (elProgressText) elProgressText.textContent = n5Percent;
  
  // Update Vocab / Kaiwa progress bars
  const elVocab = document.getElementById('vocabProgress');
  if(elVocab) elVocab.textContent = Math.round(n5Percent) + '%';
  const elKaiwa = document.getElementById('kaiwaProgress');
  if(elKaiwa) elKaiwa.textContent = '100%';
}

function recordActivity() {
  const today = new Date().toDateString();
  let lastActive = localStorage.getItem('minna_last_active');
  let currentStreak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  
  if (lastActive !== today) {
    let yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    if (lastActive === yesterday.toDateString()) {
      currentStreak++;
    } else {
      currentStreak = 1;
    }
    localStorage.setItem('minna_last_active', today);
    localStorage.setItem('minna_streak', currentStreak);
    updateStreakAndDashboard();
  }
}


function startMockTest() {
  // Set scope to All, mixed direction, 50 questions
  document.getElementById("scopeMode").value = "all";
  document.getElementById("direction").value = "mixed";
  document.getElementById("sessionSize").value = "50";
  
  // Update state and pool
  updateScopeUI(); 
  
  // Wait for pool to update then start
  setTimeout(() => {
    if(state.pool.length > 0) {
      document.getElementById('startBtn').click();
    } else {
      alert("No questions available for Mock Test yet.");
    }
  }, 100);
}


function updateDashboardStats() {
  let streak = parseInt(localStorage.getItem('minna_streak') || '0', 10);
  let streakText = document.getElementById('streakText');
  if (streakText) streakText.innerHTML = '🔥 You\'re on a ' + streak + ' day streak';
  
  // Calculate vocab stats
  let totalVocab = allVocab.length || 800; // fallback if not loaded
  
  // We don't have grammar/listening/kanji data yet, so we just show 0
  let statVocab = document.getElementById('statVocab');
  if (statVocab) statVocab.innerText = '0/' + totalVocab;
  
  let statGrammar = document.getElementById('statGrammar');
  if (statGrammar) statGrammar.innerText = '0/0';
  
  let statListening = document.getElementById('statListening');
  if (statListening) statListening.innerText = '0/0';
  
  let statKanji = document.getElementById('statKanji');
  if (statKanji) statKanji.innerText = '0/0';
  
  let n5Percent = document.getElementById('n5Percent');
  let n5Topics = document.getElementById('n5Topics');
  let n5ProgressBar = document.getElementById('n5ProgressBar');
  if (n5Percent) n5Percent.innerText = '0%';
  if (n5Topics) n5Topics.innerHTML = '0/' + totalVocab + '<br>Words';
  if (n5ProgressBar) n5ProgressBar.style.width = '0%';
}
