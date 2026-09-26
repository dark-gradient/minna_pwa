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
  $("revealBtn").onclick=reveal;
  $("knownBtn").onclick=()=>grade(true);
  $("againBtn").onclick=()=>grade(false);
  $("themeBtn").onclick=toggleTheme;
  renderLessons();renderKaiwa();updatePoolCount();
  const saved=localStorage.getItem("mnn-theme"); if(saved)document.documentElement.dataset.theme=saved;
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
  $("question").textContent=dir==="jp-en"?(state.current.kanji && state.current.kanji !== "—" ? state.current.kanji + " (" + state.current.jp + ")" : state.current.jp):state.current.en;
  $("answer").textContent=dir==="jp-en"?state.current.en:(state.current.kanji && state.current.kanji !== "—" ? state.current.kanji + " (" + state.current.jp + ")" : state.current.jp);
  $("answer").classList.add("hidden");$("revealBtn").classList.remove("hidden");
  $("knownBtn").classList.add("hidden");$("againBtn").classList.add("hidden");
  $("lessonTag").textContent=`Lesson ${state.current.lesson} · ${lessonNames[state.current.lesson]}`;
  $("quizDirection").textContent=dir==="jp-en"?"Japanese → English":"English → Japanese";
  $("quizProgress").textContent=`${state.index+1} / ${state.queue.length}`;
  $("progressBar").style.width=`${(state.index/state.queue.length)*100}%`;
}
function reveal(){$("answer").classList.remove("hidden");$("revealBtn").classList.add("hidden");$("knownBtn").classList.remove("hidden");$("againBtn").classList.remove("hidden")}
function grade(known){if(known)state.score++;state.history.push({id:state.current.id,known});state.index++;nextQuestion()}
function finishQuiz(){
  $("progressBar").style.width="100%";
  $("quizDirection").textContent="Practice complete";
  $("question").textContent=`${state.score} / ${state.queue.length}`;
  $("answer").classList.remove("hidden");$("answer").textContent="もう一度？ Keep going?";
  $("revealBtn").classList.add("hidden");$("knownBtn").classList.add("hidden");$("againBtn").classList.add("hidden");
  $("lessonTag").textContent=state.score===state.queue.length?"完璧！ Perfect session.":"いい練習でした。 Nice practice.";
  $("quizProgress").textContent="Done";
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
