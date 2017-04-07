$.ajax({
  type: 'GET',
  url: '/api/question/',
  success: function(data){
    console.log(data);
    for(var i = 0; i < data.results.length; i++){
      console.log(data.results[i]);
    $('body').append('<div id=' + data.results[i].id + '>' + data.results[i].title);
    var curr_div = document.getElementById(data.results[i].id);
    $(curr_div).html('<a href="/question_detail/'+  data.results[i].id +'" >'+data.results[i].title+'</a>');
    console.log('here')
    console.log(curr_div)
      }
    }
  })

  // $.ajax({
  //   type: 'POST',
  //   url: '/api/questions/',
  //   success: function(data){
  //     console.log(data);
  //     for(var i = 0; i< data.results.length; i++){
  //       console.log(data.results[i]);
  //     $('body').append('<div id=' + data.results[i].id + '>' + data.results[i].title);
  //     var curr_div = document.getElementById((i+1).toString())
  //     $(curr_div).html('<a href="www.google.com">'+data.results[i].title+'</a>');
  //     console.log('here')
  //     console.log(curr_div)
  //       }
  //     }
  //   })

$.post("/api/question/", {title: "Test questionsdfbsfg?", text: "This is a test question. please work", user_id: '1', csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() });

// $.ajax({
//   type: 'GET',
//   url: '/api/answers',
//   success: function(data){
//     console.log(data);
//     for(var i = 0; i< data.results.length; i++){
//       console.log(data.results[i]);
//     $('body').append('<div id=' + data.results[i].text.replace(/\s/g,'') + '>' + data.results[i].text);
//       }
//     }
//   })
