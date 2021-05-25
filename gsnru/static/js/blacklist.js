(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-blacklist-create', function(e) {
            $.get('/client/blacklist/create', function(data){
                bootbox.dialog({
                    title: 'Создать элемент',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#blacklist-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.blacklist-list').length>0) {
                                            $.get('/client/blacklist/'+data.id+'/preview', function(data) {
                                                $('.blacklist-list tbody').prepend(data);
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

        $(document).on('click', '.btn-blacklist-edit', function(e) {
            $.get('/client/blacklist/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить элемент',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#blacklist-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/blacklist/'+data.id+'/preview';
                                        if ($('.blacklist-detail').length>0)
                                            url = '/client/blacklist/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.blacklist-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-blacklist-del', function(e) {
            bootbox.confirm('Удалить элемент', function(result) {
                if (result) {
                    $.post('/client/blacklist/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.blacklist-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.blacklist-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.btn-blacklist-multi-create', function(e) {
            $.get('/client/blacklist/multi-create', function(data){
                bootbox.dialog({
                    title: 'Импортировать список телефонов',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#blacklist-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        window.location = data.object.url;
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

        $(document).on('click', '.btn-blacklist-check', function(e) {
            var input = $(this).data('input');
            var value = $('#'+input).val();
            $.get('/client/blacklist/check',{tel: value}, function(data){
                bootbox.alert(data.message);
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-blacklist-add-input', function(e) {
            var input = $(this).data('input');
            var value = $('#'+input).val();
            bootbox.confirm('Добавить телефон '+value+' в черный список?', function(result) {
                if (result) {
                    $.post('/client/blacklist/addtel',{tel: value}, function(data){
                        bootbox.alert(data.message);
                    });
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-vkblacklist-del', function(e) {
            bootbox.confirm('Удалить элемент', function(result) {
                if (result) {
                    $.post('/client/vkblacklist/'+$(e.target).data('id')+'/del', function(data) {
                        $('.blacklist-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
