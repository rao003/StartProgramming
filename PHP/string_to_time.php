<?php
//This PHP Example code shows how to add one hour to a date object

$todayDate = date("Y-m-d g:i a");// current date
$currentTime = time($todayDate); //Change date into time


//echo "<br>".$currentTime;
//Add one hour equavelent seconds 60*60

$timeAfterOneHour = $currentTime+60*60;

echo "<br>".$timeAfterOneHour;
echo "<br>Current Date and Time: ".date("Y-m-d H:i:s",$currentTime);
echo "<br>Date and Time After adding one hour: ".date("Y-m-d H:i:s",$timeAfterOneHour);

?>