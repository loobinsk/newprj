(function($) {
    $(document).ready(function() {

        var offcanvasAction = function(e){
            if ($('body').hasClass('offcanvas__page_active')) {
                $('#header-sandwitch').removeClass('sandwitch_open');
                $('body').removeClass('offcanvas__page_active');
                $('.offcanvas').removeClass('offcanvas_active');
            } else {
                $('#header-sandwitch').addClass('sandwitch_open');
                $('body').addClass('offcanvas__page_active');
                $('.offcanvas').addClass('offcanvas_active');
            }
        }

        $('#header-sandwitch').click(offcanvasAction);
        $('.offcanvas__close').click(offcanvasAction);

    });
})(jQuery);