// Ereignis-Methoden

function button1Click() {
  
}
function button2Click() {

}
function button3Click() {
   
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
  }

  // Methoden
  collectQuests(text) {
    this.max = Math.floor(text.length/5);
    for (var nr = 0; nr < this.max; nr++) {
      this.question[nr] = text[nr*5];
      this.answer1[nr]  = text[nr*5+1];
      this.answer2[nr]  = text[nr*5+2];
      this.answer3[nr]  = text[nr*5+3];
      this.correct[nr]  = text[nr*5+4];
    }
  }
  showQuest(nr) {
    document.getElementById("LBL").innerHTML = this.question[nr];
    document.getElementById("BTN1").innerHTML = this.answer1[nr];
    document.getElementById("BTN2").innerHTML = this.answer2[nr];
    document.getElementById("BTN3").innerHTML = this.answer3[nr];
  }
}

// Hauptprogramm
myQuiz = new Quiz();
// Spiel startet nach Laden der Daten
