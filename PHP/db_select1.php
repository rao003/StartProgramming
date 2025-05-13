<?php

include "db.php";

$query = "select * from EmployeeSalary";

$result = mysqli_query($conn, $query);

while($dsatz = mysqli_fetch_assoc($result))
{
   echo $dsatz["EmployeeID"] . ",".
   $dsatz["JobTitlee"] . ",".

   $dsatz["Salary"] . "";
   
}





?>
