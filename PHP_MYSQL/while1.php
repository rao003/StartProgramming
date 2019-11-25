<?php
$valor1 = 0;
$valor2 = 0;

$min = -30;
$max = 30;

while($valor1 < $max AND $valor2 > $min)
{
    echo "Valor 1: $valor1 ; Valor2: $valor2 <br>";
    $valor1 += 2;
    $valor2 -= 3;
}


?>