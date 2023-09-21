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
var xTile = 20; var x = 10 * width + 2; 
var yTile = 12; var y =  6 * width + 2;
var xPos; var yPos;
var moving = false;
var direction = 3;

// Timer-Methode
function loop() {
  Beetle.showImage();
  moveSnake();
  if (Snake.isHitting(Beetle.x, Beetle.y)) changeBeetle();
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
// Tastensteuerung
document.onkeydown = function(event) {
  if (event.key == "ArrowLeft")  direction = 1;  // Pfeil-Links
  if (event.key == "ArrowUp")    direction = 2;  // Pfeil-Rauf
  if (event.key == "ArrowRight") direction = 3;  // Pfeil-Rechts
  if (event.key == "ArrowDown")  direction = 4;  // Pfeil-Runter
}

// Schlange bewegen
function moveSnake() {
  context.fillRect(Snake.x, Snake.y, Snake.width, Snake.height);
  Snake.changeOrientation(direction);
  Snake.showImage();
}

// Zufällige Position
function chooseLocation() {
  xPos = Math.floor(Math.random()*xTile) * width + 2;
  yPos = Math.floor(Math.random()*yTile) * width + 2;
}
// Käfer neu positionieren
function changeBeetle() {
  context.fillRect(Beetle.x, Beetle.y, Beetle.width, Beetle.height);
  Snake.showImage();
  chooseLocation();
  Beetle.setPosition(xPos, yPos);
  Beetle.showImage();
}

// Hauptprogramm
createImages();
var Snake  = new Player(image[0], width, width);
var Beetle = new Player(image[1], width, width);
Snake.setPosition(x,y);
Snake.setSpeed(width, width, 200);
chooseLocation();
Beetle.setPosition(xPos, yPos);
