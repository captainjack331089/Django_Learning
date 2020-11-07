$(function () {

    var $username = $("#username_input");
    var $email = $("#email_input");

    $username.change(function () {
        var username = $username.val().trim();
        if (username.length) {
            // 将用户名发送给服务器进行预校验
            $.getJSON('/shoppingsite/checkuser/', {'username': username}, function (data) {
                console.log(data);
                var $username_info = $("#username_info");
                if (data['status'] === 200){
                    $username_info.html("用户名可用").css("color", 'green');
                }else if(data['status'] === 901){
                    $username_info.html("用户名已存在").css('color', 'red');
                }
            })
        }
    })

    $email.change(function () {
        var email = $email.val().trim();
        if (email.length) {
            // 将用户名发送给服务器进行预校验
            $.getJSON('/shoppingsite/checkemail/', {'email': email}, function (data) {
                console.log(data);
                var $email_info = $("#email_info");
                if (data['status'] === 200){
                    $email_info.html("邮箱可用").css("color", 'green');
                }else if(data['status'] === 902){
                    $email_info.html("邮箱已存在").css('color', 'red');
                }
            })
        }
    })

})
function check()  {
        var $username = $("#username_input");
        var $username = $username.val().trim();
        if (!$username){
            return false
        }

        var $email = $("#email_input");
        var $email = $email.val().trim();
        if (!$email){
            return false
        }

        var $password = $("#password_input");
        var $password = $password.val().trim();
        if (!$password){
            return false
        }
        
        var info_color1 = $("#username_info").css('color')
        var info_color2 = $("#email_info").css('color')
        if (info_color1 == 'rgb(255, 0, 0)') {
            return false
        }
        if (info_color2 == 'rgb(255, 0, 0)') {
            return false
        }
        return true
}



