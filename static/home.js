$(document).ready(function(){
    console.log(tracking)
    var resume = tracking[tracking.length - 1]
    console.log(resume)
    $("#resume").click(function(){
        window.location.assign(resume)
    })
});