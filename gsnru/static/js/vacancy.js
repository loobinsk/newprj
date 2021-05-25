(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-vacancy-create', function(e) {
            $.get('/client/vacancy/create', function(data){
                bootbox.dialog({
                    title: 'Создать вакансию',
                    message: data,
                    buttons: {
                        'Разместить вакансию': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#vacancy-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.vacancy-list').length>0) {
                                            $.get('/client/vacancy/'+data.id+'/preview', function(data) {
                                                $('.vacancy-list').prepend(data);
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

        $(document).on('click', '.btn-vacancy-edit', function(e) {
            $.get('/client/vacancy/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить вакансию',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#vacancy-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/vacancy/'+data.id+'/preview';
                                        if ($('.vacancy-detail').length>0)
                                            url = '/client/vacancy/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.vacancy-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-vacancy-del', function(e) {
            bootbox.confirm('Удалить вакансию', function(result) {
                if (result) {
                    $.post('/client/vacancy/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.vacancy-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.vacancy-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
