var form_count = document.getElementById("id_extra_duration_count").value;

document.getElementById("add-another").onclick = function() {
	form_count = form_count + 1;

	var input = document.createElement("input");
	input.setAttribute('type', 'date');
	input.setAttribute('name', 'extra_duration_' + form_count);
	document.getElementById("forms").append(input);

	document.getElementById("id_extra_duration_count").value = form_count;
}