$(document).ready(function(){

    $("#showAboutMe").click(function(){
        $("#about").show("slow");
        $("#notes").hide("slow");
        $("#next-steps").hide("slow");
        $("#comment-wrapper").hide("fast");
    });    

    $("#showNotes").click(function(){
        $("#about").hide("slow");
        $("#notes").show("slow");
        $("#next-steps").hide("slow");
        $("#comment-wrapper").show("fast");
    });

    $("#showNextSteps").click(function(){
        $("#about").hide("slow");
        $("#notes").hide("slow");
        $("#next-steps").show("slow");
        $("#comment-wrapper").show("fast");
    });
});