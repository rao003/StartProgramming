<?php

// Check for form submission
if (isset($_POST['name']) && isset($_POST['item']) && isset($_POST['date']) && isset($_POST['amount']) && isset($_POST['comentario'])) {
  // remove tags and whitespace from the beginning and end of form data
  $_POST = array_map("strip_tags", $_POST);
  $_POST = array_map("trim", $_POST);


include('connect.php');

    // store the values in an Array, escaping special characters for use in the SQL statement
    $adds['name'] = $conn->real_escape_string($_POST['name']);
    $adds['item'] = $conn->real_escape_string($_POST['item']);
    $adds['date'] = $conn->real_escape_string($_POST['date']);
     $adds['amount'] = $conn->real_escape_string($_POST['amount']);
    $adds['comentario'] = $conn->real_escape_string($_POST['comentario']);


    // sql query for INSERT INTO users
    $sql = "INSERT INTO `sales1` (`name`, `item`, `date`, `amount`, `comentario`) VALUES
    ('". $adds['name']. "', '". $adds['item']. "', '". $adds['date']. "', '". $adds['amount']. "', '". $adds['comentario']. "')";

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
