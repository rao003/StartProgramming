"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Array für Bilder
var image = [];

// Globale Variablen
var x = 15; var y = 15; var xDiff = 10;
var width = 140; var height = 210;
var delayTime; var loop = 0;
var leftright = true; var forthback = true;

// Timer-Methoden
function shiftImage() {
  context.clearRect(x, y, width, height);
  if (forthback) {
    x += xDiff;
    if (leftright)
      context.drawImage(image[1], x, y, width, height);
    else
      context.drawImage(image[5], x, y, width, height);
    leftright = !leftright;
    if (x > canvas.width-width-25) forthback = false;
  
  }
  else {
    x -= xDiff;
    if (leftright)
      context.drawImage(image[3], x, y, width, height);
    else
      context.drawImage(image[7], x, y, width, height);
    leftright = !leftright;
    if (x < 20) {
      window.clearInterval(delayTime);
      context.drawImage(image[0], x, y, width, height);
      forthback = true;
    }
  }
}
function loopImage() {
  context.clearRect(x, y, width, height);
  loop++;
  context.drawImage(image[loop], x, y, width, height);
  if (loop > 3) {
    window.clearInterval(delayTime);
    loop = 0;
  }
}
function tortImage() {
  context.clearRect(x, y, width, height);
  loop++;
  var nr = Math.floor(Math.random()*8);
  context.drawImage(image[nr], x, y, width, height);
  if (loop > 15) {
    window.clearInterval(delayTime);
    context.drawImage(image[0], x, y, width, height);
    loop = 0;
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
function turnImage() {
  delayTime = setInterval(loopImage, 200);
}
function twistImage() {
  delayTime = setInterval(tortImage, 100);
}
function hideImage() {
  context.clearRect(x, y, width, height);
}

// Hauptprogramm
createImages();
