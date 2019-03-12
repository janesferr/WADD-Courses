/*  JavaScript 6th Edition
    Chapter 10
    Hands-on Project 10-4

    Author: 
    Date:   

    Filename: script.js
*/

"use strict";

// global variables
var waitForUser;

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
   Lat = position.coords.latitude;
   Lng = position.coords.longitude;
   var mapOptions = {
      center: new google.maps.LatLng(Lat, Lng),
      zoom: 10
   };
   var map = new google.maps.Map(document.getElementById("map"), mapOptions);
/* city coordinates (student values may vary slightly)
 * Beijing: 39.912729, 116.395985
 * Paris: 48.8564826, 2.3524135
 * Rio de Janeiro: -22.9133954, -43.2007101
 */

}

function fail() {
   document.getElementById("map").innerHTML = "Unable to access your current location.";
}