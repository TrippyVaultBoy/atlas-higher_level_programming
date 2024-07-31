const jQuery = window.jQuery;

jQuery(document).ready(function () {
  jQuery('div#red_header').click(function () {
    jQuery('header').addClass('red');
  });
});