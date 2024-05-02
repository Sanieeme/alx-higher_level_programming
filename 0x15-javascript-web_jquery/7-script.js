$(document).ready(function (){
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.get(url, function(data){
        const character = data.name;
        $('<div>').attr('id', 'character').text(character).appendTo('body');    
        }).fail(function(xhr, status, error){
            console.error(error);
    });
});
