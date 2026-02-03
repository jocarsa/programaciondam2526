<?php

$csv = array_map('str_getcsv', file('idiomas.csv'));
$header = array_shift($csv);

$idiomas = array_map(
    fn($row) => array_combine($header, $row),
    $csv
);

var_dump($idiomas);
