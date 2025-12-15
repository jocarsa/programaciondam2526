CREATE TABLE producto (
  id INT,
  nombre_producto VARCHAR(255),
  descripcion VARCHAR(255),
  precio VARCHAR(255),
  stock VARCHAR(255),
  imagen VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE cliente (
  id INT,
  nombre_cliente VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255),
  direccion VARCHAR(255),
  telefono VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE pedido (
  id INT,
  fecha VARCHAR(255),
  cliente_id INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_pedido_1 FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE lineaspedido (
  id INT,
  pedido_id INT,
  cantidad VARCHAR(255),
  producto_id INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_lineaspedido_1 FOREIGN KEY (producto_id) REFERENCES producto(id),
  CONSTRAINT fk_lineaspedido_2 FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
