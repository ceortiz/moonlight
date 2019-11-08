		var currentTab = 0;
		var remaining_tabs = [0, 1, 2, 3, 4, 5];
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
					if (document.getElementById('id_profession').value == "REC") {
						restore();
						var undesired_tabs = [1, 3, 4, 5];	
						splicer(undesired_tabs);
					} else if (document.getElementById('id_profession').value != "REC" && document.getElementById('id_profession').value != "DOC") {
						restore();
						var undesired_tabs = [2, 3, 4, 5];
						splicer(undesired_tabs);
					} else if (document.getElementById('id_profession').value == "DOC") {
						restore();
						var undesired_tabs = [2];
						splicer(undesired_tabs);
					}
				}
				// splice for 5 elements instead of 6
				if (currentTab == 2 && n == 1) {
					//var remaining_tabs = [0, 1, 2, 3, 4, 5];
					if (document.getElementById('id_specialty').value == "PCP") {
						restore();
						var undesired_tabs = [2, 5];
						splicer(undesired_tabs);
					} else if (document.getElementById('id_specialty').value != "PCP") {
						restore();
						var undesired_tabs = [2, 4];
						splicer(undesired_tabs);
					}
				}
				currentTab = currentTab + n;

				// specify forms to be submitted based on remaining tabs
				if (currentTab >= remaining_tabs.length) {
					// get elements to be transferred to form1
					var form = document.getElementById("Form1");
					var y = remaining_tabs;

					//iterate through remaining tabs and assign a class
					for (i = y.length - 1; i >= 0; i--) {
						var z = document.getElementById("tab"+y[i]);
						form.insertBefore(z, form.childNodes[0]);
					}
					// submit form1
					form.submit();
					return false;


					// get the undesired tabs
					/**var x = document.getElementsByClassName("tab");
					var y = remaining_tabs;
					var z = [0,1,2,3,4,5];

					for (i = y.length - 1; i >= 0; i--)
						x.splice(y[i], 1);

					var z = document.getElementsByClassName("tab");
					z.classList.add("undesired");
					parent.removeChild(child);

					z.setAttribute('id', 'undesired');
					//remove the undesired tabs
					for (i = z.length - 1; i >= 0; i--)						
						var child = document.getElementById("undesired");
						parent.removeChild(child);

					// submit form
					document.getElementById('register').submit();
					return false;**/
				} else {
					showTab(currentTab);
				}
			}
