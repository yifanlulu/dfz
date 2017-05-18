/**
 * gulp的主文件，用于注册任务
 */

'use strict';

var gulp = require('gulp');
// css前缀
var autoprefixer = require('gulp-autoprefixer');
// 拼接所有的js放在一个文件中
var concat = require('gulp-concat');
// 压缩css文件
var cssnano = require('gulp-cssnano');
// 压缩图片
var imagemin = require('gulp-imagemin');
// 图片缓存，只有图片修改了才压缩（因为图片比较大，如果没有修改也压缩，拖慢效率）
var cache = require('gulp-cache');
// 处理sass文件
var sass = require('gulp-sass');
// js代码优化工具
var uglify = require('gulp-uglify');
// 改变文件名
var rename = require('gulp-rename');
// html压缩
var htmlmin = require('gulp-htmlmin');
// source-map
var sourcemaps = require('gulp-sourcemaps');


const path = {
	html: 'src/tpl/*/',
	css: 'src/css/*/',
	js: 'src/js/',
	images: 'src/images/*/',
	font: 'src/fonts/',
	vendor: 'src/js/vendor/'
}


// 处理html文件
gulp.task('html',function(){
	gulp.src(path.html + '*.html')
	.pipe(htmlmin({
		collapseBooleanAttributes: true,
		removeComments: true,
		removeEmptyAttributes: true,
		removeScriptTypeAttributes: true,
		removeStyleLinkTypeAttributes: true
	}))
	.pipe(gulp.dest('build/tpl/'));
});

// 处理js脚本
gulp.task('script',function(){
	gulp.src(path.js + '*.js')
    .pipe(sourcemaps.init())
	.pipe(uglify())
	.pipe(rename({suffix:'.min'}))
    .pipe(sourcemaps.write())
	.pipe(gulp.dest('js/'));
});


// 处理第三方js库文件
gulp.task('vendorjs',function(){
	gulp.src([
		path.vendor + 'jquery.js',
		path.vendor + 'hyjquery.js',
		path.vendor + 'template.js'
	])
    .pipe(sourcemaps.init())
	.pipe(concat('vendor.min.js'))
	.pipe(uglify())
    .pipe(sourcemaps.write())
	.pipe(gulp.dest('js/vendor/'));
});

// 处理sass脚本
gulp.task('style',function(){
	gulp.src(path.css + '*.scss')
	.pipe(sass())
	.pipe(autoprefixer({
		browsers: ['last 2 versions']
	}))
	.pipe(cssnano())
	.pipe(rename({ suffix:'.min' }))
	.pipe(gulp.dest('css/'));
});

// 处理图片
gulp.task('image',function(){
	gulp.src(path.images + '/*.*')
	.pipe(cache(imagemin()))
	.pipe(gulp.dest('images/'));
});

// 处理字体
gulp.task('font',function(){
	gulp.src(path.font + '*.*')
	.pipe(gulp.dest('fonts/'));
});

// 监听
gulp.task('watch',function(){
	gulp.watch(path.html + '*.html',['html']);
	gulp.watch(path.js + '*.js',['script']);
	gulp.watch(path.css + '*.scss',['style']);
	gulp.watch(path.images + '*.*',['image']);
	gulp.watch(path.font + '*.*',['font']);
	gulp.watch(path.vendor + '*.js',['vendorjs']);
});

