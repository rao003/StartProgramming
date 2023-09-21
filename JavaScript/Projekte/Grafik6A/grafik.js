"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "white", "blue", "cyan", "green", "yellow", "red", "magenta"]; 
var x,y, radius;

// Schwarzer Hintergrund
context.fillStyle = "black";
context.fillRect(0, 0, canvas.width, canvas.height);

// Bunter "Sternenhimmel"
for (var nr = 0; nr < 2000; nr++) {
  context.beginPath();
  x = Math.floor(Math.random()*canvas.width);
  y = Math.floor(Math.random()*canvas.height);
  radius = 1;
  context.arc(x, y, radius, 0, 2*Math.PI);
  context.strokeStyle = Color[Math.floor(Math.random()*Color.length)];
  context.stroke();
}
