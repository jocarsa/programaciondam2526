<?php
// sudo apt install php php-mysql
// sudo systemctl restart apache2
// sudo apt install php-sqlite3
// En windows, XAMPP lleva preinstalado, pero desactivado SQLite
// LA solución es activarlo descomentando la linea en php.ini


// Conexión a la base de datos SQLite
$db = new PDO("sqlite:empresa2026.db");

// Opcional: obtener resultados como arrays asociativos
// $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

$sql = "SELECT * FROM clientes";
$stmt = $db->query($sql);

foreach ($stmt as $row) {
    print_r($row);
}

// Cerrar conexión
$db = null;
