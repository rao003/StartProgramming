"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Bilder sammeln
var image = [];
var fname = ["pong.png", "paddle.png"];
function createImages() {
  for (var nr = 0; nr < 2; nr++) {
    var img = new Image();
    img.src = fname[nr];
    image[nr] = img;
  }
}

// Globale Variablen
var delayTime;
var rolling = false;

// Timer-Methode
function shiftImage() {
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.changePosition();
  // Kollisionskontrollen
  Pong.controlBorder(15, canvas.width-55, 15, canvas.height-55);
  Pong.controlContact(LPaddle.x, LPaddle.x+30, LPaddle.y, LPaddle.y+LPaddle.height);
  Pong.controlContact(RPaddle.x-10, RPaddle.x+20, RPaddle.y, RPaddle.y+RPaddle.height);
  Pong.showImage();
}

// Ereignis-Methoden
window.onload = function() {
  context.fillStyle = "green";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  Pong.showImage();
  LPaddle.showImage();
  RPaddle.showImage();
}
canvas.onclick = function() {
  rolling = !rolling;
  if (rolling)
    delayTime = window.setInterval(shiftImage, Pong.ms);
  else window.clearInterval(delayTime);
}

// Hauptprogramm
createImages();
var Pong = new Player(image[0], 40, 40);
Pong.setPosition(canvas.width/2-20, canvas.height/2-20);
Pong.setSpeed(10, 5, 20);
var LPaddle = new Player(image[1], 20, 100);
LPaddle.setPosition(2, canvas.height/2-50);
var RPaddle = new Player(image[1], 20, 100);
RPaddle.setPosition(canvas.width-22, canvas.height/2-50);
