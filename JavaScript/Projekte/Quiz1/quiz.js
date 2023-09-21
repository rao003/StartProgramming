// Ereignis-Methoden

function button1Click() {
   
}
function button2Click() {

}
function button3Click() {
   
}

// Quiz-Klasse
class Quiz {
  constructor(max) {
    // Attribute
    this.question = [max];
    this.answer1  = [max];
    this.answer2  = [max];
    this.answer3  = [max];
    this.correct  = [max];
  }

  // Methoden
  collectQuests() {
    this.question[0] = "Wie heißt die Hauptstadt von China?"
    this.answer1[0] = "Peking";
    this.answer2[0] = "Shanghai";
    this.answer3[0] = "Singapur";
    this.correct[0] = 0;
    this.question[1] = "Wie heißt die Hauptstadt von Australien?"
    this.answer1[1] = "Austria";
    this.answer2[1] = "Cangaroo";
    this.answer3[1] = "Canberra";
    this.correct[1] = 2;
    this.question[2] = "Wie heißt die Hauptstadt von Rumänien?"
    this.answer1[2] = "Budapest";
    this.answer2[2] = "Bukarest";
    this.answer3[2] = "Beulenpest";
    this.correct[2] = 1;
  }
  showQuest(nr) {
    document.getElementById("LBL").innerHTML = this.question[nr];
    document.getElementById("BTN1").innerHTML = this.answer1[nr];
    document.getElementById("BTN2").innerHTML = this.answer2[nr];
    document.getElementById("BTN3").innerHTML = this.answer3[nr];
  }
}

// Hauptprogramm
const max = 3;  //ändern, wenn neue Fragen/Antworten dazukommen
myQuiz = new Quiz(max);
myQuiz.collectQuests();
myQuiz.showQuest(Math.floor(Math.random()*max));
