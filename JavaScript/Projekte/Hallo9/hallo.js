// Ereignis-Methode

function itemClick() {
  var nr = document.getElementById("LST").selectedIndex;
  switch (nr) {
    case 0: 
      document.getElementById("LBL").innerHTML = "Das ist ja toll!"; break;
    case 1:
      document.getElementById("LBL").innerHTML = "Das freut mich!"; break;
    case 2:
      document.getElementById("LBL").innerHTML = "Das tut mir leid!"; break;
    case 3:
      document.getElementById("LBL").innerHTML = "Das ist ja schlimm!"; break;
    case 4:
      document.getElementById("LBL").innerHTML = "Naja ..."; break;
    case 5:
      document.getElementById("LBL").innerHTML = "Wenn du meinst ...";
  }
}
