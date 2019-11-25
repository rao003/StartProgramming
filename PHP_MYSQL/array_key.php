<?php

$employee = array("klaus" =>"zabel", "arnie" => "baumeister");
$key = "arnie";

if(array_key_exists($key, $employee)){
    echo "este elemento $key tem o valor :".$employee[$key];
} else {
    echo "o array nao tem a chave $key";
}


?>