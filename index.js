(function(){
  // Intro overlay
  var ov = document.getElementById('intro-overlay');
  if(ov){
    if(location.search.indexOf('skip') !== -1){
      ov.style.display = 'none';
    } else {
      var t = setTimeout(dismiss, 9200);
      ov.addEventListener('click', function(){ clearTimeout(t); dismiss(); });
      function dismiss(){
        ov.style.transition = 'opacity 1.1s ease';
        ov.style.opacity = '0';
        ov.style.pointerEvents = 'none';
        setTimeout(function(){ ov.style.display = 'none'; }, 1100);
      }
    }
  }

  // CTA carte 1 — "Reprendre" si déjà visitée
  try {
    if(localStorage.getItem('rc_p1_visited')){
      var label = document.querySelector('.cta-label');
      var badge = document.querySelector('.cta-btn');
      if(label){ label.textContent = 'Reprendre l\'enquête'; }
      if(badge){ badge.textContent = '↩ Continuer'; badge.style.background = '#2c4a6e'; }
    }
  } catch(e) {}
})();
