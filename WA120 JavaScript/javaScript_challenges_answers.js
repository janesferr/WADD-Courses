//Robert Brennan WA120
//June 9th 2017


//Challenge 1
function howOld (futureYear) {
	var birthYear = 1961;
	var futureYear;
	var age = futureYear - birthYear;
	console.log("In the year " + futureYear + " I will be " + age);
	}
	
	
//Challenge 2
function fortune () {
	var geoLocation = "Las Vegas";
	var jobTitle = "Programmer";
	var numKids = 3;
	var future = ("You will be work as a " + jobTitle + "in " + geoLocation + " with " + numKids + " kids!")
	console.log(future);
}


//Challenge 3
function letsEat () {
	var choices = ["Hot Dog", "Hamburger", "Pizza", "Corn Dog"];
	for (var i = 0 ; i < choices.length; i++) {
		console.log("I want a " + choices[i]);
	}
	console.log("You'll get nothing and like it!");
}