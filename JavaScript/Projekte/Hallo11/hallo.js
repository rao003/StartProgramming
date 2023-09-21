// Ereignis-Methode

function itemClick() {
  var antwort = "";
  if (document.getElementById("Nr1").checked)
    antwort = "Das ist ja toll!";
  if (document.getElementById("Nr2").checked)
    antwort = "Das freut mich!";
  if (document.getElementById("Nr3").checked)
    antwort = "Das tut mir leid!";
  if (document.getElementById("Nr4").checked)
    antwort = "Das ist ja schlimm!";
  if (document.getElementById("Nr5").checked)
    antwort = "Naja ...";
  if (document.getElementById("Nr6").checked)
    antwort =  "Wenn du meinst ...";
  document.getElementById("LBL").innerHTML = antwort;
  var scope = "";
  if (document.getElementById("Nr7").checked) scope = scope + " Seele ";
  if (document.getElementById("Nr8").checked) scope = scope + " Geist ";
  if (document.getElementById("Nr9").checked) scope = scope + " Körper ";
  document.getElementById("LBLX").innerHTML = scope; 
}



