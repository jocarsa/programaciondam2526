# Actividad (30’): “Planificador de cuadras — versión exprés”

Crea un script llamado `planificador_cuadras.py` que calcule cuántas cuadras necesitas en una fecha dada, según el número de caballos y la capacidad de cada cuadra. Debe redondear **al alza** el número de cuadras, mostrar propiedades de la fecha y presentar un pequeño informe.

## Objetivos de aprendizaje

* Usar **métodos** y **propiedades** de objetos estándar (`datetime.date`, `date.year`, `date.weekday`, etc.). 
* Llamar a **métodos “estáticos”**/de módulo como `math.ceil`. 
* Manejar **entrada → cálculo → salida** con mensajes claros. 

## Requisitos funcionales

1. **Entrada de datos (por `input`)**

   * `caballos` (entero > 0).
   * `capacidad_por_cuadra` (entero > 0).
   * `fecha` en formato `YYYY-MM-DD`.
     (Estos tres inputs siguen el patrón de los ejercicios de entrada/cálculo/salida). 
2. **Cálculos**

   * `cuadras_necesarias = ceil(caballos / capacidad_por_cuadra)` usando `math.ceil`. 
   * Crear un objeto `date` con la fecha indicada y obtener:

     * `year`, `month`, `day`
     * `weekday()` (0–6) y `isoweekday()` (1–7)
       (Como en los ejemplos de propiedades de fecha). 
3. **Salida (informe)**

   * Línea resumen con caballos, capacidad y cuadras **redondeadas al alza**.
   * Bloque “Datos de la fecha” mostrando `YYYY-MM-DD`, `year`, `month`, `day`, `weekday`, `isoweekday`.
4. **Validaciones mínimas**

   * Si algún valor no es entero positivo, mostrar un mensaje y terminar.
   * Si la fecha no cumple el formato, mostrar mensaje y terminar.
5. **(Opcional, si te da tiempo)**

   * Mostrar si la fecha cae **entre semana** o **fin de semana** (usa `isoweekday()`).


