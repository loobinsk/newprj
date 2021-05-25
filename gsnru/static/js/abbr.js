(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-abbr-create', function(e) {
            $('#abbr-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $.get('/client/abbr/'+data.id+'/preview', function(data) {
                        $('.abbr-list tbody').prepend(data);
                    });
                    $('#abbr-form')[0].reset();
                },
                error: function(e) {
                    failFunction(e);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-abbr-del', function(e) {
            bootbox.confirm('Удалить сокращение', function(result) {
                if (result) {
                    $.post('/client/abbr/'+$(e.target).data('id')+'/del', function(data) {
                        $('.abbr-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
