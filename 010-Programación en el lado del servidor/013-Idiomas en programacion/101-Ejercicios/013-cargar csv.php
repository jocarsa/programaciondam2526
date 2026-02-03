<?php

$rows = array_map('str_getcsv', file('idiomas.csv'));

var_dump($rows);

?>
