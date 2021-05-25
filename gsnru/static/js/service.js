(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-service-create', function(e) {
            var company = $(e.currentTarget).data('company');
            var user = $(e.currentTarget).data('user');
            $.get('/client/service/create', {company: company, user: user}, function(data){
                bootbox.dialog({
                    title: 'Подключить услугу',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#connected-service-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/service/'+data.id+'/preview', function(data) {
                                            $('.connected-service-list').prepend(data);
                                            $('.no-services').remove();
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

        $(document).on('click', '.btn-service-edit', function(e) {
            $.get('/client/service/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить подключенную услугу',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#connected-service-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/service/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.connected-service-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-service-del', function(e) {
            bootbox.confirm('Удалить подключенную услугу', function(result) {
                if (result) {
                    $.post('/client/service/'+$(e.target).data('id')+'/del', function(data) {
                        $('.connected-service-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
