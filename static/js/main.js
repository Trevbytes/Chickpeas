$(document).ready(function () {
  M.AutoInit();
  document.getElementById("defaultOpen").click();
});

// function addToIngredientList() {
//   $("select.ingredient_select").change(function () {
//     var selectedIngredient = $(this).children("option:selected").val();
//     alert("You have selected the country - " + selectedIngredient);
//     $("#recipe_ingredient_list").append("<li>" + selectedIngredient + "</li>");
//   });
//   $("#recipe_ingredient_list").append("<li>" + selectedIngredient + "</li>");
//   console.log(selectedIngredient);
// }

function openCity(cityName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(cityName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it

console.log("Working js");

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("ingredient_select").classList.toggle("show");
  console.log("myFunction working");
}

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
  console.log("filter working");
}

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
