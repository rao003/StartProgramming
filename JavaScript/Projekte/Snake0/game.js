"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Bilder sammeln
var image = [];
var fname = ["section.png", "beetle.png"];
function createImages() {
  for (var nr = 0; nr < 2; nr++) {
    var img = new Image();
    img.src = fname[nr];
    image[nr] = img;
  }
}

// Globale Variablen
var delayTime;
var width = 25;
var xTile = 20; var x = 10 * width; 
var yTile = 12; var y =  6 * width;
var xPos; var yPos;
var moving = false;

// Timer-Methode
function loop() {
  Snake.showImage();
  Beetle.showImage();
}

// Zufällige Position
function chooseLocation() {
  xPos = Math.floor(Math.random()*xTile) * width + 2;
  yPos = Math.floor(Math.random()*yTile) * width + 2;
}

// Ereignis-Methode
window.onload = function() {
  context.fillStyle = "yellow";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  //Snake.showImage();
}
canvas.onclick = function() {
  moving = !moving;
  if (moving)
    delayTime = window.setInterval(loop, Snake.ms);
  else window.clearInterval(delayTime);
}

// Hauptprogramm
createImages();
var Snake  = new Player(image[0], width, width);
var Beetle = new Player(image[1], width, width);
Snake.setPosition(x,y);
Snake.setSpeed(width, width, 200);
chooseLocation();
Beetle.setPosition(xPos, yPos);
