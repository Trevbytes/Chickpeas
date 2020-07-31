/* Closes the modal */
$(".custom-close").on("click", function () {
  $(".modal-backdrop").remove();
  $("#editIngredientModal").remove();
});

/* Prevents Submitting with Return key */
$('#editIngredientModal').on('keyup keypress', function(e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 13) { 
    e.preventDefault();
    return false;
  }
});

/* Functions for adding subsitute ingredients to the ingredients list in edit_ingredient.html */
var selectedIngredient;
$("select.ingredient_select").change(function () {
  selectedIngredient = $(this).children("option:selected").val();
});
function addToIngredientList() {
  if (!!selectedIngredient) {
    var commentlines = "";
    var ingredient_comment = $("#ingredient_comment").val();
    ingredient_index++;
    if (!!ingredient_comment) {
      commentlines = "---";
    } else {
      commentlines = "";
    }
    $("#sub_ingredient_list").append(
      `<li type="text" readonly class="list-group-item"><input type="text" class="form-control" readonly name="sub_ingredient_id_${ingredient_index}" value="${selectedIngredient} ${commentlines} ${ingredient_comment}"><button type="button" onclick="removeLI()" class="btn float-right delete">Remove Ingredient</button><input type="text" hidden name="name_sub_ingredient_id_${ingredient_index}" value="${selectedIngredient}"></li>`
    );
    clearAddIngredient();
  }
}

//Event listener to remove ingredients from the list
$(document).ready(function () {
    $(".delete").on("click", function () {        
        $(this).parent().children().each(function() {
            $(this).attr("name", "remove_" + $(this).attr("name"));
        });       
        $(this).parent().clone().appendTo("#remove-request");
        $("#remove-request").find("button").remove();	
        $(this).parent().remove();})
});

function clearAddIngredient() {
  $("#ingredient_select").prop("selectedIndex", 1).val();
  $("select.ingredient_select").val("selectedvalue").trigger("change");
  $("#ingredient_comment").val("");
}

/* Functions for ingredient filter */
function filterFunctionForEditIngredient() {
  var input, filter, ul, li, a, i, option;
  input = document.getElementById("edit-ingredient-dropdown-input");
  filter = input.value.toUpperCase();
  div = document.getElementById("edit-ingredient-dropdown");
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
