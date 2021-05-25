(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-tariff-create', function(e) {
            $.get('/client/tariff/create', function(data){
                bootbox.dialog({
                    title: 'Создать тариф',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#tariff-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.tariff-list').length>0) {
                                            $.get('/client/tariff/'+data.id+'/preview', function(data) {
                                                $('.tariff-list').prepend(data);
                                            });
                                        }
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

        $(document).on('click', '.btn-tariff-edit', function(e) {
            $.get('/client/tariff/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить тариф',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#tariff-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/tariff/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.tariff-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-tariff-del', function(e) {
            bootbox.confirm('Удалить тариф', function(result) {
                if (result) {
                    $.post('/client/tariff/'+$(e.target).data('id')+'/del', function(data) {
                        $('.tariff-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.btn-tariff-order', function(e) {
            $.get('/tariff/'+$(this).data('id')+'/order', function(data){
                bootbox.dialog({
                    title: 'Подключить тариф',
                    message: data,
                    buttons: {
                        'Отмена': {
                            className: 'btn-default'
                        }
                    }
                });
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-payment-order-create', function(e) {
            $('#payment-order-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    window.location = data.object.url;
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-buy-order-create', function(e) {
            $('#buy-order-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    window.location = data.object.url;
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });
    });
})(jQuery);
