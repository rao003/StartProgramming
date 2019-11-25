<?php

$counter = "texto";

$handle = fopen("counter2.txt", w);
fwrite ($handle, $counter);
fclose ($handle);

echo "o valor $counter foi salvo";

?>