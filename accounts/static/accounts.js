var initialize = function (navigator) {
    jQuery('#id_login').on('click', function ($) {
        navigator.id.request();
    });
};
window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};
