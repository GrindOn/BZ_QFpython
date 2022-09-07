
$(function () {
    //设置富文本
    tinymce.init({
        selector: '.mytextarea',
        height: 400,
        plugins: "quickbars emoticons",
        inline: false,
        toolbar: true,
        menubar: true,
        quickbars_selection_toolbar: 'bold italic | link h2 h3 blockquote',
        quickbars_insert_toolbar: 'quickimage quicktable',

    });
    //验证手机号码
    $('#InputPhone').blur(function () {
        let phone = $(this).val();
        let span_ele = $(this).next('span');
        if (phone.length == 11) {
            span_ele.text('');
            $.get('/user/checkphone', {phone: phone}, function (data) {
                // {#console.log(data);#}
                if (data.code != 200) {
                    span_ele.css({"color": "#ff0011", "font-size": "12px"});
                    span_ele.text(data.msg);
                }
            }
        )
        } else {
            span_ele.css({"color": "#ff0011", "font-size": "12px"});
            span_ele.text('手机格式错误');
        }

    });
    $('.right1').hide();
    $('.right1').eq(0).show();
    $("#left p").first().css({'background-color': 'rgba(30, 150, 196, 0.94)'});
    //切换右侧div
    $("#left p").each(function (i) {
        $(this).click(function () {
            $("#left p").css({'background-color': 'rgba(30, 150, 196, 0.94)'});
            $(this).css({'background-color': 'skyblue', 'box-shadow': '5px 5px 5px deepskyblue'});
            $('.right1').hide();
            $('.right1').eq(i).show();
        });
    });

})
