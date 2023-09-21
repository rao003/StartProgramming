// Klassen
class Monster {
  constructor(Name, Nature) {
    // Attribute
    this.name = Name;
    this.nature = Nature;
  }
  // Methoden
  type() { return("Monster"); }
  show() {
    document.getElementById("LBL1").innerHTML = "Name : " + this.name;
    document.getElementById("LBL2").innerHTML = "Wesen: " + this.nature;
    document.getElementById("LBL3").innerHTML = "Typ:   " + this.type();
  }
}
class GMonster extends Monster {
  type() { return("Geistes-Monster"); }
}
class SMonster extends Monster {
  type() { return("Seelen-Monster"); }
}
