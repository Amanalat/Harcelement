// ── Code Gate ──────────────────────────────────────────────────────────────

function checkCode() {
  var val = (document.getElementById('gate-input').value || '').replace(/\s/g,'').toUpperCase();
  var err = document.getElementById('gate-error');
  if (val === '4827') {
    document.getElementById('code-gate').style.display = 'none';
    document.getElementById('warning-overlay').style.display = 'flex';
    err.style.display = 'none';
  } else {
    err.style.display = 'block';
    document.getElementById('gate-input').style.borderColor = '#e94560';
    setTimeout(function(){ document.getElementById('gate-input').style.borderColor = '#1a5030'; }, 1500);
  }
}

document.getElementById('gate-input').addEventListener('keydown', function(e){
  if (e.key === 'Enter') checkCode();
});

// ── Initialisation UI ──────────────────────────────────────────────────────

function init() {
  // Bandeau
  document.getElementById('b-strong').textContent = WA_DATA.banner.strong;
  document.getElementById('b-tail').textContent   = WA_DATA.banner.tail;

  // En-tête groupe
  document.getElementById('wa-avatar').textContent  = WA_DATA.group.avatar;
  document.getElementById('wa-name').textContent    = WA_DATA.group.name;
  document.getElementById('wa-members').textContent = WA_DATA.group.subtitle;
  document.getElementById('back-nav').addEventListener('click', function () {
    window.location.href = WA_DATA.navigation.prev.url;
  });

  // Avertissement → ouvre la mission ensuite
  document.getElementById('w-icon').textContent  = WA_DATA.warning.icon;
  document.getElementById('w-title').textContent = WA_DATA.warning.title;
  document.getElementById('w-body').textContent  = WA_DATA.warning.body;
  var wb = document.getElementById('w-btn');
  wb.textContent = WA_DATA.warning.btn;
  wb.addEventListener('click', function () {
    document.getElementById('warning-overlay').style.display = 'none';
    document.getElementById('mission-overlay').style.display = 'flex';
  });

  // Mission overlay
  document.getElementById('m-title').textContent = WA_DATA.mission.title;
  document.getElementById('m-body').textContent  = WA_DATA.mission.body;
  var mb = document.getElementById('mission-start-btn');
  mb.textContent = WA_DATA.mission.btn;
  mb.addEventListener('click', function () {
    document.getElementById('mission-overlay').style.display = 'none';
  });

  // Bouton démarrer
  var sb = document.getElementById('start-btn');
  sb.textContent = WA_DATA.startLabel;
  sb.addEventListener('click', startPlay);

  // Modal Instagram
  document.getElementById('ig-modal-photo').src = WA_DATA.instagramCard.photo;
  document.getElementById('ig-modal-cap-text').textContent = ' ' + WA_DATA.instagramCard.caption;
  document.getElementById('ig-modal-likes').textContent    = '3 J\'aime';

  // Retour depuis Instagram ? → sauter les overlays, reprendre où on en était
  var saved = sessionStorage.getItem('harcelement_wa_state');
  if (saved !== null) {
    sessionStorage.removeItem('harcelement_wa_state');
    document.getElementById('code-gate').style.display = 'none';
    document.getElementById('warning-overlay').style.display = 'none';
    fastForwardTo(parseInt(saved, 10));
  }
}

// ── Fast-forward au retour d'Instagram ────────────────────────────────────

function fastForwardTo(targetIndex) {
  document.getElementById('start-screen').style.display = 'none';
  var container = document.getElementById('messages-container');

  var sep = document.createElement('div');
  sep.className = 'date-sep';
  sep.textContent = 'Aujourd\'hui';
  container.appendChild(sep);

  for (var i = 0; i < targetIndex && i < WA_DATA.messages.length; i++) {
    var m = WA_DATA.messages[i];
    if      (m.type === 'system')         appendSystem(m.text);
    else if (m.type === 'instagram-card') appendInstagramCard(m.sender, true);
    else if (m.type === 'time-sep')       appendTimeSep(m.text);
    else if (!m.type)                     appendMessage(m.sender, m.text, m.time, true);
    // quiz / end ignorés
  }

  msgIndex = targetIndex;
  scrollChat();
  processNext();
}

// ── Naviguer vers Instagram (sauvegarde l'état avant de partir) ───────────

function goToInstagram() {
  sessionStorage.setItem('harcelement_wa_state', String(msgIndex));
  sessionStorage.setItem('harcelement_wa_from', '1');
  window.location.href = WA_DATA.navigation.prev.url;
}

// ── Moteur de lecture automatique ─────────────────────────────────────────

var msgIndex = 0;

function startPlay() {
  document.getElementById('start-screen').style.display = 'none';
  var sep = document.createElement('div');
  sep.className = 'date-sep';
  sep.textContent = 'Aujourd\'hui';
  document.getElementById('messages-container').appendChild(sep);
  processNext();
}

