"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "ball1.png";

// Globale Variablen
var x = 50; var y = 50; var xDiff = 10;
var delayTime;

// Timer-Methode
function shiftImage() {
  context.clearRect(x, y, 150, 150);
  x += xDiff;
  context.drawImage(image, x, y, 150, 150);
  if (x > canvas.width-200)
    window.clearInterval(delayTime);
}

// Ereignis-Methoden
function showImage() {
  context.drawImage(image, x, y, 150, 150);
}
function moveImage() {
  delayTime = window.setInterval(shiftImage, 100);
  //delayTime = window.setTimeout(shiftImage, 100);
}
function hideImage() {
  context.clearRect(x, y, 150, 150);
}
