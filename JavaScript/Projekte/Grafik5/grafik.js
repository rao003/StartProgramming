"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "black", "blue", "cyan", "green", "yellow", "red", "magenta"]; 
var x, y;

// Viele bunte Hallos
for (var nr = 0; nr < 30; nr++) {
  x = Math.floor(Math.random()*canvas.width);
  y = Math.floor(Math.random()*canvas.height);
  context.beginPath();
  context.font = "30px Arial";
  context.fillStyle = Color[Math.floor(Math.random()*Color.length)];
  context.fillText("Hallo", x,y);
  context.strokeText("Hallo", x,y);
}
