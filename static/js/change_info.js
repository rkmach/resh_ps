var inputs = $('input').on('keyup', function(){
    const preenchidos = inputs.get().every(({value}) => value)
    $('button').prop('disabled', !preenchidos);
});



$.getJSON( "http://localhost:8000/users/all_users/", function( data ) {
    let emails = [];
    let usernames = [];
    for(let i = 0; i < data.length; i++){
      usernames.push(data[i]['username']);
      emails.push(data[i]["email"]);
    }
    
    $('.form-group').on('select', function () {  
      if (usernames.includes($('input[name ="username"]').val())) {
        $('#message').html('Este Nome de usuário já existe! Escolha outro').css('color', 'red');
        $('button').prop('disabled',true);
      }
      else if (emails.includes($('input[name ="email"]').val())) {
        $('#message').html('Este email já está cadastrado! Escolha outro').css('color', 'red');
        $('button').prop('disabled',true);
      }

      else{
        $('#message').html('');
        $('button').prop('disabled',false);
      }
      
    });
}, "json" );