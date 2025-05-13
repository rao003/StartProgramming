<?php

$names = array("joao", "maria", "jose");

echo "nomes por virgula <br>";
$namesStr = implode(",", $names);
echo $namesStr;

echo "<br><br>";
echo "nome por linha: <br>";
echo implode("<br>", $names);



?>