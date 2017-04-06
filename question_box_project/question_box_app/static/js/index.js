$.ajax({
  type: 'GET',
  url: '/api/questions',
  success: function(data){
    console.log(data);
    for(var i = 0; i< data.results.length; i++){
      console.log(data.results[i]);
    $('body').append('<div id=' + data.results[i].id + '>' + data.results[i].title);
    var curr_div = document.getElementById((i+1).toString())
    $(curr_div).html('<a href="www.google.com">'+data.results[i].title+'</a>');
    console.log('here')
    console.log(curr_div)
      }
    }
  })

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
