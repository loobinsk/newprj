(function($) {
    $(document).ready(function() {

        function refreshCommentCaptcha() {
            $.get('/captcha/refresh/', function(data){
                $('.captcha-form input[type="text"]').val('');
                $('.captcha-form input[type="hidden"]').val(data.key);
                $('.captcha-form img').attr('src', data.image_url);
            }, 'json');
        }

        $(document).on('click', '.btn-comment-add', function(e) {
            if (!$.trim($(e.currentTarget.form).find('textarea')[0].value)) {
                jQuery.notify('Текст сообщения пустой');
            } else {
                $(e.currentTarget.form).ajaxSubmit({
                    dataType: 'json',
                    success: function(data) {
                        if (data.object.parent) {
                            $('.children-'+data.object.parent).append(data.object.preview);
                        } else {
                            $('.comment-list').prepend(data.object.preview);
                        }
                        $(e.currentTarget.form).find('textarea').val('');
                        $(e.currentTarget.form).find('input[name="name"]').val('');
                        $('.children .comment-form').remove();
                        refreshCommentCaptcha();
                    },
                    error: failFunction
                });
            }

            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-reply', function(e) {

            var comment = $(e.currentTarget).parents('.comment-preview')[0];
            var id = $(comment).data('id');
            var key = $(comment).parents('.comments').data('key');

            if ($('.comment-form-'+id).length == 0) {
                $('.children .comment-form').remove();
                $.get('/comment/create', {'parent': id, 'key': key}, function(data){
                    $('.children-'+id).prepend(data);
                    $('.comment-form-'+id+' textarea')[0].focus();
                }).fail(failFunction);
            } else {
                $('.children .comment-form').remove();
            }

            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-del', function(e) {
            var id = $(this).data('id');
            bootbox.confirm('Удалить комментарий', function(result) {
                if (result) {
                    $.post('/comment/'+id+'/del', function(data) {
                        $('#comment-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-refresh-captcha', function(e){
            refreshCommentCaptcha();
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-comment-else', function(e){
            var comment_list = $(this).parents('.comment-list');
            var btn = this;
            $(btn).html('<div class="loading"></div>');
            var key = $(this).data('key');
            var page = $(this).data('page');
            $.get('/comment/list', {key:key, page:page}, function(data){
                $(btn).remove();
                comment_list.append(data);
            });
        });
    });
})(jQuery);
