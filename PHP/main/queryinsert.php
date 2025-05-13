<?php

include('connect.php');


$sql = "INSERT INTO `sales1` (`name`, `item`, `date`, `amount`)
VALUES ('Nome', 'Television', '2019-06-07', 2500)";

// Performs the $sql query and get the auto ID
if ($conn->query($sql) === TRUE) {
  echo 'The auto ID is: '. $conn->insert_id;
}
else {
 echo 'Error: '. $conn->error;
}

$conn->close();

?>
