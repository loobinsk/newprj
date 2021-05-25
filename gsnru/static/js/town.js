(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-town-create', function(e) {
            $.get('/client/town/create', function(data){
                bootbox.dialog({
                    title: 'Создать город',
                    message: data,
                    buttons: {
                        'Разместить новость': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#town-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.town-list').length>0) {
                                            $.get('/client/town/'+data.id+'/preview', function(data) {
                                                $('.town-list').prepend(data);
                                            });
                                        } else {
                                            window.location = data.object.url;
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

        $(document).on('click', '.btn-town-edit', function(e) {
            $.get('/client/town/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить город',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#town-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/town/'+data.id+'/preview';
                                        if ($('.town-detail').length>0)
                                            url = '/client/town/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.town-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-town-del', function(e) {
            bootbox.confirm('Удалить город', function(result) {
                if (result) {
                    $.post('/client/town/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.town-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.town-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
