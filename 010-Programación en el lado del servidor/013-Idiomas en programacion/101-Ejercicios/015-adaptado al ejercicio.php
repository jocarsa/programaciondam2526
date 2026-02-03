<?php

$csv = array_map('str_getcsv', file('idiomas.csv'));
$header = array_shift($csv); // e.g. ['clave','es','en']

foreach ($csv as $row) {
    $data = array_combine($header, $row);
    $clave = $data['clave'];

    foreach ($data as $lang => $value) {
        if ($lang === 'clave') continue;

        // escape quotes safely
        $value = addslashes($value);

        echo "\$idioma['{$lang}']['{$clave}'] = \"{$value}\";\n";
    }

    echo "\n";
}
