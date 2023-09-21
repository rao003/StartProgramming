"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");
// Bild
var image = new Image();
image.src = "pong.png";

// Globale Variablen
var delayTime;
var rolling = false;

// Timer-Methode
function shiftImage() {
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.changePosition();
  Pong.controlBorder(15, canvas.width-55, 15, canvas.height-55);
  Pong.showImage();
}

// Ereignis-Methoden
window.onload = function() {
  context.fillStyle = "green";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  Pong.showImage();
}
canvas.onclick = function() {
  rolling = !rolling;
  if (rolling)
    delayTime = window.setInterval(shiftImage, Pong.ms);
  else window.clearInterval(delayTime);
}

// Hauptprogramm
var Pong = new Player(image, 40, 40);
Pong.setPosition(canvas.width/2-20, canvas.height/2-20);
Pong.setSpeed(10, 5, 20);
