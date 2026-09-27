let VOCAB={}, KAIWA={};
let state={view:"home",pool:[],queue:[],index:0,score:0,current:null,history:[]};
const $=id=>document.getElementById(id);
const lessons=Array.from({length:25},(_,i)=>i+1);
const lessonNames={
1:"Introductions",2:"Objects & ownership",3:"Places & shopping",4:"Time & schedules",5:"Travel & dates",
6:"Food & activities",7:"Giving & receiving",8:"Adjectives & life",9:"Likes & abilities",10:"Places & positions",
11:"Counters & quantities",12:"Seasons & comparison",13:"Plans & wants",14:"Requests & directions",15:"Permission & family",
16:"Daily routines",17:"Health & problems",18:"Skills & hobbies",19:"Experiences",20:"Plain-style speech",
21:"Opinions & events",22:"Clothing & apartments",23:"Directions & crossing",24:"Showing around & helping",25:"Conditions & moving"
};
async function loadData(){
  [VOCAB,KAIWA]=await Promise.all([
    fetch("vocab.json").then(r=>r.json()),
    fetch("kaiwa.json").then(r=>r.json())
  ]);
  init();
}
function getWrongData() { return JSON.parse(localStorage.getItem("mnn-wrong-v2")) || {}; }
function saveWrongData(data) { localStorage.setItem("mnn-wrong-v2", JSON.stringify(data)); }
function clearWrongData() { if(confirm("Clear all saved wrong answers?")){ localStorage.removeItem("mnn-wrong-v2"); renderReview(); updateReviewPoolCount(); } }

