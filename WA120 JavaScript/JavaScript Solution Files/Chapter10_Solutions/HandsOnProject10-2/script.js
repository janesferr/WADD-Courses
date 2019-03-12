/*  JavaScript 6th Edition
    Chapter 10
    Hands-on Project 10-2

    Author: 
    Date:   

    Filename: script.js
*/

"use strict";

// global variables
var loc = [];
var origin;
var onTop;

// perform setup tasks when page first loads
function setUpPage() {
   var puzzlePieces = document.querySelectorAll("#pieces div");
   onTop = puzzlePieces.length + 1;
   for (var i = 0; i < puzzlePieces.length; i++) {
      // disable IE10+ interface gestures 
      puzzlePieces[i].style.msTouchAction = "none";
      puzzlePieces[i].style.touchAction = "none";
      if (puzzlePieces[i].addEventListener) {
         puzzlePieces[i].addEventListener("mousedown", startDrag, false);
         puzzlePieces[i].addEventListener("touchstart", startDrag, false);
         puzzlePieces[i].addEventListener("mspointerdown", startDrag, false);
         puzzlePieces[i].addEventListener("pointerdown", startDrag, false);
      } else if (puzzlePieces[i].attachEvent) {
         puzzlePieces[i].attachEvent("onmousedown", startDrag);
      }
   }
}

// add event listeners and move object when user starts dragging
function startDrag(event) {
   this.style.zIndex = onTop; // set z-index to move selected element on top of other elements
   onTop++; // increment z-index counter so next selected element is on top of other elements
   event.preventDefault();

   if (event.type !== "mousedown") {
      this.addEventListener("touchmove", moveDrag, false);
      this.addEventListener("mspointermove", moveDrag, false);
      this.addEventListener("pointermove", moveDrag, false);

      this.addEventListener("touchend", removeTouchListener, false);
      this.addEventListener("mspointerup", removeTouchListener, false);
      this.addEventListener("pointerup", removeTouchListener, false);
   } else {
      this.addEventListener("mousemove", moveDrag, false);
      this.addEventListener("mouseup", removeDragListener, false);
   }

   loc = [this.offsetLeft,this.offsetTop];
   origin = getCoords(event);
}

// calculate new location of dragged object
function moveDrag(event) {
   var currentPos = getCoords(event);
   var deltaX = currentPos[0] - origin[0];
   var deltaY = currentPos[1] - origin[1];
   this.style.left = (loc[0] + deltaX) + "px";
   this.style.top  = (loc[1] + deltaY) + "px";
}

// identify location of event
function getCoords(event) {
   var coords = [];
   if (event.targetTouches && event.targetTouches.length) {
      var thisTouch = event.targetTouches[0];
      coords[0] = thisTouch.clientX;
      coords[1] = thisTouch.clientY;
   } else {
      coords[0] = event.clientX;
      coords[1] = event.clientY;
   }
   return coords;
}

// remove mouse event listeners when dragging ends
function removeDragListener() {
   this.removeEventListener("mousemove", moveDrag, false);
   this.removeEventListener("mouseup", removeDragListener, false);
}

// remove touch event listeners when dragging ends
function removeTouchListener() {
   this.removeEventListener("touchmove", moveDrag, false);
   this.removeEventListener("mspointermove", moveDrag, false);
   this.removeEventListener("pointermove", moveDrag, false);
   this.removeEventListener("touchend", removeTouchListener, false);
   this.removeEventListener("mspointerup", removeTouchListener, false);
   this.removeEventListener("pointerup", removeTouchListener, false);
}

// run setUpPage() function when page finishes loading
if (window.addEventListener) {
   window.addEventListener("load", setUpPage, false);
}