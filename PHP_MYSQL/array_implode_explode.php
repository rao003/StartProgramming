<?php
$texto = "joao,maria,jose";
$nomes = explode(",", $texto);

echo "<pre>"; var_dump($nomes); echo "</pre>";

$nomes[1] = "lisa";

$texto = implode(",", $nomes);
echo $texto;

?>