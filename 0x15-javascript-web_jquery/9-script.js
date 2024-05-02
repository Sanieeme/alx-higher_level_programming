$(document).ready(function() {
    const url = 'https://api.funtranslations.com/translate/pirate.json?text=hello';
    $.get(url, function(data) {
        const word = data.contents.translated;
        
        $('<div>').attr('id', 'hello').text(word).appendTo('body');
    }).fail(function(xhr, status, error) {
        console.error('Error:', error);
    });
});
