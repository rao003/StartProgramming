<!DOCTYPE html>
<html lang="de">
 <head>
  <meta charset="UTF-8">
  <title>Nachrichten suchen</title>

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
 <a href="auslesen.php">Nachrichten</a> |
 <a href="eintragen.php">Eintragen</a> |
 <a href="bearbeiten.php">Bearbeiten</a> |
 <u>Suchen</u>
</nav>

<form action="suchen.php" method="get">
 <p>
  <input type="text" name="suchbegriff" required="required"
   value="<?php echo isset($_GET["suchbegriff"]) ? $_GET["suchbegriff"] : '' ?>">
  <input type="submit" name="suche" value="los">
 </p>
</form>

<?php
// Wurde eine Suchanfrage über GET gesendet?
if (isset($_GET["suche"])) {

 // Leerzeichen im Suchbegriff löschen.
 $_GET["suchbegriff"] = trim($_GET["suchbegriff"]);

 // Suchbegriff größer als 3 Zeichen?
 if (strlen($_GET["suchbegriff"]) >= 4) {

  // Verbindung zur Datenbank aufbauen.
  include "verbinden.php";

  // Nachrichten auslesen
  // prepare() führt die SQL-Anweisung aus, die eine
  // Ergebnismenge als PDO-Statement Objekt zurück gibt.
  $select = $db->prepare("SELECT *
                          FROM `nachrichten`
                          WHERE (`titel` LIKE :suchbegriff OR
                                 `autor` LIKE :suchbegriff OR
                                 `nachricht` LIKE :suchbegriff OR
                                 `kategorie` LIKE :suchbegriff)
                             AND `anzeige` = '1'
                          ORDER BY `datum` DESC
                          LIMIT 0, 25");

  // $select->bindValue() bindet einen Wert an den angegebenen Variablennamen
  // (der Platzhalter wird mit dem Inhalt der GET-Variable ersetzt).
  $select->bindValue(':suchbegriff', '%' . $_GET["suchbegriff"] . '%');

  // $select->execute() führt die vorbereitete Anweisung aus.
  if ($select->execute() == false) {
   // Gibt bei einer fehlerhaften Anweisung eine SQL-Fehlermeldung aus.
   print_r($select->errorInfo());
  }

  // $select->fetchAll() gibt ein Array mit allen Datensätzen zurück.
  $nachrichten = $select->fetchAll();

  // Anzahl der Nachrichten überprüfen
  $AnzahlNachrichten = $select->rowCount();
  if ($AnzahlNachrichten > 0) {
   echo '<p>&#9655; ' . $AnzahlNachrichten .
    ($AnzahlNachrichten == 1 ? ' Nachricht' : ' Nachrichten') . ' gefunden.</p>';

   // Die gefundenen Nachrichten über eine Foreach-Schleife ausgeben.
   foreach ($nachrichten as $nachricht) {
    sscanf($nachricht['datum'], "%4s-%2s-%2s", $jahr, $monat, $tag);
    echo '<p><small>' . $tag . '.' . $monat . '.' . $jahr .
     '</small> - <b>' . $nachricht['titel'] . '</b><br> Autor: <em>' .
     $nachricht['autor'] . '</em><br> Kategorie: ' .
     $nachricht['kategorie'] . '<br>' .
     nl2br($nachricht['nachricht']) . '</p>';
   } 
  }
  else {
   echo '<p>&#9655; Es wurden keine Nachrichten gefunden!</p>';
  }
 }
 else {
  echo '<p>&#9655; Suchbegriff mit mind. 4 Zeichen!</p>';
 }
}
?>

</body>
</html>