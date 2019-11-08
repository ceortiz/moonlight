		var currentTab = 0;
		var remaining_tabs = [0, 1, 2, 3, 4, 5];
		//var undesired_tabs = 
		function showTab(n) {
				var x = document.getElementsByClassName("tab");
				var y = remaining_tabs[n];

				x[y].style.display = "block";

				// buttons
				if (n == 0) {
					document.getElementById("prevBtn").style.display = "none";
				} else {
					document.getElementById("prevBtn").style.display = "inline";
				}

				if (n == (remaining_tabs.length - 1)) {
					document.getElementById("nextBtn").innerHTML = "Register";
				} else {
					document.getElementById("nextBtn").innerHTML = "Next";
				}

				//fixStepIndicator(n);
			}

		document.addEventListener('DOMContentLoaded', function() {
			showTab(currentTab);

			//function fixStepIndicator(n) {
				//removes active class of all steps
			//	var i, x = document.getElementsByClassName("step");
			//	for (i = 0; i < x.length; i++) {
			//		x[i].className = x[i].className.replace("active", "");
			//	}

				// adds active class to current step
			//	x[n].className += " active";
			//}
		});
		
		function splicer(n) {
			for (i = n.length - 1; i >= 0; i--)
				remaining_tabs.splice(n[i], 1);
		}

		function restore() {
			remaining_tabs = [0, 1, 2, 3, 4, 5];
		}

		function nextPrev(n) {
				var x = document.getElementsByClassName("tab");
				//if (n == 1 && !validateForm()) return false;
				var y = remaining_tabs[currentTab];
				x[y].style.display = "none";

				//CONDITIONALS
				// At step 1 and ONLY if next button is clicked
				if (currentTab == 0 && n == 1) {
					//var remaining_tabs = [0, 1, 2, 3, 4, 5];
					if (document.getElementById('professioninput').value == "recruiter") {
						restore();
						var undesired_tabs = [1, 3, 4, 5];	
						splicer(undesired_tabs);
					} else if (document.getElementById('professioninput').value != "recruiter" && document.getElementById('professioninput').value != "doctor") {
						restore();
						var undesired_tabs = [2, 3, 4, 5];
						splicer(undesired_tabs);
					} else if (document.getElementById('professioninput').value == "doctor") {
						restore();
						var undesired_tabs = [2];
						splicer(undesired_tabs);
					}
				}
				// splice for 5 elements instead of 6
				if (currentTab == 2 && n == 1) {
					//var remaining_tabs = [0, 1, 2, 3, 4, 5];
					if (document.getElementById('specialtyinput').value == "pcp") {
						restore();
						var undesired_tabs = [2, 5];
						splicer(undesired_tabs);
					} else if (document.getElementById('specialtyinput').value != "pcp") {
						restore();
						var undesired_tabs = [2, 4];
						splicer(undesired_tabs);
					}
				}
				currentTab = currentTab + n;

				if (currentTab >= remaining_tabs.length) {
					document.getElementById("regForm").submit();
					return false;
				} else {
					showTab(currentTab);
				}
			}
			// if recruiter iterate through tabs and append recruiter tabs to a list
			// use the list as the steps

			var x = document.getElementsByClassName("tab");
					var y = remaining_tabs;

					for (i = 0; i <= y.length - 1; i++)
						x[y[i]].classList.add('wrap_me');

					var z = document.getElementsByClassName('wrap_me');
					// create a wrapper
					var wrapper = document.createElement('form');
					// add id to the wrapper
					wrapper.setAttribute('id', 'register');
					wrapper.method = "POST";
					wrapper.action = "{% url 'registration' %}";
					// use insertbefore 
					wrapper.appendChild(z);
					// append element to the wrapper
					// submit the wrapper
					document.getElementById('register').submit();
					return false;
