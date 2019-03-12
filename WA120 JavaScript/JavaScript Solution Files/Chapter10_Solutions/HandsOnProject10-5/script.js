/*  JavaScript 6th Edition
    Chapter 10
    Hands-on Project 10-5

    Author: 
    Date:   

    Filename: script.js
*/

"use strict";

// global variables
var waitForUser;

function setUpPage() {
   var buttons = document.querySelectorAll("#cities div");
   for (var i = 0; i < buttons.length; i++ ) {
      buttons[i].addEventListener("click", createMap, false);
   }
}

function geoTest() {
   waitForUser = setTimeout(fail, 10000);
   if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(createMap, fail, {timeout: 10000});
   } else {
      fail();
   }
}

function createMap(position) {
   var Lat;
   var Lng;
   clearTimeout(waitForUser);
   if (position.coords) {
      Lat = position.coords.latitude;
      Lng = position.coords.longitude;
   } else {
      var city = this.innerHTML;
      if (city === "Beijing") {
         Lat = "39.912729";
         Lng = "116.395985";
      } else if (city === "Paris") {
         Lat = "48.8564826";
         Lng = "2.3524135";
      } else if (city === "Rio de Janeiro") {
         Lat = "-22.9133954";
         Lng = "-43.2007101";
      }
      document.getElementById("caption").innerHTML = city;
   }
   var mapOptions = {
      center: new google.maps.LatLng(Lat, Lng),
      zoom: 10
   };
   var map = new google.maps.Map(document.getElementById("map"), mapOptions);
}

function fail() {
   document.getElementById("map").innerHTML = "Unable to access your current location.";
}

// run setUpPage() function when page finishes loading
if (window.addEventListener) {
   window.addEventListener("load", setUpPage, false);
}