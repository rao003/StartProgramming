"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Bilder sammeln
var image = [];
function createImages() {
  for (var nr = 0; nr < 6; nr++) {
    var img = new Image();
    img.src = "Augen" + (nr+1) + ".png";
    image[nr] = img;
  }
}
// Globale Variablen
var x = 30; var y = 50;
var width = 175;
var Left; var Right; var Winner;

// Ereignis-Methoden
function showImage() {
  Left = Math.floor(Math.random()*6);
  context.drawImage(image[Left], x, y, width, width);
  Right = Math.floor(Math.random()*6);
  context.drawImage(image[Right], x+260, y, width, width);
  evaluate();
}
// Auswerten
function evaluate() {
  if (Left > Right) Winner = "Du hast gewonnen";
  else if (Left < Right) Winner = "Du hast verloren";
  else Winner = "Unentschieden";
  document.getElementById("LBL").innerHTML = Winner;
}

// Hauptprogramm
createImages();
