// Ereignis-Methoden

function itemClick() {
  if (document.getElementById("Nr1").checked)
    myQuiz.showResult(0);
  if (document.getElementById("Nr2").checked)
    myQuiz.showResult(1);
  if (document.getElementById("Nr3").checked)
    myQuiz.showResult(2);
}

// neue Frage
function newClick() {
  if (myQuiz.task >= myQuiz.max) {
    myQuiz.finishQuests();
    return;
  }
  var nr = Math.floor(Math.random()*myQuiz.max);
  while (myQuiz.done[nr])
    nr = Math.floor(Math.random()*myQuiz.max);
  myQuiz.showQuest(nr);
  document.getElementById("Nr1").checked = false;
  document.getElementById("Nr2").checked = false;
  document.getElementById("Nr3").checked = false;
}

// Dateiinhalt einlesen
function readFile(input) {
  var file = input.files[0];
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function() {
    // in Zeilen unterteilen, Quiz-Zahl ermitteln
    var textFile = reader.result.split('\n');
    var max = Math.floor(textFile.length/5);
    // Daten sammeln und anzeigen
    myQuiz.collectQuests(textFile);
    myQuiz.showQuest(Math.floor(Math.random()*max));
  };
  reader.onerror = function() {
    document.write(reader.error);
  };
}

// Quiz-Klasse
class Quiz {
  constructor() {
    // Attribute
    this.question = [];
    this.answer1  = [];
    this.answer2  = [];
    this.answer3  = [];
    this.correct  = [];
    this.done = [];
    this.count = 0;
    this.task = 0;
  }

  // Methoden
  collectQuests(text) {
    // Anzahl der Elemente
    this.max = Math.floor(text.length/5);
    // Quiz-Aufgaben verteilen
    for (var nr = 0; nr < this.max; nr++) {
      this.question[nr] = text[nr*5];
      this.answer1[nr]  = text[nr*5+1];
      this.answer2[nr]  = text[nr*5+2];
      this.answer3[nr]  = text[nr*5+3];
      this.correct[nr]  = text[nr*5+4];
      this.done[nr] = false;
    }
  }
  showQuest(nr) {
    // Nr. der Quiz-Aufgabe
    this.current = nr;
    document.getElementById("LBL").innerHTML = this.question[nr];
    document.getElementById("BTN1").innerHTML = this.answer1[nr] + "<br>";
    document.getElementById("BTN2").innerHTML = this.answer2[nr] + "<br>";
    document.getElementById("BTN3").innerHTML = this.answer3[nr] + "<br>";
  }
  showResult(choice) {
    // wenn bereits erledigt, Methode verlassen
    if (this.done[this.current]) return;
    // Lösungs-Nr. mit Quiz-Nr. vergleichen
    if (choice == Number(this.correct[this.current])) {
      document.getElementById("LBL").innerHTML = "RICHTIG";
      this.count++;
    }
    else
      document.getElementById("LBL").innerHTML = "FALSCH";
    // aktueller Spielstand
    var text = this.count + " von " + this.max + " Aufgaben richtig."
    document.getElementById("RES").innerHTML = text;
    // eine Aufgabe mehr erledigt
    this.done[this.current] = true;
    this.task++;
  }
  finishQuests() {
    document.getElementById("LBL").innerHTML = "ENDE";
    document.getElementById("BTN1").innerHTML = "Keine";
    document.getElementById("BTN2").innerHTML = "Fragen";
    document.getElementById("BTN3").innerHTML = "mehr";
  }
}

// Hauptprogramm
myQuiz = new Quiz();
// Spiel startet nach Laden der Daten
