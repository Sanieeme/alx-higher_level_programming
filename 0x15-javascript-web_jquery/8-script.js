$(document).ready(function (){
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.get(url, function(data) {
        const movies = data.results;
        const $list = $('<ul id="list_movies"></ul>');
        movies.forEach(movie => {
            $('<li>').text(movie.title).appendTo($list);
        });
        $list.appendTo('body');
    }).fail(function(xhr, status, error) {
        console.error('Error:', error);
    });
});
