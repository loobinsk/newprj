(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-referral-create', function(e) {
            var user = $(this).data('user');
            $.get('/client/referral/create', {user: user}, function(data){
                bootbox.dialog({
                    title: 'Создать ссылку',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#referral-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/referral/'+data.id+'/preview', function(data) {
                                            $('.referral-list tbody').prepend(data);
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

        $(document).on('click', '.btn-referral-edit', function(e) {
            $.get('/client/referral/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить ссылку',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#referral-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/referral/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.referral-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-referral-del', function(e) {
            bootbox.confirm('Удалить ссылку', function(result) {
                if (result) {
                    $.post('/client/referral/'+$(e.target).data('id')+'/del', function(data) {
                        $('.referral-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
