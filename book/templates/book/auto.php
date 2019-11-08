$(document).ready(function(){

 $(document).on('keydown', '.username', function() {
 
  var id = this.id;
  var splitid = id.split('_');
  var index = splitid[1];

  // Initialize jQuery UI autocomplete
  $( '#'+id ).autocomplete({
   source: function( request, response ) {
    $.ajax({
     url: "getDetails.php",
     type: 'post',
     dataType: "json",
     data: {
      search: request.term,request:1
     },
     success: function( data ) {
      response( data );
     }
    });
   },
   select: function (event, ui) {
    $(this).val(ui.item.label); // display the selected text
    var userid = ui.item.value; // selected value

    // AJAX
    $.ajax({
     url: 'getDetails.php',
     type: 'post',
     data: {userid:userid,request:2},
     dataType: 'json',
     success:function(response){
 
      var len = response.length;

      if(len > 0){
       var id = response[0]['id'];
       var name = response[0]['name'];
       var email = response[0]['email'];
       var age = response[0]['age'];
       var salary = response[0]['salary'];

       // Set value to textboxes
       document.getElementById('name_'+index).value = name;
       document.getElementById('age_'+index).value = age;
       document.getElementById('email_'+index).value = email;
       document.getElementById('salary_'+index).value = salary;
 
      }
 
     }
    });

    return false;
   }
  });
 });
 
 // Add more
 $('#addmore').click(function(){

  // Get last id 
  var lastname_id = $('.tr_input input[type=text]:nth-child(1)').last().attr('id');
  var split_id = lastname_id.split('_');

  // New index
  var index = Number(split_id[1]) + 1;

  // Create row with input elements
  var html = "<tr class='tr_input'><td><input type='text' class='username' id='username_"+index+"' placeholder='Enter username'></td><td><input type='text' class='name' id='name_"+index+"' ></td><td><input type='text' class='age' id='age_"+index+"' ></td><td><input type='text' class='email' id='email_"+index+"' ></td><td><input type='text' class='salary' id='salary_"+index+"' ></td></tr>";

  // Append data
  $('tbody').append(html);
 
 });
});