function processNext() {
  if (msgIndex >= WA_DATA.messages.length) return;
  var msg = WA_DATA.messages[msgIndex++];

  if (msg.type === 'quiz') {
    openQuiz(msg.quizId);
    return;
  }
  if (msg.type === 'end') {
    showEndState();
    return;
  }
  if (msg.type === 'system') {
    appendSystem(msg.text);
    wait(msg.delay || 800, processNext);
    return;
  }
  if (msg.type === 'time-sep') {
    appendTimeSep(msg.text);
    scrollChat();
    wait(msg.delay || 1000, processNext);
    return;
  }

  var typingMs = (msg.type === 'instagram-card')
    ? 1000
    : Math.min(1200, Math.max(300, (msg.text || '').length * 16));

  var typingEl = showTyping(msg.sender);
  scrollChat();
  wait(typingMs, function () {
    typingEl.remove();
    if (msg.type === 'instagram-card') {
      appendInstagramCard(msg.sender, false);
    } else {
      appendMessage(msg.sender, msg.text, msg.time, false);
    }
    scrollChat();
    wait(msg.delay || 700, processNext);
  });
}

function wait(ms, cb) { setTimeout(cb, ms); }

function scrollChat() {
  var ca = document.getElementById('chat-area');
  ca.scrollTop = ca.scrollHeight;
}

// ── Création des éléments ─────────────────────────────────────────────────

function showTyping(sender) {
  var color = WA_DATA.senderColors[sender] || '#8696a0';
  var row = document.createElement('div');
  row.className = 'typing-row';
  row.innerHTML =
    '<div class="typing-sender" style="color:' + color + '">' + sender + '</div>' +
    '<div class="typing-bubble">' +
      '<div class="dot"></div><div class="dot"></div><div class="dot"></div>' +
    '</div>';
  document.getElementById('messages-container').appendChild(row);
  return row;
}

function appendMessage(sender, text, time, instant) {
  var color     = WA_DATA.senderColors[sender] || '#8696a0';
  var container = document.getElementById('messages-container');
  var row       = document.createElement('div');
  row.className    = 'msg-row';
  row.dataset.sender = sender;
  if (instant) row.style.animation = 'none';

  var prev = container.lastElementChild;
  var showName = !prev
    || prev.dataset.sender !== sender
    || prev.classList.contains('ig-card-row')
    || prev.classList.contains('time-sep')
    || prev.classList.contains('date-sep')
    || prev.classList.contains('sys-msg');

  var nameHtml = showName
    ? '<div class="msg-sender" style="color:' + color + '">' + sender + '</div>'
    : '';

  row.innerHTML = nameHtml +
    '<div class="msg-bubble">' +
      formatText(text) +
      '<span class="msg-time">' + (time || '') + '</span>' +
    '</div>';
  container.appendChild(row);
}

function appendSystem(text) {
  var el = document.createElement('div');
  el.className = 'sys-msg';
  el.textContent = text;
  document.getElementById('messages-container').appendChild(el);
}

function appendTimeSep(text) {
  var el = document.createElement('div');
  el.className = 'time-sep';
  el.textContent = '— ' + text + ' —';
  document.getElementById('messages-container').appendChild(el);
}

function appendInstagramCard(sender, instant) {
  var color = WA_DATA.senderColors[sender] || '#8696a0';
  var card  = WA_DATA.instagramCard;
  var container = document.getElementById('messages-container');

  var row = document.createElement('div');
  row.className = 'ig-card-row';
  row.dataset.sender = sender;
  if (instant) row.style.animation = 'none';

  var cardEl = document.createElement('div');
  cardEl.className = 'ig-card';
  cardEl.innerHTML =
    '<div class="ig-card-header">' +
      '<div class="ig-card-avatar"><img src="images_clara/clara_profil.png" alt=""></div>' +
      '<div>' +
        '<div class="ig-card-name">' + esc(card.account) + '</div>' +
        '<div class="ig-card-app">📷 Instagram</div>' +
      '</div>' +
    '</div>' +
    '<img class="ig-card-photo" src="' + esc(card.photo) + '" alt="">' +
    '<div class="ig-card-caption">' + esc(card.caption) + '</div>' +
    '<button class="ig-card-btn">' + esc(card.seeBtn) + '</button>';

  cardEl.querySelector('.ig-card-btn').addEventListener('click', openIgModal);

  row.innerHTML = '<div class="msg-sender" style="color:' + color + '">' + sender + '</div>';
  row.appendChild(cardEl);
  container.appendChild(row);
}

// Échappe le HTML, met les @mentions en vert avec data-attr pour event delegation
function formatText(str) {
  return esc(str).replace(/@([\w]+)/g, function (match, username) {
    return '<span class="mention" style="cursor:pointer;text-decoration:underline dotted" ' +
           'title="Voir ses messages sur l\'Instagram de Clara" ' +
           'data-goto-instagram="1">@' + username + '</span>';
  });
}

function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Modal Instagram ────────────────────────────────────────────────────────

var igCommentsPlayed = false;

function openIgModal() {
  document.getElementById('ig-modal').classList.add('open');
  if (!igCommentsPlayed) {
    igCommentsPlayed = true;
    playIgComments();
  }
}

