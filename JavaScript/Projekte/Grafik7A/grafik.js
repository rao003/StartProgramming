"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Globale Variablen
var active = false;
var drawing = false;

// Ereignisse und Funktionen
canvas.onmousedown = function() {
  active = true;
}
canvas.onmouseup = function() {
  active = false;
  drawing = false;
}
canvas.onmousemove = function(event) {
  var x, y;
  if (!active) return;
  // Mausposition ermitteln
  x = event.offsetX;
  y = event.offsetY;
  // "Zeichenstift" setzen oder sichtbar bewegen
  if (!drawing) {
    context.beginPath();
    context.moveTo(x, y);
    drawing = true;
  }
  else {
    context.lineTo(x, y);
    context.stroke();
  }
}
