$(document).ready(function () {
    $("#username").keyup(function () {
        let data = $("#register_form").serializeArray();
        console.log(data[0].value);  // '0' is username.
        let api_endpoint = 'http://' + document.domain + ':' + location.port + '/api/validation/validate_user';
        $.ajax(
            {
                url: api_endpoint,
                data: JSON.stringify(data[0].value),
                contentType: 'application/json;charset=UTF-8',
                type: 'post',
                async: false,
                dataType: 'json',
                success: function (response) {
                    console.log(response);
                    if (response.message === 'username is available') {
                        $('#username').attr('class', 'form-control is-valid');
                        $('#usernameIsFree').show();
                        $('#usernameIsBusy').hide();
                    } else if (response.message === 'username is already in use') {
                        $('#username').attr('class', 'form-control is-invalid');
                        $('#usernameIsFree').hide();
                        $('#usernameIsBusy').show();
                    }
                },
                error: function (data) {
                    callFailureAlertify(data);
                }

            });
    });
    $("#email").keyup(function () {
        let data = $("#register_form").serializeArray();
        console.log(data[3].value);  // '3' is email.
        let api_endpoint = 'http://' + document.domain + ':' + location.port + '/api/validation/validate_email';
        $.ajax(
            {
                url: api_endpoint,
                data: JSON.stringify(data[3].value),
                contentType: 'application/json;charset=UTF-8',
                type: 'post',
                async: false,
                dataType: 'json',
                success: function (response) {
                    console.log(response);
                    if (response.message === 'email is available') {
                        $('#email').attr('class', 'form-control is-valid');
                        $('#emailIsFree').show();
                        $('#emailIsBusy').hide();
                    } else if (response.message === 'email is already in use') {
                        $('#email').attr('class', 'form-control is-invalid');
                        $('#emailIsFree').hide();
                        $('#emailIsBusy').show();
                    }
                },
                error: function (data) {
                    callFailureAlertify(data);
                }
            });
    });

    $("#repeat_password").keyup(function () {
        let password = $("#password").val();
        let confirmPassword = $("#repeat_password").val();

        if (password !== confirmPassword)
            $("#passwordsNotMatch").show();
        else
            $("#passwordsNotMatch").hide();
    });

});