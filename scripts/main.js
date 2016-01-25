$(document).ready(function(){

    $("#showAboutMe").click(function(){
        $("#about").show("slow");
        $("#notes").hide("slow");
        $("#next_steps").hide("slow");
    });    

    $("#showNotes").click(function(){
        $("#about").hide("slow");
        $("#notes").show("slow");
        $("#next_steps").hide("slow");
    });

    $("#showNextSteps").click(function(){
        $("#about").hide("slow");
        $("#notes").hide("slow");
        $("#next_steps").show("slow");
    });

});