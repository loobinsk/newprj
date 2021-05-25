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

        $(document).on('change', 'form.file-upload-form input[type="file"]', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    $(e.currentTarget.form).find('.upload-file-list').append('<li data-id="'+data.id+'">'+data.object.name+'<button class="close" aria-hidden="true" data-id="'+data.id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    values_node.append('<input type="hidden" name="'+id+'" value="'+data.id+'">');
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('click', 'form.file-upload-form .close', function(e) {
            $.post('/ufile/'+$(e.currentTarget).data('id')+'/del', function(data) {
                var id = $(e.currentTarget).data('id');
                var form_id = $(e.currentTarget.form).data('id');
                var values_node = $('#'+form_id+'-values');
                values_node.find('input[value="'+id+'"]').remove();
                $('form.file-upload-form li[data-id='+id+']').remove();
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.file-upload-form .file-upload-choose', function(e){
            $(e.currentTarget.parentNode.parentNode).find('input[type="file"]').click();
            e.preventDefault();
            return false;
        });

        $(document).on('change', 'form.file-upload-form .file-upload input[type="file"]', function(e) {
            $('.file-upload .filename').text(e.currentTarget.value);
        });

    });
})(jQuery);
