
$.getJSON('http://127.0.0.1:5000/cars', function(data) {        
  var select = document.getElementById('dm');   
  for (var i = 0; i < data.length ; i++)
        {
          console.log(`${data[i][0]}`)
          var op = document.createElement("option")
          op.setAttribute("id", "brand")
          select.appendChild(op)
          op.innerHTML=`${data[i][0]}`
        }
    });
    $(function() {
      $('#dm').change(function() {
          let value = $(this).val();
          $.getJSON('http://127.0.0.1:5000/model/' + value, function(models) {
              $('#dmo').html('');
              
                console.log(models)
                var selects = document.getElementById('dmo'); 
                for (var i = 0; i < models.length ; i++)
                {
                  var opt = document.createElement("option")
                  selects.appendChild(opt)
                  opt.innerHTML=`${models[i][0]}`
                }
              
          })
  
      })
  
  });
