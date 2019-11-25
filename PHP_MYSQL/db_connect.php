<?php

include "db_connect.inc.php";

$query = "select * from Mitarbeiter";

$result = mysqli_query($conn, $query);

while($dsatz = mysqli_fetch_assoc($result))
{
   echo $dsatz["name"] . " <br>,".
   $dsatz["vorname"] . "<br>,".
   $dsatz["personalnummer"] . "<br>,".
   $dsatz["gehalt"] . "<br>,".
   $dsatz["geburstag"] . "";
   
}





?>
