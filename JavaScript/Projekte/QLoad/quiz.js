// Ereignis-Methode

function readFile(input) {
  var file = input.files[0];
  var reader = new FileReader();
  reader.readAsText(file);
  reader.onload = function() {  
    var textFile = reader.result;
    // gesamter Text
    document.write(textFile + "<br>" + "<br>");
    // in Zeilen unterteilt
    textFile = textFile.split('\n');
    for (var nr = 0; nr < textFile.length; nr++)
      document.write(textFile[nr] + "<br>");
    //document.write("<br>" + textFile.length + " Zeilen");
  };
  reader.onerror = function() {
    document.write(reader.error);
  };
}  
 
