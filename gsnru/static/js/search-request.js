(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-search-request-form-create', function(e) {
            $('#catalog-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    bootbox.hideAll();
                    window.location = data.object.url;
                },
                error: failFunction
            });
        });

        $(document).on('click', '.btn-search-request-form-edit', function(e) {
            $('#catalog-form').ajaxSubmit({
                dataType: 'json',
                success: function(data) {
                    window.location = data.object.url;
                },
                error: failFunction
            });
        });

        $(document).on('click', '.btn-search-request-del', function(e) {
            bootbox.confirm('Удалить заявку', function(result) {
                if (result) {
                    $.post('/client/search-request/'+$(e.target).data('id')+'/del', function(data) {
                        $('.request-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-search-request-start', function(e) {
            bootbox.confirm('Запустить поиск по заявке', function(result) {
                if (result) {
                    $.post('/client/search-request/'+$(e.target).data('id')+'/start', function(data) {
                        $.get('/client/search-request/'+data.id+'/preview', function(preview) {
                            $('.request-item-'+data.id).replaceWith(preview);
                        });
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-search-request-stop', function(e) {
            bootbox.confirm('Остановить поиск по заявке', function(result) {
                if (result) {
                    $.post('/client/search-request/'+$(e.target).data('id')+'/stop', function(data) {
                        $.get('/client/search-request/'+data.id+'/preview', function(preview) {
                            $('.request-item-'+data.id).replaceWith(preview);
                        });
                    }, 'json').fail(failFunction);
                }
            });
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-show-request-clients', function(e){
            var tr = $($(this).attr('href'));
            var col_price = $(this).parents('.col-price');
            if (tr.hasClass('hidden')) {
                var content = tr.find('.clients');
                if (content.html() == '') {
                    content.css('display', 'none').append('<div class="loading"></div>').slideDown(400, function(){
                        content.load('/client/search-request/'+content.data('id')+'/clients');
                    });
                } else {
                    content.css('display', 'none').slideDown(400);
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

        $(document).on('click', '.btn-search-request-not-send', function(e) {
            $.post('/client/search-request/'+$(e.target).data('sr')+'/not-send', {id: $(e.target).data('id')}, function(data) {
                if (data.result) {
                    $(e.target).removeClass('btn-search-request-not-send').addClass('btn-search-request-do-send');
                    $(e.target).html('<span class="glyphicon glyphicon-ban-circle text-danger" aria-hidden="true"></span> Рассылка выкл.')
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.btn-search-request-do-send', function(e) {
            $.post('/client/search-request/'+$(e.target).data('sr')+'/do-send', {id: $(e.target).data('id')}, function(data) {
                if (data.result) {
                    $(e.target).removeClass('btn-search-request-do-send').addClass('btn-search-request-not-send');
                    $(e.target).html('<span class="glyphicon glyphicon-ok-circle text-success" aria-hidden="true"></span> Рассылка вкл.')
                }
            }, 'json').fail(failFunction);
            e.preventDefault();
            return false;
        });

    });
})(jQuery);