function closeIgModal() {
  document.getElementById('ig-modal').classList.remove('open');
}

function playIgComments() {
  var container = document.getElementById('ig-modal-comments');
  var note      = document.getElementById('ig-note');
  var comments  = WA_DATA.instagramComments;
  var accum     = 0;
  comments.forEach(function (c) {
    accum += c.delay;
    (function (comment, delay) {
      setTimeout(function () {
        var el = document.createElement('div');
        el.className = 'ig-comment';
        el.innerHTML =
          '<span class="c-user">' + esc(comment.user) + '</span> ' +
          '<span class="c-text">' + esc(comment.text) + '</span>';
        container.appendChild(el);
        if (container.children.length === comments.length) {
          setTimeout(function () { note.style.display = 'block'; }, 400);
        }
      }, delay);
    })(c, accum);
  });
}

// ── Quiz ──────────────────────────────────────────────────────────────────

function openQuiz(quizId) {
  var q = WA_DATA.quizzes[quizId];
  if (!q) { closeQuizContinue(); return; }

  document.getElementById('quiz-icon').textContent  = q.icon;
  document.getElementById('quiz-label').textContent = q.label;
  document.getElementById('quiz-question').textContent = q.question;

  var opts = document.getElementById('quiz-options');
  opts.innerHTML = '';
  q.options.forEach(function (opt, i) {
    var btn = document.createElement('button');
    btn.className = 'quiz-opt';
    btn.textContent = opt;
    btn.addEventListener('click', function () { answerQuiz(q, i); });
    opts.appendChild(btn);
  });

  var fb = document.getElementById('quiz-feedback');
  fb.style.display = 'none'; fb.className = 'quiz-fb';
  document.getElementById('quiz-continue').style.display = 'none';
  document.getElementById('quiz-overlay').classList.add('open');
}

function answerQuiz(q, chosen) {
  var correct = chosen === q.correct;
  document.querySelectorAll('.quiz-opt').forEach(function (b, i) {
    b.disabled = true;
    if (i === q.correct)               b.classList.add('correct');
    else if (i === chosen && !correct) b.classList.add('wrong');
  });
  var fb = document.getElementById('quiz-feedback');
  fb.style.display = 'block';
  fb.className = 'quiz-fb ' + (correct ? 'good' : 'bad');
  fb.innerHTML = (correct ? '<strong>✓ Bonne réponse !</strong><br>' : '<strong>✗ Pas tout à fait.</strong><br>') + esc(q.explanation);
  document.getElementById('quiz-continue').style.display = 'inline-block';
}

function closeQuizContinue() {
  document.getElementById('quiz-overlay').classList.remove('open');
  processNext();
}

// ── État final + synthèse ─────────────────────────────────────────────────

function showEndState() {
  document.getElementById('chat-area').style.display = 'none';
  document.getElementById('wa-input').style.display  = 'none';

  var end  = document.getElementById('end-state');
  var data = WA_DATA.endMessage;
  document.getElementById('end-title').textContent = data.title;
  document.getElementById('end-note').textContent  = data.note;

  var list = document.getElementById('end-list');
  list.innerHTML = '';
  data.points.forEach(function (p) {
    var li = document.createElement('li');
    li.textContent = p;
    list.appendChild(li);
  });

  var synthEl = document.getElementById('synthesis-section');
  synthEl.innerHTML = '';
  var titleDiv = document.createElement('div');
  titleDiv.className   = 'synth-title-wa';
  titleDiv.textContent = WA_DATA.synthesis.title;
  synthEl.appendChild(titleDiv);
  WA_DATA.synthesis.items.forEach(function (item) {
    var div = document.createElement('div');
    div.className = 'synth-item-wa';
    div.innerHTML =
      '<div class="synth-head-wa">' +
        '<span class="synth-icon-wa">' + item.icon + '</span>' +
        '<span class="synth-type-wa">' + esc(item.type) + '</span>' +
      '</div>' +
      '<div class="synth-exp-wa">' + esc(item.exp) + '</div>';
    synthEl.appendChild(div);
  });

  document.getElementById('end-prev').textContent = WA_DATA.navigation.prev.label;
  document.getElementById('end-prev').href        = WA_DATA.navigation.prev.url;
  document.getElementById('end-next').textContent = WA_DATA.navigation.next.label;
  document.getElementById('end-next').href        = WA_DATA.navigation.next.url;

  end.classList.add('active');
}

// ── Event listeners statiques ─────────────────────────────────────────────

document.getElementById('gate-btn').addEventListener('click', checkCode);
document.getElementById('quiz-continue').addEventListener('click', closeQuizContinue);
document.getElementById('ig-modal-close').addEventListener('click', closeIgModal);
document.getElementById('ig-modal-back').addEventListener('click', closeIgModal);

// Event delegation pour les @mentions dynamiques
document.getElementById('messages-container').addEventListener('click', function (e) {
  if (e.target.closest('[data-goto-instagram]')) goToInstagram();
});

// ── Démarrage ─────────────────────────────────────────────────────────────
init();
