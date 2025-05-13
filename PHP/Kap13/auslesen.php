<!DOCTYPE html>
<html lang="de">
 <head>
  <meta charset="UTF-8">
  <title>Nachrichten</title>

  <style>
  body {
   font-family: Verdana, Arial, Sans-Serif;
   background-color: Whitesmoke;
  }

  a:link, a:visited {
   color: Royalblue;
   text-decoration: None;
  }
  </style>

 </head>
<body>

<nav>
 <u>Nachrichten</u> |
 <a href="eintragen.php">Eintragen</a> |
 <a href="bearbeiten.php">Bearbeiten</a> |
 <a href="suchen.php">Suchen</a>
</nav>

<?php
// Verbindung zur Datenbank aufbauen
include "verbinden.php";

// Anzahl der Datensätze (Nachrichten) pro Seite
$DatensaetzeSeite = 2;

// Anzahl der Datensätze ermitteln
$AnzahlDatensaetze = $db->query("SELECT COUNT(*) FROM `nachrichten` WHERE `anzeige` = '1'")->fetchColumn(0);

// Sind Datensätze vorhanden?
if ($AnzahlDatensaetze > 0) {

 // Die Anzahl der Seiten ermitteln
 $AnzahlSeiten = ceil($AnzahlDatensaetze / $DatensaetzeSeite);

 // Die aktuelle Seite ermitteln
 $AktuelleSeite = isset($_GET["seite"]) ? $_GET["seite"] : 1;

 // Den Wert überprüfen und ggf. ändern
 $AktuelleSeite = ctype_digit($AktuelleSeite) ? $AktuelleSeite : 1;
 $AktuelleSeite = $AktuelleSeite < 1 || $AktuelleSeite > $AnzahlSeiten ? 1 : $AktuelleSeite;

 // Den Versatz ermitteln
 $Versatz = $AktuelleSeite * $DatensaetzeSeite - $DatensaetzeSeite;
 
 // Alle Datensätze auslesen die in der DB-Spalte `anzeige` den Wert 1 haben.
 // Mit LIMIT die Ausgabe der Datensätze begrenzen (Versatz und Datensätze pro Seite).
 $select = $db->prepare("SELECT `titel`, `autor`, `nachricht`, `kategorie`, `datum`
                         FROM `nachrichten`
                         WHERE `anzeige` = '1'
                         ORDER BY `datum` DESC
                         LIMIT :versatz, :DatensaetzeSeite");
 $select->bindParam(':versatz', $Versatz, PDO::PARAM_INT);
 $select->bindParam(':DatensaetzeSeite', $DatensaetzeSeite, PDO::PARAM_INT);
 $select->execute();
 $nachrichten = $select->fetchAll();

 // Ausgabe über eine Foreach-Schleife
 foreach ($nachrichten as $nachricht) {
  // Mit sscanf() wird das Format des Datums in die Variablen $jahr, $monat und $tag extrahiert.
  sscanf($nachricht['datum'], "%4s-%2s-%2s", $jahr, $monat, $tag);

  echo '<p><small>' . $tag . '.' . $monat . '.' . $jahr .
   '</small> - <b>' . $nachricht['titel'] . '</b><br>' .
   ' Kategorie: ' . $nachricht['kategorie'] . '<br>' .
   ' Autor: <em>' . $nachricht['autor'] . '</em><br>' .
   nl2br($nachricht['nachricht']) . '</p>';
 }

 // Formular.- und Blätterfunktion (Wer sich da auskennt bekommt einen Preis verliehen ;)
 echo '<form action="auslesen.php" method="GET" autocomplete="off">' . 
  (($AktuelleSeite - 1) > 0 ?
    '<a href="?seite=' . ($AktuelleSeite - 1) . '">&#9668;</a>' :
    ' &#9668;') .
 ' <label>Seite <input type="text" value="' . $AktuelleSeite . '" name="seite" size="3"' .
 ' title="Seitenzahl eingeben und die Eingabetaste drücken."> von ' . $AnzahlSeiten . '</label>' .
  (($AktuelleSeite + 1) <= $AnzahlSeiten ?
    ' <a href="?seite=' . ($AktuelleSeite + 1) . '">&#9658;</a>' :
    ' &#9658;') .
 '</form>';
}
else {
 echo '<p>Keine Nachrichten vorhanden!</p>';
}
?>

</body>
</html>