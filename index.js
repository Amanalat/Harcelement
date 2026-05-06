(function(){
  var ov = document.getElementById('intro-overlay');
  if(!ov) return;
  var t = setTimeout(dismiss, 9200);
  ov.addEventListener('click', function(){ clearTimeout(t); dismiss(); });
  function dismiss(){
    ov.style.transition = 'opacity 1.1s ease';
    ov.style.opacity = '0';
    ov.style.pointerEvents = 'none';
    setTimeout(function(){ ov.style.display = 'none'; }, 1100);
  }
})();
