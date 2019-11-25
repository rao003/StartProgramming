<?php

$handle = fopen ("counter2.txt", "r");

while ($conteudo = fgets ($handle, 4096))
{
    echo "<li> $conteudo";
}

fclose($handle)

?>