//get value of extra duration count (hidden) and assign to form count
//form_count = Number($("[name=extra_duration_count]").val());
form_count = $('input[name*=extra_duration_count]').val());

// on click, increment form count by 1
$("#add-another").click(function() {
	form_count++;

	// create a text field w/ name of extra duration_(form count) and append it to form
	element = $('<input type="date">');
	element.attr('name', 'extra_duration_' + form_count);
	$("#forms").append(element);

	//update value of edc (hidden) w/ form count
	$("[name=extra_duration_count]").val(form_count);
})