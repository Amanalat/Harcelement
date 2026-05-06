var G=TEXTES.G, CRISIS=TEXTES.CRISIS, REVELATIONS=TEXTES.REVELATIONS;

var trust=0,good=0,step=0,crisisUsed=false,phase='story',busy=false,tyEl=null;
var ma=document.getElementById('ma'),ca=document.getElementById('ca');
var tf=document.getElementById('tf'),tlb=document.getElementById('tlb'),tdl=document.getElementById('tdl');

// Initialise les éléments statiques de l'en-tête depuis TEXTES
document.getElementById('av').textContent=TEXTES.contact.avatar;
document.getElementById('cn').textContent=TEXTES.contact.name;
document.getElementById('st').textContent=TEXTES.contact.statusOnline;

function sl(ms){return new Promise(function(r){setTimeout(r,ms);});}

function addBub(txt,type){
  var d=document.createElement('div');
  d.className='bb '+type;
  d.innerHTML=txt.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\n/g,'<br>');
  ma.appendChild(d);
  ma.scrollTop=ma.scrollHeight;
}
function showTy(){
  tyEl=document.createElement('div');
  tyEl.className='tyi';
  tyEl.innerHTML='<span></span><span></span><span></span>';
  ma.appendChild(tyEl);
  ma.scrollTop=ma.scrollHeight;
  document.getElementById('st').textContent=TEXTES.contact.statusTyping;
}
function hideTy(){
  if(tyEl){tyEl.remove();tyEl=null;}
  document.getElementById('st').textContent=TEXTES.contact.statusOnline;
}
function updateBar(prev){
  var pct=Math.max(5,Math.min(95,(trust+4)/8*100));
  tf.style.width=pct+'%';
  tf.style.background=trust>=2?'#30d158':trust>=0?'#ff9f0a':'#ff453a';
  tlb.textContent=TEXTES.trustLabels[Math.max(0,Math.min(8,trust+4))];
  tlb.style.color=trust>=2?'#30d158':trust>=0?'#ff9f0a':'#ff453a';
  var d=trust-prev;
  if(d!==0){
    tdl.textContent=(d>0?'+':'')+d;
    tdl.style.color=d>0?'#30d158':'#ff453a';
    tdl.style.opacity='1';
    clearTimeout(tdl._t);
    tdl._t=setTimeout(function(){tdl.style.opacity='0';},1600);
  }
}
function showChoices(arr,isCr){
  ca.innerHTML='<div class="chint'+(isCr?' cr':'')+'">'+
    (isCr?TEXTES.choiceHintCrise:TEXTES.choiceHint)+'</div>';
  arr.forEach(function(c){
    var b=document.createElement('button');
    b.className='cb'+(isCr?' cr-btn':'');
    b.innerHTML='<span class="cl">'+c.l+'</span><span>'+c.t+'</span>';
    b.addEventListener('click', function(){pick(c);});
    ca.appendChild(b);
  });
}

async function showNextStep(){
  await sl(430);
  var ns=G[step];
  if(ns.intro){
    showTy();
    var delay=ns.intro.length>2?900:1100;
    await sl(delay);hideTy();
    for(var i=0;i<ns.intro.length;i++){
      if(i>0){
        await sl(ns.intro[i-1].startsWith('(')?400:700);
        if(i<ns.intro.length-1){showTy();await sl(800);hideTy();}
      }
      addBub(ns.intro[i],ns.intro[i].startsWith('(')? 'sy':'r');
    }
    await sl(350);
  }
  if(ns.edu){
    await sl(500);
    addBub(ns.edu,'ed');
    await sl(700);
  }
  showChoices(ns.c,false);
  busy=false;
}

