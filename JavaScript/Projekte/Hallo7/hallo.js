// Ereignis-Methode

function buttonClick() {
  var text = document.getElementById("INP").value;
  if (text == "gut") 
    document.getElementById("LBL").innerHTML = "Das freut mich!";
  if (text == "schlecht") 
    document.getElementById("LBL").innerHTML = "Das tut mir leid!";
}
