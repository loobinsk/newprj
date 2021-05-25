(function($) {
    $(document).ready(function() {

        var offcanvasAction = function(e){
            if ($('body').hasClass('offcanvas-filter__page_active')) {
                $('#catalog-filter-btn').removeClass('catalog-filter_open');
                $('body').removeClass('offcanvas-filter__page_active');
                $('.offcanvas-filter').removeClass('offcanvas-filter_active');
            } else {
                $('#catalog-filter-btn').addClass('catalog-filter_open');
                $('body').addClass('offcanvas-filter__page_active');
                $('.offcanvas-filter').addClass('offcanvas-filter_active'); 
            }
        }

        $('#catalog-filter-btn').click(offcanvasAction);
        $('.offcanvas-filter__close').click(offcanvasAction);
    });
})(jQuery);