/*  JavaScript 6th Edition
    Chapter 12
    Hands-on Project 12-2

    Author: 
    Date:   

    Filename: script.js
*/

// convert entered pounds value to kilograms and display
function convert() {
   var lb = $("#pValue").val();
   var kg = Math.round(lb / 2.2);
   $("#kValue").html(kg);
}

// add backward compatible event listener to Convert to Kg button and clear form
$("#convertButton").click(convert);
$("#pValue").val("");
$("#kValue").html("");