let count = 0;

function addQuestion() {
    let div = document.createElement('div');
    document.getElementById('questions').appendChild(div);
    div.innerHTML =
        '<div class="form-group">' +
        '<label for="question_text" class="font-weight-bold">' + ++count + '.</label>' +
        '<input class="form-control" id="question_text" name="question-' + count + '[question-text]" placeholder="Please enter question text" type="text" required>' +
        '</div>' +
        '<div class="form-group"><label for="answer-' + count + '-1" class="font-weight-light">Answer version 1</label>' +
        '<input class="form-control" id="answer-' + count + '-1" name="question-' + count + '[choice][answer-1]" placeholder="Please enter answer version" type="text" required>' +
        '</div>' +
        '<div class="form-group"><label for="answer-' + count + '-2" class="font-weight-light">Answer version 2</label>' +
        '<input class="form-control" id="answer-' + count + '-2" name="question-' + count + '[choice][answer-2]" placeholder="Please enter answer version" type="text" required>' +
        '</div>' +
        '<div class="form-group"><label for="answer-' + count + '-3" class="font-weight-light">Answer version 3</label>' +
        '<input class="form-control" id="answer-' + count + '-3" name="question-' + count + '[choice][answer-3]" placeholder="Please enter answer version" type="text" required>' +
        '</div>' +
        '<div class="form-group"><label for="answer-' + count + '-4" class="font-weight-light">Answer version 4</label>' +
        '<input class="form-control" id="answer-' + count + '-4" name="question-' + count + '[choice][answer-4]" placeholder="Please enter answer version" type="text" required>' +
        '</div>' +
        '<div class="form-group"><label for="is-correct">Choice the answer that will be marked as correct:</label>' +
        '<br/>' +
        '<div>' +
        '<input id="is_correct-' + count + '-1" name="question-' + count + '[choice][is-correct]" required type="radio" value="answer-1"><label for="is_correct-' + count + '-1">Answer 1</label>' +
        '<input id="is_correct-' + count + '-2" name="question-' + count + '[choice][is-correct]" required type="radio" value="answer-2"><label for="is_correct-' + count + '-2">Answer 2</label>' +
        '<input id="is_correct-' + count + '-3" name="question-' + count + '[choice][is-correct]" required type="radio" value="answer-3"><label for="is_correct-' + count + '-3">Answer 3</label>' +
        '<input id="is_correct-' + count + '-4" name="question-' + count + '[choice][is-correct]" required type="radio" value="answer-4"><label for="is_correct-' + count + '-4">Answer 4</label>' +
        '</div>' +
        '</div>';
}

function sendData() {
    let data = $("#quiz_form").serializeJSON();
    console.log(data);
    let api_endpoint = 'http://' + document.domain + ':' + location.port + '/api/quiz_create';
    $.ajax(
        {
            url: api_endpoint,
            data: JSON.stringify(data),
            contentType: 'application/json;charset=UTF-8',
            type: 'post',
            async: false,
            dataType: 'json',
            success: function (response) {
                console.log(response);
                if (response['message'] === 'no data'){
                    callFailureAlertify({"message": "Some fields are empty!"});
                }
            },
            error: function (data) {
                callFailureAlertify(data);
            }
        });
}