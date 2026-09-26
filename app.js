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
function init(){
  const opts=lessons.map(n=>`<option value="${n}">Lesson ${n}</option>`).join("");
  $("lessonFrom").innerHTML=opts;$("lessonTo").innerHTML=opts;
  $("lessonFrom").value=1;$("lessonTo").value=5;
  document.querySelectorAll(".nav-btn").forEach(b=>b.onclick=()=>showView(b.dataset.view));
  ["scopeMode","lessonFrom","lessonTo"].forEach(id=>$(id).addEventListener("change",updatePoolCount));
  $("startBtn").onclick=startPractice;
  $("nextBtn").onclick=grade;
  $("themeBtn").onclick=toggleTheme;
  renderLessons();renderKaiwa();updatePoolCount();
  const saved=localStorage.getItem("mnn-theme"); if(saved)document.documentElement.dataset.theme=saved;
}
function reviewWrongAnswers() {
  const wrongIds = JSON.parse(localStorage.getItem("mnn-wrong")) || [];
  if (!wrongIds.length) { alert("No wrong answers to review!"); return; }
  state.pool = lessons.flatMap(n=>(VOCAB[n]||[]).map((v,i)=>({...v,lesson:+n,id:`${n}-${i}`}))).filter(v => wrongIds.includes(v.id));
  state.queue=shuffle(state.pool);state.index=0;state.score=0;state.history=[];
  $("quizScope").textContent="Reviewing Wrong Answers";
  showView("quiz");nextQuestion();
}
function showView(view){
  const map={home:"homeView",quiz:"quizView",lessons:"lessonsView",lessonDetail:"lessonDetailView",kaiwa:"kaiwaView"};
  Object.values(map).forEach(id=>$(id).classList.remove("active"));
  $(map[view]).classList.add("active"); state.view=view;
  document.querySelectorAll(".nav-btn").forEach(b=>b.classList.toggle("active",b.dataset.view===view));
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
  const isCorrect = selected.id === state.current.id;
  state.lastCorrect = isCorrect;
  if(!isCorrect) {
    let wrongAnswers = JSON.parse(localStorage.getItem("mnn-wrong")) || [];
    if (!wrongAnswers.includes(state.current.id)) {
      wrongAnswers.push(state.current.id);
      localStorage.setItem("mnn-wrong", JSON.stringify(wrongAnswers));
    }
  }
  state.currentOptions.forEach((opt, i) => {
    const btn = $("opt"+i);
    btn.disabled = true;
    if (opt.id === state.current.id) btn.classList.add("correct");
    else if (i === idx && !isCorrect) btn.classList.add("incorrect");
  });
  $("nextAction").classList.remove("hidden");
}
function grade(){
  if(state.lastCorrect) state.score++;
  state.history.push({id:state.current.id,known:state.lastCorrect});
  state.index++;
  nextQuestion();
}
function finishQuiz(){
  $("progressBar").style.width="100%";
  $("quizProgress").textContent="Done";
  showView("resultsView");
  const wrongCount = state.history.filter(h => !h.known).length;
  const acc = Math.round((state.score / state.queue.length) * 100);
  $("resultsSummary").innerHTML = `
    <div class="big-number">${state.score} / ${state.queue.length}</div>
    <p>Accuracy: ${acc}%</p>
    <p>Correct: ${state.score} | Incorrect: ${wrongCount}</p>
    <p>${wrongCount} questions added to Wrong Answers.</p>
  `;
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
function openLesson(n){
  $("detailHeader").innerHTML=`<div class="eyebrow">LESSON ${String(n).padStart(2,"0")}</div><h1>${lessonNames[n]}</h1><p>${VOCAB[n].length} vocabulary entries • separate from Kaiwa.</p>`;
  $("vocabTable").innerHTML=VOCAB[n].map(v=>`<div class="vocab-row"><span class="vocab-jp">${escapeHtml(v.kanji && v.kanji !== "—" ? v.kanji + " (" + v.jp + ")" : v.jp)}</span><span class="vocab-en">${escapeHtml(v.en)}</span></div>`).join("");
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
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]))}
loadData();
