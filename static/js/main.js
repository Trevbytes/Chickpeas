$(document).ready(function () {
  M.AutoInit();
  $('.carousel').carousel();
$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  e.target // newly activated tab
  e.relatedTarget // previous active tab
})
});
console.log("Working js");
