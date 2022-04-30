$(document).ready(function(){
    var learning = {{learning | tojson}}
    var tracking = {{tracking | tojson}}
    
    var resume = tracking[tracking.length - 1]

    if(resume == undefined){
        console.log("undefined");
        $("#resume").addClass("disabled");
        $("#resume").prop('disabled', true);
    }
    else{
        $("#resume").removeClass("disabled");
        $("#resume").click(function(){
            window.location.assign(resume)
        })
    }
});