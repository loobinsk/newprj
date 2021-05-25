gulp = require('gulp')
less = require('gulp-less')
concat = require('gulp-concat')
cssmin = require('gulp-cssmin')
uglify = require('gulp-uglify')
series = require('stream-series')
livereload = require('gulp-livereload')
autoprefixer = require('gulp-autoprefixer')
cleancss = require('gulp-clean-css')

cssStream = ()->
    gulp.src([
        # 'static/bootstrap/css/bootstrap.css'
        'static/css/bootstrap-notify.css'
        'static/css/styles/alert-bangtidy.css',
#        'static/css/animate.css'
        'static/colorbox/example1/colorbox.css'
        'static/uimg/css/styles.css'
        'static/ufile/css/styles.css'
        'static/uvideo/css/styles.css'
        'static/ucomment/css/styles.css'
        'static/css/typeahead.js-bootstrap.css',
        'static/bootstrapformhelpers/css/bootstrap-formhelpers.css'
        'static/css/datepicker3.css'
        'static/css/slider.css',
        'node_modules/font-awesome/css/font-awesome.css'
    ])

lessStream = ()->
    gulp.src([
        'static/css/bootstrap.less'
        'static/css/vashdom.less'
        'static/css/block/**/*.less'
    ])
    .pipe less()
    .pipe(autoprefixer())
    .on('error', console.log)

jsStream = ()->
    gulp.src [
        'static/js/jquery-2.0.3.min.js'
        'static/js/jquery.form.js',
        'static/js/jquery.easing.1.3.js',
        'static/js/jquery.cookie.js',
        'static/bootstrap/js/bootstrap.js',
        'static/js/bootbox.js',
        'static/js/bootstrap-notify.js',
        'static/js/jquery.lazyload.js',
        'static/uimg/js/uimg.js',
        'static/ufile/js/ufile.js',
        'static/uvideo/js/uvideo.js',
        'static/js/ucomment.js',
        'static/colorbox/jquery.colorbox.js',
        # 'js/typeahead.js',
        # 'js/handlebars.js',
        'static/js/jquery.mask.min.js',
        'static/bootstrapformhelpers/js/bootstrap-formhelpers.js',
        'static/js/bootstrap-datepicker.js',
        'static/js/bootstrap-datepicker.ru.js',
        'static/js/bootstrap-slider.js',
        'static/js/scripts.js',
        'static/js/vashdom.js',
        'static/js/news.js',
        'static/js/offcanvas.js',
        'static/js/offcanvas-filter.js'
    ]

gulp.task 'css', ()->
    series(cssStream(), lessStream())
        .pipe concat('styles.css')
        .pipe cleancss()
        .pipe gulp.dest('static/packed')
        .pipe livereload()


gulp.task 'css-build', ()->
    series(cssStream(), lessStream())
        .pipe concat('styles.min.css')
        .pipe cleancss()
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