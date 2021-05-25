(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-password-create', function(e) {
            var user = $(this).data('user');
            $.get('/client/password/create', {user: user}, function(data){
                bootbox.dialog({
                    title: 'Создать пароль',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#password-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/password/'+data.id+'/preview', function(data) {
                                            $('.password-list tbody').prepend(data);
                                        });
                                        bootbox.hideAll();
                                    },
                                    error: failFunction
                                });
                                return false;
                            }
                        },
                        'Отмена': {
                            className: 'btn-default'
                        }
                    }
                });
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-password-edit', function(e) {
            $.get('/client/password/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить пароль',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#password-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/password/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.password-item-'+data.id).replaceWith(preview);
                                        });
                                        bootbox.hideAll();
                                    },
                                    error: failFunction
                                });
                                return false;
                            }
                        },
                        'Отмена': {
                            className: 'btn-default'
                        }
                    }
                });
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-password-del', function(e) {
            bootbox.confirm('Удалить пароль', function(result) {
                if (result) {
                    $.post('/client/password/'+$(e.target).data('id')+'/del', function(data) {
                        $('.password-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
