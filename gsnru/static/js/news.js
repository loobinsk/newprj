(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-news-create-client', function(e) {
            $.get('/client/news/create', function(data){
                bootbox.dialog({
                    title: 'Написать новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Разместить новость': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.news-list').length>0) {
                                            $.get('/client/news/'+data.id+'/preview', function(data) {
                                                $('.news-list').prepend(data);
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

        $(document).on('click', '.btn-news-create', function(e) {
            $.get('/news/create', function(data){
                bootbox.dialog({
                    title: 'Написать новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Разместить новость': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('.news-list').length>0) {
                                            $.get('/news/'+data.id+'/preview', function(data) {
                                                $('.news-list').prepend(data);
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

        $(document).on('click', '.btn-news-edit-client', function(e) {
            $.get('/client/news/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/news/'+data.id+'/preview';
                                        if ($('.news-detail').length>0)
                                            url = '/client/news/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.news-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-news-edit', function(e) {
            $.get('/news/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить новость',
                    message: data,
                    size: 'large',
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                CKEDITOR.instances['id_body'].updateElement();
                                $('#news-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/news/'+data.id+'/preview';
                                        if ($('.news-detail').length>0)
                                            url = '/news/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.news-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-news-del-client', function(e) {
            bootbox.confirm('Удалить новость', function(result) {
                if (result) {
                    $.post('/client/news/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.news-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.news-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.btn-news-del', function(e) {
            bootbox.confirm('Удалить новость', function(result) {
                if (result) {
                    $.post('/news/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.news-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.news-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
