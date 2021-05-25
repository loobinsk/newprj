(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        function setBasketCount(c) {
            $('#basket-count').html(c);
        }

        //        авторизация
        $('form.agent24-form').ajaxForm({
            dataType: 'json',
            url: '/login/ajax',
            form: this,
            success: function(data, status, xhr, form) {
                if (data.success){
                    window.location = data.url;
                } else {
                    $(form).find('.output').removeClass('alert-success').addClass("alert alert-danger").html(data.message);
                    $(form).find('#id_access_code').popover({
                        content: data.message,
                        html: true,
                        placement: 'left',
                        title: 'Ошибка',
                        trigger: 'focus'
                    });
                    $(form).find('#id_access_code').popover('show');
                    $(form).find('.btn-login').button('reset');
                }
            },
            error: failFunction
        });


        $(document).on('click', '.btn-basket-add', function(e){
            var id = $(this).data('id');
            var btn = this;
            $.post('/client/catalog/basket/add', {'id': id}, function(data){
                if (data['result']){
                    $(btn).removeClass('btn-basket-add btn-default').addClass('btn-basket-del btn-danger').html('<span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> Убрать');
                    setBasketCount(data.basket_count);
                    $('.bottom-left').notify({
                        message: { html: data.message },
                        closable: true
                    }).show();
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-basket-del', function(e){
            var id = $(this).data('id');
            var btn = this;
            $.post('/client/catalog/basket/del', {'id': id}, function(data){
                if (data['result']) {
                    $(btn).removeClass('btn-basket-del btn-danger').addClass('btn-basket-add btn-default').html('<span class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> В корзину');
                    setBasketCount(data.basket_count);
                    $('.bottom-left').notify({
                        message: { html: data.message },
                        closable: true
                    }).show();
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-basket-clear', function(e){
            bootbox.confirm('Очистить корзину?', function(result) {
                if (result) {
                    $.post('/client/catalog/basket/clear', function (data) {
                        if (data['result']) {
                            $('.catalog-preview').remove();
                            setBasketCount(data.basket_count);
                            $('.bottom-left').notify({
                                message: {html: data.message},
                                closable: true
                            }).show();
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-basket-order', function(e) {
            $.get('/client/catalog/basket/order', function(data){
                bootbox.dialog({
                    title: 'Оформление заказа',
                    message: data,
                    buttons: {
                        'Отправить риелтору': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#client-request-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $('.catalog-preview').remove();
                                        setBasketCount(data.object.basket_count);
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

    });
})(jQuery);