async function pick(choice){
  if(busy)return;
  busy=true;
  ca.querySelectorAll('button').forEach(function(b){b.disabled=true;});
  addBub(choice.t,'s');

  if(choice.end==='imm'){
    ca.innerHTML='';
    await sl(600);showTy();await sl(900);hideTy();
    addBub(TEXTES.finImmediate[0].t,TEXTES.finImmediate[0].type);
    await sl(350);addBub(TEXTES.finImmediate[1].t,TEXTES.finImmediate[1].type);
    endGame('imm');return;
  }

  var prev=trust;
  if(phase==='story'&&choice.e>0)good++;
  trust+=choice.e;
  updateBar(prev);
  ca.innerHTML='';

  if(trust<=-3){
    await sl(500);showTy();await sl(1200);hideTy();
    addBub(TEXTES.blocageMessages[0].t,TEXTES.blocageMessages[0].type);
    await sl(350);addBub(TEXTES.blocageMessages[1].t,TEXTES.blocageMessages[1].type);
    await sl(300);addBub(TEXTES.blocageMessages[2].t,TEXTES.blocageMessages[2].type);
    endGame('block');return;
  }

  if(phase==='crisis'){
    phase='story';
    step++;
    if(step>=G.length){await sl(400);showTy();await sl(1400);hideTy();endGame('final');return;}
    await showNextStep();return;
  }

  if(trust<=-2&&!crisisUsed&&step<G.length-1){
    crisisUsed=true;phase='crisis';
    await sl(600);showTy();await sl(1400);hideTy();
    for(var i=0;i<CRISIS.intro.length;i++){
      addBub(CRISIS.intro[i],'cr');
      await sl(i<CRISIS.intro.length-1?700:300);
    }
    showChoices(CRISIS.c,true);
    busy=false;return;
  }

  step++;
  if(step>=G.length){await sl(400);showTy();await sl(1400);hideTy();endGame('final');return;}
  await showNextStep();
}

