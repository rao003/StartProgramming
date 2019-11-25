<?php
$max = 30;
$count = 0;
$increment = 3;

while($count < $max)
{
    if($count == 20)
    {
        echo "paramos no 10";
    break;
    }
    echo "$count , ";
    $count += $increment;
}

?>