<?php

include "db_connect.inc.php";

$query = "select * from falken";

$result = mysqli_query($conn, $query);

while($dsatz = mysqli_fetch_assoc($result))
{
   echo $dsatz["id"] . ",".
   $dsatz["name"] . ",".
   $dsatz["rasse"] . ",".
   $dsatz["alterTier"] . "";
   
}





?>

