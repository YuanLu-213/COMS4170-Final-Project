

$(document).ready(function () {
  // $('h4').hide();

  // $('#hint').click(function(){
  //     $("h4").slideToggle();
  // })
  if(userChoice.length > 0){
    $.each(userChoice,function(index,value){
      console.log(value);
      console.log(index);
      console.log(correctChoice[index]);
      // let correctchoice = correctChoice[index];
      let newindex = parseInt(index)+1;
      let newindexs = newindex.toString();
      console.log(newindexs);
      if (value == correctChoice[index]){
        $('#q' + newindexs).css({"background-color":"rgba(0, 239, 0, 0.49)","border-color":"rgba(0, 239, 0, 0.49)","color":"white"});
      }
      else{
        $('#q' + newindexs).css({"background-color":"rgb(244 67 54 / 48%)","border-color":"rgb(244 67 54 / 48%)","color":"white"});
      }
    })
  }

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
