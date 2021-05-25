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

        $(document).on('change', 'form.image-upload-form .single-image-input', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    var single = false;
                    if ($(e.currentTarget.form).hasClass('single'))
                        single = true;
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    if (single)
                        $(e.currentTarget.form).find('.upload-image-list').empty();
                    $(e.currentTarget.form).find('.upload-image-list').append('<li data-id="'+data[0].id+'"><img src="'+data[0].url+'"><button class="close" aria-hidden="true" data-id="'+data[0].id+'">&times;</button></li>');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    if (single)
                        values_node.empty();
                    values_node.append('<input type="hidden" name="'+id+'" value="'+data[0].id+'">');
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('change', 'form.image-upload-form .multiple-image-input', function(e) {
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            console.log(e.currentTarget.form);
            $(e.currentTarget.form).ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $(e.currentTarget.form).find('.progress').addClass('hidden');
                    var id = $(e.currentTarget.form).data('id');
                    var values_node = $('#'+id+'-values');
                    for (var i in data) {
                        $.get('/uimg/'+data[i].id+'/preview', {}, function(html){
                            $(e.currentTarget.form).find('.upload-image-list').append(html);
                        });
                        values_node.append('<input type="hidden" name="'+id+'" value="'+data[i].id+'">');
                    }
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
        });

        $(document).on('click', 'form.image-upload-form .close', function(e) {
            var id = $(e.currentTarget).data('id');
            var form_id = $(e.currentTarget.form).data('id');
            var values_node = $('#'+form_id+'-values');
            values_node.find('input[value="'+id+'"]').remove();
            $('form.image-upload-form li[data-id='+id+']').remove();
            $.post('/uimg/'+$(e.currentTarget).data('id')+'/del', function(data) {}, 'json');
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'form.image-upload-form .description-edit', function(e) {
            var id = $(e.currentTarget).data('id');
            if ($(e.currentTarget.nextSibling).hasClass('in')) {
                $(e.currentTarget).popover('destroy');
            } else {
                $.get('/uimg/'+id+'/edit',{}, function(data){
                    $(e.currentTarget).popover({
                        html: true,
                        placement: 'bottom',
                        trigger: 'manual',
                        title: 'Описание',
                        content: data
                    });
                    $(e.currentTarget).popover('show');
                });
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-userimage-form-save', function(e){
            var id = $(e.currentTarget).data('id');
            $('#userimage-form-'+id).ajaxSubmit({
                dataType: 'json',
                success: function(data){
                    $(e.currentTarget).parents('.upload-image-list').find('li[data-id="'+data.id+'"]').replaceWith(data.object.preview);
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.uimg-library .item', function(e){
            $('.uimg-library .item').removeClass('active');
            $(e.currentTarget).addClass('active');
        });

        $(document).on('click', '.btn-library-more', function(e) {
            var id = $(e.currentTarget).data('lib');
            loadUserImageLibrary(id);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '#userimage-library-form button.btn', function(e){
            $(e.currentTarget.form).find('.progress').removeClass('hidden');
            $(e.currentTarget.form).find('.progress-bar').css('width', '0');
            $('#userimage-library-form').ajaxSubmit({
                dataType: 'json',
                success: function(data){
                    $.get('/uimg/'+data[0].id+'/lib/preview', function(preview){
                        $($('.uimg-library')[0]).prepend(preview);
                    }).fail(failFunction);
                },
                error: failFunction,
                uploadProgress: function(event, position, total, percentComplete) {
                    $(e.currentTarget.form).find('.progress-bar').css('width', percentComplete+'%');
                }
            });
            e.preventDefault();
            return false;
        });

        $('form.image-upload-form').hover(function(e){
            $(e.currentTarget).toggleClass('hover');
        });

        $('.image-list.gallery .carousel').on('slid.bs.carousel', function () {
            var items = $(this).find('.carousel-inner .item');
            for (var i=0; i<items.length; i++) {
                if ($(items[i]).hasClass('active')) {
                    $(this).find('.number').html(i+1);
                }
            }
        });

    });
})(jQuery);


function loadUserImageLibrary(id) {
    var page = (Number)($(id).data('page'));
    $(id + ' .loading').removeClass('hidden');
    $.get('/uimg/lib/list', {'page': page}, function(data){
        $(id + ' .content').append(data);
        $(id).data('page', page+1);
        $(id + ' .loading').addClass('hidden');
    });
}
