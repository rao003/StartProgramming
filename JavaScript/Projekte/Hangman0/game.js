//"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Globale Variablen
var x = 20; var y = 20;
var width = 110; var height = 200;
var text = ""; var guess = [];
var hang = 0; var ok;

// Ereignis-Funktionen

function testLetter() {
  var choice = document.getElementById("INP").value;
  ok = false;
  for (var nr = 0; nr < text.length; nr++) {
    if (choice == text[nr]) {
      guess[nr] = choice;
      document.getElementById("LBL").innerHTML = guess;
      ok = true;
    }
  }
}
function newWord() {
  text = "hangman";
  guess[0] = text[0];
  for (var nr = 1; nr < text.length; nr++)
    guess[nr] = "?";
  document.getElementById("LBL").innerHTML = guess;
  hang = 0;
}
