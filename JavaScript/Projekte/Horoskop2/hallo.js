// Ereignis-Methode

function itemClick() {
  var nr = document.getElementById("LST").selectedIndex;
  switch (nr) {
    case 0: 
      document.getElementById("LBL").innerHTML = "Januar"; break;
    case 1:
      document.getElementById("LBL").innerHTML = "Februar"; break;
    case 2:
      document.getElementById("LBL").innerHTML = "März"; break;
    case 3:
      document.getElementById("LBL").innerHTML = "April"; break;
    case 4:
      document.getElementById("LBL").innerHTML = "Mai"; break;
    case 5:
      document.getElementById("LBL").innerHTML = "Juni"; break;
    case 6:
      document.getElementById("LBL").innerHTML = "Juli"; break;
    case 7:
      document.getElementById("LBL").innerHTML = "August"; break;
    case 8:
      document.getElementById("LBL").innerHTML = "September"; break;
     case 9:
      document.getElementById("LBL").innerHTML = "Oktober"; break;
    case 10:
      document.getElementById("LBL").innerHTML = "November"; break;
    case 11:
      document.getElementById("LBL").innerHTML = "Dezember";
  }
}