function init(){
  const opts=lessons.map(n=>`<option value="${n}">Lesson ${n}</option>`).join("");
  $("lessonFrom").innerHTML=opts;$("lessonTo").innerHTML=opts;
  $("lessonFrom").value=1;$("lessonTo").value=5;
  $("reviewLessonFrom").innerHTML=opts;$("reviewLessonTo").innerHTML=opts;
  $("reviewLessonFrom").value=1;$("reviewLessonTo").value=5;
  
  document.querySelectorAll(".nav-btn").forEach(b=>b.onclick=()=>showView(b.dataset.view));
  ["scopeMode","lessonFrom","lessonTo"].forEach(id=>$(id).addEventListener("change",updatePoolCount));
  ["reviewScopeMode","reviewLessonFrom","reviewLessonTo"].forEach(id=>$(id).addEventListener("change",updateReviewPoolCount));
  
  $("startBtn").onclick=startPractice;
  $("startReviewBtn").onclick=startReviewPractice;
  $("clearWrongBtn").onclick=clearWrongData;
  $("nextBtn").onclick=grade;
  $("themeBtn").onclick=toggleTheme;
  renderLessons();renderKaiwa();updatePoolCount();updateReviewPoolCount();
  const saved=localStorage.getItem("mnn-theme"); if(saved)document.documentElement.dataset.theme=saved;
}
function reviewWrongAnswers() {
  showView("review");
}
function showView(view){
  const map={home:"homeView",quiz:"quizView",lessons:"lessonsView",lessonDetail:"lessonDetailView",kaiwa:"kaiwaView",review:"reviewView",resultsView:"resultsView"};
  Object.values(map).forEach(id=>$(id).classList.remove("active"));
  $(map[view]).classList.add("active"); state.view=view;
  document.querySelectorAll(".nav-btn").forEach(b=>b.classList.toggle("active",b.dataset.view===view));
  if(view==="review") renderReview();
  window.scrollTo({top:0,behavior:"smooth"});
}
function poolForScope(){
  const mode=$("scopeMode").value;
  let nums=[];
  if(mode==="lesson")nums=[$("lessonFrom").value];
  else if(mode==="range"){let a=+$("lessonFrom").value,b=+$("lessonTo").value;if(a>b)[a,b]=[b,a];for(let i=a;i<=b;i++)nums.push(i)}
  else nums=lessons;
  return nums.flatMap(n=>(VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`})));
}
function updatePoolCount(){
  const mode=$("scopeMode").value;
  $("lessonFromWrap").classList.toggle("hidden",mode==="all");
  $("lessonToWrap").classList.toggle("hidden",mode!=="range");
  $("poolCount").textContent=`${poolForScope().length} words`;
}
function shuffle(a){return [...a].sort(()=>Math.random()-.5)}
function startPractice(){
  state.pool=poolForScope();
  if(!state.pool.length)return;
  const size=$("sessionSize").value==="all"?state.pool.length:+$("sessionSize").value;
  state.queue=shuffle(state.pool).slice(0,size);state.index=0;state.score=0;state.history=[];
  $("quizScope").textContent=scopeLabel();
  showView("quiz");nextQuestion();
}
function scopeLabel(){
  const mode=$("scopeMode").value;
  if(mode==="lesson")return`Lesson ${$("lessonFrom").value}`;
  if(mode==="range")return`Lessons ${Math.min($("lessonFrom").value,$("lessonTo").value)}–${Math.max($("lessonFrom").value,$("lessonTo").value)}`;
  return"Lessons 1–25";
}
function nextQuestion(){
  if(state.index>=state.queue.length){finishQuiz();return}
  state.current=state.queue[state.index];
  const dir=$("direction").value==="mixed"?(Math.random()<.5?"jp-en":"en-jp"):$("direction").value;
  state.current.dir=dir;
  const isJpEn = dir==="jp-en";
  $("question").textContent=isJpEn?(state.current.kanji && state.current.kanji !== "—" ? state.current.kanji + " (" + state.current.jp + ")" : state.current.jp):state.current.en;
  
  let options = [state.current];
  let distractorPool = state.pool.filter(v => v.id !== state.current.id && v.lesson === state.current.lesson);
  if (distractorPool.length < 3) {
      const extra = state.pool.filter(v => v.id !== state.current.id && !distractorPool.includes(v));
      distractorPool.push(...extra);
  }
  if (distractorPool.length < 3) {
      const allVocab = lessons.flatMap(n=>(VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`})));
      const extra = allVocab.filter(v => v.id !== state.current.id && !distractorPool.includes(v));
      distractorPool.push(...extra);
  }
  options.push(...shuffle(distractorPool).slice(0, 3));
  options = shuffle(options);
  state.currentOptions = options;
  state.answered = false;
  
  $("mcqGrid").innerHTML = options.map((opt, i) => {
    let text = isJpEn ? opt.en : (opt.kanji && opt.kanji !== "—" ? opt.kanji + " (" + opt.jp + ")" : opt.jp);
    return `<button class="mcq-option" id="opt${i}" onclick="selectOption(${i})">${escapeHtml(text)}</button>`;
  }).join("");
  
  $("mcqGrid").classList.remove("hidden");
  $("nextAction").classList.add("hidden");
  
  $("lessonTag").textContent=`Lesson ${state.current.lesson} · ${lessonNames[state.current.lesson]}`;
  $("quizDirection").textContent=isJpEn?"Japanese → English":"English → Japanese";
  $("quizProgress").textContent=`${state.index+1} / ${state.queue.length}`;
  $("progressBar").style.width=`${(state.index/state.queue.length)*100}%`;
}
function selectOption(idx) {
  if (state.answered) return;
  state.answered = true;
  const selected = state.currentOptions[idx];
  state.lastSelectedObj = selected;
  const isCorrect = selected.id === state.current.id;
  state.lastCorrect = isCorrect;
  state.currentOptions.forEach((opt, i) => {
    const btn = $("opt"+i);
    btn.disabled = true;
    if (opt.id === state.current.id) btn.classList.add("correct");
    else if (i === idx && !isCorrect) btn.classList.add("incorrect");
  });
  $("nextAction").classList.remove("hidden");
}
function grade(){
  if (state.lastCorrect) {
    state.score++;
    markCorrect(state.current.id);
  } else {
    markWrong(state.current.id);
  }
  const isJpEn = state.current.dir === "jp-en";
  const qJp = state.current.kanji && state.current.kanji !== "—" ? state.current.kanji + " (" + state.current.jp + ")" : state.current.jp;
  const qEn = state.current.en;
  
  const selJp = state.lastSelectedObj ? (state.lastSelectedObj.kanji && state.lastSelectedObj.kanji !== "—" ? state.lastSelectedObj.kanji + " (" + state.lastSelectedObj.jp + ")" : state.lastSelectedObj.jp) : "";
  const selEn = state.lastSelectedObj ? state.lastSelectedObj.en : "";

  state.history.push({
    id: state.current.id,
    lesson: state.current.lesson,
    dir: state.current.dir,
    questionText: isJpEn ? qJp : qEn,
    selectedAnswer: state.lastSelectedObj ? (isJpEn ? selEn : selJp) : "Timeout",
    correctAnswer: isJpEn ? qEn : qJp,
    known: state.lastCorrect
  });
  
  state.index++;
  nextQuestion();
}
function finishQuiz(){
  $("progressBar").style.width="100%";
  $("quizProgress").textContent="Done";
  showView("resultsView");
  const wrongList = state.history.filter(h => !h.known);
  const wrongCount = wrongList.length;
  const acc = Math.round((state.score / state.queue.length) * 100);
  
  let html = `
    <div class="results-desktop-split">
      <div style="background:var(--surface); border:1px solid var(--line); border-radius:22px; padding:30px; text-align:center; box-shadow:var(--shadow);">
        <div class="big-number">${state.score} / ${state.queue.length}</div>
        <div style="font-size: 24px; font-weight: 800; color: var(--muted); margin-bottom: 20px;">${acc}%</div>
        <div style="display:flex; justify-content:center; gap:20px; font-weight:700; font-size:14px;">
          <span style="color: #137333;">✓ Correct &nbsp; ${state.score}</span>
          <span style="color: var(--red);">✕ Wrong &nbsp; ${wrongCount}</span>
        </div>
      </div>
  `;
  
  if (wrongCount === 0) {
    html += `
      <div style="flex:1; display:flex; align-items:center; justify-content:center;">
        <div style="color: #137333; font-weight: 800; font-size:18px; text-align:center;">Perfect!<br><span style="font-size:14px; color: var(--muted);">All questions correct.</span></div>
      </div>
    </div>`;
    $("btnReviewWrong").style.display = "none";
  } else {
    html += `
      <div>
        <div class="eyebrow" style="margin-bottom: 15px; text-align:center;">WHAT YOU GOT WRONG</div>
        <div style="display:flex; flex-direction:column; gap:12px;">
    `;
    wrongList.forEach(w => {
      html += `
        <div style="background:var(--surface2); border-radius:12px; padding:16px; border:1px solid var(--line); text-align:left;">
          <div style="font-size:18px; font-weight:800; font-family:'Noto Sans JP'; margin-bottom:8px;">${escapeHtml(w.questionText)}</div>
          <div style="font-size:13px; color:var(--red); font-weight:600; margin-bottom:4px;">Your: ${escapeHtml(w.selectedAnswer)}</div>
          <div style="font-size:13px; color:#137333; font-weight:600; margin-bottom:8px;">Correct: ${escapeHtml(w.correctAnswer)}</div>
          <div class="lesson-tag" style="display:inline-block; padding: 4px 8px; font-size:10px;">Lesson ${w.lesson}</div>
        </div>
      `;
    });
    html += `</div></div></div>`;
    $("btnReviewWrong").style.display = "block";
  }
  
  $("resultsSummary").innerHTML = html;
}
function quickStart(n){
  $("scopeMode").value="lesson";$("lessonFrom").value=n;updatePoolCount();startPractice();
}
function renderLessons(){
  const total=lessons.reduce((a,n)=>a+(VOCAB[n]?.length||0),0);$("totalVocab").textContent=`${total} entries`;
  $("lessonGrid").innerHTML=lessons.map(n=>`
    <button class="lesson-card" onclick="openLesson(${n})">
      <span class="lesson-no">LESSON ${String(n).padStart(2,"0")}</span>
      <h3>${lessonNames[n]}</h3><p>${VOCAB[n].length} vocabulary entries</p>
    </button>`).join("");
}
let currentLessonWords = [];
function openLesson(n){
  currentLessonWords = VOCAB[n] || [];
  $("detailHeader").innerHTML=`<div class="eyebrow">LESSON ${String(n).padStart(2,"0")}</div><h1>${lessonNames[n]}</h1><p>${VOCAB[n].length} vocabulary entries • separate from Kaiwa.</p>`;
  $("vocabTable").innerHTML=VOCAB[n].map((v, i)=>`<div class="vocab-row" id="vocab-row-${i}" style="align-items: center; transition: 0.2s;"><div style="display:flex; align-items:center; gap:12px;"><button class="speaker-btn" aria-label="Pronounce ${escapeHtml(v.jp)}" onclick="pronounceWord('${escapeHtml(v.jp.replace(/'/g, "\\'"))}', this)" style="border:none;background:var(--surface2);border-radius:50%;width:40px;height:40px;display:flex;align-items:center;justify-content:center;cursor:pointer;flex-shrink:0;">🔊</button><span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span></div><span class="vocab-en">${escapeHtml(v.en)}</span></div>`).join("");
  $("detailPractice").onclick=()=>{ $("scopeMode").value="lesson";$("lessonFrom").value=n;updatePoolCount();startPractice(); };
  showView("lessonDetail");
}
function renderKaiwa(){
  $("kaiwaGrid").innerHTML=lessons.map(n=>{
    const k=KAIWA[n]; if(!k)return"";
    return `<article class="kaiwa-card"><div class="kaiwa-head"><strong>Lesson ${n} · ${escapeHtml(k.title)}</strong><span class="count-pill">${k.lines.length} lines</span></div><div class="dialogue">${k.lines.map(l=>`<div class="line"><span class="speaker">${escapeHtml(l.kanji && l.kanji !== "—" ? l.kanji + " (" + l.speaker + ")" : l.speaker)}</span><span>${escapeHtml(l.text)}</span></div>`).join("")}</div></article>`
  }).join("");
}
function toggleTheme(){
  const dark=document.documentElement.dataset.theme==="dark";
  document.documentElement.dataset.theme=dark?"":"dark";
  localStorage.setItem("mnn-theme",dark?"":"dark");
}
function markWrong(id) {
  let data = getWrongData();
  if(!data[id]) data[id] = { wrongCount: 0, correctStreak: 0 };
  data[id].wrongCount++;
  data[id].correctStreak = 0;
  data[id].lastIncorrect = Date.now();
  data[id].lastPracticed = Date.now();
  saveWrongData(data);
}
function markCorrect(id) {
  let data = getWrongData();
  if(data[id]) {
    data[id].correctStreak++;
    data[id].lastPracticed = Date.now();
    if(data[id].correctStreak >= 2) {
      delete data[id];
    }
    saveWrongData(data);
  }
}
function poolForReviewScope(){
  const mode=$("reviewScopeMode").value;
  let nums=[];
  if(mode==="lesson")nums=[$("reviewLessonFrom").value];
  else if(mode==="range"){let a=+$("reviewLessonFrom").value,b=+$("reviewLessonTo").value;if(a>b)[a,b]=[b,a];for(let i=a;i<=b;i++)nums.push(i)}
  else nums=lessons;
  const wrongData = getWrongData();
  return nums.flatMap(n=>(VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`}))).filter(v => wrongData[v.id]);
}
function updateReviewPoolCount(){
  const mode=$("reviewScopeMode").value;
  $("reviewLessonFromWrap").classList.toggle("hidden",mode==="all");
  $("reviewLessonToWrap").classList.toggle("hidden",mode!=="range");
  $("wrongPoolCount").textContent=`${poolForReviewScope().length} words`;
}
function startReviewPractice(){
  state.pool=poolForReviewScope();
  if(!state.pool.length){ alert("No wrong answers for this selection!"); return; }
  const size=$("sessionSize").value==="all"?state.pool.length:+$("sessionSize").value;
  state.queue=shuffle(state.pool).slice(0,size);state.index=0;state.score=0;state.history=[];
  $("quizScope").textContent="Reviewing Wrong Answers";
  showView("quiz");nextQuestion();
}
function renderReview(){
  const data = getWrongData();
  const ids = Object.keys(data);
  const total = ids.length;
  $("wrongStats").innerHTML = `<div style="font-size: 14px; color: var(--muted); line-height: 1.4;">${total} words<br>${new Set(ids.map(id => id.split('-')[0])).size} lessons affected</div>`;
  if(total === 0) {
    $("wrongListContainer").innerHTML = `<div class="quiz-card" style="min-height: auto; padding: 30px;"><div style="font-size: 24px; font-weight: 800; font-family: 'Noto Sans JP'; color: var(--muted);">まだ間違いはありません</div><p style="color: var(--muted);">No wrong answers yet. Words you answer incorrectly will appear here for review.</p><button class="secondary-btn" onclick="showView('home')" style="margin-top: 15px;">Back to Practice</button></div>`;
    $("reviewSetupPanel").style.display = "none";
    return;
  }
  $("reviewSetupPanel").style.display = "block";
  let html = "";
  for(let n of lessons) {
    const wrongInLesson = (VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`})).filter(v => data[v.id]);
    if(wrongInLesson.length > 0) {
      html += `<div style="margin-bottom: 30px;"><div class="eyebrow" style="margin-bottom: 10px;">Lesson ${n}</div>`;
      html += `<div class="vocab-table">` + wrongInLesson.map(v => `<div class="vocab-row"><div style="display:flex; flex-direction:column; gap:4px;"><span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span><span style="font-size:11px; color:var(--red); font-weight:700;">Wrong ${data[v.id].wrongCount}×${data[v.id].correctStreak > 0 ? ` (1 correct)`: ''}</span></div><span class="vocab-en">${escapeHtml(v.en)}</span></div>`).join("") + `</div></div>`;
    }
  }
  $("wrongListContainer").innerHTML = html;
}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]))}
// Speech Synthesis
let currentSpeakerBtn = null;
let lessonSpeechIndex = 0;
let lessonSpeechStage = "STOPPED"; // STOPPED, JAPANESE, PAUSE_AFTER_JAPANESE, ENGLISH, PAUSE_AFTER_ENGLISH
let playbackTimeout = null;

