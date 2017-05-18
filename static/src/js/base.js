/**
 * Created by huang on 2017/5/17.
 */
'use strict';

$(function () {
    var href = window.location.href;
    var topNav = $('.top-nav');
    var index = 0;
    if(href.indexOf('news') > 0){
        index = 0;
    }else if(href.indexOf('course') > 0){
        index = 1;
    }else if(href.indexOf('payinfo') > 0){
        index = 2;
    }else if(href.indexOf('search') > 0){
        index = 3;
    }else if(href.indexOf('account') > 0){
        index = -1;
    }

    if(index >= 0){
        topNav.children().eq(index).addClass('active').siblings().removeClass('active');
    }else{
        topNav.children().removeClass('active');
    }
});

// 图形验证码
$(function () {
    var captchaImg = $('.captcha-img');
    if(!captchaImg){
        return;
    }
    captchaImg.click(function (event) {
        // 重新设置一下这个url
        var oldSrcArray = $(this).attr('src').split('xx');
        var oldSrc = oldSrcArray[0];
        var rel = '';
        if(oldSrcArray.length > 1){
            rel = 'xx=' + Math.random()
        }else{
            rel = '?xx=' + Math.random()
        }
        var newSrc = oldSrc + rel;
        $(this).attr('src',newSrc);
    });
});
