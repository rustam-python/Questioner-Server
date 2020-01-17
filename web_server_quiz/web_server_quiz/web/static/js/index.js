$(document).ready(function () {
    let api_endpoint = 'http://' + document.domain + ':' + location.port + '/api/get_quiz/quiz_list';
    $.ajax(
        {
            url: api_endpoint,
            type: 'get',
            async: false,
            success: function (response) {
                console.log(response);
                for (let i = 0; i < response.length; i++) {
                    let div = document.createElement("div");
                    document.getElementById('quiz_list').appendChild(div);
                    div.innerHTML =
                        '<a href="quiz/' + response[i]["quiz_id"] + '" class="list-group-item list-group-item-action">'
                        + response[i]["quiz_name"] + ' --- ' + response[i]["description"] + ' There are ' +
                        response[i]["questions_count"] + ' questions in the quiz.' + '</a>';
                }
            },
            error: function (data) {
                callFailureAlertify(data);
            }
        });
});