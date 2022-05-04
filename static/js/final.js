$(document).ready(function () {
  $("#back").click(function () {
    /* redirect to the home page */
    window.location.assign("/");
  });
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
});
