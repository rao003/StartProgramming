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
var x = 30; var y = 50; var width = 175;
var Left; var Right; var Winner;
var count = [0, 0, 0];

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
  if (Left > Right) {
    Winner = "Du hast gewonnen";
    count[0]++; count[1]++;
  }
  else if (Left < Right) {
    Winner = "Du hast verloren";
    count[0]++; count[2]++;
  } 
  else {
    Winner = "Unentschieden";
    count[0]++;
  }
  var text1 = "Dein Spielstand:  " + count[1] + "/" + count[0];
  var text2 = "Spielstand Gegner:  " + count[2] + "/" + count[0];
  document.getElementById("LBL1").innerHTML = Winner;
  document.getElementById("LBL2").innerHTML = text1;
  document.getElementById("LBL3").innerHTML = text2;
}

// Hauptprogramm
createImages();
