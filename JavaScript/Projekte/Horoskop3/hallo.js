// Ereignis-Methode

function itemClick() {
  var monat = "";
  if (document.getElementById("Nr1").checked) monat = "Januar";
  if (document.getElementById("Nr2").checked) monat = "Februar";
  if (document.getElementById("Nr3").checked) monat = "März";
  if (document.getElementById("Nr4").checked) monat = "April";
  if (document.getElementById("Nr5").checked) monat = "Mai";
  if (document.getElementById("Nr6").checked) monat = "Juni";
  if (document.getElementById("Nr7").checked) monat = "Juli";
  if (document.getElementById("Nr8").checked) monat = "August";
  if (document.getElementById("Nr9").checked) monat = "September";
  if (document.getElementById("Nr10").checked) monat = "Oktober";
  if (document.getElementById("Nr11").checked) monat = "November";
  if (document.getElementById("Nr12").checked) monat = "Dezember";
  document.getElementById("LBL").innerHTML = monat;
}
