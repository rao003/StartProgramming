"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "figur01.png";

// Globale Variablen
var x = 15; var y = 15; var xDiff = 10;
var width = 140; var height = 210;
var delayTime;

// Timer-Methode
function shiftImage() {
  context.clearRect(x, y, width, height);
  x += xDiff;
  context.drawImage(image, x, y, width, height);
  if (x > canvas.width-width-25)
    window.clearInterval(delayTime);
}
// Ereignis-Methoden
function showImage() {
  context.drawImage(image, x, y, width, height);
}
function moveImage() {
  delayTime = window.setInterval(shiftImage, 100);
}
function hideImage() {
  context.clearRect(x, y, width, height);
}
