<?php
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

try {
    $json = file_get_contents('php://input');
    if ($json === false || trim($json) === '') {
        throw new RuntimeException('Body JSON vacío');
    }

    $document = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
    if (!is_array($document)) {
        throw new RuntimeException('JSON no es un objeto/array válido');
    }

    $document['_created_at'] = new MongoDB\BSON\UTCDateTime((int)(microtime(true) * 1000));

    $manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

    $bulk = new MongoDB\Driver\BulkWrite();
    $id = $bulk->insert($document);

    $manager->executeBulkWrite('microtienda.pedidos', $bulk);

    echo json_encode(['ok' => true, 'id' => (string)$id], JSON_UNESCAPED_UNICODE);

} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => $e->getMessage()], JSON_UNESCAPED_UNICODE);
}
