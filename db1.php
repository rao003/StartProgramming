<?php

$db_host = 'raspberrypilocalhost'; // Server Name

$db_user = 'phpuser'; // Username

$db_pass = 'Ig86N3tUa9'; // Password

$db_name = 'phptest'; // Database Name



$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

if (!$conn) {

	die ('Failed to connect to MySQL: ' . mysqli_connect_error());

}

echo "Connected successfully";

?>