"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "white", "blue", "cyan", "green", "yellow", "red", "magenta"]; 
var x, y, z;

// Schwarzer Hintergrund
context.fillStyle = "black";
context.fillRect(0, 0, canvas.width, canvas.height);

// Bunt und eckig
for (var nr = 0; nr < 200; nr++) {
  context.beginPath();
  x = Math.floor(Math.random()*canvas.width);
  y = Math.floor(Math.random()*canvas.height);
  z = Math.floor(Math.random()*30);
  context.fillStyle = Color[Math.floor(Math.random()*Color.length)];
  context.fillRect(x, y, z, z);
  context.strokeStyle = "white";
  context.strokeRect(x, y, z, z);
}
