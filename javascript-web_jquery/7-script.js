const jQuery = window.jQuery;

jQuery(document).ready(function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  jQuery.get(url, function (data) {
    jQuery('#character').text(data.name);
  });
});