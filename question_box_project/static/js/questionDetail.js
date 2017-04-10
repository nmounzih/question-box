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

function newQuestionUpvote(e) {
  e.preventDefault();
  var post_data = {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                    question: $('#question_id').val(),
                    is_upvote: true,
                  };
  console.log(post_data);

  var settings = {
    method: "POST",
    url: "/api/question_votes/",
    data: post_data
  }
  $.ajax(settings);
  console.log('test1');
}

function newQuestionDownvote(e) {
  e.preventDefault();
  var post_data = {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                    question: $('#question_id').val(),
                    is_upvote: false,
                  };
  console.log(post_data);

  var settings = {
    method: "POST",
    url: "/api/question_votes/",
    data: post_data
  }
  $.ajax(settings);
  console.log('test1');
}

function newAnswerUpvote(e) {
  e.preventDefault();
  var post_data = {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                    answer: $('#answer_id').val(),
                    is_upvote: true,
                  };
  console.log(post_data);

  var settings = {
    method: "POST",
    url: "/api/answer_votes/",
    data: post_data
  }
  $.ajax(settings);
  console.log('test1');
}

function newAnswerDownvote(e) {
  e.preventDefault();
  console.log(e)
  console.log(e.target.attributes.aid)
  var id = e.target.attributes.aid
  var post_data = {
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                    answer: id,
                    is_upvote: false,
                  };
  console.log(post_data.answer);

  var settings = {
    method: "POST",
    url: "/api/answer_votes/",
    data: post_data
  }
  $.ajax(settings).done();
  console.log('test1');
}

$("#newAnswer").click(new_a);
$("#qUpvoteButton").click(newQuestionUpvote);
$("#qDownvoteButton").click(newQuestionDownvote);
$(".upVote").click(newAnswerUpvote);
$(".downVote").click(newAnswerDownvote);
