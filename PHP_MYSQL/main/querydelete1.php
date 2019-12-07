<?php

// Check for form submission
if (isset($_POST['id']) ) {
  // remove tags and whitespace from the beginning and end of form data
  $_POST = array_map("strip_tags", $_POST);
  $_POST = array_map("trim", $_POST);


include('connect.php');

    // store the values in an Array, escaping special characters for use in the SQL statement
    $adds['id'] = $conn->real_escape_string($_POST['id']);



    // sql query for INSERT INTO users
    $sql = "DELETE FROM `sales1` WHERE  `sales1`.`id` = ('". $adds['id']. "')";

    // Performs the $sql query on the server to insert the values
    if ($conn->query($sql) === TRUE) {
      echo 'JEZUZ TE AMA !';
    }
    else {
      echo 'Error: '. $conn->error;
    }

    $conn->close();
  }
  else {
    // else, if errors, it adds them in string format and print it
    echo implode('<br />', $erors);
  }


?>
