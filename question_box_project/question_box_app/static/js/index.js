console.log("js ran");

function new_q(e) {
  e.preventDefault();
  var post_data = { title: $("#title").val(),
                    text: $("#text").val(),
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                    user: $("#user_id").val(),
                  };
  console.log(post_data);

  var settings = {
    method: "POST",
    url: "/api/question/",
    data: post_data
  }
  $.ajax(settings)
  //  $.post('/api/question/', { title: $("input[name=title]").val(), text: $("input[name=text]").val()})
}

$("#newQuestion").click(new_q);

var modal = document.getElementById('newmodal');
var btn = document.getElementById("new");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function() {
    modal.style.display = "block";
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
