
$(document).ready(function () {

    //Remove the navbar toggle button 
    $(".navbar-toggler").remove()

    //Remove the contact portion
    $("#contact").remove()

    //Remove the about portion
    $("#about").remove()


    $(function () {
        $("#datetimepicker").datetimepicker();
    })
})
