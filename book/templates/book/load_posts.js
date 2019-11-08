$(document).ready(function(){

  //everytime the username input is pressed run the autocomplete
 $(document).on('keydown', '.where', function() {
 
 // id = "username_1"
  var id = this.id;
  //splitid is an array
  //var splitid = id.split('_');
  //var index = splitid[1];

  // Initialize jQuery UI autocomplete
  //for username
  $( '#'+id ).autocomplete({
   source: function( request, response ) {
    $.ajax({
     url: "ajax/load-posts/",
     type: "POST",
     dataType: "json",
     data: { 
      search: request.term, 
      request: 1, 
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
     success: function( data ) {
      response( data );
     }
    });
   },
   //after selecting a username
   select: function (event, ui) {
    $(this).val(ui.item.label); // display the selected text
    var userid = ui.item.value; // selected value

    // to complete all the textboxes
    // AJAX
    $.ajax({
     url: "ajax/load-posts/",
     type: "POST",
     data: { userid: userid, request: 2, csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val() },
     dataType: "json",
     success:function(response){
 
      var len = response.length;

      // EDIT THIS
      if(len > 0){
       var id = response[0]['id'];
       var name = response[0]['name'];
       var email = response[0]['email'];
       var age = response[0]['age'];
       var salary = response[0]['salary'];

       // Set value to textboxes
       document.getElementById('who').value = name;
       document.getElementById('setting').value = age;
       document.getElementById('requirements').value = email;
       document.getElementById('incentives').value = salary;
 
      }
 
     }
    });

    return false;
   }
  });
 });
