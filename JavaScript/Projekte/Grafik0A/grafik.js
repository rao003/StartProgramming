"use strict";
var canvas = document.getElementById("PIX");
var context = canvas.getContext("2d");

context.beginPath();
context.moveTo(100, 300);
context.lineTo(200, 100); context.lineTo(300, 300);
context.closePath();
context.stroke();
