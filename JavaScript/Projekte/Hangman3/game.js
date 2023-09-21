"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Globale Variablen
var x = 20; var y = 20;
var width = 110; var height = 200;
var text = ""; var guess = [];
var hang = 0; var ok;
var quest = []; var max;
var over = false;

// Bilder sammeln
var image = [];
function createImages() {
  for (var nr = 0; nr < 7; nr++) {
    var img = new Image();
    if (nr == 0)
      img.src = "galgen.png";
    else 
      img.src = "hangman" + nr + ".png";
    image[nr] = img;
  }
  drawGallows();
}
// Galgen zeichnen
function drawGallows() {
  context.clearRect(x, y,  width+70, height+60);
  context.drawImage(image[0], x, y, width+70, height+60);
}

// Ereignis-Funktionen

function readFile(input) {
  var file = input.files[0];
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function() {
    // in Zeilen unterteilen, Anzahl ermitteln
    var textFile = reader.result.split('\n');
    max = textFile.length;
    // Wörter sammeln
    for (var nr = 0; nr < max; nr++) 
      quest[nr] = textFile[nr];
  };
  reader.onerror = function() {
    document.write(reader.error);
  };
}
function testLetter() {
  // wenn Raten vorbei, Funktion verlassen
  if (over) return;
  var choice = document.getElementById("INP").value;
  ok = false;
  // Buchstaben einzeln vergleichen
  for (var nr = 0; nr < text.length; nr++) {
    if (choice == text[nr]) {
      guess[nr] = choice;
      document.getElementById("LBL").innerHTML = guess;
      ok = true;
    }
  }
  // Wenn falsch geraten
  if (!ok) {
    hang++;
    context.drawImage(image[hang], x+65, y+25, width, height);
  }
  // wenn zu oft falsch geraten
  if (hang > 5) {
    document.getElementById("LBL").innerHTML = "TOT";
    context.clearRect(x+65, y+30, width, height);
    context.drawImage(image[hang], x+65, y+30, width, height);
    over = true;
  }
  // wenn alle Buchstaben richtig
  var all = "";
  for (var nr = 0; nr < guess.length; nr++)
    all = all + guess[nr];
  if (text.substr(0,text.length-1) == all)
    over = true;
}
function newWord() {
  drawGallows();
  // Zufälliges Wort
  text = quest[Math.floor(Math.random()*max)];
  guess = [];
  guess[0] = text[0];
  for (var nr = 1; nr < text.length-1; nr++)
    guess[nr] = "?";
  document.getElementById("LBL").innerHTML = guess;
  hang = 0; over = false;
}

// Hauptprogramm
createImages();