function buildIgCard(ig){
  var esc=function(s){return s.replace(/\\/g,'\\\\').replace(/'/g,"\\'");};
  return '<div class="igcard">'+ig.label+'<br>'
    +'<span style="color:#888;font-size:10.5px;">'+ig.compteLabel+'</span> <span class="igusr">'+ig.compte+'</span>'
    +' <button class="cpbtn" onclick="doCopy(this,\''+esc(ig.compte)+'\')">📋</button><br>'
    +'<span style="color:#888;font-size:10.5px;">'+ig.mdpLabel+'</span> <span class="igpwd">'+ig.mdp+'</span>'
    +' <button class="cpbtn" onclick="doCopy(this,\''+esc(ig.mdp)+'\')">📋</button>'
    +'<div class="igwarn">'+ig.warn+'</div></div>';
}

function doCopy(btn,text){
  var done=function(){
    var orig=btn.textContent;
    btn.textContent='✓';btn.classList.add('ok');
    setTimeout(function(){btn.textContent=orig;btn.classList.remove('ok');},1800);
  };
  if(navigator.clipboard){
    navigator.clipboard.writeText(text).then(done).catch(function(){fallbackCopy(text);done();});
  }else{fallbackCopy(text);done();}
}
function fallbackCopy(text){
  var ta=document.createElement('textarea');
  ta.value=text;ta.style.cssText='position:fixed;opacity:0;top:0;left:0;';
  document.body.appendChild(ta);ta.select();
  try{document.execCommand('copy');}catch(e){}
  document.body.removeChild(ta);
}

function buildRevCards(){
  var h='<div style="color:#4dcc70;font-size:10px;font-weight:700;margin-bottom:6px;letter-spacing:.04em;border-bottom:0.5px solid #1a4a1a;padding-bottom:5px;">'+TEXTES.revelationsHeader+'</div>';
  REVELATIONS.forEach(function(r){
    h+='<div class="revcard"><div class="revcard-head"><span class="revcard-icon">'+r.icon+'</span><span class="revcard-title">'+r.title+'</span></div><div class="revcard-txt">'+r.txt+'</div></div>';
  });
  return h;
}

function endGame(type){
  var html='';
  var F=TEXTES.fins;
  if(type==='imm'){
    html='<div style="color:#555;font-size:10.5px;font-weight:600;margin-bottom:7px;">'+F.imm.titre+'</div>'
      +'<div style="color:#555;font-size:12px;">'+F.imm.corps+'</div>';
    html+='<button class="rb js-restart">'+TEXTES.restartBtn+'</button>';
    ca.innerHTML='<div class="ea">'+html+'</div>';
  }else if(type==='block'){
    html='<div style="color:#ff453a;font-size:10.5px;font-weight:600;margin-bottom:7px;">'+F.blocage.titre+'</div>'
      +'<div style="color:#e5e5ea;font-size:12px;line-height:1.65;">'
      +'<span style="color:#555">'+TEXTES.contact.name+' :</span> '+F.blocage.ines+'<br>'
      +'<span style="color:#555">'+F.blocage.sys+'</span></div>';
    html+='<button class="rb js-restart">'+TEXTES.restartBtn+'</button>';
    ca.innerHTML='<div class="ea">'+html+'</div>';
  }else if(good>=2){
    finalSuccessPhase(good>=3);
  }else{
    html='<div style="color:#ff453a;font-size:10.5px;font-weight:600;margin-bottom:6px;">'+F.echec.titre+'</div>'
      +'<div style="color:#e5e5ea;font-size:12px;line-height:1.65;">'
      +'<span style="color:#555">'+TEXTES.contact.name+' :</span> '+F.echec.ines.replace(/\n/g,'<br>')+'<br><br>'
      +'<span style="color:#555">'+F.echec.sys+'</span></div>';
    html+='<button class="rb js-restart">'+TEXTES.restartBtn+'</button>';
    ca.innerHTML='<div class="ea">'+html+'</div>';
  }
}

async function finalSuccessPhase(isSuccess){
  var F=TEXTES.fins;
  var fin=isSuccess?F.succes:F.fragile;
  ca.innerHTML='';

  // Phase 1 — Inès demande de promettre d'être prudent
  await sl(600);showTy();await sl(1000);hideTy();
  addBub(fin.p1ines,'r');
  await sl(400);
  ca.innerHTML='<div class="chint">'+TEXTES.choiceHint+'</div>'
    +'<button class="cb js-p1"><span class="cl">→</span><span>'+fin.p1leo+'</span></button>';
  await new Promise(function(r){
    ca.querySelector('.js-p1').addEventListener('click',function(){addBub(fin.p1leo,'s');r();});
  });
  ca.innerHTML='';

  if(isSuccess&&fin.p1suite){
    await sl(500);showTy();await sl(700);hideTy();
    addBub(fin.p1suite,'r');
    await sl(400);
  }

  // Phase 2 — Inès demande de respecter la vie privée de Clara
  showTy();await sl(900);hideTy();
  addBub(fin.p2ines,'r');
  await sl(400);
  ca.innerHTML='<div class="chint">'+TEXTES.choiceHint+'</div>'
    +'<button class="cb js-p2"><span class="cl">→</span><span>'+fin.p2leo+'</span></button>';
  await new Promise(function(r){
    ca.querySelector('.js-p2').addEventListener('click',function(){addBub(fin.p2leo,'s');r();});
  });
  ca.innerHTML='';

  // Phase 3 — Inès donne les codes
  await sl(700);showTy();await sl(1200);hideTy();
  addBub(fin.codesMsg,'r');
  await sl(600);

  // Phase 4 — Résumé : codes + bilan + navigation
  var titleColor=isSuccess?'#30d158':'#ff9f0a';
  var html='<div style="color:'+titleColor+';font-size:10.5px;font-weight:600;margin-bottom:6px;">'+fin.titre+'</div>';
  html+=buildIgCard(fin.ig);
  html+='<div style="margin-top:8px;">'+buildRevCards()+'</div>';
  html+='<a href="2_Insta_de_Clara.html" class="nxbtn">'+fin.nextPartBtn+'</a>';
  html+='<button class="rb js-restart" style="margin-top:6px;">'+TEXTES.restartBtn+'</button>';
  ca.innerHTML='<div class="ea">'+html+'</div>';
}

async function startGame(){
  trust=0;good=0;step=0;crisisUsed=false;phase='story';busy=false;tyEl=null;
  ma.innerHTML='';ca.innerHTML='<div class="chint">…</div>';
  tf.style.width='50%';tf.style.background='#ff9f0a';
  tlb.textContent=TEXTES.trustInitial;tlb.style.color='#ff9f0a';
  tdl.style.opacity='0';
  document.getElementById('st').textContent=TEXTES.contact.statusOnline;

  var O=TEXTES.ouverture;
  await sl(500);
  addBub(O[0].t,O[0].type);
  showTy();await sl(700);hideTy();
  addBub(O[1].t,O[1].type);
  await sl(300);
  addBub(O[2].t,O[2].type);
  showTy();await sl(1100);hideTy();
  addBub(O[3].t,O[3].type);
  await sl(320);
  addBub(O[4].t,O[4].type);
  showTy();await sl(900);hideTy();
  addBub(O[5].t,O[5].type);
  await sl(350);
  if(G[0].edu){await sl(400);addBub(G[0].edu,'ed');await sl(600);}
  showChoices(G[0].c,false);
  busy=false;
}

// Event delegation pour le bouton restart généré dynamiquement
ca.addEventListener('click', function(e){
  if(e.target.closest('.js-restart')) startGame();
});

try { localStorage.setItem('rc_p1_visited','1'); } catch(e) {}

var intro1El = document.getElementById('intro1');
if(intro1El){
  function dismissIntro(){
    intro1El.style.transition='opacity .9s ease';
    intro1El.style.opacity='0';
    intro1El.style.pointerEvents='none';
    setTimeout(function(){intro1El.style.display='none';startGame();},900);
  }
  document.getElementById('intro1-btn').addEventListener('click',function(e){
    e.stopPropagation();dismissIntro();
  });
  intro1El.addEventListener('click',dismissIntro);
}else{
  startGame();
}
