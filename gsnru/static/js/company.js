(function($) {
    $(document).ready(function() {

        function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

        $(document).on('click', '.btn-company-edit', function(e) {
            $.get('/client/company/'+$(e.target).data('id')+'/edit', function(data){
                bootbox.dialog({
                    title: 'Изменить информацию агентства',
                    message: data,
                    buttons: {
                        'Сохранить': {
                            className: 'btn-primary',
                            callback: function() {
                                $('#company-form').ajaxSubmit({
                                    dataType: 'json',
                                    success: function(data) {
                                        var url = '/client/company/'+data.id+'/preview';
                                        if ($('.company-detail').length>0)
                                            url = '/client/company/'+data.id+'/detail';
                                        if ($('.my-company').length>0)
                                            url = '/client/company/my';
                                        $.get(url, function(preview) {
                                            $('.company-item-'+data.id).replaceWith(preview);
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

        $(document).on('click', '.btn-company-status', function(e) {
            var name = $(this).data('name');
            var status = $(this).data('status');
            var status_text = '';
            if (status == 'a')
                status_text = 'Активный';
            if (status == 'm')
                status_text = 'На модерации';
            if (status == 'b')
                status_text = 'Заблокирован';
            bootbox.confirm('Установить статус агентства '+name+' - '+status_text, function(result) {
                if (result) {
                    $.post('/client/company/'+$(e.target).data('id')+'/status?status='+status, function(data) {
                        var url = '/client/company/'+data.id+'/preview';
                        if ($('.company-detail').length>0)
                            url = '/client/company/'+data.id+'/detail';
                        $.get(url, function(preview) {
                            $('.company-item-'+data.id).replaceWith(preview);
                        });
                    }, 'json').fail(failFunction);
                }
            });
        });

        $(document).on('click', '.show-company-tel', function(e){
            var id = $(this).data('id');
            $(this.parentNode).append('<img src="/phone/company?id='+id+'">');
            $(this).remove();
            e.preventDefault();
            return false;
        });

    });
})(jQuery);
