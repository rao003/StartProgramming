"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "pong.png";

// Globale Variablen
var width = 40; var xDiff = 10; var yDiff = 5;
var x = canvas.width/2 - width/2;
var y = canvas.height/2 - width/2;
var delayTime; var rolling = false;

// Timer-Methode
function shiftImage() {
  context.fillRect(x, y, width, width);
  x += xDiff; y += yDiff;
  controlBorder();
  context.drawImage(image, x, y, width, width); 
}

// Grenzen kontrollieren
function controlBorder() {
  if (x < 15 || x > canvas.width-width-15)  xDiff = -xDiff;
  if (y < 15 || y > canvas.height-width-15) yDiff = -yDiff;
}

// Ereignis-Methoden
window.onload = function() {
  context.fillStyle = "green";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  context.drawImage(image, x, y, width, width);
}
canvas.onclick = function() {
  rolling = !rolling;
  if (rolling)
    delayTime = window.setInterval(shiftImage, 20);
  else window.clearInterval(delayTime);
}
