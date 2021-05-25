#-*- coding: utf-8 -*-
from django_assets import Bundle, register

# JS

js_vashdom = Bundle('js/jquery.form.js',
            'js/jquery.easing.1.3.js',
            'js/jquery.cookie.js',
            'bootstrap/js/bootstrap.min.js',
            'js/bootbox.js',
            'js/bootstrap-notify.js',
            'js/jquery.lazyload.js',
            'uimg/js/uimg.js',
            'ufile/js/ufile.js',
            'uvideo/js/uvideo.js',
            'js/ucomment.js',
            'colorbox/jquery.colorbox-min.js',
            # 'js/typeahead.js',
            # 'js/handlebars.js',
            'js/jquery.mask.min.js',
            'bootstrapformhelpers/js/bootstrap-formhelpers.js',
            'js/bootstrap-datepicker.js',
            'js/bootstrap-datepicker.ru.js',
            'js/bootstrap-slider.js',
            'js/scripts.js',
            'js/vashdom.js',
            'js/news.js',
            filters='jsmin',
            output='packed/vashdom.js')

register('js_vashdom', js_vashdom)


# CSS

css_vashdom = Bundle('bootstrap/css/bootstrap.css',
                     'css/animate.css',
                     'colorbox/example1/colorbox.css',
                     'uimg/css/styles.css',
                     'ufile/css/styles.css',
                     'uvideo/css/styles.css',
                     'ucomment/css/styles.css',
                     'css/typeahead.js-bootstrap.css',
                     'bootstrapformhelpers/css/bootstrap-formhelpers.min.css',
                     'css/datepicker3.css',
                     'css/slider.css',
                    'css/vashdom.css',
                    filters='cssmin,cssrewrite',
                    output='packed/vashdom.css')

register('css_vashdom', css_vashdom)
