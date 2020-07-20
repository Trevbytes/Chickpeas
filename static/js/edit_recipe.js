	var selectedIngredient;
  $("select.ingredient_select").change(function () {
    selectedIngredient = $(this).children("option:selected").val();
  });
  function addToIngredientList() {
    if (!!selectedIngredient) {
      var ingredient_measurement = $("#ingredient_measurement").val();
      var commentlines = "";
      var ingredient_comment = $("#ingredient_comment").val();

      if (!!ingredient_comment) {
        commentlines = "---";
      } else {
        commentlines = "";
      }
       ingredient_index++;     
      $("#recipe_ingredient_list").append(
        `<li type="text" readonly class="list-group-item"><input type="text" class="form-control" readonly name="recipe_ingredient_id_${ingredient_index}" value="${ingredient_measurement} ${selectedIngredient} ${commentlines} ${ingredient_comment}"><button type="button" onclick="removeLI()" class="btn float-right delete">Remove Ingredient</button><input type="text" hidden name="name_recipe_ingredient_id_${ingredient_index}" value="${selectedIngredient}"></li>`
      );
      clearAddIngredient();
    }
  }
    function clearAddIngredient() {
    $("#ingredient_select").prop("selectedIndex", 1).val();
    $("select.ingredient_select").val("selectedvalue").trigger("change");
    $("#ingredient_comment").val("");
    $("#ingredient_measurement").val("");
  }
  function removeLI() {
    $(".delete").on("click", function () {
      $(this).parent().remove();
    });
  }

    $(".custom-close").on('click', function() {
        
         $('.modal-backdrop').remove();
         $('#ajaxModal').remove();     
    });
    
      function filterForEditRecipeIngredients() {
    var input, filter, ul, li, a, i, option;
    input = document.getElementById("editRecipeDropdownInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("editRecipeDropdown");
    a = div.getElementsByTagName("option");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }

$(document).ready(function () {
    $(function () {
    $('[data-toggle="tooltip"]').tooltip()})                        
});