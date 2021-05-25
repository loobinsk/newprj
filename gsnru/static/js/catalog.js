(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: '<div class="icon"></div>' + data.message },
                closable: true,
                type: 'notice'
            }).show();
        }

        $(document).on('click', '.btn-catalog-create', function(e) {
            $.get('/client/catalog/create', function(data){
                bootbox.dialog({
                    title: 'Подать объявление',
                    message: data,
                    buttons: {
                        'Разместить объявление': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#catalog-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        if ($('body.client').length>0) {
                                            if ($('.catalog-list').length>0) {
                                                $.get('/client/catalog/'+data.id+'/preview', function(data) {
                                                    $('.catalog-list').prepend(data);
                                                });
                                            } else {
                                                window.location = data.object.url;
                                            }
                                        }
                                        $('.bottom-left').notify({
                                            message: { html: data.object.message },
                                            closable: true,
                                            fadeOut: { enabled: true, delay: 7000 }
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

        $(document).on('click', '.btn-catalog-edit', function(e) {
            $.get('/client/catalog/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить объявление',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#catalog-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/catalog/'+data.id+'/preview';
                                        if ($('.catalog-detail').length>0)
                                            url = '/client/catalog/'+data.id+'/detail';
                                        $.get(url, function(preview) {
                                            $('.catalog-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-catalog-del', function(e) {
            bootbox.confirm('Удалить объявление', function(result) {
                if (result) {
                    $.post('/client/catalog/'+$(e.target).data('id')+'/del', function(data) {
                        if ($('.catalog-detail').length>0)
                            window.location = data.object.url;
                        else
                            $('.catalog-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', 'body.catalog .numbers .pagination a', function(e){
            var href = $(this).attr('href');
            $('#content').addClass('loading').load(href, function(e){
                $(this).removeClass('loading');
                $('html, body').animate({ scrollTop: 0 }, "slow");
            });
            e.preventDefault();
            return false;
        });

        $('body.catalog #filter .btn-search').click(function(e){
            var content = $('#content');
            content.addClass('loading');
            showProgressBar(true);
            setProgressBar(30, null, 5000);
            $(this.form).ajaxSubmit({
                success: function(data) {
                    content.html(data);
                    content.removeClass('loading');
                    setProgressBar(100, function(){
                        showProgressBar(false);
                    });
                },
                error: failFunction
            });
            e.preventDefault();
            return false;
        });

        $('.catalog-filter form').on('reset', function(e){
            $('.catalog-filter .btn-group label').each(function(index, e){
                if (e.parentNode.getAttribute('id') != 'id_type2')
                    $(e).removeClass('active');
            });

            var inputs = $(this).find(":radio");
            inputs.each(function() {
                if (this.getAttribute('name') == 'type2')
                    $(this).data('value', $(this).is(':checked'));
                $(this).removeAttr('checked');
            });
            this.reset();
            inputs.each(function() {
                if (this.getAttribute('name') == 'type2')
                    $(this).attr('checked', $(this).data('value'));
            });
            $('.catalog-filter form .metro-list a').removeClass('active');
            $('.catalog-filter form .metro-map a').removeClass('active');
            $('.catalog-filter form .metro-dropdown button').html('Метро');
            $('.catalog-filter form .metro-dropdown .selected .item').remove();

            $('.catalog-filter form .select-dropdown .item').removeClass('active');
            $('.catalog-filter form .select-dropdown button').html('Выбрать <b class="caret"></b>');
        });

        $(document).on('click', '.btn-catalog-form-create', function(e) {
            $('#catalog-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.hideAll();
                    bootbox.alert(data.object.message, function(){
                        window.location.reload();
                    });
                },
                error: failFunction
            });
        });

        $(document).on('click', '.btn-catalog-form-edit', function(e) {
            $('#catalog-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.alert(data.object.message);
                },
                error: failFunction
            });
        });

        $(document).on('click', '.btn-catalog-show-desc', function(e){
            var parent = $(this.parentNode);
            if (parent.hasClass('open')) {
                parent.removeClass('open');
                $(this).html('Подробно');
            } else {
                parent.addClass('open');
                $(this).html('Скрыть');
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-show-metro', function(e){
            var parent = $(this.parentNode);
            if (parent.hasClass('open')) {
                parent.removeClass('open');
                $(this).html('Показать все...');
            } else {
                parent.addClass('open');
                $(this).html('Скрыть...');
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-add-favorite', function(e){
            var id = $(this).data('id');
            var btn = this;
            $.post('/client/catalog/fav', {'id': id}, function(data){
                if (data['result'])
                    $(btn).addClass('in');
                else
                    $(btn).removeClass('in');
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-load-images', function(e){
            var id = $(this).data('id');
            var target = $(this.parentNode).find('.dropdown-menu');
            if (target.find('.loading').length > 0)
                target.load('/client/catalog/'+id+'/img', function(){
                    target.find('.colorbox').colorbox({
                        scalePhotos: true,
                        maxWidth: '100%',
                        maxHeight: '100%',
                        fixed: true
                    });
                });
        });

        $(document).on('click', '.btn-load-images-vk', function(e){
            var id = $(this).data('id');
            var target = $(this.parentNode).find('.dropdown-menu');
            if (target.find('.loading').length > 0)
                target.load('/client/catalog/vk/'+id+'/img', function(){
                    target.find('.colorbox').colorbox({
                        scalePhotos: true,
                        maxWidth: '100%',
                        maxHeight: '100%',
                        fixed: true
                    });
                });
        });

        $(document).on('click', '.btn-catalog-buy', function(e) {
            var id = $(e.target).data('id');
            var btn = this;
            $.get('/client/catalog/buy', {id: id}, function(data){
                bootbox.dialog({
                    title: 'Выкупить объявление №' + id + '?',
                    message: data,
                    buttons: {
                        ok: {
                            label: 'Выкупить',
                            className: 'btn-primary',
                            callback: function() {
                                    $('#buy-form-'+id).ajaxSubmit({
                                        dataType: 'json',
                                        success:function(data) {
                                                    if (data.object.result) {
                                                        $('.bottom-left').notify({
                                                            message: { html: '<div class="icon"></div>' + data.object.message },
                                                            closable: true,
                                                            type: 'notice'
                                                        }).show();
                                                        $(btn.parentNode).append('<div class="buyed">Выкуплено</div>');
                                                        $(btn).remove();
                                                    } else {
                                                        $('.bottom-left').notify({
                                                            message: { html: '<div class="icon"></div>' + data.object.message },
                                                            closable: true,
                                                            type: 'notice'
                                                        }).show();
                                                    }
                                                },
                                        error: failFunction
                                    })
                                }
                            },
                        cancel: {
                            label: 'Отмена',
                            className: 'btn-default'
                        }
                    }
                });
            });

            e.preventDefault();
            return false;
        });

        $('#catalog-style-map').click(function(e){
            if ($('body.catalog #filter').length > 0) {
                $('#id_map').val('1');
                $('body.catalog #filter .btn-search').click();
                $(this).addClass('active');
                $('#catalog-style-list').removeClass('active');
                e.preventDefault();
                return false;
            }
        });

        $('#catalog-load-map').click(function(e){
            if ($('.catalog-filter form').length > 0) {
                $('#id_map').val('1');
                $('.view-on-map').find('a').addClass('hidden');
                $('.view-on-map').find('span').addClass('hidden');
                $('.view-on-map').css({height: 78, padding: 0}).animate({height: '0'}, function(){
                    $('.view-on-map').addClass('hidden');
                });
                $('#catalog-map').css('height', 1);
                $('#catalog-map').animate({height: 500}, function(){
                    if ($.trim($('#catalog-map').html()) == '') {
                        $('#catalog-map').append('<div class="loading"></div>');
                        $('.catalog-filter form').ajaxSubmit({
                            target: '#catalog-map'
                        });
                    }
                });
                e.preventDefault();
                return false;
            }
        });

        $(document).on('click', '.btn-close-map', function(e){
            $('#catalog-map').animate({height: 0});
            $('.view-on-map').removeClass('hidden').animate({height: 78}, function(){
                $('.view-on-map').css('padding', '25px');
                $('.view-on-map').find('a').removeClass('hidden');
                $('.view-on-map').find('span').removeClass('hidden');
            })
        });

        //$('.btn-address-map').click(function(e){
        //    if ($('.address-map').hasClass('hidden')) {
        //        var id = $(this).data('id');
        //        $('.address-map').css('height', 1).removeClass('hidden');
        //        $('.address-map').animate({height: 300}, function(){
        //            if ($.trim($('.address-map').html()) == '') {
        //                $('.address-map').append('<div class="loading"></div>').load('/catalog/'+id+'/map');
        //            }
        //        });
        //    } else {
        //        $('.address-map').animate({height:0}, function(){
        //            $('.address-map').addClass('hidden');
        //        });
        //    }
        //    e.preventDefault();
        //    return false;
        //});

        $(document).on('click', '.btn-address-map-client', function(e){
            var id = $(this).data('id');
            $(this.parentNode).find('.map').removeClass('hidden');
            if ($.trim($(this.parentNode).find('.map .content').html()) == '') {
                $(this.parentNode).find('.map .content').append('<div class="loading"></div>')
                    .load('/client/catalog/'+id+'/map');
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-address-map-close-client', function(e){
            $(this).parents('.map').addClass('hidden');
            e.preventDefault();
            return false;
        });

        $('#catalog-style-list').click(function(e){
            if ($('body.catalog #filter').length > 0) {
                $('#id_map').val('0');
                $('body.catalog #filter .btn-search').click();
                $(this).addClass('active');
                $('#catalog-style-map').removeClass('active');
                e.preventDefault();
                return false;
            }
        });

        $('.btn-catalog-send').click(function(e){
            var btn = this;
            $(btn).button('loading');
            $('#feedback-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    $('#feedback-form-result').html(data.object.message);
                    $(btn).button('reset');
                },
                error: function(e) {
                    failFunction(e);
                    $(btn).button('reset');
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-request', function(e) {
            var id = $(this).data('id');
            var request_url = '/catalog/request';
            if (id)
                request_url = request_url + '?id=' + id;
            $.get(request_url, function(data){
                bootbox.dialog({
                    title: 'Заявка специалисту',
                    message: data,
                    buttons: {
                        'Разместить заявку': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#catalog-request-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        bootbox.alert(data.object.message);
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

        $('.btn-request-remove').click(function(e){
            $('#request-remove-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.alert(data.object.message);
                    $('#request-remove-form')[0].reset();
                },
                error: function(e) {
                    failFunction(e);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-complain', function(e) {
            var id = $(e.target).data('id');
            var complain = $(e.target).text();
            var reason = $(e.target).data('reason');
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain + '?', function(result) {
                if (result) {
                    $.post('/catalog/'+id+'/complain',{complain: complain, reason:reason}, function(data) {
                        if (data.result) {
                            bootbox.alert(data.message);
                        } else {
                            $('.bottom-left').notify({
                                message: { html: data.message },
                                closable: true
                            }).show();
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
            bootbox.confirm('Пожаловаться на объявление №' + id + ': ' + complain + '?', function(result) {
                if (result) {
                    $.post('/client/catalog/vk/'+id+'/complain',{complain: complain, reason: reason}, function(data) {
                        if (data.result) {
                            $('.catalog-item-'+data.id).replaceWith('<tr class="catalog-hidden"><td colspan="9">Это объявление скрыто</td></tr>');
                            $('.bottom-left').notify({
                                message: { html: '<div class="icon"></div>' + data.message },
                                closable: true,
                                type: 'notice'
                            }).show();
                        } else {
                            $('.bottom-left').notify({
                                message: { html: '<div class="icon"></div>' + data.message },
                                closable: true,
                                type: 'notice'
                            }).show();
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-fold', function(e){
            var preview = $(this).parents('.catalog-preview');
            var id = $(this).data('id');
            if (preview.hasClass('fold')) {
                $(this).html('свернуть');
                $.post('/client/catalog/'+id+'/fold', {fold: false});
            } else {
                $(this).html('развернуть');
                $.post('/client/catalog/'+id+'/fold', {fold: true});
            }
            preview.toggleClass('fold');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-show-comments', function(e){
            var tr = $($(this).attr('href'));
            if (tr.hasClass('hidden')) {
                tr.find('.comments').css('display', 'none').slideDown(400);
                tr.removeClass('hidden');
            } else {
                tr.find('.comments').slideUp(400, function() {
                    tr.addClass('hidden');
                });
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-show-complains', function(e){
            var tr = $($(this).attr('href'));
            if (tr.hasClass('hidden')) {
                var complains = tr.find('.complains');
                if ($.trim(complains.html()) == '') {
                    complains.css('display', 'none').slideDown(400, function(){
                        complains.append('<div class="loading"></div>').load('/client/catalog/'+complains.data('id')+'/complains');
                    });
                } else {
                    complains.css('display', 'none').slideDown(400);
                }
                tr.removeClass('hidden');
            } else {
                tr.find('.complains').slideUp(400, function() {
                    tr.addClass('hidden');
                });
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-show-clients', function(e){
            var tr = $($(this).attr('href'));
            var col_price = $(this).parents('.col-price');
            if (tr.hasClass('hidden')) {
                var content = tr.find('.clients .tab-all');
                var clients = tr.find('.clients');
                if ($.trim(content.html()) == '') {
                    clients.css('display', 'none').slideDown(400, function(){
                        content.append('<div class="loading"></div>').load('/client/catalog/'+clients.data('id')+'/clients');
                    });
                } else {
                    clients.css('display', 'none').slideDown(400);
                }
                col_price.addClass('open');
                tr.removeClass('hidden');
            } else {
                tr.find('.clients').slideUp(400, function() {
                    tr.addClass('hidden');
                    col_price.removeClass('open');
                });
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.catalog-clients .nav-tabs a', function(e){
            var content = $(e.currentTarget.hash);
            if ($.trim(content.html()) == '') {
                var clients = $(e.currentTarget).parents('.clients');
                var owner = $(e.currentTarget).data('owner');
                content.append('<div class="loading"></div>').load('/client/catalog/'+clients.data('id')+'/clients?owner='+owner);
            }
        });

        $(document).on('click', '.btn-more-clients', function(e){
            var btn = this;
            $(btn).html('Загрузка...');
            var id = $(btn).data('id');
            var page = $(btn).data('page');
            var content = $(btn).parents('.tab-pane');
            var owner = $(btn).data('owner');
            $.get('/client/catalog/'+id+'/clients', {page: page, owner: owner}, function(data) {
                $(btn).remove();
                content.append(data);
            });

        });

        $(document).on('click', '.btn-catalog-approve', function(e) {
            var id = $(e.target).data('id');
            bootbox.confirm('Разместить объявление №' + id + '?', function(result) {
                if (result) {
                    $('#catalog-form').ajaxSubmit({
                        url: '/client/catalog/'+id+'/approve',
                        dataType: 'json',
                        success: function(data) {
                            bootbox.alert(data.object.message, function() {
                                window.location = data.object.url;
                            });
                        },
                        error: failFunction
                    });
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-is-agent', function(e) {
            var id = $(e.target).data('id');
            var input = $(this).data('input');
            var value = $('#'+input).val();
            bootbox.confirm('Пометить объявление №' + id + ' как агентское?', function(result) {
                if (result) {
                    $.post('/client/blacklist/addtel',{tel: value}, function(data) {
                        if (id) {
                            $.post('/client/catalog/'+id+'/is_agent', function(data) {
                                if (data.result) {
                                    bootbox.alert(data.message, function(){
                                        window.location = data.url;
                                    });
                                } else {
                                    $('.bottom-left').notify({
                                        message: { html: data.message },
                                        closable: true
                                    }).show();
                                }
                            }, 'json').fail(failFunction);
                        } else {
                            bootbox.alert(data.message, function(){
                                window.location.reload();
                            });
                        }
                    });
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-not-answer', function(e) {
            var id = $(e.target).data('id');
            bootbox.confirm('Отправить объявление №' + id + ' на модерацию и отметить что владелец не отвечает?', function(result) {
                if (result) {
                    $('#catalog-form').ajaxSubmit({
                        dataType: 'json',
                        data: {'not_answer': '1'},
                        success: function(data) {
                            bootbox.alert(data.object.message, function() {
                                window.location = data.object.url;
                            });
                        },
                        error: failFunction
                    });
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-irrelevant', function(e) {
            var id = $(e.target).data('id');

            bootbox.confirm('Отметить объявление №' + id + ' как неактуальное?', function(result) {
                if (result) {
                    if (id) {
                        $.post('/client/catalog/'+id+'/irrelevant', function(data) {
                            if (data.result) {
                                bootbox.alert(data.message, function() {
                                    window.location = data.url;
                                });
                            } else {
                                $('.bottom-left').notify({
                                    message: { html: data.message },
                                    closable: true
                                }).show();
                            }
                        }, 'json').fail(failFunction);
                    } else {
                        window.location.reload();
                    }
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-check', function(e) {
            var input = $(this).data('input');
            var value = $('#'+input).val();
            var advert_id = $(this.form).data('advert-id');
            $.get('/client/blacklist/check',{tel: value}, function(data){
                if (data.result) {
                    $('.bottom-left').notify({
                        message: { html: data.message },
                        closable: true
                    }).show();
                } else {
                    $('#catalog-form').ajaxSubmit({
                        url: '/client/catalog/duplicate',
                        data: {id: advert_id},
                        dataType: 'json',
                        success: function(data) {
                            if (data.result) {
                                if (data.exists) {
                                    $('.bottom-left').notify({
                                        message: { html: data.message },
                                        closable: true
                                    }).show();
                                } else {
                                    $('.bottom-left').notify({
                                        message: { html: '<div class="success-advert"><img src="/static/img/ok.png"><p>Совпадений с черным списком и дубликатов объявления не найдено</p>' },
                                        closable: true
                                    }).show();
                                }
                            } else {
                                $('.bottom-left').notify({
                                    message: { html: data.message },
                                    closable: true
                                }).show();
                            }
                        },
                        error: failFunction
                    });
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-to-archive', function(e){
            var id = $(this).data('id');
            var btn = this;
            $.post('/client/catalog/archive', {'id': id, 'archive': 1}, function(data){
                if (data['result']){
                    $(btn).removeClass('btn-catalog-to-archive').addClass('btn-catalog-from-archive').html('<span class="glyphicon glyphicon-trash" aria-hidden="true"></span> В архиве');
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-from-archive', function(e){
            var id = $(this).data('id');
            var btn = this;
            $.post('/client/catalog/archive', {'id': id, 'archive': 0}, function(data){
                if (data['result']) {
                    $(btn).removeClass('btn-catalog-from-archive').addClass('btn-catalog-to-archive').html('<span class="glyphicon glyphicon-ok" aria-hidden="true"></span> Актуально');
                    setBasketCount(data.basket_count);
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-catalog-next-page', function(e){
            $(this).html('Загружаем...');
            $.get(this.href, function(data){
                $('.ext-pagination').remove();
                var container = $('.catalog-col');
                if (!container.length) {
                    container = $('#content');
                }
                container.append(data);
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-vk-is-agent', function(e) {
            var id = $(e.target).data('id');
            bootbox.confirm('Пометить объявление №' + id + ' как агентское?', function(result) {
                if (result) {
                    $.post('/client/catalog/vk/'+id+'/is_agent', function(data) {
                        if (data.result) {
                            bootbox.alert(data.message);
                            $.get('/client/catalog/vk/'+data.id+'/preview', function(preview){
                                $('.catalog-item-'+data.id).replaceWith(preview);
                            });
                        } else {
                            $('.bottom-left').notify({
                                message: { html: data.message },
                                closable: true
                            }).show();
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-vk-irrelevant', function(e) {
            var id = $(e.target).data('id');
            bootbox.confirm('Отметить объявление №' + id + ' как неактуальное?', function(result) {
                if (result) {
                    $.post('/client/catalog/vk/'+id+'/irrelevant', function(data) {
                        if (data.result) {
                            bootbox.alert(data.message);
                            $.get('/client/catalog/vk/'+data.id+'/preview', function(preview){
                                $('.catalog-item-'+data.id).replaceWith(preview);
                            });
                        } else {
                            $('.bottom-left').notify({
                                message: { html: data.message },
                                closable: true
                            }).show();
                        }
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

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
                console.log(l);
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


        function showProgressBar(show) {
            if (show) {
                $('#progress-bar .bar').css('width', '0');
                $('#progress-bar').removeClass('hidden');
            } else {
                $('#progress-bar').addClass('hidden');
            }
        }

        function setProgressBar(percent, callback, delay) {
            if (!delay)
                delay = 400;
            jQuery('#progress-bar .bar').stop().animate({width: percent+'%'}, delay, callback);
        }
    });
})(jQuery);
