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
var delayTime; var delayTime2;
var rolling = false;
var count = [0, 0];
var tactics = 0;
var interval = 150;
var rep_ms = 20;

// Funktions-Arrays
var repTime = {}; 
var keyMove = {
  38: function() { movePaddle(LPaddle.y-20); },
  40: function() { movePaddle(LPaddle.y+20); }
};

// Timer-Methoden
function shiftImage() {
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.changePosition();
  // Kollisionskontrollen
  var dir = Pong.controlXBorder(15, canvas.width-55, 15, canvas.height-55);
  evaluate(dir);
  Pong.controlXContact
  (LPaddle.x, LPaddle.x+30, LPaddle.y, LPaddle.y+LPaddle.height, 2);
  Pong.controlXContact
  (RPaddle.x-10, RPaddle.x+20, RPaddle.y, RPaddle.y+RPaddle.height, 2);
  Pong.showImage();
}
function shiftImage2() {
  context.fillRect(RPaddle.x, RPaddle.y, RPaddle.width, RPaddle.height);
  // Wechsel der Taktik
  tactics++;
  if (tactics <= interval) playClever(0);
  if (tactics > interval && tactics < 2*interval) playClever(1);
  if (tactics > 2*interval) tactics = 0;
  // Kollisionskontrolle
  RPaddle.controlBorder(0, 0, 15, canvas.height-115);
  RPaddle.showImage();
}

// Ereignis-Methoden
window.onload = function() {
  context.fillStyle = "green";
  context.fillRect(2, 2, canvas.width-4, canvas.height-4);
  Pong.showImage();
  LPaddle.showImage();
  RPaddle.showImage();
}
// Bewegung von Ball und Paddle
canvas.onclick = function() {
  centerBall();
  rolling = !rolling;
  if (rolling) {
    delayTime = window.setInterval(shiftImage, Pong.ms);
    delayTime2 = window.setInterval(shiftImage2, RPaddle.ms);
  }
  else {
    window.clearInterval(delayTime);
    window.clearInterval(delayTime2);
  }
}
//  Maus-Steuerung Spieler
canvas.onmousemove = function(event) {
  if (rolling) { 
    var y = event.offsetY;
    movePaddle(y);
  }
}
// Tasten-Steuerung Spieler
document.onkeydown = function(event) {
  if (rolling) { 
    var key = event.keyCode;
    if (!(key in repTime)) {
      repTime[key]= null;
      repTime[key] = setInterval(keyMove[key], rep_ms);
    }
  }
}
document.onkeyup = function(event) {
  var key = event.keyCode;
  if (key in repTime) {
    if (repTime[key] != null)
      clearInterval(repTime[key]);
    delete repTime[key];
  }
}

// Ball (wieder) ins Zentrum setzen
function centerBall() {
  context.fillRect(Pong.x, Pong.y, Pong.width, Pong.height);
  Pong.setPosition(canvas.width/2-20, canvas.height/2-20);
  Pong.showImage();
}

// Linkes Paddle bewegen
function movePaddle(y) {
  if (y < 15) y = 5;
  if (y > canvas.height-105) y = canvas.height-105;
  context.fillRect(LPaddle.x, LPaddle.y, LPaddle.width, LPaddle.height);
  LPaddle.setPosition(2, y);
  LPaddle.showImage();
}

// "Spiel-Intelligenz" Gegner
function playClever(mode) {
  if (mode == 0) // nur auf und ab
    RPaddle.changePosition();
  else // dem Ball folgend
    if (Pong.y < canvas.height-100)
      RPaddle.setPosition(canvas.width-22, Pong.y);
}

// Auswertung
function evaluate(dir) {
  if (dir == 1) { count[1]++; }
  if (dir == 3) { count[0]++; }
  document.getElementById("LBL").innerHTML = count[0] + " : " + count[1];
}

// Hauptprogramm
createImages();
var Pong = new Player(image[0], 40, 40);
Pong.setPosition(canvas.width/2-20, canvas.height/2-20);
Pong.setSpeed(10, 5, 15);
var LPaddle = new Player(image[1], 20, 100);
LPaddle.setPosition(2, canvas.height/2-50);
var RPaddle = new Player(image[1], 20, 100);
RPaddle.setPosition(canvas.width-22, canvas.height/2-50);
RPaddle.setSpeed(0, 5, 20);
