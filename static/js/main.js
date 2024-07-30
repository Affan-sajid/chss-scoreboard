function fetchScores() {

    console.log('fetching...');

    $.ajax({
        url: '/get-scores/',
        method: 'GET',
        success: function(data) {
            console.log(data);

            $('#Red .score').text(data.Red);
            $('#Orange .score').text(data.Orange);
            $('#Yellow .score').text(data.Yellow);
            $('#Green .score').text(data.Green);
            $('#Blue .score').text(data.Blue);




            $('#teamB-score').text(data.teamB);
            $('#last-updated').text('Last updated: ' + data.last_updated);
        },
        error: function(error) {
            console.error('Error fetching scores:', error);
        }
    });
}

// function isMobile() {
//         return ;
//     }

$(document).ready(function() {
    console.log('readedeedy...');
    fetchScores();  // Fetch scores initially
    console.log(Window.innerWidth >= 640)
    if(window.innerWidth >= 640){

        setInterval(fetchScores, 1000);  // Fetch scores every 5 seconds
    }

});



// function fetchScores() {
//     $.ajax({
//         url: '/get-scores/',
//         method: 'GET',
//         success: function(data) {
//             $('#teamA-score').text(data.teamA);
//             $('#teamB-score').text(data.teamB);
//             $('#last-updated').text('Last updated: ' + data.last_updated);
//         },
//         error: function(error) {
//             console.error('Error fetching scores:', error);
//         }
//     });
// }

// function isMobile() {
//     return window.innerWidth <= 768;
// }

// $(document).ready(function() {
//     fetchScores();
//     if (isMobile()) {
//         $('.desktop-only').hide();
//         $('.mobile-only').show();
//     } else {
//         $('.mobile-only').hide();
//         fetchScores();  // Fetch scores initially
//         setInterval(fetchScores, 5000);  // Fetch scores every 5 seconds
//     }

//     $('#reload-button').click(function() {
//         fetchScores();
//     });
// });
