function sendData() {
    let data = $("#quiz_form").serializeJSON();
    data["url"] = window.location.pathname; //add url to JS object.
    let api_endpoint = 'http://' + document.domain + ':' + location.port + '/api/get_quiz/quiz_result';
    $.ajax(
        {
            url: api_endpoint,
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            type: 'post',
            async: false,
            dataType: 'json',
            success: function (response) {
                if (response['message'] === 'no data') {
                    callFailureAlertify({"message": "Some fields are empty!"});
                } else {
                    callSuccessAlertify({"message": response['score'] + '% correct!'});
                }
            },
            error: function (data) {
                callFailureAlertify(data);
            }
        });
}