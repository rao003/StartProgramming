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
var direction = 2;
var count = 0;

// Array für Schlangenglieder
var Section = [];
var numSec = 0;

// Timer-Methode
function loop() {
  Beetle.showImage();
  moveSnake();
  Section.forEach(showSection);
  if (Snake.isHitting(Beetle.x, Beetle.y)) {
    changeBeetle();
    evaluate();
  }
  document.getElementById("LBL").innerHTML = "Score: " + count;
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

// Sektions-Daten neu hinzufügen
function appendSection(dir, step) {
  Section.unshift({x: Snake.x, y: Snake.y});
  // wenn zu lang, letztes Element wieder entfernen 
  if (Section.length > numSec) Section.pop();
}
// Sektionen anzeigen
function showSection(item) {
  SPart.setPosition(item.x, item.y);
  SPart.showImage(); 
}

// Schlange bewegen
function moveSnake() {
  appendSection();
  context.fillRect(Snake.x, Snake.y, Snake.width, Snake.height);
  context.fillRect(SPart.x, SPart.y, SPart.width, SPart.height);
  Snake.changeOrientation(direction);
  Snake.controlEdge(2, canvas.width-width-2, 2, canvas.height-width-2);
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

// Auswertung
function evaluate() {
  count += 10;
  numSec++;
}

// Hauptprogramm
createImages();
var Snake  = new Player(image[0], width, width);
var SPart  = new Player(image[0], width, width);
var Beetle = new Player(image[1], width, width);
Snake.setPosition(x,y);
Snake.setSpeed(width, width, 200);
chooseLocation();
Beetle.setPosition(xPos, yPos);
