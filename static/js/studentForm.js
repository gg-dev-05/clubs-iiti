


$(document).ready(function () {



    //Add space below the submit button
    $("button").addClass("mb-5");


    // VALIDATING ROLL NO FIELD AND PUTTING THE EXPECTED VALUES

    $("#phone_no").focusout(function () {
        if (this.value.length != 10) {
            alert("Invalid Phone No.")
            $("#phone_no").val("");
            $("#phone_no").focus();
        }

    })


    var branch = $("#mail_id").val()[8];
    var year = 21 - $("#mail_id").val().slice(3, 5)
    console.log(year)

    switch (year) {
        case 1:
            $("#year1").prop("checked", true);
            break;
        case 2:
            $("#year2").prop("checked", true);
            break;
        case 3:
            $("#year3").prop("checked", true);
            break;
        case 4:
            $("#year4").prop("checked", true);
            break;
        default:
        // code block
    }

    $("#year").val(year);

    if (branch == 1) {
        $("#branch").val("CSE");
    }

    else if (branch == 2) {
        $("#branch").val("EE");

    }

    else if (branch == 3) {
        $("#branch").val("ME");

    }

    else if (branch == 4) {
        $("#branch").val("CE");

    }

    else if (branch == 5) {
        $("#branch").val("MEMS");

    }

});