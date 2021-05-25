(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-user-create', function(e) {
            $.get('/client/user/create', function(data){
                bootbox.dialog({
                    title: 'Создать пользователя',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#user-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/user/'+data.id+'/preview', function(data) {
                                            $('.user-list').prepend(data);
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

        $(document).on('click', '.btn-user-edit', function(e) {
            $.get('/client/user/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить пользователя',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#user-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/user/'+data.id+'/preview';
                                        if ($('.user-detail').length>0)
                                            url = '/client/user/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.user-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-user-del', function(e) {
            var name = $(this).data('name');
            bootbox.confirm('Удалить пользователя ' + name + '?', function(result) {
                if (result) {
                    $.post('/client/user/'+$(e.target).data('id')+'/del', function(data) {
                        $('.user-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.btn-user-create-by-user', function(e) {
            $.get('/client/company/user/create', function(data){
                bootbox.dialog({
                    title: 'Создать пользователя',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#user-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/user/'+data.id+'/preview', function(data) {
                                            $('.user-list').prepend(data);
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

        $(document).on('click', '.btn-user-edit-by-user', function(e) {
            $.get('/client/company/user/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить пользователя',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#user-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/user/'+data.id+'/preview';
                                        if ($('.user-detail').length>0)
                                            url = '/client/user/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.user-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-user-del-by-user', function(e) {
            var name = $(this).data('name');
            bootbox.confirm('Удалить пользователя ' + name + '?', function(result) {
                if (result) {
                    $.post('/client/company/user/'+$(e.target).data('id')+'/del', function(data) {
                        $('.user-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.show-user-tel', function(e){
            var id = $(this).data('id');
            $(this.parentNode).find('img').remove();
            $(this.parentNode).append('<img src="/phone/user?id='+id+'&hash='+Math.random().toString(10).substr(2)+'">');
            $(this).html('Обновить телефон');
            $(this).parents('.showtel').addClass('open');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.show-owner-tel', function(e){
            var id = $(this).data('id');
            $(this.parentNode).find('img').remove();
            $(this.parentNode).append('<img src="/phone/owner?id='+id+'&hash='+Math.random().toString(10).substr(2)+'">');
            $(this).html('Обновить телефон');
            $(this).parents('.showtel').addClass('open');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.show-owner-vk', function(e){
            var id = $(this).data('id');
            var btn = this;
            $(this.parentNode).find('img').remove();
            $(this.parentNode).find('.owner-vkid').remove();
            $(this.parentNode).append('<img src="/phone/ownervk?id='+id+'&hash='+Math.random().toString(10).substr(2)+'">');
            $.get('/phone/ownervkid?id='+id+'&hash='+Math.random().toString(10).substr(2), function(data){
                $(btn.parentNode).append(data);
            });
            $(this).html('Обновить контакты');
            $(this).parents('.showtel').addClass('open');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-user-perms-save', function(e) {
            $('#user-perms-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $('.bottom-left').notify({
                        message: { html: data.object.message },
                        closable: true
                    }).show();
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-user-status', function(e) {
            var name = $(this).data('name');
            var status = $(this).data('status');
            var status_text = '';
            if (status == 'a')
                status_text = 'Активный';
            if (status == 'm')
                status_text = 'На модерации';
            if (status == 'b')
                status_text = 'Заблокирован';
            bootbox.confirm('Установить статус агента '+name+' - '+status_text, function(result) {
                if (result) {
                    $.post('/client/user/'+$(e.target).data('id')+'/status?status='+status, function(data) {
                        var url = '/client/user/'+data.id+'/preview';
                        if ($('.user-detail').length>0)
                            url = '/client/user/'+data.id+'/detail';
                        $.get(url, function(preview) {
                            $('.user-item-'+data.id).replaceWith(preview);
                        });
                    }, 'json').fail(failFunction);
                }
            });
        });
    });
})(jQuery);
