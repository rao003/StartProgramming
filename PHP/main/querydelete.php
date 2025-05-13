<?php

include('connect.php');

$sql = "DELETE FROM  `rkamtest`.`sales1` WHERE  `sales1`.`id` =8";

// Performs the $sql query on the server to insert the values
if ($conn->query($sql) === TRUE) {
  echo 'users entry deleted successfully';
}
else {
 echo 'Error: '. $conn->error;
}

$conn->close();

?>
