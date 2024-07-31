const jQuery = window.jQuery;

jQuery(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  jQuery.get(url, function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      jQuery('<li></li>').text(movie.title).appendTo('UL#list_movies');
    });
  });
});