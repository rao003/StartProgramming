<?php
// Verbindung zur Datenbank aufbauen.
include "verbinden.php";

try {
 // Anlegen der Datenbank-Tabelle.
 $db->exec("CREATE TABLE IF NOT EXISTS `nachrichten` (
            `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `titel` VARCHAR(80) NOT NULL,
            `autor` varchar(30) NOT NULL DEFAULT 'Werner',
            `nachricht` TEXT NOT NULL,
            `kategorie` VARCHAR(25) NOT NULL,
            `anzeige` TINYINT(1) NOT NULL,
            `datum` DATE NOT NULL
           ) ENGINE = MYISAM DEFAULT CHARSET=utf8");

 echo '<p>&#9655; Die Datenbank-Tabelle wurde angelegt.<br>
 <a href="eintragen.php">Erste Nachricht eintragen</a></p>';
}
catch (PDOException $e) {
 // Bei einem Fehler eine Nachricht ausgeben.
 exit('<p>&#9655; Fehler beim anlegen der Datenbank-Tabelle!</p>' .
  $e->getMessage());
}
?>