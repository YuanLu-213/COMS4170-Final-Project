$(document).ready(function () {
  let location = window.location.href;
  console.log(location);

  $.ajax({
    type: "POST",
    url: "/track_learning",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(location),
    success: function (res) {
      console.log("succeed");
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
});
