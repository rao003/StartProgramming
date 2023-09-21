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
    document.write("Name : " + this.name + "<br>");
    document.write("Wesen: " + this.nature + "<br>");
    document.write("Typ:   " + this.type() + "<br><br>");
  }
}
class GMonster extends Monster {
  type() { return("Geistes-Monster"); }
}
class SMonster extends Monster {
  type() { return("Seelen-Monster"); }
}
