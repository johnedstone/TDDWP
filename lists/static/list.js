/* This appears to be removed by QUnit test
 * so I've added it directly to the test
 */
jQuery.noConflict();
jQuery(document).ready(function($) {
    console.log("Ready two three four");
    $('input').on('keypress', function () {
        $('.has-error').hide();
    });
});
