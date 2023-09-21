"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

// Farben-Array
var Color = ["gray", "black", "blue", "cyan", "green", "yellow", "red", "magenta"]; 

// Bunte Rechtecke
for (var nr = 0; nr < 60; nr++) {
  context.beginPath();
  context.rect(nr*4, nr*3, canvas.width-nr*8, canvas.height-nr*6);
  context.strokeStyle = Color[Math.floor(Math.random()*Color.length)];
  context.stroke();
}
