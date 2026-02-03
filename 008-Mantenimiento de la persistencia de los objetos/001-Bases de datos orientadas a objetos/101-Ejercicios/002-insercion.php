<?php
// sudo apt install php-mongodb
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

$order = [
  'order_number' => 'MT-2026-000123',
  'status' => 'paid',
  'currency' => 'EUR'
];

$order['_created_at'] = new MongoDB\BSON\UTCDateTime((int)(microtime(true) * 1000));

$manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

$bulk = new MongoDB\Driver\BulkWrite();
$id = $bulk->insert($order);

$manager->executeBulkWrite('microtienda.pedidos', $bulk);

echo json_encode([
  'ok' => true,
  'id' => (string)$id
], JSON_UNESCAPED_UNICODE);
