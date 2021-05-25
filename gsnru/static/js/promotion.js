(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-promotion-create', function(e) {
            var user = $(this).data('user');
            $.get('/client/promotion/create', {user: user}, function(data){
                bootbox.dialog({
                    title: 'Создать промоакцию',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#promotion-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/promotion/'+data.id+'/preview', function(data) {
                                            $('.promotion-list tbody').prepend(data);
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

        $(document).on('click', '.btn-promotion-edit', function(e) {
            $.get('/client/promotion/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить промоакцию',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#promotion-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/promotion/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.promotion-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-promotion-del', function(e) {
            bootbox.confirm('Удалить промоакцию', function(result) {
                if (result) {
                    $.post('/client/promotion/'+$(e.target).data('id')+'/del', function(data) {
                        $('.promotion-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
        
        $(document).on('click', '.btn-promocode-create', function(e) {
            var user = $(this).data('user');
            $.get('/client/promocode/create', {user: user}, function(data){
                bootbox.dialog({
                    title: 'Создать промокод',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#promocode-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/promocode/'+data.id+'/preview', function(data) {
                                            $('.promocode-list tbody').prepend(data);
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

        $(document).on('click', '.btn-promocode-edit', function(e) {
            $.get('/client/promocode/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить промокод',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#promocode-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/promocode/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.promocode-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-promocode-del', function(e) {
            bootbox.confirm('Удалить промокод', function(result) {
                if (result) {
                    $.post('/client/promocode/'+$(e.target).data('id')+'/del', function(data) {
                        $('.promocode-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
