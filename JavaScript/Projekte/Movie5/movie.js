"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Array für Bilder
var image = [];

// Globale Variablen
var x = 15; var y = 15; var xDiff = 10;
var width = 140; var height = 210;
var delayTime;
var leftright = true;

// Timer-Methode
function shiftImage() {
  context.clearRect(x, y, width, height);
  x += xDiff;
  if (leftright)
    context.drawImage(image[1], x, y, width, height);
  else
    context.drawImage(image[5], x, y, width, height);
  leftright = !leftright;
  if (x > canvas.width-width-25) {
    window.clearInterval(delayTime);
    context.drawImage(image[0], x, y, width, height);
  }
}
// Bilder sammeln
function createImages() {
  for (var nr = 0; nr < 8; nr++) {
    var img = new Image();
    img.src = "Figur0"+(nr+1)+".png";
    image[nr] = img;
  }
}

// Ereignis-Methoden
function showImage() {
  context.drawImage(image[0], x, y, width, height);
}
function moveImage() {
  delayTime = window.setInterval(shiftImage, 100);
}
function hideImage() {
  context.clearRect(x, y, width, height);
}

// Hauptprogramm
createImages();
