"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "black", "blue", "cyan", "green", "yellow", "red", "magenta"]; 

// Bunte Kreise
for (var nr = 0; nr < 40; nr++) {
  context.beginPath();
  context.arc(canvas.width/2, canvas.height/2, canvas.height/2-nr*4, 0, 2*Math.PI);
  context.strokeStyle = Color[Math.floor(Math.random()*Color.length)];
  context.stroke();
}
