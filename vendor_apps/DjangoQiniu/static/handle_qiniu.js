/**
 * Created by huang on 2017/5/11.
 */
function handle_qiniu(xtparams) {
    var qiniu_field_name = xtparams['qiniu_field_name'];
    var qiniu_domain = xtparams['qiniu_domain'];
    var uptoken_url = xtparams['uptoken_url'];
    var file_type = xtparams['file_type'];

    var progressBox = $('#'+qiniu_field_name+'_progress_box');
    var progressBar = progressBox.children(0);
    var uploadBtn = $('#'+qiniu_field_name+'_btn');

    var mime_types = [];
    if(file_type == 'full'){
        mime_types = [
            {title: 'Image files', extensions: 'jpg,gif,png'},
            {title: 'Video files', extensions: 'flv,mpg,mpeg,avi,wmv,mov,asf,rm,rmvb,mkv,m4v,mp4'}
        ]
    }else if(file_type == 'video'){
        mime_types = [{title: 'Video files', extensions: 'flv,mpg,mpeg,avi,wmv,mov,asf,rm,rmvb,mkv,m4v,mp4'}]
    }else{
        mime_types = [{title: 'Image files', extensions: 'jpg,gif,png'}]
    }

    var params = {
        browse_button: qiniu_field_name+'_btn',
        runtimes: 'html5,flash,html4', //上传模式，依次退化
        max_file_size: '500mb', //文件最大允许的尺寸
        dragdrop: false, //是否开启拖拽上传
        chunk_size: '4mb', //分块上传时，每片的大小
        uptoken_url: uptoken_url, //ajax请求token的url
        domain: qiniu_domain, //图片下载时候的域名
        get_new_uptoken: false, //是否每次上传文件都要从业务服务器获取token
        auto_start: true, //如果设置了true,只要选择了图片,就会自动上传
        unique_names: true,
        multi_selection: false,
        filters: {
            mime_types: mime_types
        },
        log_level: 0, //log级别
        init: {
            'FileUploaded': function (up, file, info) {
                var fileUrl = qiniu_domain + file.target_name;
                $('input[name='+qiniu_field_name+']').val(fileUrl);
                $('span.text-success').show();
                $('span.text-danger').hide();
            },
            'Error': function (up, err, errTip) {
                $('span.text-success').hide();
                $('span.text-danger').show();
                alert('七牛上传失败：'+errTip);
            },
            'UploadProgress': function (up, file) {
                var percent = file.percent;
                progressBar.attr('aria-valuenow',percent);
                progressBar.css('width',percent+'%');
                progressBar.text(percent+'%');
            },
            'FilesAdded': function (up, files) {
                progressBox.show();
                uploadBtn.button('loading');
            },
            'UploadComplete': function () {
                progressBox.hide();
                progressBar.attr('aria-valuenow',0);
                progressBar.css('width','0%');
                progressBar.text('0%');
                uploadBtn.button('reset');
            }
        }
    };
    var uploader = Qiniu.uploader(params);
    uploader.start();
}
