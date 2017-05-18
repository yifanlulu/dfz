
'use strict';

// banner事件 
$(function(){
	var banner = $('#banner');
    var preBtn = $('.pre-arrow-btn');
    var nextBtn = $(".next-arrow-btn");
    var pageControl = $('.page-control-group > ul');
    var bannerWidth = banner.width();
    var itemWidth = bannerWidth / 4;

    function updateBannerLeft(left){
    	var left = parseInt(left);
    	banner.animate({'left':left},500);
    	// 算出是第几张
		var index = Math.ceil(Math.abs(left/itemWidth));
		pageControl.children().eq(index).addClass('active').siblings().removeClass('active');
	}

    function startTimer(){
        var timer = setInterval(function () {
            var currentLeft = parseInt(banner.css('left'));
            if(currentLeft > itemWidth - bannerWidth){
                updateBannerLeft(currentLeft-itemWidth);
            }else{
                updateBannerLeft(0);
            }
        },4000);
        return timer;
	}

	var timer = startTimer();

	banner.mouseenter(function (event) {
		clearInterval(timer);
    });

	banner.mouseleave(function(event){
		timer = startTimer();
	});

	preBtn.click(function (event) {
		clearInterval(timer);
		var currentLeft = parseInt(banner.css('left'));
		if(currentLeft < 0){
            updateBannerLeft(currentLeft+itemWidth);
		}else{
			updateBannerLeft(itemWidth - bannerWidth);
		}
    });

	nextBtn.click(function(event){
        clearInterval(timer);
        var currentLeft = parseInt(banner.css('left'));
        if(currentLeft > itemWidth - bannerWidth){
            updateBannerLeft(currentLeft-itemWidth);
        }else{
            updateBannerLeft(0);
		}
	});

	pageControl.children().each(function (idx,obj) {
		(function (index,obj) {
            $(obj).click(function (event) {
                clearInterval(timer);
                var left = -index * itemWidth;
                updateBannerLeft(left);
            });
        })(idx,obj);
    });
});


// 点击加载更多事件
$(function () {
    $('#load-more-btn').click(function (event) {
        event.preventDefault();
        $.hyget({
            url: '/news/list/',
            data: {
                'p': 0,
                'c': 0
            },
            success: function(result){
                console.log(result);
            },
            error: function (err) {
                console.log(err);
            },
            complete: function () {
                console.log('complete');
            }
        });
    });
});
