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
var state = 0;
var count = 0;

// Timer-Methode
function shiftImage() {
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.changePosition();
  var ping = Pong.controlXEdge(15, canvas.width-75, 15, canvas.height-75);
  if (ping)
    Pong.setPosition(canvas.width-75, newPosition());
  Dodger.showImage();
  Pong.showImage(); 
  // Wenn Player nicht ausweicht, Spiel-Ende
  if (Pong.x < Dodger.x+Dodger.width/2+20)
    if (!isDodging()) endGame();
  document.getElementById("LBL").innerHTML = "Score: " + count;
}

// zufällig oben oder unten
function newPosition() {
  count += 10;
  var highlow = Math.floor(Math.random()*2);
  return (highlow * canvas.height/2 + Pong.width/2);
}

// Status ändern, neues Bild
function setState(nr) {
  state = nr;
  Dodger.image = image[nr];
  context.fillRect(Dodger.x, Dodger.y, Dodger.width, Dodger.height);
}

// Ausgewichen?
function isDodging() {
  if ((Pong.y < canvas.height/2 && state == 1) 
   || (Pong.y > canvas.height/2 && state == 2))
    return true
  else
    return false
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
document.onkeydown = function(event) {
  if (rolling) { 
    if (event.key == "ArrowDown") setState(1);  // Pfeil-Runter
    if (event.key == "ArrowUp")   setState(2);  // Pfeil-Rauf   
  }
}
document.onkeyup = function(event) {
  setState(0);
  Dodger.showImage();
}

// Spiel-Ende: Aufräumungsarbeiten
function endGame() {
  rolling = false; 
  window.clearInterval(delayTime);
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.setPosition(canvas.width-75, newPosition());
  Dodger.showImage();
}

// Hauptprogramm
createImages();
var Dodger = new Player(image[0], 120, 175);
Dodger.setPosition(15, 40);
var Pong = new Player(image[3], 60, 60);
Pong.setPosition(canvas.width-75, newPosition());
Pong.setSpeed(-10, 0, 20);
