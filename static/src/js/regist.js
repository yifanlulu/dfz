/**
 * Created by huang on 2017/5/18.
 */

// 点击发送短信验证码执行事件
$(function () {
    $('.captcha-btn').click(function (event) {
        event.preventDefault();
        var self = $(this);
        var dangerText = $('.danger-text');
        var telephone = $("input[name='telephone']").val();
        if(!telephone || telephone.length != 11){
            dangerText.text('请填入正确的手机号码！');
            dangerText.parent().show();
        }
        // 发送ajax请求
        $.hyget({
            'url': '/account/sms_captcha/',
            'data': {
                'telephone': telephone
            },
            'success': function (result) {
                if(result['code'] == 200){
                    // 倒计时
                    self.addClass('disabled-captcha-btn');
                    self.text('60');
                    var count = 60;
                    var timer = setInterval(function () {
                        count--;
                        if(count <= 0){
                            clearInterval(timer);
                            self.removeClass('disabled-captcha-btn');
                            self.text('发送验证码');
                        }
                    },1000);
                }else{
                    dangerText.text(result['message']);
                    dangerText.parent().show();
                }
            }
        });
    });
});

// 注册按钮执行事件
$(function () {
    $("#submit-btn").click(function (event) {
        event.preventDefault();
        var dangerText = $('.danger-text');

        // 获取各个标签
        var telephoneInput = $("input[name='telephone']");
        var usernameInput = $("input[name='username']");
        var graphCaptchaInput = $("input[name='graph-captcha']");
        var password1Input = $("input[name='password1']");
        var password2Input = $("input[name='password2']");
        var smsCaptchaInput = $("input[name='sms-captcha']");
        
        var telephone = telephoneInput.val();
        var graphCaptcha = graphCaptchaInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        var smsCaptcha = smsCaptchaInput.val();
        var username = usernameInput.val();
        
        // 发送请求
        $.hypost({
            'url': '/account/regist/',
            'data': {
                'telephone': telephone,
                'graph_captcha': graphCaptcha,
                'password1': password1,
                'password2': password2,
                'sms_captcha': smsCaptcha,
                'username': username
            },
            'success': function (result) {
                if(result['code'] == 200){
                    // 跳转到首页
                    window.location = '/';
                }else{
                    dangerText.text(result['message']);
                    dangerText.parent().show();
                }
            },
            'error': function (err) {
                console.log(err);
            }
        });
    });
});
