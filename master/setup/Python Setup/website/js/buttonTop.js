window.onscroll = function() {displayButton()};

function displayButton() {
  document.querySelector('#topButton').style.display = "block";
}

function toTop() {
  window.scrollTo(0, 0);
}
