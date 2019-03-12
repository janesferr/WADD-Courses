/*    JavaScript 6th Edition
 *    Chapter 9
 *    Hands-on Project 9-1

 *    Author: 
 *    Date:   

 *    Filename: script.js
 */

"use strict";

function populateInfo() {
   if (location.search) {
      var greeting = location.search;
      greeting = greeting.replace("+", " ");
      greeting = greeting.substring(greeting.lastIndexOf("=") + 1);
      document.getElementById("greetingtext").innerHTML = decodeURIComponent(greeting);
   }
}

if (window.addEventListener) {
   window.addEventListener("load", populateInfo, false);
} else if (window.attachEvent) {
   window.attachEvent("onload", populateInfo);
}