"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Bilder sammeln
var image = [];
var fname = ["standing.png", "ducking.png", "jumping.png", "pong.png"];
function createImages() {
  for (var nr = 0; nr < 4; nr++) {
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
  var ping = Pong.controlXEdge(15, canvas.width-75, 15, canvas.height-75);
  if (ping)
    Pong.setPosition(canvas.width-75, newPosition());
  Pong.showImage();
  Dodger.showImage();
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
  Dodger.showImage();
}
canvas.onclick = function() {
  rolling = !rolling;
  if (rolling)
    delayTime = window.setInterval(shiftImage, Pong.ms);
  else window.clearInterval(delayTime);
}

// Hauptprogramm
createImages();
var Dodger = new Player(image[0], 120, 175);
Dodger.setPosition(15, 40);
var Pong = new Player(image[3], 60, 60);
Pong.setPosition(canvas.width-75, newPosition());
Pong.setSpeed(-10, 0, 20);
