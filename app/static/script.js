
$.getJSON('https://flask-apps-2021.herokuapp.com/cars', function(data) {        
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
          $.getJSON('https://flask-apps-2021.herokuapp.com/model/' + value, function(models) {
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
  $(function() {
    $('#send').on('click', function() {
        let symbole = $('#symbo').val();
        let fType = $('#fType').val();
        let asp = $('#asp').val();
        let doo = $('#doo').val();
        let carbody = $('#carbody').val();
        let drwh = $('#drwh').val();
        let enlo = $('#enlo').val();
        let whba = $('#whba').val();
        let clength = $('#clength').val();
        let cwidth = $('#cwidth').val();
        let cheight = $('#cheight').val();
        let cuwe = $('#cuwe').val();
        let enty = $('#enty').val();
        let cynum = $('#cynum').val();
        let engsize = $('#engsize').val();
        let fsys = $('#fsys').val();
        let bratio = $('#bratio').val();
        let stroke = $('#stroke').val();
        let compRatio = $('#compRatio').val();
        let hpower = $('#hpower').val();
        let prpm = $('#prpm').val();
        let cmpg = $('#cmpg').val();
        let hmpg = $('#hmpg').val();
        $.getJSON('https://flask-apps-2021.herokuapp.com/models/' + symbole +'/'+ fType +'/'+ asp +'/'+ doo +'/'+carbody+'/'
        +drwh+'/'+enlo+'/'+whba+'/'+clength+'/'+cwidth+'/'+cheight+'/'+cuwe+'/'+enty+'/'
        +cynum+'/'+engsize+'/'+fsys+'/'+bratio+'/'+stroke+'/'+compRatio+'/'+hpower+'/'+prpm+'/'+cmpg+'/'
        +hmpg , function(results) {

          
          for (var i = 0; i < results.length ; i++)
                {   var msg = `${results[i][0]}`
                    console.log(msg)
                    window.alert("Bravo ! \n Nous pouvons vendre votre voiture au prix de "+msg+ " €");
 
                }
        })

    })

});