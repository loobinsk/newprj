(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-question-create', function(e) {
            $.get('/client/question/create', function(data){
                bootbox.dialog({
                    title: 'Создать вопрос',
                    message: data,
                    buttons: {
                        'Разместить вопрос': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#question-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.question-list').length>0) {
                                            $.get('/client/question/'+data.id+'/preview', function(data) {
                                                $('.question-list').prepend(data);
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

        $(document).on('click', '.btn-question-edit', function(e) {
            $.get('/client/question/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить вопрос',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#question-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/question/'+data.id+'/preview';
                                        if ($('.question-detail').length>0)
                                            url = '/client/question/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.question-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-question-del', function(e) {
            bootbox.confirm('Удалить вопрос', function(result) {
                if (result) {
                    $.post('/client/question/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.question-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.question-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.btn-faq', function(e) {
            $.get('/question/create', function(data){
                bootbox.dialog({
                    title: 'Задать вопрос',
                    message: data,
                    buttons: {
                        'Задать вопрос': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#question-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $('.bottom-left').notify({
                                            message: { html: data.object.message },
                                            closable: true
                                        }).show();
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
    });
})(jQuery);
