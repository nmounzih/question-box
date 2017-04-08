function new_a(e) {
  e.preventDefault();
  var post_data = {
                    text: $("#text").val(),
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                    question: $('#question_id').val()
                  };
  console.log(post_data);

  var settings = {
    method: "POST",
    url: "/api/answers/",
    data: post_data
  }
  $.ajax(settings);
  console.log('test1');
}

$("#newAnswer").click(new_a);
