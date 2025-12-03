
## **Actividad Práctica: "Factura con IVA y Descuento"**
**Objetivo:**
Crear un programa en Python que calcule el total de una factura aplicando IVA y un descuento fijo, usando **solo los conceptos de la Unidad 1**.

---

### **Enunciado**
Desarrolla un programa llamado **`factura_con_iva_descuento.py`** que:
1. Pida al usuario el **nombre del cliente** y el **precio bruto** de un producto.
2. Aplique un **IVA del 21%** y un **descuento fijo de 10 €** (solo si el precio bruto es mayor o igual a 50 €).
3. Calcule y muestre:
   - Precio bruto.
   - IVA aplicado.
   - Descuento aplicado (si corresponde).
   - **Total a pagar**.
4. Documenta el código con comentarios y un docstring.

---

### **Requisitos Detallados**
#### 1. **Variables y Constantes**
   - Usa variables para:
     - `nombre_cliente` (cadena).
     - `precio_bruto` (decimal).
     - `IVA` (constante = 0.21).
     - `DESCUENTO` (constante = 10.0).
   - Usa literales para los mensajes de salida.

#### 2. **Entrada de Datos**
   - Usa `input()` para pedir el nombre y el precio bruto.
   - Convierte el precio a `float`.

#### 3. **Cálculos**
   - Calcula el **IVA aplicado**: `precio_bruto * IVA`.
   - Calcula el **subtotal con IVA**: `precio_bruto + IVA aplicado`.
   - Aplica el descuento **solo si el precio bruto es ≥ 50 €** (usa operadores de comparación y una variable booleana para guardar si se aplica o no).
   - Calcula el **total a pagar**:
     - Si se aplica descuento: `subtotal_con_iva - DESCUENTO`.
     - Si no: `subtotal_con_iva`.

#### 4. **Salida de Datos**
   - Muestra un resumen con:
     - Nombre del cliente.
     - Precio bruto.
     - IVA aplicado.
     - Descuento aplicado (o "0 €" si no se aplica).
     - **Total a pagar**.

#### 5. **Documentación**
   - Docstring con autor, versión y descripción.
   - Comentarios para cada sección del código.

---

