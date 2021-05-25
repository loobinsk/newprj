(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-show-cr-adverts', function(e){
            var tr = $($(this).attr('href'));
            if (tr.hasClass('hidden')) {
                var content = tr.find('.clients');
                if (content.html() == '') {
                    content.css('display', 'none').append('<div class="loading"></div>').slideDown(400, function(){
                        content.load('/client/agent24/'+content.data('id')+'/clients');
                    });
                } else {
                    content.css('display', 'none').slideDown(400);
                }
                tr.removeClass('hidden');
            } else {
                tr.find('.clients').slideUp(400, function() {
                    tr.addClass('hidden');
                });
            }
            e.preventDefault();
            return false;
        });

    });
})(jQuery);