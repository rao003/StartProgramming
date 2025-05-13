<?php

const VERSAO = "1.0.5";
const MAXIMO = 10;

$email = "info@php.de";

echo "esta eh a versao".VERSAO;

if( strlen($email) > MAXIMO){
    echo "<br/> este email pode ser no maximo ".MAXIMO." eh de";
}
?>