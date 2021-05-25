gulp = require('gulp')
less = require('gulp-less')
concat = require('gulp-concat')
cssmin = require('gulp-cssmin')
uglify = require('gulp-uglify')
series = require('stream-series')
livereload = require('gulp-livereload')

cssStream = ()->
    gulp.src([
        'static/bootstrap/css/bootstrap.css',
        'static/css/bootstrap-notify.css',
        'static/css/styles/alert-bangtidy.css',
        'static/css/style.css',
        'static/colorbox/example1/colorbox.css',
        'static/uimg/css/styles.css',
        'static/ufile/css/styles.css',
        'static/uvideo/css/styles.css',
        'static/ucomment/css/styles.css',
        'static/bootstrapformhelpers/css/bootstrap-formhelpers.min.css',
        'static/css/datepicker3.css',
        'static/css/slider.css',
        'static/css/animate.css',
    ])

lessStream = ()->
    gulp.src([
        'static/css/agent.less'
        # 'static/css/agent24.less'
        # 'static/css/linkdomain.less'
        # 'static/css/public.less'
        'static/css/style.less'
    ])
    .pipe less()
    .on('error', console.log)

jsStream = ()->
    gulp.src [
        'static/js/jquery-2.0.3.min.js',
        'static/js/jquery.form.js',
        'static/js/jquery.cookie.js',
        'static/bootstrap/js/bootstrap.min.js',
        'static/js/bootbox.js',
        'static/js/bootstrap-notify.js',
        'static/js/jquery.lazyload.js',
        'static/js/news.js',
        'static/js/town.js',
        'static/js/vacancy.js',
        'static/js/district.js',
        'static/js/metro.js',
        'static/js/catalog.js',
        'static/js/search-request.js',
        'vjs/client-request.js',
        'static/js/question.js',
        'static/js/user.js',
        'static/js/company.js',
        'static/js/blacklist.js',
        'static/js/tariff.js',
        'static/js/abbr.js',
        'static/js/service.js',
        'static/js/password.js',
        'static/js/promotion.js',
        'static/js/referral.js',
        'static/uimg/js/uimg.js',
        'static/ufile/js/ufile.js',
        'static/uvideo/js/uvideo.js',
        'static/ucomment/js/ucomment.js',
        'static/colorbox/jquery.colorbox-min.js',
        # 'ckeditor/ckeditor/ckeditor.js',
        'static/js/handlebars.js',
        'static/js/bloodhound.js',
        'static/js/jquery.mask.min.js',
        'static/bootstrapformhelpers/js/bootstrap-formhelpers.js',
        'static/js/bootstrap-datepicker.js',
        'static/js/bootstrap-datepicker.ru.js',
        'static/js/bootstrap-slider.js',
        'static/js/scripts.js',
        'static/js/gsn.js',
    ]

gulp.task 'css', ()->
    series(cssStream(), lessStream())
        .pipe concat('styles.css')
        .pipe gulp.dest('static/packed')
        .pipe livereload()


gulp.task 'css-build', ()->
    series(cssStream(), lessStream())
        .pipe concat('styles.min.css')
        # .pipe cssmin()
        .pipe gulp.dest('static/packed')

gulp.task 'js', ()->
    jsStream()
        .pipe concat('scripts.js')
        .pipe gulp.dest('static/packed')
        .pipe livereload()

gulp.task 'js-build', ()->
    jsStream()
        .pipe concat('scripts.min.js')
        .pipe uglify(mangle: false)
        .pipe gulp.dest('static/packed')

gulp.task 'watch', ['css', 'js'], ()->
    livereload.listen()
    gulp.watch ['static/css/**/*.css', 'static/css/**/*.less'], ['css']
    gulp.watch ['static/js/**/*.js'], ['js']


gulp.task 'build', ['css-build','js-build']