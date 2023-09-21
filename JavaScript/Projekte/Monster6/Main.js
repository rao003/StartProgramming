"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d"); 

// Bilder sammeln
var fname = ["frank.png", "albert.png", "sigmund.png"];
var image = [];
function createImages() {
  for (var nr = 0; nr < 3; nr++) {
    var img = new Image();
    img.src = fname[nr];
    image[nr] = img;
  }
}
// Globale Variablen
var x = 185; var y = 25;
var width = 200;

//Ereignis-Funktionen

function showMonster() {
  Frank.show();
  context.drawImage(image[0], x, y, width, width);
}
function showGMonster() {
  Albert.show();
  context.drawImage(image[1], x, y, width, width);
}
function showSMonster() {
  Sigmund.show();
  context.drawImage(image[2], x, y, width, width);
}

//Hauptprogramm
var Frank = new Monster("Frankie", "ungewöhnlich");
var Albert = new GMonster("Bertie", "nachdenklich");
var Sigmund = new SMonster("Sigi", "einfühlsam");
createImages();
