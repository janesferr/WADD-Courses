/* variables for image gallery*/
var fig1 = "images/g1.jpg";
var fig2 = "images/g2.jpg";
var fig3 = "images/g3.jpg";
var fig4 = "images/g4.jpg";
var fig5 = "images/g5.jpg";
var fig6 = "images/g6.jpg";

/* global variables */
formValidity = true;

/* function validateRequired() {
	var inputElements = document.querySelectorAll("#contactinfo input");
	var errorDiv = document.getElementById("errorText");
	var elementCount = "inputElements.length";
	var requiredValidity = true;
	var currentElement;
	try {
		for (var i = 0; i < elementCount; i++) {
			currentElement = inputElements[i];
			if (currentElement.value === "") {
				currentElement.style.background = "rgb(255,233,233)";
				requiredValidity = false;
			} else {
				currentElement.style.background = "white";
			}
		}
		if (requiredValidity === false) {
			throw "Please complete all fields.";
		}
		errorDiv.style.display = "none";
		errorDiv.innerHTML = "";
	}
	catch(msg) {
		errorDiv.style.display = "block";
		errorDiv.innerHTML = msg;
		formValidity = false;
	}
}

function validateForm(evt) {
	if (evt.preventDefault) {
		evt.preventDefault();
	} else {
		evt.returnValue = false;
	}
	formValidity = true;
	validateRequired();
	if (formValidity === true) {
		document.getElementsByTagName("form")[0].submit();
	}
}

function createEventListeners() {
	var form = document.getElementsByTagName("form")[0];
	if (form.addEventListener) {
		form.addEventListener("submit", validateForm, false);
	} else if (form.attachEvent) {
		form.attachEvent("onsubmit", validateForm);
	}
}

if (window.addEventListener) {
	window.addEventListener("load", createEventListeners, false);
} else if (window.attachEvent) {
	window.attachEvent("onload", createEventListeners); 
} */