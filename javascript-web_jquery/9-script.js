const jQuery = window.jQuery;

jQuery(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  jQuery.get(url, function (data) {
    jQuery('#hello').text(data.hello);
  });
});