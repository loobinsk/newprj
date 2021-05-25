(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true,
                type: 'notice'
            }).show();
        }

//        выбор города
        $('.choose-town').click(function(e){
           bootbox.dialog({
               message: $($('.choose-town-list')[0].parentNode).html(),
               title: 'Выберите город',
               cancel: {
                   label: "Закрыть"
               }
           });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.choose-town-list a', function(e){
            var id = $(e.currentTarget).data('id');
            $.cookie('town', id, {
                path: '/'
            });
            if ($('.page-catalog').length > 0 )
                $('#catalog-filter form').submit();
            else
                window.location.reload();
        });

//        авторизация
        $('form.login-form').ajaxForm({
            dataType: 'json',
            url: '/login/ajax',
            form: this,
            success: function(data, status, xhr, form) {
                if (data.success){
                    $(form).find('.name').html(data.username);
                    if (data.activated) {
                        $(form).find('.company').html(data.company);
                    } else {
                        $(form).find('.company').html(data.company + '<br><strong>Ваше агентство еще не прошло модерацию</strong>');
                    }

                    if (data.image) {
                        $(form).find('.avatar img').attr('src', data.image);
                    }
                    $(form).find('.on-anonymous').addClass('hidden');
                    $(form).find('.on-auth').removeClass('hidden');
                    window.location = '/client/news/';
                } else {
                    $(form).find('.output').removeClass('alert-success').addClass("alert alert-danger").html(data.message);
                    $(form).find('#id_username').popover({
                        content: data.message,
                        html: true,
                        placement: 'left',
                        title: 'Ошибка',
                        trigger: 'focus'
                    });
                    $(form).find('#id_username').popover('show');
                    $(form).find('.btn-login').button('reset');
                }
            },
            error: failFunction
        });

//        feedback
        $('.btn-feedback').click(function(e){
            var btn = this;
            $(btn).button('loading');
            $('#feedback-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.alert(data.object.message);
                    $(btn).button('reset');
                    $('#feedback-form')[0].reset();
                },
                error: function(e) {
                    failFunction(e);
                    $(btn).button('reset');
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-ask-manager', function(e) {
            $.get('/client/feedback', function(data){
                bootbox.dialog({
                    title: 'Отправить сообщение менеджеру',
                    message: data,
                    buttons: {
                        'Отправить сообщение': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#feedback-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        bootbox.hideAll();
                                        bootbox.alert(data.object.message);
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

        $('.btn-feedback-client').click(function(e){
            var btn = this;
            $(btn).button('loading');
            $('#feedback-form-block').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.alert(data.object.message);
                    $(btn).button('reset');
                    $('#feedback-form-block')[0].reset();
                },
                error: function(e) {
                    failFunction(e);
                    $(btn).button('reset');
                }
            });
            e.preventDefault();
            return false;
        });

//        reclame
        $('.btn-reclame').click(function(e){
            var btn = this;
            $(btn).button('loading');
            $('#reclame-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.alert(data.object.message);
                    $(btn).button('reset');
                    $('#reclame-form')[0].reset();
                },
                error: function(e) {
                    failFunction(e);
                    $(btn).button('reset');
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-agreement', function(e){
            var input = $(this).data('id');
            $.get('/agree', function(data){
                bootbox.dialog({
                    title: 'Условия работы сервиса заявок',
                    message: data,
                    buttons: {
                        'Принимаю': {
                            className: 'btn-primary',
                            callback: function() {
                                $(input).prop('checked', true);
                                return true;
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

        $(document).on('click', '.btn-agreement-big', function(e){
            var input = $(this).data('id');
            $.get('/agree-big', function(data){
                bootbox.dialog({
                    title: 'Условия работы сервиса заявок',
                    message: data,
                    buttons: {
                        'Принимаю': {
                            className: 'btn-primary',
                            callback: function() {
                                $(input).prop('checked', true);
                                return true;
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