/*    JavaScript 6th Edition
 *    Chapter 8
 *    Hands-on Project 8-5

 *    Author: 
 *    Date:   

 *    Filename: script.js
 */

"use strict";

var list = [];

// add new item to bottom of array
function addItem() {
   var newItem = document.getElementById("newItem");
   // add new item to list array
   list.push(newItem.value);
   newItem.focus();
   newItem.value = "";
   generateList();
}

// move list item to start of array and regenerate list
function moveToTop(evt) {
   if (evt === undefined) { // get caller element in IE8
      evt = window.event;
   }
   var callerElement = evt.target || evt.srcElement;
   var listItems = document.getElementsByTagName("li");
   var parentItem = callerElement.parentNode;
   for (var i = 0; i < list.length; i++) {
      if (parentItem.innerHTML.search(list[i]) !== -1) {
         var itemToMove = list.splice(i, 1);
         list.unshift(itemToMove);
      }
   }
   generateList();
}

// move list item to end of array and regenerate list
function moveToBottom(evt) {
   if (evt === undefined) { // get caller element in IE8
      evt = window.event;
   }
   var callerElement = evt.target || evt.srcElement;
   var listItems = document.getElementsByTagName("li");
   var parentItem = callerElement.parentNode;
   for (var i = 0; i < list.length; i++) {
      if (parentItem.innerHTML.search(list[i]) !== -1) {
         var itemToMove = list.splice(i, 1);
         list.push(itemToMove);
      }
   }
   generateList();
}

// create list from array
function generateList() {
   // clear ordered list
   var listItems = document.getElementsByTagName("li");
   for (var i = listItems.length - 1; i >= 0; i--) {
      document.getElementsByTagName("ol")[0].removeChild(listItems[i]);
   }
   // recreate ordered list using new array order
   for (var i = 0; i < list.length; i++) {
      var newItem = "<span class='first'>first</span>" + "<span class='last'>last</span>" + list[i];
      var newListItem = document.createElement("li");
      newListItem.innerHTML = newItem;
      document.getElementsByTagName("ol")[0].appendChild(newListItem);
      var firstButtons = document.querySelectorAll(".first");
      var lastFirstButton = firstButtons[firstButtons.length - 1];
      var lastButtons = document.querySelectorAll(".last");
      var lastLastButton = lastButtons[lastButtons.length - 1];
      if (lastFirstButton.addEventListener) {
        lastFirstButton.addEventListener("click", moveToTop, false);
        lastLastButton.addEventListener("click", moveToBottom, false);
      } else if (lastFirstButton.attachEvent)  {
        lastFirstButton.attachEvent("onclick", moveToTop);
        lastLastButton.attachEvent("onclick", moveToBottom);
      }
   }
}

// add backward compatible event listener to Submit button
function createEventListener() {
   var addButton = document.getElementById("button");
   if (addButton.addEventListener) {
     addButton.addEventListener("click", addItem, false); 
   } else if (addButton.attachEvent)  {
     addButton.attachEvent("onclick", addItem);
   }
}

if (window.addEventListener) {
   window.addEventListener("load", createEventListener, false);
} else if (window.attachEvent) {
   window.attachEvent("onload", createEventListener);
}