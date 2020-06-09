$(document).ready(function () {
  M.AutoInit();
  document.getElementById("defaultOpen").click();
});


// Thumbnail image controls
function currentSlide(n) {
  clearTimeout(slidetime);
  showSlides((slideIndex = n));
}

var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  slidetime = setTimeout(showSlides, 6000); // Change image every 2 seconds
}
