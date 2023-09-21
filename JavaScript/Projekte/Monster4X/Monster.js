// Klassen
class Monster {
  constructor(Name, Nature) {
    // Attribute
    this.name = Name;
    this.nature = Nature;
  }

  // get-set
  get newName() {
    return this.name;
  }
  set newName(Name) {
    this.name = Name;
  }
  get newNature() {
    return this.nature;
  }
  set newNature(Nature) {
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
