-- 1) Quitar FKs (las que te bloquean)
ALTER TABLE lineaspedido DROP FOREIGN KEY fk_lineaspedido_1;
ALTER TABLE lineaspedido DROP FOREIGN KEY fk_lineaspedido_2;
ALTER TABLE pedido      DROP FOREIGN KEY fk_pedido_1;

-- 2) Poner AUTO_INCREMENT en las PK
ALTER TABLE producto    MODIFY id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE cliente     MODIFY id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE pedido      MODIFY id INT NOT NULL AUTO_INCREMENT;
ALTER TABLE lineaspedido MODIFY id INT NOT NULL AUTO_INCREMENT;

-- 3) Volver a crear FKs (mismo nombre y columnas)
ALTER TABLE pedido
  ADD CONSTRAINT fk_pedido_1
  FOREIGN KEY (cliente_id) REFERENCES cliente(id);

ALTER TABLE lineaspedido
  ADD CONSTRAINT fk_lineaspedido_1
  FOREIGN KEY (producto_id) REFERENCES producto(id);

ALTER TABLE lineaspedido
  ADD CONSTRAINT fk_lineaspedido_2
  FOREIGN KEY (pedido_id) REFERENCES pedido(id);
