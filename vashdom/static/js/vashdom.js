(function($) {
    $(document).ready(function() {
        //multiple select
        function multipleSelectActivated(dropDownSelect, id) {
            var select = dropDownSelect.find('select');
            var values = select.val();
            if (!values)
                values = [];
            values.push(id);
            select.val(values);
            if (values.length) {
                var l = [];
                var options = select.find('option:checked');
                for (var i=0; i<options.length; i++)
                    l.push(options[i].text);
                dropDownSelect.find('button').html(l.join(', ') + '<b class="caret"></b>');
            } else
                dropDownSelect.find('button').html('Выбрать <b class="caret"></b>');

            dropDownSelect.find('.item-list a[data-value='+id+']').addClass('active');
        }

        function multipleSelectDeactivate(dropDownSelect, id) {
            var select = dropDownSelect.find('select');
            var values = select.val();
            if (!values)
                values = [];
            var pos = values.indexOf(id);
            if (pos>=0)
                values.splice(pos, 1);
            select.val(values);
            if (values.length) {
                var l = [];
                var options = select.find('option:checked');
                for (var i = 0; i < options.length; i++)
                    l.push(options[i].text);
                dropDownSelect.find('button').html(l.join(', ') + '<b class="caret"></b>');
            } else
                dropDownSelect.find('button').html('Выбрать <b class="caret"></b>');

            dropDownSelect.find('.item-list a[data-value='+id+']').removeClass('active');
        }

        $(document).on('click', '.select-dropdown .item-list .item', function(e){
            if ($(this).hasClass('active')) {
                multipleSelectDeactivate($(this).parents('.select-dropdown'), $(this).data('value').toString());
            } else {
                multipleSelectActivated($(this).parents('.select-dropdown'), $(this).data('value').toString());
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-next-page', function(e){
            $(this).html('Загружается...');
            $.get(this.href, function(data){
                $('.ext-pagination').remove();
                $('.ext-links').remove();
                var container = $('#content');
                container.append(data);
            });
            e.preventDefault();
            return false;
        });

        // $(document).on('click', '.choose-town-list a', function(e){
        //     var id = $(e.currentTarget).data('id');
        //     $.cookie('town', id, {
        //         path: '/'
        //     });
        //     window.location.href = '/' + $(e.currentTarget).data('slug') +'/arenda/';
        //     e.preventDefault();
        //     return false;
        // });

        $('#contacts-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                    jQuery.notify(data.object.message);
                    $('#contacts-form')[0].reset();
            },
            error: failFunction
        });

        $('#payment-fastorder-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                if (data.object.type == 'payment')
                    window.location = data.object.url;
                if (data.object.type == 'free') {
                    bootbox.hideAll();
                    bootbox.alert(data.object.message);
                }
            },
            error: failFunction
        });

        $('#payment-alert-form').ajaxForm({
            dataType: 'json',
            form: this,
            success: function(data, status, xhr, form) {
                    jQuery.notify(data.object.message);
                    $('#payment-alert-form')[0].reset();
            },
            error: failFunction
        });

        $(document).on('change', '.order-form #id_town', function(){
            var id = $('.order-form #id_town').val();
            if (id) {
                if (town_bases[id].main_base)
                    $('.order-form .need_main_base').removeClass('hidden');
                else
                    $('.order-form .need_main_base').addClass('hidden');

                if (town_bases[id].vk_base)
                    $('.order-form .need_vk_base').removeClass('hidden');
                else
                    $('.order-form .need_vk_base').addClass('hidden');

                if (town_bases[id].main_base && town_bases[id].vk_base)
                    $('.order-form .need_vk_base.need_main_base').removeClass('hidden');
                else
                    $('.order-form .need_vk_base.need_main_base').addClass('hidden');

                $('.order-form .city').addClass('city-hidden');
                $('.order-form .city-'+id).removeClass('city-hidden');
            }
        });

        $(document).on('click', '.btn-get-access', function(e){
            var id = $(this).data('id');
            var vk = $(this).hasClass('vk');
            $.get('/get-access', {id: id, vk: vk}, function(data){
                 bootbox.dialog({
                    title: 'Получить доступ',
                    message: data,
                    buttons: {
                        'Закрыть': {
                            className: 'btn-default'
                        }
                    }
                });
            });
        });

        $(document).on('click', '.btn-open-tel', function(e){
            var id = $(this).data('id');
            var password = $('#password').val();
            $('.password-tel').html('<img src="/phone?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2)+'">');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-open-vktel', function(e){
            var id = $(this).data('id');
            var password = $('#password').val();
            $('.password-tel').html('<img src="/vkphone?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2)+'">');
            $.get('/vkid?id='+id+'&password=' + password + '&hash='+Math.random().toString(10).substr(2), function(data){
                $('.password-vkid').html(data);
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-complain', function(e) {
            var id = $(e.target).data('id');
            var reason = $(this).data('reason');
            var complain = $(e.target).text();
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain, function(result) {
                if (result) {
                    $('#complain-dlg-'+id).modal('hide');
                    $('.modal-backdrop').remove();
                    $.post('/id'+id+'/complain',{complain: complain, reason:reason}, function(data) {
                        if (data.result) {
                            $('.catalog-item-'+data.id).replaceWith('<div class="catalog-hidden animated fadeIn">Это объявление скрыто</div>');
                            jQuery.notify(data.message);
                        } else {
                            jQuery.notify(data.message);
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-vkcomplain', function(e) {
            var id = $(e.target).data('id');
            var reason = $(this).data('reason');
            var complain = $(e.target).text();
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain, function(result) {
                if (result) {
                    $('#complain-dlg-'+id).modal('hide');
                    $('.modal-backdrop').remove();
                    $.post('/vkid'+id+'/complain',{complain: complain, reason: reason}, function(data) {
                        if (data.result) {
                            $('.catalog-item-'+data.id).replaceWith('<div class="catalog-hidden animated fadeIn">Это объявление скрыто</div>');
                            jQuery.notify(data.message);
                        } else {
                            jQuery.notify(data.message);
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-referral-create', function(e) {
            var user = $(this).data('user');
            bootbox.confirm('Получить реферальную ссылку', function(result) {
                if (result) {
                    $.post('/referral/create', function(data) {
                        if ($('.referral-list tbody').length == 0)
                            window.location.reload();
                        else
                            $('.referral-list tbody').prepend(data.preview);
                        $.notify('Ссылка получена');
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-sr-simple', function(e){
            var id = $(this).data('catalog');
            $.get('/search-request/simple/', {id: id}, function(data){
                 bootbox.dialog({
                    title: 'Подписаться на похожие объявления',
                    message: data,
                    buttons: {
                        'Подписаться': {
                            className: 'btn btn-primary',
                            callback: function(e) {
                                $('.bootbox .btn-primary').button('loading');
                                $('#sr-simple-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        bootbox.hideAll();
                                        bootbox.alert(data.object.message);
                                    },
                                    error: function(e) {
                                        $('.bootbox .btn-primary').button('reset');
                                        failFunction(e);
                                    }
                                });
                                return false;
                            }
                        },
                        'Закрыть': {
                            className: 'btn-default pull-left'
                        }
                    }
                });
            });
        });


        var lastPageYOffset = 0;
        window.onscroll = function() {
            var pageYOffset = 0;
            if (window.pageXOffset !== undefined)
                pageYOffset = window.pageYOffset;
            else
                pageYOffset = document.documentElement.scrollTop;
            if (pageYOffset > 145) {
                if (lastPageYOffset < pageYOffset)
                    $('.mainmenu').addClass('fixed animated slideInDown');
            } else {
                $('.mainmenu').removeClass('fixed animated slideInDown');
            }
            lastPageYOffset = pageYOffset;
        }

        $(document).on('click', '.vk-catalog-preview', function(e){
            var url = $(e.currentTarget).data('url');
            if(url != null) {
                window.location.href = url;
            } 
        });

        $(document).on('click', '.offcanvas__link_alltowns', function(e){
            $('.offcanvas__item_town.offcanvas__item_additional').addClass('visible');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.tariff-choose-btn', function(e){
            $(e.currentTarget).find('input[type="radio"]')[0].click();
            $('.tariff-choose-btn').removeClass('selected');
            $(e.currentTarget).addClass('selected');
        });

    });
})(jQuery);
