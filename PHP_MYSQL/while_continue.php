<?php
$max = 30;
$count = 0;
$increment = 3;

while($count < $max)
{
    $count += $increment;
    if($count >= 10 AND $count <= 15 )
    {
        echo "entre um e outro <br/>";
    continue;
    }
    echo "$count <br/> ";
    
}

?>