<?php

$db_host = 'localhost'; // Server Name

$db_user = 'id9226424_vhs'; // Username

$db_pass = 'start123'; // Password

$db_name = 'id9226424_vhs'; // Database Name


$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

if (!$conn) {

	die ('Failed to connect to MySQL: ' . mysqli_connect_error());

}

echo "Connected successfully";

?>