(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-metro-create', function(e) {
            var town = $(e.currentTarget).data('town')
            $.get('/client/metro/create?town='+town, function(data){
                bootbox.dialog({
                    title: 'Создать метро',
                    message: data,
                    buttons: {
                        'Создать': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#metro-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        $.get('/client/metro/'+data.id+'/preview', function(data) {
                                            $('.metro-list').prepend(data);
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

        $(document).on('click', '.btn-metro-edit', function(e) {
            $.get('/client/metro/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить метро',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#metro-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/metro/'+data.id+'/preview';
                                        $.get(url, function(preview) {
                                            $('.metro-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-metro-del', function(e) {
            bootbox.confirm('Удалить метро', function(result) {
                if (result) {
                    $.post('/client/metro/'+$(e.target).data('id')+'/del', function(data) {
                        $('.metro-item-'+data.id).remove();
                    }, 'json').fail(failFunction);
                }
            });
        });

        function selectMetro(dropDownMetro, id) {
            var select = dropDownMetro.find('select');
            var values = select.val();
            if (!values)
                values = [];
            values.push(id);
            select.val(values);
            if (values.length)
                dropDownMetro.find('button').html('Метро ('+values.length+')');
            else
                dropDownMetro.find('button').html('Метро');

            dropDownMetro.find('.metro-map a[data-value='+id+']').addClass('active');
            dropDownMetro.find('.metro-list a[data-value='+id+']').addClass('active');
            dropDownMetro.find('.selected').append('<div class="item" data-value="'+id+'">' + dropDownMetro.find('.metro-list a[data-value='+id+']')[0].text + '<span class="deselect">&times;</span></div>');

        }

        function deselectMetro(dropDownMetro, id) {
            var select = dropDownMetro.find('select');
            var values = select.val();
            if (!values)
                values = [];
            var pos = values.indexOf(id);
            if (pos>=0)
                values.splice(pos, 1);
            select.val(values);
            if (values.length)
                dropDownMetro.find('button').html('Метро ('+values.length+')');
            else
                dropDownMetro.find('button').html('Метро');

            dropDownMetro.find('.metro-map a[data-value='+id+']').removeClass('active');
            dropDownMetro.find('.metro-list a[data-value='+id+']').removeClass('active');
            dropDownMetro.find('.selected .item[data-value='+id+']').remove();
        }

        $(document).on('click', '.metro-dropdown .metro-list a', function(e){
            if ($(this).hasClass('active')) {
                deselectMetro($(this).parents('.metro-dropdown'), $(this).data('value').toString());
            } else {
                selectMetro($(this).parents('.metro-dropdown'), $(this).data('value').toString());
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.metro-dropdown .metro-map a', function(e){
            if ($(this).hasClass('active')) {
                deselectMetro($(this).parents('.metro-dropdown'), $(this).data('value').toString());
            } else {
                selectMetro($(this).parents('.metro-dropdown'), $(this).data('value').toString());
            }
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.metro-dropdown .close', function(e){
            $(this).parents('.metro-dropdown').removeClass('open');
            jQuery(this).parents('.modal').removeClass('metro-open');
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.metro-dropdown .clearmap', function(e){
            var dropdownMetro = $(this).parents('.metro-dropdown');
            dropdownMetro.find('.metro-list a').removeClass('active');
            dropdownMetro.find('.metro-map a').removeClass('active');
            dropdownMetro.find('button').html('Метро');
            dropdownMetro.find('.selected .item').remove();
            dropdownMetro.find('select').val([]);
            e.preventDefault();
            return false;
        });

        $(document).on('click', '.metro-dropdown .deselect', function(e){
            deselectMetro($(this).parents('.metro-dropdown'), $(this.parentNode).data('value').toString());
            e.preventDefault();
            return false;
        });

        metromap_is_move = false;
        metromap_coord = [0, 0];

        $(document).on('mousedown', '.metro-map .move', function(e) {
            metromap_is_move = true;
            metromap_coord = [e.screenX, e.screenY];
            e.preventDefault();
            return false;
        });

        $(document).on('mouseup', '.metro-map .move', function(e) {
            metromap_is_move = false;
            e.preventDefault();
            return false;
        });

        $(document).on('mouseleave', '.metro-map .move', function(e) {
            metromap_is_move = false;
            return false;
        });

        $(document).on('mousemove', '.metro-map .move', function(e) {
            if (metromap_is_move) {
                var newLeft = e.currentTarget.offsetLeft+e.screenX-metromap_coord[0];
                var newTop = e.currentTarget.offsetTop+e.screenY-metromap_coord[1];
//                if (newLeft>20) newLeft=20;
//                if (newTop>20) newTop=20;
//                var map = $('.metro-map')[0];
//                if (newLeft+e.currentTarget.clientWidth<map.clientWidth) newLeft = map.clientWidth-e.currentTarget.clientWidth;
//                if (newTop+e.currentTarget.clientHeight<map.clientHeight) newTop = map.clientHeight-e.currentTarget.clientHeight;
                $(e.currentTarget).css({
                    top: newTop,
                    left: newLeft
                });
                metromap_coord = [e.screenX, e.screenY];
            }
            e.preventDefault();
            return false;
        });

        $(document).on('keyup', '.metro-filter', function(e) {
            var text = $(this).val().toLowerCase();
            $(this).parents('.metro-dropdown').find('.metro-list a').each(function(index, value){
                if (value.text.toLowerCase().indexOf(text)>-1) {
                    $(value).removeClass('hidden');
                } else {
                    $(value).addClass('hidden');
                }
            });
        });

    });
})(jQuery);
