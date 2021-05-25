(function($) {

    var comet_client_id = '';
    var comet_key = '';

    function failFunction(e) {
            var data = jQuery.parseJSON(e.responseText);
            $('.bottom-left').notify({
                message: { html: data.message },
                closable: true
            }).show();
        }

    function createCometClient() {
        $.get('/comet/client', function(data){
            comet_client_id = data.client_id;
            comet_key = data.key;
            Shaveet.init(comet_client_id, comet_key);

            Shaveet.listenSingle('notice-'+comet_client_id, function(msg){
                data = jQuery.parseJSON(msg.payload_raw);
                if ('msg' in data) {
                    var icon_html = '<div class="icon"></div>';
                    if ('icon' in data)
                        icon_html = '<div class="icon custom"><img src="'+data.icon+'"></div>';
                    var title_html = '<h2>Уведомление</h2>';
                    if ('title' in data)
                        title_html = '<h2>' + data.title + '</h2>';
                    $('.bottom-left').notify({
                        message: {html: icon_html + title_html + data.msg},
                        closable: true,
                        fadeOut: {enabled: false},
                        type: 'notice'
                    }).show();
                }
            });
        });
    }

    createCometClient();

})(jQuery);
