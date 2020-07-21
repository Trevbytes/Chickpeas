/* Functions for ingredient filter and dropdown */
function myFunctiondrop() {
  document.getElementById("myDropdown").classList.toggle("show");
  $("#myInput").focus();
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
}

//Ajax Modals
$('[data-toggle="submitIngredientModal"]').on("click", function (e) {
  $("#submitIngredientModal").remove();
  e.preventDefault();
  var $this = $(this),
    $remote = $this.data("remote") || $this.attr("href"),
    $modal = $(
      '<div class="modal" id="submitIngredientModal"><div class="modal-body"></div></div>'
    );
  $("body").append($modal);
  $modal.modal({ backdrop: "static", keyboard: false });
  $modal.load($remote);
});

$('[data-toggle="editIngredientModal"]').on("click", function (e) {
  $("#editIngredientModal").remove();
  e.preventDefault();
  var $this = $(this),
    $remote = $this.data("remote") || $this.attr("href"),
    $modal = $(
      '<div class="modal" id="editIngredientModal"><div class="modal-body"></div></div>'
    );
  $("body").append($modal);
  $modal.modal({ backdrop: "static", keyboard: false });
  $modal.load($remote);
});

$('[data-toggle="ajaxModalIngredient"]').on("click", function (e) {
  $("#ajaxModalIngredient").remove();
  e.preventDefault();
  var $this = $(this),
    $remote = $this.data("remote") || $this.attr("href"),
    $modal = $(
      '<div class="modal" id="ajaxModalIngredient"><div class="modal-body"></div></div>'
    );
  $("body").append($modal);
  $modal.modal({ backdrop: "static", keyboard: false });
  $modal.load($remote);
});

//Delete Confirmation
function confirmDelete() {
  if (confirm("Are you sure you want to delete this ingredient?") == false) {
    return false;
  } else {
    return true;
  }
}
