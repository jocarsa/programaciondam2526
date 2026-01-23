<?php

$conn = mysqli_connect(
    "localhost",
    "empresa2026",
    "Empresa2026$",
    "empresa2026"
);

if (!$conn) {
    die("Error de conexión: " . mysqli_connect_error());
}

mysqli_set_charset($conn, "utf8mb4");

$result = mysqli_query($conn, "SELECT * FROM clientes");

while ($row = mysqli_fetch_assoc($result)) {
    print_r($row);
}

mysqli_close($conn);
