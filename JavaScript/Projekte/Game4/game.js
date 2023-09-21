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
  var ping = Pong.controlXEdge(15, canvas.width-75, 15, canvas.height-75);
  if (ping)
    Pong.setPosition(canvas.width-75, newPosition());
  Pong.showImage();
}

// zufällig oben oder unten
function newPosition() {
  var xy = Math.floor(Math.random()*2);
  return (xy * canvas.height/2 + Pong.width/2);
}

// Ereignis-Methoden
window.onload = function() {
  context.fillStyle = "cyan";
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
var Pong = new Player(image, 60, 60);
Pong.setPosition(canvas.width-75, newPosition());
Pong.setSpeed(-10, 0, 20);
