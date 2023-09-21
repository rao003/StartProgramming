"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Bilder sammeln
var image = [];
var fname = ["schere.png", "stein.png", "papier.png"];

function createImages() {
  for (var nr = 0; nr < 3; nr++) {
    var img = new Image();
    img.src = fname[nr];
    image[nr] = img;
  }
}

// Globale Variablen
var x = 30; var y = 25;
var width = 175; var height = 225;
var Left; var Right; var Winner;
var count = [0, 0, 0];

// Ereignis-Methoden
function showScissors() { Left = 0; showImage(); }
function showStone()    { Left = 1; showImage(); }
function showPaper()    { Left = 2; showImage(); }

function showImage() {
  context.drawImage(image[Left], x, y, width, height);
  Right = Math.floor(Math.random()*3);
  context.drawImage(image[Right], x+260, y, width, height);
  evaluate();
}
// Auswerten
function evaluate() {
  count[0]++; Winner = "unentschieden";
  if (Left == 0 && Right == 1) // Schere-Stein
  { count[2]++; Winner = "Du hast verloren"; }
  if (Left == 1 && Right == 2) // Stein-Papier
  { count[2]++; Winner = "Du hast verloren"; }
  if (Left == 2 && Right == 0) // Papier-Schere
  { count[2]++; Winner = "Du hast verloren"; }
  if (Left == 0 && Right == 2) // Schere-Papier
  { count[1]++; Winner = "Du hast gewonnen"; }
  if (Left == 1 && Right == 0) // Stein-Schere
  { count[1]++; Winner = "Du hast gewonnen"; }
  if (Left == 2 && Right == 1) // Papier-Stein
  { count[1]++; Winner = "Du hast gewonnen"; }
  // Spielstand
  var text1 = "Dein Spielstand:  " + count[1] + "/" + count[0];
  var text2 = "Spielstand Gegner:  " + count[2] + "/" + count[0];
  document.getElementById("LBL1").innerHTML = Winner;
  document.getElementById("LBL2").innerHTML = text1;
  document.getElementById("LBL3").innerHTML = text2;
}

// Hauptprogramm
createImages();