function getJpVoice() {
  const voices = speechSynthesis.getVoices();
  return voices.find(v => v.lang === "ja-JP" || v.lang === "ja") || null;
}
function getEnVoice() {
  const voices = speechSynthesis.getVoices();
  return voices.find(v => v.lang === "en-US" || v.lang === "en-GB" || v.lang.startsWith("en")) || null;
}
function saveSpeechRate() {
  localStorage.setItem("mnn-speech-rate", $("speechRate").value);
}
function loadSpeechRate() {
  const r = localStorage.getItem("mnn-speech-rate");
  if(r && $("speechRate")) $("speechRate").value = r;
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
      if (lessonSpeechStage.startsWith("PAUSED") || lessonSpeechStage === "STOPPED") return;
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
      if (lessonSpeechStage.startsWith("PAUSED") || lessonSpeechStage === "STOPPED") return;
      stopLesson();
    };
    speechSynthesis.speak(utterance);
  }
}

function pauseLesson() {
  clearTimeout(playbackTimeout);
  if (lessonSpeechStage === "JAPANESE" || lessonSpeechStage === "PAUSE_AFTER_JAPANESE") {
    lessonSpeechStage = "PAUSED_JAPANESE";
  } else if (lessonSpeechStage === "ENGLISH" || lessonSpeechStage === "PAUSE_AFTER_ENGLISH") {
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
    setTimeout(() => { msg.style.display = "none"; }, 3000);
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
  document.querySelectorAll(".vocab-row").forEach(el => el.classList.remove("active-row"));
  if (idx >= 0) {
    const el = $("vocab-row-" + idx);
    if (el) el.classList.add("active-row");
  }
}

if (window.speechSynthesis) {
  speechSynthesis.onvoiceschanged = () => { getJpVoice(); getEnVoice(); };
}
document.addEventListener("DOMContentLoaded", loadSpeechRate);

loadData();
