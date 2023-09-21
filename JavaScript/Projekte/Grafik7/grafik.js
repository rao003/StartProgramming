"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Globale Variablen
var active = false;
var drawing = false;

// Event-Handler
canvas.addEventListener("mousedown", doMouseDown, false);
canvas.addEventListener("mouseup", doMouseUp, false);
canvas.addEventListener("mousemove", moveMouse, false);

// Ereignis-Funktionen
function doMouseDown() {
  active = true;
}
function doMouseUp() {
  active = false;
  drawing = false;
}
function moveMouse(event) {
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
