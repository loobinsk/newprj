#-*- coding: utf-8 -*-
from django_assets import Bundle, register

# JS
js_all = Bundle('js/jquery.form.js',
            'js/jquery.cookie.js',
            'bootstrap/js/bootstrap.min.js',
            'js/bootbox.js',
            'js/bootstrap-notify.js',
            'js/jquery.lazyload.js',
            'js/news.js',
            'js/town.js',
            'js/vacancy.js',
            'js/district.js',
            'js/metro.js',
            'js/catalog.js',
            'js/search-request.js',
            'js/client-request.js',
            'js/question.js',
            'js/user.js',
            'js/company.js',
            'js/blacklist.js',
            'js/tariff.js',
            'js/abbr.js',
            'js/service.js',
            'js/password.js',
            'js/promotion.js',
            'js/referral.js',
            'uimg/js/uimg.js',
            'ufile/js/ufile.js',
            'uvideo/js/uvideo.js',
            'ucomment/js/ucomment.js',
            'colorbox/jquery.colorbox-min.js',
            # 'ckeditor/ckeditor/ckeditor.js',
            'js/handlebars.js',
            'js/bloodhound.js',
            'js/jquery.mask.min.js',
            'bootstrapformhelpers/js/bootstrap-formhelpers.js',
            'js/bootstrap-datepicker.js',
            'js/bootstrap-datepicker.ru.js',
            'js/bootstrap-slider.js',
            'js/scripts.js',
            'js/gsn.js',
            filters='jsmin',
            output='packed/packed.js')

register('js_all', js_all)


# CSS

css_all = Bundle('bootstrap/css/bootstrap.css',
                 'css/bootstrap-notify.css',
                 'css/styles/alert-bangtidy.css',
                 'css/style.css',
                 'colorbox/example1/colorbox.css',
                 'uimg/css/styles.css',
                 'ufile/css/styles.css',
                 'uvideo/css/styles.css',
                 'ucomment/css/styles.css',
                 'bootstrapformhelpers/css/bootstrap-formhelpers.min.css',
                 'css/datepicker3.css',
                 'css/slider.css',
                 'css/animate.css',
                 filters='cssmin,cssrewrite',
                 output='packed/packed.css')

register('css_all', css_all)


css_public = Bundle('css/public.css',
                 filters='cssmin,cssrewrite',
                 output='packed/public.css')

register('css_public', css_public)

css_agent = Bundle('css/agent.css',
                    filters='cssmin,cssrewrite',
                    output='packed/agent.css')

register('css_agent', css_agent)


css_linkdomain = Bundle('css/public.css',
                        'css/linkdomain.css',
                 filters='cssmin,cssrewrite',
                 output='packed/linkdomain.css')

register('css_linkdomain', css_linkdomain)
