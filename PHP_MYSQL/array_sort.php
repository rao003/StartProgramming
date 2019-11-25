<?php

$nomes = array("klaus", "joao", "Maria", "jose");

sort($nomes);
echo implode (",<br>", $nomes);

natcasesort($nomes);
echo implode (",", $nomes);

?>