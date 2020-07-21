//Opens the default breakfast tab
$(document).ready(function () {
  document.getElementById("defaultOpen").click();
});

function openCourse(mealType, elmnt, color) {
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
  document.getElementById(mealType).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
  document.body.style.backgroundColor = color;
}

// Thumbnail image controls
function currentSlide(n) {
  clearTimeout(slidetime);
  showSlides((slideIndex = n));
}

// Get the elements with class="column"
var elements = document.getElementsByClassName("column");

// Declare a loop variable
var i;

// List View
function listView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "100%";
  }
}

// Grid View
function gridView() {
  for (i = 0; i < elements.length; i++) {
    elements[i].style.width = "50%";
  }
}

//Confirms deletion
function confirmDelete() {
  if (confirm("Are you sure you want to delete this recipe?") == false) {
    return false;
  } else {
    return true;
  }
}

//Ajax Modal
$('[data-toggle="ajaxModal"]').on("click", function (e) {
  $("#ajaxModal").remove();
  e.preventDefault();
  var $this = $(this),
    $remote = $this.data("remote") || $this.attr("href"),
    $modal = $(
      '<div class="modal" id="ajaxModal"><div class="modal-body"></div></div>'
    );
  $("body").append($modal);
  $modal.modal({ backdrop: "static", keyboard: false });
  $modal.load($remote);
});
