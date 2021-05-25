function failFunction(e) {
    var data = jQuery.parseJSON(e.responseText);
    jQuery.notify(data.message);
}

(function($) {
    $(document).ready(function() {

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        };

        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            crossDomain: false, // obviates need for sameOrigin test
            beforeSend: function(xhr, settings) {
                //if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                //}
            }
        });

        $('.dropdown.auto').mouseenter(function(e) {
            $(this).addClass('open');
        });
        $('.dropdown.auto').mouseleave(function(e) {
            $(this).removeClass('open');
        });

        $('.dropdown .item').hover(function(e) {
            $(this).toggleClass('hover');
        });

        $('.dropdown.keep-open').on({
            "click":             function(e) {
                this.closable = $(e.target).parents('.dropdown-menu').length == 0;
            },
            "hide.bs.dropdown":  function() {
                return this.closable;
            }
        });

        $('[data-toggle="tooltip"]').tooltip();

        $('.colorbox').colorbox({
            scalePhotos: true,
            maxWidth: '100%',
            maxHeight: '100%',
            fixed: true
        });

        if (messages) {
            for (var i in messages) {
                jQuery.notify(messages[i]);
            }
        }

        $('.masked-phone').mask('+7(999) 999-9999');

        bootbox.setDefaults({
            locale: 'ru'
        });

        $("img.lazy").lazyload({
            effect : "fadeIn"
        });

        $.notifyDefaults({
            delay: 5000,
            animate: {
                enter: 'animated fadeInRight',
                exit: 'animated fadeOutRight'
            }
        });

        $('#scroll-up').click(function(e) {
            $('html, body').animate({ scrollTop: 0 }, "slow");
            e.preventDefault();
            return false;
        });

        window.onscroll = function() {
            var scrollup = $('#scroll-up');
            if (window.pageYOffset>250) {
                $(scrollup).removeClass('hidden');
            } else {
                $(scrollup).addClass('hidden');
            }
        }

    });
})(jQuery);
