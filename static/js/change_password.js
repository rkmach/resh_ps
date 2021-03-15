$('input[name ="old_password"], input[name ="new_password"]').on('keyup', function () {
    if ($('input[name ="old_password"]').val() == $('input[name ="new_password"]').val()) {
      $('#message').html('Senhas iguais').css('color', 'red');
    } else{
      $('#message').html('');
    }
});