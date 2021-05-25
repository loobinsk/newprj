(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                type: 'bangTidy',
                closable: true
            }).show();
        }

        $(document).on('click', 'form.video-upload-form .close', function(e) {
            $.post('/uvideo/'+$(e.currentTarget).data('id')+'/del', function(data) {
                var id = $(e.currentTarget).data('id');
                var form_id = $(e.currentTarget.form).data('id');
                var values_node = $('#'+form_id+'-values input');
                values_node.attr('value', '')
                $('form.video-upload-form li[data-id='+id+']').remove();
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.video-upload-form .video-link-upload', function(e){
            $(e.currentTarget.form).ajaxSubmit({
                dataType:'json',
                success:function(data) {
                    $(e.currentTarget.form).find('.upload-video-list').empty().append('<li data-id="'+data.id+'"><img src="'+data.object.url+'"><button class="close" aria-hidden="true" data-id="'+data.id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values input');
                    values_node.attr('value', data.id);
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

    });
})(jQuery);
