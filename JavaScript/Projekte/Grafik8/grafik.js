"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

var image = new Image();
image.src = "ball1.png";
image.onload = function () {
  context.drawImage(image, 50, 50, 150, 150);
}
