"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "black", "blue", "cyan", "green", "yellow", "red", "magenta"]; 

// Lauter bunte Linien
for (var nr = 0; nr < 105; nr++) {
  context.beginPath();
  context.moveTo(0, nr*4);
  context.lineTo(canvas.width, canvas.height-nr*4);
  context.moveTo(nr*6, 0);
  context.lineTo(canvas.width-nr*6, canvas.height);
  context.strokeStyle = Color[Math.floor(Math.random()*Color.length)];
  context.stroke();
}
