  function confirmDelete() {
    if (confirm("Do you want to delete this recipe?") == false) {
      return false;
    } else {
      return true;
    }
  }

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

function goBack() {
  window.history.back();
}