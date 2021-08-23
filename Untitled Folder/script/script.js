//javascript function for the disappearing design button and text appearing on click
var times = 0;

$(".designbtn").on("click", function() {
    times++;
    if (times % 2 === 1) {
        $("#designparagraph").fadeIn("slow");
        $('.designbtn').css({
            'display': 'none',

        });


    } else {
        $("#designparagraph").fadeOut("slow");

    }

});


//javascript function for disappearing development button
var times2 = 0;

$("#devbtn").on("click", function() {
    times2++;
    if (times2 % 2 === 1) {
        $("#devparagraph").fadeIn("slow");
        $('#devbtn').css({
            'display': 'none',

        });
    } else {
        $("#devparagraph").fadeOut("slow");

    }

});

//javascript for the disappearing product button for the paragraph to appear

var times3 = 0;

$("#productbtn").on("click", function() {
    times3++;
    if (times3 % 2 === 1) {
        $("#productparagraph").fadeIn("slow");
        $('#productbtn').css({
            'display': 'none',


        });
    } else {
        $("#productparagraph").fadeOut("slow");

    }

});

//function for the alertbox popup to show when user clicks the button

function myFunction() {
    let varName = document.getElementById("MERGE1").value;
    //includes a line of code to auto capitalize the 1st letter of the users name.
    const nameCaps = varName.charAt(0).toUpperCase() + varName.slice(1)
    alert("Hey " + nameCaps + ". Thank you for reaching out to us.\nWe have received your message.\nHave a nice day");
}

//this function prevents the page from redirecting someone to the mailchimp thanks for subscribing webpage
//however, the return false part makes the form not clear the input field cleared and not return to top of page on submit

$(document).ready(function() {
    var $form = $('form');
    $form.submit(function() {
        $.post($(this).attr('action'), $(this).serialize(), function(response) {
            // do something here on success
        }, 'json');
        return false;

    });
});


//this function deals with the issue of the form not returning to the top on submission due to the above function since the return value is false
function scrollToTop() {
    window.scrollTo(0, 0);
    return true;
}