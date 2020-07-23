function confirmDelete() {
  if (confirm("Do you want to delete this recipe?") == false) {
    return false;
  } else {
    return true;
  }
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
