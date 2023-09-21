"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "pong.png";

// Globale Variablen
var width = 40; var xDiff = 10;
var x = 10; //canvas.width/2 - width/2;
var y = canvas.height/2 - width/2;
var delayTime;

// Timer-Methode
function shiftImage() {
  context.fillRect(x, y, width, width);
  x += xDiff;
  context.drawImage(image, x, y, width, width);
  if (x > canvas.width-width-15)
    window.clearInterval(delayTime);
}

// Ereignis-Methode
window.onload = function() {
  context.fillStyle = "green";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  context.drawImage(image, x, y, width, width);
  delayTime = window.setInterval(shiftImage, 100);
}
