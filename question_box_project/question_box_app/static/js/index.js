$.ajax({
  type: 'GET',
  url: 'http://127.0.0.1:8000/api/questions',
  success: function(data){
    console.log(data);
    for(var i = 0; i< data.results.length; i++){
      console.log(data.results[i]);
    }
    }
  })
