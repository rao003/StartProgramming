"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "ball1.png";

// Globale Variablen
var x = 50; var y = 50; var xDiff = 10;

// Ereignis-Methoden
function showImage() {
  context.drawImage(image, x, y, 150, 150);
}
function moveImage() {
  while (x < canvas.width-200) {
    context.clearRect(x, y, 150, 150);
    x += xDiff;
    context.drawImage(image, x, y, 150, 150);
  }
}
function hideImage() {
  context.clearRect(x, y, 150, 150);
}
