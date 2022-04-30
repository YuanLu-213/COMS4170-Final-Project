$(document).ready(function () {
  // $('h4').hide();

  // $('#hint').click(function(){
  //     $("h4").slideToggle();
  // })
  $("#dialog").dialog({
    autoOpen: false,
    modal: true,
  });

  $("#dialog-check").dialog({
    autoOpen: false,
    modal: true,
  });

  $("form").submit(function (event) {
    if ($("input[name=radAnswer]:checked").length > 0) {
      return;
    }

    $("#dialog-check").dialog({
      buttons: {
        Confirm: function () {
          $(this).dialog("close");
        },
      },
    });

    $("#dialog-check").dialog("open");
    event.preventDefault();
  });

  $(".again").click(function (e) {
    var targetUrl = "/quiz_start";
    e.preventDefault();
    $("#dialog").dialog({
      buttons: {
        Confirm: function () {
          window.location.href = targetUrl;
        },
        Cancel: function () {
          $(this).dialog("close");
        },
      },
    });

    $("#dialog").dialog("open");
  });
});

$("#confirm").click(function (e) {
  var targetUrl = $(this).attr("href");
  e.preventDefault();
  $("#dialog").dialog({
    buttons: {
      Confirm: function () {
        window.location.href = targetUrl;
      },
      Cancel: function () {
        $(this).dialog("close");
      },
    },
  });

  $("#dialog").dialog("open");
});
