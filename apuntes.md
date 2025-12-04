# programaciondam2526

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Identificación de los elementos de un programa informático](#identificacion-de-los-elementos-de-un-programa-informatico)
  - [Estructura y bloques fundamentales](#estructura-y-bloques-fundamentales)
  - [Variables](#variables)
  - [Tipos de datos](#tipos-de-datos)
  - [Literales](#literales)
  - [Constantes](#constantes)
  - [Operadores y expresiones](#operadores-y-expresiones)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad)
- [Utilización de objetos](#utilizacion-de-objetos)
  - [Características de los objetos](#caracteristicas-de-los-objetos)
  - [Instanciación de objetos](#instanciacion-de-objetos)
  - [Utilización de métodos. Parámetros](#utilizacion-de-metodos-parametros)
  - [Utilización de propiedades](#utilizacion-de-propiedades)
  - [Utilización de métodos estáticos](#utilizacion-de-metodos-estaticos)
  - [Constructores](#constructores)
  - [Destrucción de objetos y liberación de memoria](#destruccion-de-objetos-y-liberacion-de-memoria)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-1)
- [Uso de estructuras de control](#uso-de-estructuras-de-control)
  - [Estructuras de selección](#estructuras-de-seleccion)
  - [Estructuras de repetición](#estructuras-de-repeticion)
  - [Estructuras de salto](#estructuras-de-salto)
  - [Control de excepciones](#control-de-excepciones)
  - [Aserciones](#aserciones)
  - [Prueba, depuración y documentación de la aplicación](#prueba-depuracion-y-documentacion-de-la-aplicacion)
  - [Ejercicio](#ejercicio)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-2)
- [Desarrollo de clases](#desarrollo-de-clases)
  - [Concepto de clase](#concepto-de-clase)
  - [Estructura y miembros de una clase. Visibilidad](#estructura-y-miembros-de-una-clase-visibilidad)
  - [Creación de propiedades](#creacion-de-propiedades)
  - [Creación de métodos](#creacion-de-metodos)
  - [Creación de constructores](#creacion-de-constructores)
  - [Utilización de clases y objetos](#utilizacion-de-clases-y-objetos)
  - [Utilización de clases heredadas](#utilizacion-de-clases-heredadas)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-3)
- [Lectura y escritura de información](#lectura-y-escritura-de-informacion)
  - [Flujos. Tipos bytes y caracteres. Clases relacionadas](#flujos-tipos-bytes-y-caracteres-clases-relacionadas)
  - [Ficheros de datos. Registros](#ficheros-de-datos-registros)
  - [Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros](#apertura-y-cierre-de-ficheros-modos-de-acceso-escritura-y-lectura-de-informacion-en-ficheros)
  - [Utilización de los sistemas de ficheros.](#utilizacion-de-los-sistemas-de-ficheros)
  - [Creación y eliminación de ficheros y directorios](#creacion-y-eliminacion-de-ficheros-y-directorios)
  - [Entrada desde teclado. Salida a pantalla. Formatos de visualización](#entrada-desde-teclado-salida-a-pantalla-formatos-de-visualizacion)
  - [Interfaces gráficas](#interfaces-graficas)
  - [Concepto de evento](#concepto-de-evento)
  - [Creación de controladores de eventos](#creacion-de-controladores-de-eventos)
  - [- Simulacro examen miercoles](#simulacro-examen-miercoles)
  - [Ejercicio de final de unidad](#ejercicio-de-final-de-unidad-4)
  - [Examen final](#examen-final)
  - [Carpeta sin título](#carpeta-sin-titulo)
- [Aplicación de las estructuras de almacenamiento](#aplicacion-de-las-estructuras-de-almacenamiento)
  - [Estructuras estáticas y dinámicas](#estructuras-estaticas-y-dinamicas)
  - [Creación de matrices (arrays)](#creacion-de-matrices-arrays)
  - [Matrices (arrays) multidimensionales](#matrices-arrays-multidimensionales)
  - [Genericidad](#genericidad)
  - [Cadenas de caracteres. Expresiones regulares](#cadenas-de-caracteres-expresiones-regulares)
  - [Colecciones Listas, Conjuntos y Diccionarios](#colecciones-listas-conjuntos-y-diccionarios)
  - [Operaciones agregadas filtrado, reducción y recolección](#operaciones-agregadas-filtrado-reduccion-y-recoleccion)
- [Utilización avanzada de clases](#utilizacion-avanzada-de-clases)
  - [Repaso](#repaso)
  - [Composición de clases](#composicion-de-clases)
  - [Herencia y polimorfismo](#herencia-y-polimorfismo)
  - [Jerarquía de clases Superclases y subclases](#jerarquia-de-clases-superclases-y-subclases)
  - [Clases y métodos abstractos y finales](#clases-y-metodos-abstractos-y-finales)
  - [Interfaces](#interfaces)
  - [Sobreescritura de métodos](#sobreescritura-de-metodos)
  - [Constructores y herencia](#constructores-y-herencia)
- [Mantenimiento de la persistencia de los objetos](#mantenimiento-de-la-persistencia-de-los-objetos)
  - [Bases de datos orientadas a objetos](#bases-de-datos-orientadas-a-objetos)
  - [Características de las bases de datos orientadas a objetos](#caracteristicas-de-las-bases-de-datos-orientadas-a-objetos)
  - [Instalación del gestor de bases de datos](#instalacion-del-gestor-de-bases-de-datos)
  - [Creación de bases de datos](#creacion-de-bases-de-datos)
  - [Mecanismos de consulta](#mecanismos-de-consulta)
  - [El lenguaje de consultas sintaxis, expresiones, operadores](#el-lenguaje-de-consultas-sintaxis-expresiones-operadores)
  - [Recuperación, modificación y borrado de información](#recuperacion-modificacion-y-borrado-de-informacion)
  - [Tipos de datos objeto; atributos y métodos](#tipos-de-datos-objeto-atributos-y-metodos)
  - [Tipos de datos colección](#tipos-de-datos-coleccion)
- [Gestión de bases de datos](#gestion-de-bases-de-datos)
  - [Acceso a bases de datos. Estándares. Características](#acceso-a-bases-de-datos-estandares-caracteristicas)
  - [Establecimiento de conexiones](#establecimiento-de-conexiones)
  - [Almacenamiento, recuperación, actualización y eliminación de información en bases de datos](#almacenamiento-recuperacion-actualizacion-y-eliminacion-de-informacion-en-bases-de-datos)
- [Programación en el lado del servidor](#programacion-en-el-lado-del-servidor)
  - [Fundamentos](#fundamentos)
  - [get y post](#get-y-post)
  - [Persistencia](#persistencia)
  - [Proyecto Ana](#proyecto-ana)
- [.git](#git)
  - [branches](#branches)
  - [hooks](#hooks)
  - [info](#info)
  - [logs](#logs)
  - [objects](#objects)
  - [refs](#refs)

---

<a id="identificacion-de-los-elementos-de-un-programa-informatico"></a>
# Identificación de los elementos de un programa informático

<a id="estructura-y-bloques-fundamentales"></a>
## Estructura y bloques fundamentales

En el vasto universo de la programación, cada programa informático es como una obra maestra compuesta por diversos elementos que trabajan juntos para crear algo funcional y eficiente. La carpeta `Primero/Programación/001-Identificación de los elementos de un programa informático/001-Estructura y bloques fundamentales` nos invita a explorar la esencia de estas obras maestras, desentrañando sus secretos y revelando las estructuras que sostienen su funcionamiento.

El primer elemento fundamental que encontramos en cualquier programa es la **estructura**. Es como el esqueleto de una casa: define cómo están organizados los diferentes componentes. En un programa, esta estructura se compone de bloques fundamentales que son las unidades más pequeñas y autónomas del código. Cada bloque puede ser una declaración simple o una secuencia de instrucciones complejas.

Siguiendo este esquema, cada uno de estos bloques es como una pieza en un rompecabezas. Al juntarlas adecuadamente, formamos la estructura general del programa. Esta estructura no solo determina cómo se ejecutan las instrucciones, sino también cómo interactúan entre sí.

La **variables** son otro elemento crucial que juegan un papel fundamental en el funcionamiento de los programas. Son como contenedores donde almacenamos datos que pueden cambiar durante la ejecución del programa. Cada variable tiene un nombre y un tipo específico, lo que le da una identidad única y permite realizar operaciones específicas con ella.

Las **operadores** son las herramientas que nos permiten manipular los valores de las variables. Son símbolos o palabras clave que realizan funciones como la suma, resta, multiplicación, comparación, entre otras. Los operadores son esenciales para construir expresiones y realizar cálculos complejos.

La **literales** son constantes que se utilizan directamente en el código. Pueden ser números, cadenas de texto o valores booleanos. Son los elementos concretos que forman parte del programa y que no cambian durante su ejecución.

Las **constantes**, por otro lado, son valores fijos que no pueden cambiar durante la ejecución del programa. A diferencia de las literales, las constantes tienen un nombre específico y se declaran una vez para toda la duración del programa.

La **programación orientada a objetos** introduce nuevos conceptos como las **clases**, los **objetos** y los **métodos**. Las clases son plantillas que definen las características comunes de un conjunto de objetos, mientras que los objetos son instancias concretas de esas clases. Los métodos son funciones asociadas a los objetos que realizan operaciones específicas.

La **programación estructurada**, por otro lado, se centra en la organización del código mediante estructuras como las **estructuras de control de flujo**. Estas estructuras permiten controlar el orden en que se ejecutan las instrucciones, determinando qué partes del programa se ejecutan y cuándo.

La **programación funcional**, por otro lado, enfatiza la idea de funciones puras y sin efectos secundarios. Las funciones funcionales toman entradas y producen salidas, pero no modifican el estado del programa ni interactúan con él fuera de su ámbito.

En conclusión, cada programa informático es una obra maestra compuesta por diversos elementos que trabajan juntos para crear algo funcional y eficiente. La estructura y los bloques fundamentales son los pilares sobre los cuales se construye todo el edificio. Desde las variables hasta las constantes, desde los operadores hasta los métodos, cada elemento tiene un papel específico y contribuye a la funcionalidad del programa. Al entender estos elementos y cómo interactúan entre sí, podemos desarrollar programas más complejos y eficientes.

# Programa informático

Acaba empezando por un archivo de texto plano que contiene el código fuente del programa que estamos creando
Cuando el programa crece, un proyecto puede contener múltiples archivos de código

El código fuente debe ser interepretado o compilado para ser ejecutado

Lenguajes de bajo nivel dependen de compiladores = C++
Lenguajes de alto nivel tienen intérpretes = Python/Javascript

Partes de un programa informático:
1. Docstring
2. Importaciones (librerías u otros archivos)
3. Declaración de variables globales
4. Funciones/clases (paquetes de lógico de código reutilizables)
5. Función principal (la que lo pone todo en marcha)

### Holamundo

```python
print("Hola mundo desde Python")
```

<a id="variables"></a>
## Variables

En el vasto universo de la programación, las variables son como los ingredientes que forman una receta culinaria. Cada variable es un contenedor que almacena un valor específico, que puede ser modificado a lo largo del tiempo. En este capítulo, nos adentramos en el mundo de las variables, explorando sus características y su papel fundamental en la construcción de programas informáticos.

Las variables son declaradas con un nombre único que actúa como una etiqueta para identificar el contenido almacenado. Al igual que los ingredientes en una receta, cada variable tiene un tipo específico, que determina qué tipo de datos puede contener. Por ejemplo, puedes tener una variable llamada `edad` que almacene un número entero, o una variable llamada `nombre` que almacene una cadena de texto.

La declaración de variables es como preparar los ingredientes antes de comenzar a cocinar. En la programación, esto se hace utilizando palabras clave específicas para cada tipo de dato. Por ejemplo, en muchos lenguajes de programación, puedes declarar una variable entera con el nombre `edad` y asignarle un valor inicial de 25 así: `int edad = 25;`. Esta línea de código es como decir "prepara un contenedor llamado `edad`, que puede almacenar números enteros, y coloca en él el número 25".

Una vez declaradas, las variables pueden ser utilizadas en cualquier parte del programa. Es como tener una receta que menciona los ingredientes necesarios para preparar una ensalada. En la programación, puedes utilizar la variable `edad` en diferentes partes de tu código para realizar operaciones o mostrar información al usuario.

Es importante recordar que las variables son mutables, lo que significa que su valor puede cambiar a lo largo del tiempo. Por ejemplo, si tienes un programa que calcula el descuento de un producto, puedes declarar una variable `precio` y otra `descuento`. Inicialmente, la variable `precio` podría tener el valor 100, pero luego podrías modificarla para reflejar el precio final después del descuento.

Además de almacenar valores simples como números o texto, las variables también pueden contener estructuras más complejas. Por ejemplo, puedes tener una variable que almacene un nombre completo, que sería una cadena compuesta por varias palabras. Otra variable podría almacenar una lista de productos en un carrito de compras.

La gestión eficiente de variables es crucial para la legibilidad y el mantenimiento del código. Es como organizar los ingredientes de una receta de manera clara y sistemática, para que sea fácil encontrar lo que se necesita cuando se necesite. Por eso es importante dar nombres descriptivos a las variables, que reflejen su contenido o propósito.

En resumen, las variables son el corazón de cualquier programa informático. Son los contenedores que almacenan los datos y permiten que el programa interactúe con ellos. Al entender cómo declarar, utilizar y gestionar variables, se abre la puerta a la creación de programas complejos y eficientes. Es un concepto fundamental que todos los programadores deben dominar para poder expresar sus ideas en código.

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

<a id="tipos-de-datos"></a>
## Tipos de datos

En el vasto mundo de la programación, los tipos de datos son como las piezas fundamentales que construyen la estructura de cualquier programa informático. Estos elementos esenciales determinan cómo se almacenan y manipulan los datos dentro del sistema, influyendo en su eficiencia y precisión.

Los tipos de datos pueden clasificarse en varias categorías principales, cada una con sus propias características y usos específicos. Por ejemplo, los tipos numéricos incluyen enteros, flotantes y complejos, cada uno diseñado para representar diferentes rangos y precisiones de valores numéricos. Los tipos de texto, por otro lado, permiten almacenar cadenas de caracteres que pueden formar palabras, frases o incluso párrafos.

Además de los tipos numéricos y de texto, existen otros tipos de datos que son cruciales para la programación moderna. Los booleanos, por ejemplo, solo pueden tomar dos valores: verdadero o falso, lo que es fundamental para el control de flujo en programas. Las fechas y horas también son un tipo de dato común, permitiendo al programa manejar información temporal con precisión.

La elección del tipo de datos adecuado es crucial para la eficiencia del programa. Un tipo de dato incorrecto puede llevar a errores de ejecución o incluso a problemas de rendimiento significativos. Por lo tanto, comprender y utilizar correctamente los tipos de datos es una habilidad esencial en cualquier lenguaje de programación.

Además de estos tipos básicos, muchos lenguajes de programación ofrecen tipos de datos más complejos que permiten representar estructuras de datos más sofisticadas. Las matrices o arrays, por ejemplo, son tipos de datos que pueden almacenar colecciones de elementos del mismo tipo. Los diccionarios o hashes, en cambio, permiten asociar claves con valores, lo que es útil para almacenar y recuperar información de manera eficiente.

La comprensión de los tipos de datos también facilita la depuración y el mantenimiento del código. Al conocer cómo se manejan diferentes tipos de datos, los programadores pueden identificar rápidamente errores y optimizar el rendimiento del programa.

En resumen, los tipos de datos son una parte esencial de cualquier sistema informático. Desde los simples hasta los complejos, cada uno desempeña un papel crucial en la estructura y funcionamiento del programa. Comprender y utilizar correctamente estos tipos es fundamental para desarrollar software eficiente y robusto.

La programación no es solo sobre escribir código; es también sobre entender cómo se organiza y manipula la información dentro de ese código. Los tipos de datos son el lenguaje con el que los programadores comunican esta información al ordenador, y su correcta utilización es una habilidad clave en cualquier proyecto informático.

Al explorar los diferentes tipos de datos disponibles en un lenguaje de programación, los estudiantes pueden adquirir una comprensión profunda de cómo se construyen y funcionan los programas. Esta conocimiento les permitirá crear aplicaciones más complejas y eficientes, capaces de manejar una amplia gama de tareas y procesos.

En conclusión, los tipos de datos son el esqueleto sobre el cual se construye cualquier programa informático. Comprenderlos completamente es un paso crucial en el viaje hacia la programación experta, permitiendo a los desarrolladores crear software que sea no solo funcional, sino también eficiente y escalable.

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

<a id="literales"></a>
## Literales

En el vasto mundo de la programación, los literales son como las joyas que adornan la estructura fundamental de un programa informático. Estos elementos representan valores inmutables que se utilizan directamente en el código fuente, proporcionando una forma sencilla y eficiente de incorporar datos específicos dentro del programa. Los literales pueden ser de diversos tipos, cada uno con su propia semántica y uso específico.

Los literales numéricos son un ejemplo claro de este concepto. Incluyen enteros (como 42 o -7), reales (como 3.14 o -0.001) y complejos (como 2+3i). Cada uno de estos tipos permite representar diferentes magnitudes y precisiones, adaptándose a las necesidades del programa.

Los literales de texto son otro tipo importante de literal. En la programación, los textos se representan generalmente como cadenas de caracteres encerradas entre comillas simples ('') o dobles (""). Estas cadenas pueden contener cualquier carácter imprimible y suelen ser utilizadas para almacenar nombres de variables, mensajes de error, instrucciones del usuario, etc.

Los literales booleanos son un tipo especial que solo puede tomar dos valores: verdadero (true) o falso (false). Son fundamentales en la toma de decisiones dentro del programa, permitiendo controlar el flujo de ejecución según ciertas condiciones.

Además de estos tipos básicos, existen literales más complejos como los literales nulos (null), que representan la ausencia de valor. También hay literales de fecha y hora, que permiten trabajar con momentos específicos del tiempo dentro del programa.

La utilización de literales en el código es crucial porque proporciona una forma directa y rápida de incorporar datos sin necesidad de variables o funciones adicionales. Esto facilita la lectura y comprensión del código, ya que los valores se pueden ver inmediatamente en su contexto.

Sin embargo, es importante recordar que los literales tienen un alcance limitado dentro del programa. Una vez definidos, no pueden cambiar su valor durante la ejecución, lo que las hace ideales para representar constantes o datos fijos.

En resumen, los literales son una herramienta fundamental en el lenguaje de programación, permitiendo incorporar valores directamente en el código fuente. Cada tipo de literal tiene sus propias características y usos específicos, contribuyendo así a la estructura y funcionalidad del programa informático.

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

<a id="constantes"></a>
## Constantes

En el vasto mundo de la programación, las constantes desempeñan un papel fundamental, como pilares esenciales que sostienen la estructura del edificio. Estos son valores inmutables, una vez establecidos, permanecen firmes y no pueden ser modificados durante la ejecución del programa. Las constantes son declaradas con el fin de proporcionar nombres significativos a ciertos valores, facilitando así su uso y comprensión en el código.

La declaración de constantes es un acto de claridad y organización. Al nombrar un valor como una constante, se le da un nombre que refleja su propósito o contenido, lo que hace que sea más fácil entender su uso en el programa. Por ejemplo, si tienes un valor que representa la cantidad máxima de usuarios permitidos en un sistema, declararlo como una constante con el nombre `MAX_USUARIOS` facilita su identificación y modificación si es necesario.

Las constantes también contribuyen a la seguridad del código. Al establecer valores importantes como constantes, se reduce el riesgo de errores al modificar directamente los valores en el código fuente. Esto es especialmente útil cuando estos valores son utilizados en múltiples lugares dentro del programa, ya que cualquier cambio realizado en una sola ubicación garantiza que todos los demás lugares reflejen la nueva configuración.

Además, las constantes pueden mejorar la eficiencia del programa. Algunos compiladores y intérpretes de código optimizan automáticamente el uso de constantes, lo que puede llevar a un rendimiento más rápido. Esto es especialmente beneficioso cuando se utilizan valores fijos en bucles o operaciones repetitivas.

La gestión adecuada de las constantes también facilita la mantenibilidad del código. Si necesitas cambiar un valor importante, simplemente debes modificar la declaración de la constante y no tienes que buscar y reemplazar el valor en todo el programa. Esto reduce significativamente el riesgo de errores y asegura que todos los lugares donde se use el valor reflejen la nueva configuración.

Las constantes son una herramienta poderosa en la programación, proporcionando un medio para nombrar y utilizar valores importantes de manera segura y eficiente. Al declarar y utilizar constantes con inteligencia, puedes mejorar la calidad del código, su legibilidad y su mantenimiento a largo plazo.

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

<a id="operadores-y-expresiones"></a>
## Operadores y expresiones

En el vasto mundo de la programación, los operadores y las expresiones son como los bloques con los que se construyen las estructuras fundamentales de cualquier programa informático. Estos elementos permiten a los desarrolladores manipular datos, realizar cálculos y tomar decisiones en función de ciertas condiciones.

Los operadores son símbolos o palabras clave que indican una acción específica sobre uno o más operandos (valores o variables). Por ejemplo, el operador `+` indica la adición de dos números. Los operadores pueden ser aritméticos, relacionales, lógicos y de asignación, cada uno con su propio conjunto de funciones específicas.

Las expresiones son combinaciones de operandos y operadores que se evalúan para producir un valor. Por ejemplo, la expresión `a + b` es una suma de dos variables `a` y `b`. Las expresiones pueden ser simples o complejas, dependiendo del número de operadores y operandos involucrados.

La importancia de los operadores y las expresiones radica en su capacidad para realizar cálculos y tomar decisiones. Por ejemplo, una expresión como `if (x > 0)` evalúa si la variable `x` es mayor que cero, lo que determina el flujo del programa. Los operadores de asignación, como `=`, permiten almacenar valores en variables, mientras que los operadores relacionales, como `==` o `!=`, comparan dos valores y devuelven un resultado booleano.

La comprensión de los operadores y las expresiones es fundamental para cualquier programador. No solo son la base de todas las operaciones matemáticas y lógicas en el código, sino que también permiten a los desarrolladores crear algoritmos complejos y resolver problemas de forma eficiente. A través del uso de operadores y expresiones, se pueden manipular datos, realizar cálculos y tomar decisiones en función de ciertas condiciones.

Los operadores y las expresiones son herramientas poderosas que permiten a los programadores crear programas complejos y eficientes. Al dominar estos elementos, se abre la puerta a una amplia gama de posibilidades en el mundo de la programación, desde aplicaciones simples hasta sistemas empresariales complejos.

En resumen, los operadores y las expresiones son los pilares sobre los cuales se construyen los programas informáticos. Su comprensión es fundamental para cualquier programador y permite a los desarrolladores crear algoritmos complejos y resolver problemas de forma eficiente. A través del uso de operadores y expresiones, se pueden manipular datos, realizar cálculos y tomar decisiones en función de ciertas condiciones, lo que abre la puerta a una amplia gama de posibilidades en el mundo de la programación.

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```

<a id="ejercicio-de-final-de-unidad"></a>
## Ejercicio de final de unidad

### Holamundo

```python
print("Hola mundo desde Python")
```

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```


<a id="utilizacion-de-objetos"></a>
# Utilización de objetos

<a id="caracteristicas-de-los-objetos"></a>
## Características de los objetos

Los objetos son los bloques fundamentales de la programación orientada a objetos (POO), representando entidades del mundo real con sus propiedades y comportamientos. En este contexto, los objetos se caracterizan por su estado, comportamiento y identidad.

El estado de un objeto refleja su situación actual en el programa, definido por sus atributos o variables miembro que almacenan datos relevantes. Por ejemplo, un objeto de tipo "Coche" podría tener atributos como color, marca y modelo, cada uno con un valor específico que describe su estado.

El comportamiento de los objetos se expresa a través de métodos o funciones asociados a ellos. Estos métodos definen las acciones que el objeto puede realizar. Siguiendo el ejemplo del coche, podrían existir métodos como arrancar(), frenar() y acelerar(). Cada método realiza una tarea específica relacionada con el estado del objeto.

La identidad de un objeto es única en su contexto, lo que se refleja en la referencia a él. En Python, por ejemplo, cada objeto tiene una dirección de memoria única que lo distingue de otros objetos. Esta identidad es crucial para acceder y manipular los objetos dentro del programa.

Además de estos tres aspectos fundamentales, los objetos pueden interactuar entre sí mediante mensajes o invocaciones a métodos. Cuando un objeto recibe un mensaje, ejecuta el método correspondiente, lo que puede modificar su estado o generar algún efecto secundario visible en el sistema.

La programación orientada a objetos permite organizar y estructurar el código de manera lógica y coherente, facilitando la reutilización y mantenimiento del software. Al tratar los datos y las operaciones sobre ellos como entidades interconectadas, se pueden crear sistemas complejos pero manejables.

La herencia es otro concepto clave en la POO que permite crear nuevas clases a partir de clases existentes, heredando sus atributos y métodos. Esto facilita el reutilización del código y la creación de jerarquías lógicas de objetos. Por ejemplo, una clase "Automóvil" podría ser una superclase para las clases "Coche", "Motocicleta" y "Truck".

La encapsulación es un principio que oculta los detalles internos de un objeto y expone solo lo necesario a través de métodos públicos. Esto protege el estado del objeto y permite modificarlo de manera controlada, evitando cambios no deseados o inconsistencias.

En resumen, los objetos son la base de la programación orientada a objetos, representando entidades con estado, comportamiento y identidad únicas. Su uso permitirá crear sistemas complejos pero manejables, facilitando la reutilización del código y la creación de jerarquías lógicas de objetos.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### objeto math

```python

```

<a id="instanciacion-de-objetos"></a>
## Instanciación de objetos

La instanciación de objetos es una etapa fundamental en la programación orientada a objetos (POO), representando el proceso mediante el cual se crean objetos a partir de clases. Este concepto es como la "fabricación" de instancias concretas basadas en un modelo general, conocido como clase.

En este contexto, cada objeto creado a partir de una clase es una instancia única que posee los atributos y métodos definidos por dicha clase, pero también puede tener valores específicos para sus propiedades. La instanciación es el punto de partida para interactuar con los objetos en un programa POO, permitiendo manipular su estado y comportamiento.

La creación de una instancia implica la asignación de memoria para almacenar sus datos y la ejecución del constructor de la clase, que inicializa los atributos del objeto. Este proceso es crucial porque determina cómo el objeto será utilizado en el programa, definiendo su identidad y su comportamiento inicial.

La instanciación también permite la creación de múltiples objetos a partir de una misma clase, lo cual es útil para representar entidades distintas pero similares dentro del mismo contexto. Cada uno de estos objetos puede tener valores diferentes para sus atributos, permitiendo así una gran flexibilidad en el manejo de datos y operaciones.

Además, la instanciación facilita la reutilización de código, ya que permite crear múltiples objetos con comportamientos similares sin necesidad de escribir nuevamente las mismas líneas de código. Esto mejora la eficiencia del programa y reduce el riesgo de errores al mantener una única definición de comportamiento.

La instanciación es un concepto básico pero poderoso en POO, ya que permite crear objetos con estados y comportamientos específicos, lo cual es fundamental para representar entidades del mundo real dentro de un programa. Esta capacidad es esencial para la creación de aplicaciones complejas y dinámicas, donde los objetos interactúan entre sí para lograr funcionalidades avanzadas.

La instanciación también implica el manejo de recursos como memoria, lo cual es una consideración importante en la programación moderna. La asignación y liberación de memoria adecuada son cruciales para evitar problemas de rendimiento y evitar fugas de memoria, que pueden llevar a problemas graves en aplicaciones largas o intensivas.

En resumen, la instanciación de objetos es un proceso fundamental en la programación orientada a objetos, permitiendo crear entidades concretas a partir de clases. Este concepto es esencial para representar el mundo real dentro de un programa y facilita la reutilización de código, lo cual es crucial para la creación de aplicaciones complejas y eficientes. La comprensión y correcta implementación de la instanciación son habilidades fundamentales en cualquier desarrollo de software basado en POO.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### namespace

```python
import math
```

<a id="utilizacion-de-metodos-parametros"></a>
## Utilización de métodos. Parámetros

En el vasto mundo de la programación, los objetos son como las piezas fundamentales que conforman una construcción sólida. Cada objeto es un contenedor de datos y métodos que trabajan juntos para realizar tareas específicas. En esta subunidad didáctica, nos adentramos en el fascinante mundo de cómo utilizar métodos y parámetros dentro de estos objetos.

Los métodos son como las acciones que los objetos pueden realizar. Son funciones asociadas a un objeto que definen su comportamiento. Al igual que una persona puede caminar, correr o saltar, un objeto puede tener métodos para realizar ciertas operaciones. Por ejemplo, si tenemos un objeto de tipo "Coche", podemos definir métodos como "acelerar", "frenar" y "girar".

Los parámetros son los valores que se pasan a estos métodos cuando se invocan. Son como las instrucciones adicionales que proporcionamos para que el método haga algo específico. Por ejemplo, si queremos acelerar nuestro coche, podemos pasar un valor como la velocidad deseada al método "acelerar". De esta manera, el objeto sabe exactamente qué hacer.

La utilización de métodos y parámetros es fundamental en la programación orientada a objetos (POO). Permite una mayor modularidad y reutilización del código. Cada método puede ser invocado por diferentes partes del programa, lo que facilita su mantenimiento y escalabilidad. Además, los parámetros permiten personalizar el comportamiento de los métodos según las necesidades específicas de cada llamada.

En la práctica, trabajar con métodos y parámetros implica una buena planificación y organización. Es importante definir métodos que sean claros, descriptivos y que cumplan con un solo propósito. Además, el uso adecuado de parámetros permite hacer que los métodos sean más flexibles y reutilizables.

La comprensión de cómo utilizar métodos y parámetros es crucial para desarrollar programas eficientes y mantenibles. Al trabajar con objetos, estos elementos nos permiten encapsular funcionalidades relacionadas en una sola unidad, lo que facilita su uso y evita la redundancia del código. Además, el uso de parámetros nos permite adaptar el comportamiento de los métodos según las necesidades específicas de cada situación.

En resumen, la utilización de métodos y parámetros es un concepto fundamental en la programación orientada a objetos. Permite una mayor modularidad, reutilización del código y flexibilidad en el diseño de programas. Al trabajar con estos elementos, podemos crear objetos que sean más potentes y versátiles, lo que facilita su uso y mantenimiento en proyectos de cualquier tamaño.

Esta subunidad didáctica nos introduce en la práctica de cómo utilizar métodos y parámetros dentro de los objetos. A través de ejemplos y explicaciones detalladas, aprenderemos a definir y usar estos elementos para crear programas más eficientes y organizados. Con el tiempo y la práctica, dominaremos esta habilidad esencial que es fundamental en cualquier proyecto de programación orientada a objetos.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### llamada a metodos

```python
import math as matematicas

print(matematicas.ceil(7.2))
```

### sparse is better than dense

```python
import math as matematicas

numero = 7.2
redondeo = matematicas.ceil(numero)
print(redondeo)
```

### sparse

```python
import math as matematicas

print(matematicas.ceil(7.2))
```

<a id="utilizacion-de-propiedades"></a>
## Utilización de propiedades

En el mundo de la programación, los objetos son una construcción fundamental que nos permite modelar y representar entidades del mundo real dentro de nuestros programas. Cada objeto es una instancia de una clase, que define su estructura y comportamiento. Los objetos tienen propiedades, que son atributos que almacenan datos sobre el estado del objeto, y métodos, que definen las acciones que puede realizar.

La utilización de propiedades en los objetos es un paso crucial para dar forma a estos entidades dentro de nuestro código. Las propiedades nos permiten almacenar información relevante y manipularla fácilmente. Por ejemplo, si estamos creando una clase `Persona`, podemos definir propiedades como `nombre`, `edad` o `email`. Cada uno de estos atributos almacena un valor específico que describe el estado del objeto.

La manipulación de las propiedades es tan sencilla como acceder a ellas y cambiar su valor. Por ejemplo, si queremos cambiar el nombre de una persona, simplemente asignamos un nuevo valor a la propiedad `nombre`. Esta flexibilidad nos permite interactuar con los objetos de manera intuitiva y natural.

Además de almacenar datos, las propiedades también pueden tener métodos asociados que permiten modificar su estado. Por ejemplo, en nuestra clase `Persona`, podríamos tener un método `cumplirAnios` que aumente el valor de la propiedad `edad`. Esta capacidad nos permite no solo leer los valores actuales de las propiedades, sino también cambiarlos y mantener el objeto en un estado coherente.

La utilización de propiedades es una práctica común en la programación orientada a objetos, ya que facilita la representación y manipulación de datos complejos. Al definir propiedades, estamos creando una forma clara y estructurada de almacenar información dentro de nuestros objetos, lo que hace que nuestro código sea más fácil de entender y mantener.

Además, las propiedades pueden tener modificadores de acceso que controlan quién puede leer o modificar su valor. Por ejemplo, podemos definir una propiedad como `privada`, lo que significa que solo el objeto mismo puede acceder a ella. Esto nos permite ocultar detalles internos del objeto y exponer solo la información relevante al resto del programa.

La utilización de propiedades también facilita la implementación de patrones de diseño, como los getters y setters. Los getters son métodos que devuelven el valor actual de una propiedad, mientras que los setters son métodos que permiten modificar su valor. Esta práctica nos permite agregar lógica adicional al acceso a las propiedades, lo que puede ser útil para validar los valores asignados o realizar acciones adicionales cuando se cambia el estado del objeto.

En resumen, la utilización de propiedades en los objetos es una herramienta poderosa y versátil en la programación orientada a objetos. Nos permite representar y manipular datos complejos de manera intuitiva y estructurada, facilitando la creación de programas robustos y mantenibles. Al dominar el uso de propiedades, podemos mejorar significativamente la calidad y eficiencia de nuestro código, permitiéndonos crear aplicaciones más sofisticadas y funcionales.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### propiedades

```python
import math as matematicas

PI = matematicas.pi
print(PI)
```

<a id="utilizacion-de-metodos-estaticos"></a>
## Utilización de métodos estáticos

En el mundo de la programación, los objetos son una construcción fundamental que nos permite modelar entidades del mundo real dentro de nuestros programas. Cada objeto tiene propiedades (datos) y métodos (funciones), lo que le confiere un comportamiento específico.

Los métodos estáticos son un tipo especial de método que pertenecen a la clase en sí misma, no a una instancia específica del objeto. Esto significa que puedes llamar a estos métodos sin necesidad de crear un objeto de la clase. Son útiles para operaciones que no dependen del estado interno del objeto, como utilidades generales o funciones de conversión.

La principal ventaja de los métodos estáticos es su independencia del contexto del objeto. No requieren acceso a variables de instancia ni a otros métodos de la clase, lo que las hace más fáciles de probar y mantener. Además, pueden ser llamados directamente desde la clase, lo que puede hacer que el código sea más limpio y organizado.

La implementación de un método estático en un lenguaje como Java sería algo así:

```java
public class Matematicas {
    public static int sumar(int a, int b) {
        return a + b;
    }
}
```

Aquí, el método `sumar` es estático y puede ser llamado directamente desde la clase `Matematicas`, sin necesidad de crear una instancia del objeto:

```java
int resultado = Matematicas.sumar(5, 3);
System.out.println("El resultado es: " + resultado);
```

Esta capacidad de llamar a métodos estáticos sin instanciar objetos puede ser muy útil en situaciones donde no necesitas el estado interno del objeto para realizar una tarea. Sin embargo, también es importante recordar que los métodos estáticos no pueden acceder directamente a las variables de instancia ni a otros métodos no estáticos de la misma clase.

La utilización de métodos estáticos puede llevar a un código más limpio y organizado, especialmente cuando se realizan operaciones que son independientes del estado interno del objeto. Sin embargo, es importante mantener una buena separación entre lo que es estático y lo que no lo es para evitar problemas de mantenimiento y confusión en el código.

En resumen, los métodos estáticos son una herramienta poderosa en la programación orientada a objetos, permitiendo realizar operaciones útiles sin necesidad de instanciar objetos. Sin embargo, su uso debe ser cuidadoso para mantener un diseño limpio y coherente en nuestros programas.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### Gato

```python
class Gato():
  def __init__(self):
    self.nombre = ""
  def maulla():
    return "miau"
    
gato1 = Gato()
gato1.nombre = "Micifu"

gato2 = Gato()
gato2.nombre = "Belcebú"
```

### Matematicas

```python
class Matematicas():
  def __init__(self):
    self.numero = 0
  def suma(self,a,b):
    return a+b
    
operacion1 = Matematicas()
print(operacion1.suma(4,3))

operacion2 = Matematicas()
print(operacion2.suma(6,7))
```

### metodo pseudoestatico

```python
class Matematicas():
  def __init__(self):
    self.numero = 0
  def suma(self,a,b):
    return a+b
    
print(Matematicas.suma(6,7))
```

### metodo estatico

```python
class Matematicas():
  def __init__(self):
    self.numero = 0
  @staticmethod
  def suma(a,b):
    return a+b
    
print(Matematicas.suma(6,7))
```

<a id="constructores"></a>
## Constructores

En el mundo de la programación, los constructores son una pieza fundamental que nos permite dar forma a nuestros objetos. Son como las fábricas que crean los productos finales, pero en este caso, los "productos" son instancias de clases. Un constructor es un método especial dentro de una clase que se ejecuta automáticamente cuando se crea una nueva instancia del objeto.

Imagina que tienes una receta para hacer un pastel. La receta es como la clase, y cada vez que quieres preparar un pastel, sigues los pasos descritos en la receta. El constructor sería el primer paso de esta receta, donde especificas todos los ingredientes necesarios y las condiciones iniciales del pastel.

En programación, cuando creamos una instancia de una clase, estamos creando un objeto con todas sus propiedades y métodos definidos. Pero antes de que podamos usar este objeto, es necesario inicializarlo con valores específicos. Es aquí donde entra en juego el constructor. Nos permite establecer los valores iniciales de las variables miembro del objeto.

Por ejemplo, si tienes una clase `Persona` con dos atributos: `nombre` y `edad`, puedes definir un constructor que acepte estos parámetros para inicializarlos cuando se crea una nueva instancia de la clase. De esta manera, cada persona tendrá su propio nombre y edad, configurados según los valores proporcionados al crearla.

Los constructores también pueden tener parámetros por defecto, lo que significa que si no se proporcionan valores al momento de crear el objeto, se utilizarán estos valores predeterminados. Esto nos brinda la flexibilidad de crear objetos con diferentes configuraciones iniciales sin necesidad de sobrecargar nuestro código.

Además, los constructores pueden ser sobrecargados, lo que significa que puedes tener varios métodos constructor dentro de una misma clase, cada uno con un conjunto diferente de parámetros. Esto nos permite crear objetos de la misma clase de diferentes maneras según nuestras necesidades.

Es importante destacar que el constructor es el primer método que se ejecuta cuando creamos una instancia de una clase. Por lo tanto, cualquier inicialización o configuración que necesitemos hacer antes de usar el objeto debe ser realizada en este método.

En resumen, los constructores son un elemento esencial en la programación orientada a objetos. Nos permiten crear y configurar objetos con valores iniciales específicos, facilitando así su uso y manipulación en nuestro código. Al entender cómo funcionan y cómo utilizarlos de manera efectiva, podemos mejorar significativamente la calidad y eficiencia de nuestras aplicaciones.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### fechas en python

```python
import datetime as fechas

hoy = fechas.date(2025, 9, 11)
print(hoy)
```

### propiedades de la fecha

```python
import datetime as fechas

hoy = fechas.date(2025, 9, 11)
print(hoy)

print(hoy.year)
print(hoy.month)
print(hoy.day)

diadelasemana = hoy.weekday()
print(diadelasemana)
diadelasemana = hoy.isoweekday()
print(diadelasemana)
```

<a id="destruccion-de-objetos-y-liberacion-de-memoria"></a>
## Destrucción de objetos y liberación de memoria

En el vasto universo de la programación, los objetos son como personajes vivos que interactúan entre sí en un escenario digital. Cada objeto tiene su propia identidad, características y comportamientos, pero también es parte del sistema más amplio conocido como la memoria del programa.

La destrucción de objetos y la liberación de memoria es una tarea crucial que los programadores deben entender y manejar con cuidado. Es como cuando un personaje muere en una historia: su vida se termina, pero su impacto puede seguir siendo sentido por el resto del mundo. En la programación, cuando un objeto deja de ser necesario o no es accesible desde ninguna parte del programa, debe ser eliminado para liberar los recursos que ocupaba.

La destrucción de objetos ocurre automáticamente en muchos lenguajes de programación modernos, gracias a lo que se conoce como recolección de basura. Este proceso automático busca y elimina los objetos que ya no son utilizados, asegurando que el programa no se quede sin espacio para nuevos objetos o variables.

Sin embargo, en algunos lenguajes, como Java o C++, la destrucción de objetos debe ser gestionada manualmente. Es como si tuviéramos que controlar cada muerte en una historia: cuando un personaje muere, debemos asegurarnos de que su vida se termina y no deje rastro.

La liberación de memoria es el siguiente paso crucial después de la destrucción del objeto. Es como recoger los objetos eliminados y colocarlos en un cesto para reciclaje. En la programación, esto implica limpiar la memoria ocupada por los objetos que ya no son necesarios, asegurando que el programa no se quede sin espacio.

La gestión de la destrucción de objetos y la liberación de memoria es importante porque puede afectar significativamente el rendimiento del programa. Si no se maneja correctamente, puede llevar a problemas como fugas de memoria, donde el programa consume más memoria de la necesaria, o incluso a errores graves que pueden hacer que el programa se detenga.

Para evitar estos problemas, los programadores deben entender cómo funciona la recolección de basura y aprender a gestionar manualmente la destrucción de objetos en lenguajes como Java o C++. También es crucial realizar pruebas exhaustivas para asegurar que no hay fugas de memoria ni errores relacionados con la gestión de memoria.

En resumen, la destrucción de objetos y la liberación de memoria son procesos fundamentales en la programación. Aunque pueden parecer complicados al principio, una comprensión profunda de estos conceptos puede ayudar a los programadores a crear programas más eficientes y seguros. Es como saber cómo manejar bien las muertes en una historia: es una parte importante del proceso, pero también es necesario para que la historia continúe sin problemas.

### Nota importante

```markdown
Nota importante para la generación de ejercicios de esta subunidad:
Esta subunidad trata, no la creación de clases personalizadas, sino la utilización de objetos predeterminados existentes en el propio lenguaje de programación.
Para crear actividades, ajustate al alcance concreto de los ejercicios desarrollados en la carpeta 101-Ejercicios.
```

### destruccion de objetos

```python
import datetime as fechas

hoy = fechas.date(2025, 9, 11)
print(hoy)

print(hoy.year)
print(hoy.month)
print(hoy.day)

diadelasemana = hoy.weekday()
print(diadelasemana)
diadelasemana = hoy.isoweekday()
print(diadelasemana)

del hoy
print(hoy)
```

### caballos en la cuadra

```python
''' 
    Calculadora de cuadras
    v0.1 (c) 2025 Jose Vicente Carratalá
    Programa que calcula número de cuadras a partir de los caballos
'''
```

### propiedades

```python
''' 
    Calculadora de cuadras
    v0.1 (c) 2025 Jose Vicente Carratalá
    Programa que calcula número de cuadras a partir de los caballos
'''

# Datos de inicio
caballos = 0
cuadras = 0
```

### entrada calculo y salida

```python
''' 
    Calculadora de cuadras
    v0.1 (c) 2025 Jose Vicente Carratalá
    Programa que calcula número de cuadras a partir de los caballos
'''

# Datos de inicio
caballos = 0
cuadras = 0

# Entrada de información
caballos = int(input("Introduce el número de caballos: "))

# Realización de cálculos
cuadras = caballos / 3

# Salida de resultados
print("Si tienes",caballos,"caballos")
print("Y te caben tres caballos por cuadra")
print("En ese caso necesitas",cuadras,"cuadras")
```

### libreria matematica

```python
''' 
    Calculadora de cuadras
    v0.1 (c) 2025 Jose Vicente Carratalá
    Programa que calcula número de cuadras a partir de los caballos
'''

import math as matematicas

# Datos de inicio
caballos = 0
cuadras = 0
caballos_por_cuadra = 0

# Entrada de información
caballos_por_cuadra = int(input("Introduce el número de caballos por cuadra: "))
caballos = int(input("Introduce el número de caballos: "))

# Realización de cálculos
cuadras = caballos / caballos_por_cuadra
redondeoalza = matematicas.ceil(cuadras)

# Salida de resultados
print("Si tienes",caballos,"caballos")
print("Y te caben tres caballos por cuadra")
print("En ese caso necesitas",redondeoalza,"cuadras")
```

<a id="ejercicio-de-final-de-unidad-1"></a>
## Ejercicio de final de unidad

### Holamundo

```python
print("Hola mundo desde Python")
```

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```


<a id="uso-de-estructuras-de-control"></a>
# Uso de estructuras de control

<a id="estructuras-de-seleccion"></a>
## Estructuras de selección

En el vasto mundo de la programación, las estructuras de control son como los pilares que sostienen la construcción de nuestros programas. Esenciales para organizar y dirigir el flujo de ejecución, estas estructuras nos permiten tomar decisiones basadas en condiciones específicas, lo que es fundamental para crear software inteligente y adaptable.

La carpeta `001-Estructuras de selección` del módulo `Programación/003-Uso de estructuras de control` se centra precisamente en este concepto crucial. Aquí, los estudiantes encontrarán una introducción a las decisiones que el programa debe tomar según ciertas condiciones. Es como un jardín de preguntas y respuestas, donde cada pregunta (condición) determina la rama por la que seguirá nuestro código.

La primera lección del submódulo nos introduce al concepto básico de estructuras de selección, destacando cómo estas permiten que el programa ejecute diferentes bloques de código dependiendo de si una condición es verdadera o falsa. Es como un camino bifurcado en la selva digital, donde cada sendero representa una posible ruta para seguir.

La siguiente lección profundiza en las estructuras `if`, `else` y `elif`, enseñándonos cómo estas herramientas nos permiten expresar decisiones complejas. Aprenderemos a construir sentencias que evalúan múltiples condiciones, creando un laberinto de posibilidades dentro de nuestro programa.

La carpeta también incluye ejemplos prácticos y problemas resueltos, ilustrando cómo aplicar estas estructuras en situaciones reales. A través de estos ejercicios, los estudiantes pueden experimentar la magia de las decisiones programáticas, comprobando cómo un simple cambio en una condición puede alterar completamente el comportamiento del programa.

Además, se aborda el tema de la optimización y la eficiencia en la selección de estructuras. Aprenderemos que no todas las estructuras son iguales, y que elegir la adecuada depende del contexto y de los requisitos específicos del problema a resolver. Es como seleccionar el mejor camino para llegar a un destino, considerando factores como la distancia, el tiempo y las condiciones meteorológicas.

La carpeta también destaca la importancia de la legibilidad y la mantenibilidad en la programación. Aprenderemos que una buena estructura de selección no solo debe funcionar correctamente, sino que también debe ser fácil de entender y modificar por otros desarrolladores. Es como construir un castillo de bloques de construcción: cada pieza debe tener su lugar y significado para que todo funcione armoniosamente.

Finalmente, se exploran los conceptos avanzados de las estructuras de selección, incluyendo el uso de operadores lógicos y la creación de estructuras anidadas. Aprenderemos cómo combinar múltiples condiciones en una sola sentencia, creando un jardín de posibilidades infinitas dentro de nuestro programa.

En resumen, la carpeta `001-Estructuras de selección` es un viaje emocionante por el mundo de las decisiones programáticas. Desde los conceptos básicos hasta las técnicas avanzadas, ofrece una comprensión profunda y práctica del poder de las estructuras de control en la programación. Es como descubrir cómo crear un laberinto digital que nos lleve a cualquier lugar que desee, siempre y cuando sepamos cómo tomar las decisiones correctas en cada paso del camino.

### Condicional

```python
# El código solo se ejecuta si la expresión es verdadera
edad = 47

if edad < 30:
  print("Eres un joven")
```

### else

```python
# El código solo se ejecuta si la expresión es verdadera
edad = 47

if edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### varios if

```python
# El código solo se ejecuta si la expresión es verdadera
edad = 47

if edad < 30:
  print("Eres un joven")
  
if edad > 30:
  print("Ya no eres un joven")
```

### varios if

```python
# El código solo se ejecuta si la expresión es verdadera
edad = 47

if edad < 10:
  print("Eres un niño")
else if edad >= 10 and edad < 20:
  print("Eres un adolescente)
else if edad >= 20 and edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### particula elif

```python
# El código solo se ejecuta si la expresión es verdadera
edad = 47

if edad < 10:
  print("Eres un niño")
elif edad >= 10 and edad < 20:
  print("Eres un adolescente")
elif edad >= 20 and edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### anidacion

```python
# Esto no hay que hacerlo

edad = 47

if edad < 30:
  if edad < 20:
    print("Eres muuuuy joven")
  else:
    print("eres un joven")
else:
  if edad < 40:
    print("Eres bastante poco joven")
  else:
    print("Ya no eres joven")
```

### Ejercicio en clase

```python
# Docstring
''' 
  Programa clasificador de baloncesto
  v0.1 Jose Vicente Carratala
  Este programa clasifica categorías por edades
'''

# Importaciones
# Este programa no requiere importaciones

# Declaración de variables globales
# Inicializamos las variables con valores vacíos

edad = 0
categoria = ""

# Funciones/clases
# En este programa no hay funciones o clases

# Función principal

edad = input("Introduce tu edad: ")
edad = int(edad) # Convierto la edad en un entero
if edad < 8:
  categoria = "pre-mini"
elif edad >= 8 and edad <= 11:
  categoria = "mini"
elif edad >= 12 and edad <=15:
  categoria = "infantil"
elif edad >= 16 and edad <=17:
  categoria = "cadete"
elif edad >= 18 and edad <=20:
  categoria = "junior"
else:
  categoria = "senior"
  
print("Tu edad es de",edad,"años y tu categoría es: ",categoria)  

if edad > 40:
  print("Veterano con experiencia en la cancha")
  
  
  
  
  
```

<a id="estructuras-de-repeticion"></a>
## Estructuras de repetición

En el vasto mundo de la programación, las estructuras de control son como los pilares que sostienen una construcción. Una de estas estructuras es la repetición, un concepto fundamental que permite a los programas realizar acciones múltiples veces bajo ciertas condiciones. En esta subunidad didáctica, nos adentramos en el estudio de las estructuras de repetición, que son herramientas poderosas para automatizar tareas y optimizar procesos.

La primera estructura de repetición que exploramos es la **sentencia `for`**. Esta estructura se utiliza cuando sabemos exactamente cuántas veces queremos que un bloque de código se ejecute. Es como decirle a tu robot: "Repite esto 10 veces". La sintaxis de una sentencia `for` suele ser sencilla y directa, permitiendo definir el número de repeticiones con precisión.

Después de la sentencia `for`, nos encontramos con la **sentencia `while`**. Esta estructura es más flexible que la anterior, ya que se ejecuta mientras una condición específica sea verdadera. Es como decirle a tu robot: "Haz esto mientras no llegues al final del camino". La ventaja de esta estructura radica en su capacidad para manejar situaciones donde el número exacto de repeticiones es incierto o depende de ciertos eventos.

La subunidad también aborda la importancia de **la optimización de bucles**. Aunque las estructuras de repetición son útiles, su uso excesivo puede llevar a problemas de rendimiento. Es como cuando intentas recoger una cesta de juguetes con un solo brazo: es posible, pero no eficiente. La optimización implica encontrar el equilibrio perfecto entre la cantidad de repeticiones y la eficiencia del código.

Además, se introduce el concepto de **la sentencia `break`** y la **sentencia `continue`**. Estas sentencias son como los comandos especiales en un juego: `break` es como decirle a tu robot: "Detente todo ahora", mientras que `continue` es como decirle: "Pasa al siguiente turno, pero no hagas nada más". Son herramientas valiosas para controlar el flujo de ejecución dentro de los bucles.

La subunidad también explora la **programación funcional** y cómo las estructuras de repetición pueden ser utilizadas en este paradigma. En programación funcional, las funciones son ciudadanos de primera clase, lo que significa que se pueden tratar como cualquier otro tipo de dato. Las estructuras de repetición pueden ser implementadas mediante funciones recursivas o utilizando bibliotecas específicas.

Finalmente, la subunidad concluye con ejercicios prácticos diseñados para aplicar los conocimientos adquiridos sobre las estructuras de repetición. Estos ejercicios son como el desafío final en un juego: requieren práctica y paciencia para resolverlos correctamente. A través de estos ejercicios, los estudiantes pueden experimentar la eficacia de las estructuras de repetición en diferentes contextos y aprender a optimizar su uso.

En resumen, esta subunidad didáctica es una introducción profunda a las estructuras de repetición en programación. Desde el concepto básico hasta técnicas avanzadas y aplicaciones prácticas, cada capítulo proporciona un paso más hacia la comprensión completa de cómo controlar el flujo de ejecución en los programas.

### saltos

```python
# Cuento los días del mes
for pares in range(0,100,2):
  print(pares)
```

### ineficiente

```python
# Cuento los días del mes
print("Hoy es el dia 1 del mes")
print("Hoy es el dia 2 del mes")
print("Hoy es el dia 3 del mes")
print("Hoy es el dia 4 del mes")
print("Hoy es el dia 5 del mes")
# ...
```

### estructura for

```python
# Cuento los días del mes
for dia in range(1,31):
  print("Hoy es el dia ",dia,"del mes")
```

### anidacion

```python
# Cuento los días del mes
for mes in range(1,13):
  for dia in range(1,31):
    print("Hoy es el dia ",dia,"del mes",mes)
```

### mas anidacion

```python
# Cuento los días del mes
for anio in range(1978,2026):
  for mes in range(1,13):
    for dia in range(1,31):
      print("Hoy es el dia ",dia,"del mes",mes,"del año",anio)
```

### ahora los impares

```python
# Cuento los días del mes
for pares in range(1,100,2):
  print(pares)
```

### while

```python
dia = 1

while dia < 31:
  print("hoy es el dia",dia,"del mes")
```

### incremento

```python
dia = 1

while dia < 31:
  print("hoy es el dia",dia,"del mes")
  dia += 1  # dia = dia + 1
```

### Ejercicio propuesto patitos

```markdown
Ejercicio: Contando patitos de goma

Escribe un programa en Python que utilice bucles for para simular el conteo de patitos de goma en una fábrica.

El programa debe recorrer:

Los años de producción (por ejemplo, de 2000 a 2025).

Los meses del año (de 1 a 12).

Los días del mes (del 1 al 30).

Por cada día, el programa mostrará un mensaje indicando cuántos patitos de goma se han fabricado ese día.

Requisitos adicionales:

Cada día se fabrican exactamente 10 patitos de goma.

El programa debe mostrar mensajes como:

Día 5 del mes 3 del año 2010: 10 patitos de goma fabricados


Al terminar el bucle, el programa debe mostrar el total de patitos fabricados en todo el período.
```

<a id="estructuras-de-salto"></a>
## Estructuras de salto

En el vasto universo de la programación, las estructuras de control son como los pilares que sostienen la construcción de algoritmos. Estas estructuras permiten a los programadores dirigir el flujo de ejecución del programa según ciertas condiciones o patrones específicos. En esta subunidad didáctica, nos adentramos en el fascinante mundo de las estructuras de salto, que son un elemento fundamental para controlar la dirección y velocidad de la ejecución de nuestro código.

La primera estructura de salto que exploramos es el `if-else`, una construcción que permite tomar decisiones basadas en condiciones booleanas. Este esencialmente dice: "Si esta condición se cumple, realiza esto; si no, realiza algo diferente". Es como un interruptor que decide qué camino seguir según las circunstancias.

El siguiente paso en nuestro viaje por las estructuras de salto es el `switch-case`, una alternativa más eficiente para múltiples condiciones. Este tipo de estructura permite evaluar una expresión y ejecutar diferentes bloques de código dependiendo del valor de esa expresión. Es como tener varias puertas que conducen a diferentes habitaciones, pero solo una se abre según el valor de la llave.

La importancia de las estructuras de salto no puede ser subestimada. Nos permiten crear programas que respondan dinámicamente a los cambios en el entorno y que tomen decisiones basadas en datos variables. Estas estructuras son esenciales para implementar algoritmos complejos, manejar errores y excepciones, y optimizar la eficiencia del código.

Además de las estructuras básicas `if-else` y `switch-case`, también exploramos el uso de bucles, que son una forma poderosa de repetir un bloque de código hasta que se cumpla una condición específica. Los bucles `for` e `while` nos permiten automatizar tareas repetitivas y procesar listas o conjuntos de datos de manera eficiente.

La comprensión y uso adecuado de las estructuras de salto es crucial para cualquier programador, ya que son la base sobre la cual se construyen algoritmos complejos y programas robustos. Cada estructura tiene sus propias características y ventajas, y aprender a elegir la más apropiada en cada situación es una habilidad valiosa.

A medida que avanzamos en nuestra exploración de las estructuras de control, nos encontraremos con técnicas más sofisticadas como el `break` y el `continue`, que nos permiten alterar el flujo de ejecución dentro de bucles. El `break` nos ayuda a salir prematuramente de un bucle cuando se cumple una condición específica, mientras que el `continue` nos permite saltar a la siguiente iteración sin ejecutar el resto del código dentro del bucle.

Finalmente, es importante destacar que las estructuras de salto no son solo herramientas técnicas; también son fundamentos para la lógica y la pensamiento computacional. Aprender a controlar el flujo de ejecución con precisión nos prepara para abordar problemas complejos en programación y crear soluciones eficientes y efectivas.

En conclusión, las estructuras de salto son una parte esencial del lenguaje de la programación, permitiendo a los desarrolladores controlar el flujo de ejecución de manera precisa y eficiente. A través de esta subunidad didáctica, hemos explorado sus fundamentos y aplicaciones, preparándonos para enfrentar desafíos más complejos en el mundo del desarrollo de software.

### Funciones

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola():
  print("Te digo hola")
  
```

### uso de la funcion

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola():
  print("Te digo hola")
  
diHola()
```

### parametros

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola(nombre):
  print("Hola,",nombre,"yo te saludo")
  
diHola()
```

### Llamada correcta

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola(nombre):
  print("Hola,",nombre,"yo te saludo")
  
diHola("Jose Vicente")
diHola("Jorge")
```

### varios parametros

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo

def diHola(nombre,edad):
  print("Hola,",nombre,", tienes",edad," años y yo te saludo")
  
diHola("Jose Vicente",47)
diHola("Jorge",48)
```

### las funcione retornan

```python
# Deben escribirse con camelCase
# Deben tener un verbo (infinito o imperativo) y un objeto directo
# Deben tener un nombre descriptivo
# Parámetro es el valor que entra en la función
# Return es la forma limpia de sacar información de una función

def diHola(nombre,edad):
  return "Hola,"+nombre+", tienes"+str(edad)+" años y yo te saludo"
  
diHola("Jose Vicente",47)
diHola("Jorge",48)
```

### funcion de sumar

```python
'''
 Funcion correcta:
 Nombre: Verbo imperativo (o infinitivo) + objeto directo
 Usa camelCase
 Debe tener parámetros de entrada
 Debe tener una salida con return
 Debemos evitar prints u otros recursos de salida dentro de la funcion
'''

def calculaSuma(operando1,operando2):
  resultado = operando1 + operando2
  return resultado
  
print(calculaSuma(4,3))
```

### llamada a la funcion de suma

```python
# from archivo import funcion,funcion2,funcion3

from funcionsuma import calculaSuma

print(calculaSuma(4,3))
```

### funcionsuma

```python
'''
 Funcion correcta:
 Nombre: Verbo imperativo (o infinitivo) + objeto directo
 Usa camelCase
 Debe tener parámetros de entrada
 Debe tener una salida con return
 Debemos evitar prints u otros recursos de salida dentro de la funcion
'''

def calculaSuma(operando1,operando2):
  resultado = operando1 + operando2
  return resultado
```

<a id="control-de-excepciones"></a>
## Control de excepciones

En el mundo de la programación, las excepciones son como los obstáculos inesperados que aparecen mientras nuestro programa intenta ejecutar sus instrucciones. Estos obstáculos pueden surgir por muchas razones: un error en una operación matemática, la lectura de un archivo que no existe o incluso la interrupción del usuario. El control de excepciones es una técnica fundamental que nos permite manejar estos problemas de manera eficiente y prevenir que el programa se bloquee.

La gestión de excepciones comienza con la identificación de los posibles errores en nuestro código. Cada error tiene un tipo específico, como `ValueError` para errores relacionados con valores inapropiados o `FileNotFoundError` cuando intentamos acceder a un archivo que no existe. Una vez identificados estos tipos de errores, podemos programar respuestas específicas para cada uno.

El bloque `try-except` es la herramienta principal para manejar excepciones en Python. En este bloque, colocamos el código que podría generar una excepción dentro del bloque `try`, y luego definimos cómo responder a esa excepción en el bloque `except`. Si ocurre una excepción durante la ejecución del código en `try`, el flujo de control inmediatamente salta al bloque `except` correspondiente.

Además de manejar excepciones, también es importante saber cómo crear nuestras propias excepciones personalizadas. Esto nos permite expresar con precisión los errores específicos que ocurren en nuestro programa y proporcionar mensajes útiles para el usuario o el desarrollador. Para crear una excepción personalizada, simplemente definimos una nueva clase que herede de la clase base `Exception`.

El control de excepciones también implica la gestión de recursos. A menudo, cuando abrimos un archivo o establecemos una conexión a una base de datos, es crucial asegurarnos de que estos recursos se liberen correctamente incluso si ocurren errores. Para hacer esto, usamos el bloque `finally`, que siempre se ejecuta después del bloque `try-except`, independientemente de si ocurrió una excepción o no.

La importancia del control de excepciones en la programación es inmensa. No solo ayuda a prevenir que nuestro programa se bloquee debido a errores, sino que también mejora su robustez y fiabilidad. Al manejar adecuadamente las excepciones, podemos proporcionar experiencias más seguras y fáciles para los usuarios finales.

Además de la gestión de excepciones, es crucial entender cómo usar el registro de errores. El registro nos permite capturar información sobre los errores que ocurren en nuestro programa, lo que facilita su diagnóstico y solución. Python ofrece varias bibliotecas para el registro de errores, como `logging`, que nos permiten configurar diferentes niveles de detalle y formatos de salida.

El control de excepciones también es fundamental para la implementación de políticas de seguridad en nuestros programas. Al capturar y manejar adecuadamente las excepciones, podemos prevenir accesos no autorizados o operaciones peligrosas que podrían comprometer la integridad del sistema.

En resumen, el control de excepciones es una habilidad esencial en la programación. Nos permite manejar errores inesperados de manera eficiente y prevenir que nuestro programa se bloquee. Al aprender a identificar, capturar y gestionar excepciones, podemos crear programas más seguros, robustos y fáciles de mantener.

### tryexcept

```python
try:
  print(4+3)
except:
  print("Ha ocurrido un error")
  
print("Pero el programa continúa pase lo que pase")
```

### error

```python
print(4/0)

print("Y el programa continua")
```

### error con try except

```python
try:
  print(4/0)
except:
  print("No puedo ejecutar eso")

print("Y el programa continua")
```

### pseudocodigo

```python
try:
  print(4/0)
  print("Intento conectarme a la base de datos")
  print("pero falla")
except:
  print("No puedo ejecutar eso")
  print("Pues por lo menos guardo los datos a un archivo local temporal")

print("Y el programa continua")
```

### Excepcion como e

```python
dividendo = 4
divisor = 0

try:
  division = dividendo/divisor
except:
  print("Hay un error")
```

### capturo el error

```python
dividendo = 4
divisor = 0

try:
  division = dividendo/divisor
except Exception as mierror:
  print("Hay un error")
  print(mierror)
```

### errores personalizados

```python
dividendo = 4
divisor = 0

try:
  division = dividendo/divisor
except ZeroDivisionError:
  print("Tienes un error de division por cero")
except Exception as mierror:
  print("Hay un error")
  print(mierror)
```

### todos los posibles

```python
dividendo = 4
divisor = 0

try:
    division = dividendo / divisor

except ZeroDivisionError:
    print("❌ Error: división por cero.")

except TypeError:
    print("❌ Error: tipos de datos incompatibles para la operación.")

except ValueError:
    print("❌ Error: valor no válido.")

except NameError:
    print("❌ Error: variable no definida.")

except IndexError:
    print("❌ Error: índice fuera de rango.")

except KeyError:
    print("❌ Error: clave inexistente en un diccionario.")

except AttributeError:
    print("❌ Error: atributo no encontrado en el objeto.")

except ImportError:
    print("❌ Error: problema al importar un módulo o función.")

except FileNotFoundError:
    print("❌ Error: archivo no encontrado.")

except PermissionError:
    print("❌ Error: permiso denegado al acceder a un recurso.")

except OSError:
    print("❌ Error del sistema operativo (archivos, rutas, etc.).")

except MemoryError:
    print("❌ Error: la memoria disponible se ha agotado.")

except RecursionError:
    print("❌ Error: recursión demasiado profunda.")

except Exception as e:
    print("⚠️  Error inesperado:")
    print(type(e).__name__, "-", e)

except BaseException as e:
    print("🛑 Error crítico del sistema:")
    print(type(e).__name__, "-", e)

else:
    print("✅ La operación se realizó correctamente.")

finally:
    print("🔚 Fin del bloque try-except.")
```

### atrapar dato en consola

```python
try:
    numero = int("hola")  # Intentamos convertir texto no numérico a entero
    print("El número es:", numero)

except ValueError:
    print("❌ Error: valor no válido (no se puede convertir a número).")

finally:
    print("🔚 Fin del bloque try-except.")
```

<a id="aserciones"></a>
## Aserciones

En el mundo de la programación, las aserciones son una herramienta poderosa que nos permite verificar la integridad del programa durante su ejecución. Estas declaraciones condicionales permiten comprobar si ciertas condiciones son verdaderas o no, y en caso de que no lo sean, detienen la ejecución del programa para evitar errores inesperados.

Las aserciones se utilizan principalmente para asegurar que el estado interno de un programa sea correcto antes de continuar con las operaciones. Son especialmente útiles durante el desarrollo y la depuración, ya que nos permiten identificar rápidamente dónde algo sale mal en nuestro código. En su forma más básica, una aserción se compone de una expresión booleana que debe evaluarse como verdadera para que el programa continúe ejecutándose.

La implementación de aserciones en la programación es relativamente sencilla. Se utiliza un comando específico dependiendo del lenguaje de programación utilizado, pero generalmente sigue el patrón: "si la expresión es falsa, detén la ejecución". Esta estructura permite que los desarrolladores se aseguren de que ciertos invariants o precondiciones sean cumplidos antes de avanzar.

Es importante destacar que las aserciones no deben usarse como un mecanismo principal para el control del flujo normal del programa. Su uso debe estar limitado a situaciones excepcionales, donde la violación de una condición implica un error grave o una inconsistencia interna que no puede ser manejada de otra manera. En su lugar, las aserciones deben complementar otras técnicas como el manejo de errores y excepciones para proporcionar una mayor robustez al programa.

La práctica del uso de aserciones en la programación es un aspecto fundamental de la metodología ágil y la ingeniería de software moderna. Algunas prácticas recomendadas incluyen la activación de las aserciones durante el desarrollo, pero su desactivación o supresión durante la fase de producción para evitar interrupciones inesperadas del programa.

En resumen, las aserciones son una herramienta valiosa en el arsenal del programador que nos permite asegurar la integridad y consistencia de nuestro código. Aunque deben usarse con precaución y no como un reemplazo del manejo de errores, su uso judicioso puede mejorar significativamente la calidad y confiabilidad de nuestros programas.

### chivato

```python
assert 3 == 3 , "Eso no es cierto"
```

### el chivato salta

```python
assert 3 == 2 , "Eso no es cierto"
```

### ejemplo no tan traumatico

```python
edad = 47

assert edad == 48, "no es correcto"
```

### combinacion

```python
edad = 47
try:
  assert edad == 48, "no es correcto"
except:
  print("Error determinado")
```

<a id="prueba-depuracion-y-documentacion-de-la-aplicacion"></a>
## Prueba, depuración y documentación de la aplicación

En el mundo digital, la programación es una habilidad fundamental que requiere no solo conocimiento técnico, sino también una mentalidad crítica y creativa. La carpeta `Primero/Programación/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación` nos guía a través de un proceso esencial en el desarrollo de software: la prueba, la depuración y la documentación.

La prueba es una etapa crucial que permite verificar si nuestro programa cumple con los requisitos establecidos. Es como hacer un examen exhaustivo para asegurarnos de que todo funciona correctamente. En este proceso, se realizan pruebas unitarias individuales para cada función o método, así como pruebas integrales que evalúan cómo estas partes interactúan entre sí.

La depuración es el proceso de identificar y corregir errores en nuestro código. Es como buscar una pequeña falla en un edificio para asegurar su estabilidad. Utilizamos herramientas especializadas y técnicas de programación para localizar los problemas, ya sean faltas lógicas o errores de sintaxis.

La documentación es la parte que nos permite compartir nuestro trabajo con otros desarrolladores y recordar nuestros propios pensamientos en el futuro. Es como dejar un mapa detallado de cómo se construyó un edificio para que otros puedan seguir las mismas instrucciones. La documentación incluye comentarios dentro del código, explicaciones de los algoritmos utilizados y descripciones de las funciones.

Juntos, estos tres procesos forman una base sólida para el desarrollo de software. Prueba nos asegura que nuestro programa funcione como se espera, depuración nos permite corregir errores y documentación nos facilita la colaboración y el mantenimiento a largo plazo. Es un ciclo continuo que implica revisión, corrección y mejora constante.

La prueba es el ojo del juez en nuestro código, la depuración es su mano que corrige los defectos y la documentación es su voz que explica las intenciones detrás de cada línea. Juntos, forman una trifecta incesante de mejora y optimización.

Es importante recordar que el desarrollo de software no es solo sobre escribir código, sino también sobre entender cómo funciona nuestro programa y cómo podemos mejorarlo continuamente. Prueba, depuración y documentación son las herramientas que nos permiten lograr este objetivo, asegurando que nuestro trabajo sea robusto, confiable y fácil de mantener.

En resumen, la carpeta `Primero/Programación/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación` nos enseña cómo llevar a cabo estos procesos esenciales en el desarrollo de software. Es un camino que requiere atención, paciencia y dedicación, pero que resulta en programas más sólidos y eficientes.

### funcion de division

```python
def hazDivision(dividendo,divisor):
  resultado = dividendo/divisor
  return resultado
  
print(hazDivision(4,3))

for i in range(-100,100):
  for j in range(-100,100):
    hazDivision(i,j)

print("Todo ha ido correcto")
```

### mejora

```python
def hazDivision(dividendo,divisor):
  if divisor != 0:
    resultado = dividendo/divisor
  else:
    resultado = 0
  return resultado
  
print(hazDivision(4,3))

for i in range(-100,100):
  for j in range(-100,100):
    hazDivision(i,j)

print("Todo ha ido correcto")
```

### nuevo fallo

```python
def hazDivision(dividendo,divisor):
  if divisor != 0:
    resultado = dividendo/divisor
  else:
    resultado = 0
  return resultado
  
print(hazDivision(4,a))
```

### nuevo fallo mas

```python
def hazDivision(dividendo,divisor):
  # Comprobamos si son números
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      resultado = dividendo/divisor
    else:
      resultado = 0
    return resultado
  else:
    return 0
  
print(hazDivision(4,"a"))
```

### cadenas

```python
def hazDivision(dividendo,divisor):
  # Comprobamos si son números
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      resultado = dividendo/divisor
    else:
      resultado = 0
    return resultado
  else:
    return 0
  
print(hazDivision(4,"3"))
```

### mejoro cadenas

```python
def hazDivision(dividendo,divisor):
  # Comprobamos si son números
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      resultado = dividendo/divisor
      return resultado
    else:
      resultado = 0
  else:
    try:
      # Vamos a intentar convertirlo a numeros
      dividendo = float(dividendo)
      divisor = float(divisor)
      resultado = dividendo/divisor
      return resultado
    except:
      return 0
  
print(hazDivision(4,"3"))
```

### depuracion

```python
def hazDivision(dividendo,divisor):
  # Comprobamos si son números
  print("Entramos en la funcion")
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    print("parece que los parametros son numeros")
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      print("parece que los puedo dividir")
      resultado = dividendo/divisor
      return resultado
    else:
      print("No puedo dividir porque el divisor es cero")
      resultado = 0
  else:
    print("Los parametros no son numeros, pero voy a intentar convertirlos")
    try:
      print("Intento convertir a numeros con exito")
      # Vamos a intentar convertirlo a numeros
      dividendo = float(dividendo)
      divisor = float(divisor)
      resultado = dividendo/divisor
      return resultado
    except:
      print("He intentado convertir a numeros, pero no he podido")
      return 0
  
print(hazDivision(4,"3"))
```

### documentacion de la funcion

```python
def hazDivision(dividendo,divisor):
  '''
    Función de división
    Entradas: dividendo y divisor que se espera que sean numéricos
    Salidas: resultado de la división como número (o cero si hay fallo)
    Capturas de error: 
      1.-Si es numérico
      2.-Si se puede convertir a número
      3.-Si no es división entre cero
  '''
  # Comprobamos si son números
  print("Entramos en la funcion")
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    print("parece que los parametros son numeros")
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      print("parece que los puedo dividir")
      resultado = dividendo/divisor
      return resultado
    else:
      print("No puedo dividir porque el divisor es cero")
      resultado = 0
  else:
    print("Los parametros no son numeros, pero voy a intentar convertirlos")
    try:
      print("Intento convertir a numeros con exito")
      # Vamos a intentar convertirlo a numeros
      dividendo = float(dividendo)
      divisor = float(divisor)
      resultado = dividendo/divisor
      return resultado
    except:
      print("He intentado convertir a numeros, pero no he podido")
      return 0
  
print(hazDivision(4,"3"))
```

### extraccion de funcion

```python
from funciondivision import hazDivision
  
print(hazDivision(4,"3"))
```

### ejercicio propuesto

```python
Enunciado: Raíz cuadrada segura

Implementa una función raizSegura(numero) que cumpla:

Validación y manejo de errores

Si numero es un valor numérico (int o float) y es mayor o igual a 0 → devuelve su raíz cuadrada.

Si numero es una cadena, intenta convertirla a float y aplica la regla anterior.

Si la conversión falla, o si el número es negativo, la función debe devolver 0.

Usa try/except para capturar errores en la conversión o en el cálculo.

Aserciones

Usa al menos dos assert internos, por ejemplo:

que la salida siempre sea un número (int o float),

que si la entrada es negativa, la salida sea exactamente 0.

Documentación

Escribe un docstring que explique entradas, salidas y qué errores controla.

Estructura del proyecto

Guarda la función en funcionraiz.py.

Crea un archivo main.py que importe la función y realice 3 pruebas de ejemplo mostrando los resultados por pantalla.

Prueba unitaria pequeña

Crea un archivo test_raiz.py que contenga varios assert para verificar:

Caso correcto con número positivo.

Caso con cadena convertible.

Caso con número negativo.

Caso con cadena no convertible.

Caso con 0.
```

### tres en raya

```python
print("Tres en raya - 2 jugadores humanos")
print("(c) 2025 Jose Vicente Carratala")

jugador = 1
casilla1 = 1
casilla2 = 2
casilla3 = 3
casilla4 = 4
casilla5 = 5
casilla6 = 6
casilla7 = 7
casilla8 = 8
casilla9 = 9

while True:
  print(f'{casilla1}|{casilla2}|{casilla3}')
  print(f'------')
  print(f'{casilla4}|{casilla5}|{casilla6}')
  print(f'------')
  print(f'{casilla7}|{casilla8}|{casilla9}')
  tirada = input("Tirada del jugador "+str(jugador))
  if int(tirada) == 1:
    if jugador == 1:
      casilla1 = "X"
    else:
      casilla1 = "O"
  if int(tirada) == 2:
    if jugador == 1:
      casilla2 = "X"
    else:
      casilla2 = "O"
  if int(tirada) == 3:
    if jugador == 1:
      casilla3 = "X"
    else:
      casilla3 = "O"
  if int(tirada) == 4:
    if jugador == 1:
      casilla4 = "X"
    else:
      casilla4 = "O"
  if int(tirada) == 5:
    if jugador == 1:
      casilla5 = "X"
    else:
      casilla5 = "O"
  if int(tirada) == 6:
    if jugador == 1:
      casilla6 = "X"
    else:
      casilla6 = "O"
  if int(tirada) == 7:
    if jugador == 1:
      casilla7 = "X"
    else:
      casilla7 = "O"
  if int(tirada) == 8:
    if jugador == 1:
      casilla8 = "X"
    else:
      casilla8 = "O"
  if int(tirada) == 9:
    if jugador == 1:
      casilla9 = "X"
    else:
      casilla9 = "O"
  if jugador == 1:
    jugador = 2
  else:
    jugador = 1
  
```

### funciondivision

```python
def hazDivision(dividendo,divisor):
  '''
    Función de división
    Entradas: dividendo y divisor que se espera que sean numéricos
    Salidas: resultado de la división como número (o cero si hay fallo)
    Capturas de error: 
      1.-Si es numérico
      2.-Si se puede convertir a número
      3.-Si no es división entre cero
  '''
  # Comprobamos si son números
  print("Entramos en la funcion")
  if isinstance(dividendo, (int, float, complex)) and isinstance(divisor, (int, float, complex)):
    print("parece que los parametros son numeros")
    # Comprobamos que el divisor no es cero
    if divisor != 0:
      print("parece que los puedo dividir")
      resultado = dividendo/divisor
      return resultado
    else:
      print("No puedo dividir porque el divisor es cero")
      resultado = 0
  else:
    print("Los parametros no son numeros, pero voy a intentar convertirlos")
    try:
      print("Intento convertir a numeros con exito")
      # Vamos a intentar convertirlo a numeros
      dividendo = float(dividendo)
      divisor = float(divisor)
      resultado = dividendo/divisor
      return resultado
    except:
      print("He intentado convertir a numeros, pero no he podido")
      return 0
```

<a id="ejercicio"></a>
## Ejercicio

En el mundo de la programación, las estructuras de control son como los pilares que sostienen una construcción. Son fundamentales para organizar y controlar el flujo de ejecución del programa, permitiendo decisiones condicionales y repeticiones precisas. En esta carpeta, nos sumergimos en el ejercicio práctico de cómo aplicar estas estructuras en nuestro código.

Comenzamos con la estructura de selección, que es como una bifurcación en un camino. Dependiendo del valor de una expresión booleana, el programa tomará diferentes caminos. Esta es una herramienta poderosa para manejar decisiones complejas y tomar acciones basadas en condiciones específicas.

La siguiente estructura es la repetición, que nos permite realizar una tarea varias veces hasta que se cumpla una condición determinada. Este tipo de control es esencial para tareas como recorrer listas, procesar archivos o ejecutar algoritmos iterativos. Aprender a controlar el número de repeticiones y la condición de terminación es crucial para optimizar el rendimiento del programa.

Además, existen estructuras de control que nos permiten manejar excepciones, situaciones inesperadas durante la ejecución del programa. Estas estructuras son como una red de seguridad que previene caídas y permite recuperarse de errores sin interrumpir completamente la operación del programa.

La programación también implica el uso de bucles anidados, donde un bucle está dentro de otro. Este tipo de estructura es útil cuando necesitamos realizar una tarea repetitiva en múltiples niveles o dimensiones. Es como construir con bloques de construcción, donde cada nivel depende del anterior.

La programación orientada a objetos introduce la estructura de las clases y los métodos. Las clases son como plantillas para crear objetos, mientras que los métodos definen las acciones que pueden realizar estos objetos. Esta estructura permite organizar el código en bloques lógicos y reutilizables, facilitando su mantenimiento y escalabilidad.

Además, la programación también implica el uso de bucles controlados por contador, donde se especifica explícitamente cuántas veces se ejecutará un bloque de código. Este tipo de estructura es útil cuando sabemos con certeza el número exacto de repeticiones necesarias.

La programación también requiere el manejo de eventos y callbacks, que son funciones que se ejecutan en respuesta a ciertas acciones o cambios en el programa. Estas estructuras permiten crear programas interactivos y responder dinámicamente a las entradas del usuario.

Finalmente, la programación implica el uso de bucles controlados por sentinela, donde el número de repeticiones depende de una entrada externa o un cambio en el estado del programa. Este tipo de estructura es útil cuando no sabemos con certeza cuántas veces se ejecutará un bloque de código.

En resumen, las estructuras de control son herramientas fundamentales para organizar y controlar el flujo de ejecución del programa. Aprender a usar estas estructuras correctamente es esencial para escribir programas eficientes, seguros y fáciles de mantener.

### ejercicio for

```python
for dia in range(1,31):
  print("Hoy es el dia",dia,"del mes")
  if dia == 15:
    print("🎉 Hoy es el cumpleaños de mi amigo")
    
```

### ejercicio escalones

```python
escalon = 1

while escalon < 16:
  print("Estoy en el escalon",escalon)
  escalon += 1
```

### subir escalones de dos en dos

```python
escalon = 1

while escalon < 16:
  print("Estoy en el escalon",escalon)
  escalon += 2
```

### dragones

```python
# En este bloque tomo los datos del usuario #######################

nombre_dragon_a = input("Dime el nombre del dragón A: ")
edad_dragon_a = input("Dime la edad del dragón A: ")
clasificacion_dragon_a = ""
fuerza_dragon_a = 0
resistencia_dragon_a = 0

print("El nombre del dragon A es:",nombre_dragon_a)
print("La edad del dragon A es:",edad_dragon_a)

nombre_dragon_b = input("Dime el nombre del dragón B: ")
edad_dragon_b = input("Dime la edad del dragón B: ")
clasificacion_dragon_b = ""
fuerza_dragon_b = 0
resistencia_dragon_b = 0

print("El nombre del dragon A es:",nombre_dragon_b)
print("La edad del dragon A es:",edad_dragon_b)

# En este bloque me aseguro de que son enteros #######################

try:
  edad_dragon_a = int(edad_dragon_a)
  print("He convertido la edad A correctamente")
except:
  edad_dragon_a = 100
  print("No he convertido la edad A correctamente, asigno 100")
  
try:
  edad_dragon_b = int(edad_dragon_b)
  print("He convertido la edad B correctamente")
except:
  edad_dragon_b = 100
  print("No he convertido la edad B correctamente, asigno 100")

# En este bloque clasifico a los dragones #######################

if edad_dragon_a < 50:
  clasificacion_dragon_a = "Joven"
elif edad_dragon_a >= 50 and edad_dragon_a <= 199:
  clasificacion_dragon_a = "Adulto"
elif edad_dragon_a >= 200:
  clasificacion_dragon_a = "Anciano"
print("El dragon A es:",clasificacion_dragon_a)
  
if edad_dragon_b < 50:
  clasificacion_dragon_b = "Joven"
elif edad_dragon_b >= 50 and edad_dragon_b <= 199:
  clasificacion_dragon_b = "Adulto"
elif edad_dragon_b >= 200:
  clasificacion_dragon_b = "Anciano"
print("El dragon B es:",clasificacion_dragon_b)

# Ahora los vamos a entrenar ###################################

for dia in range (1,4):
  # Como entrenar a tu dragon A
  if clasificacion_dragon_a == "Joven":
    fuerza_dragon_a += 2
    resistencia_dragon_a += 2
  elif clasificacion_dragon_a == "Adulto":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  elif clasificacion_dragon_a == "Anciano":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  print("Final del dia",dia)
  print("El dragon A ahora tiene ",fuerza_dragon_a,"de fuerza y ",resistencia_dragon_a,"de resistencia")
  # Como entrenar a tu dragon B
  if clasificacion_dragon_b == "Joven":
    fuerza_dragon_b += 2
    resistencia_dragon_b += 2
  elif clasificacion_dragon_b == "Adulto":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  elif clasificacion_dragon_b == "Anciano":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  print("Final del dia",dia)
  print("El dragon B ahora tiene ",fuerza_dragon_b,"de fuerza y ",resistencia_dragon_b,"de resistencia")
```

### enunciado

```markdown
Descripción

Registro de dragones (entrada del usuario)

Pide por consola nombre y edad de cada dragón: Dragón A y Dragón B.

Convierte la edad a entero con try/except. Si falla, usa un valor por defecto (p. ej., 100 años).

Clasifica cada dragón por edad con condicionales:

< 50 → “Joven”

50–199 → “Adulto”

≥ 200 → “Anciano”

Entrenamiento (bucle for)

Simula 3 días de entrenamiento por dragón con un for.

Cada día incrementa:

fuerza (p. ej., +2 por día si es Joven, +1 si es Adulto, +1 si es Anciano).

resistencia (regla similar).

Muestra por pantalla el progreso de cada día (una línea por día).

Funciones obligatorias

calculaFuerzaBase(edad) -> int
Devuelve una fuerza inicial según la categoría (elige una regla y documéntala).

turnoDeAtaque(fuerza, resistenciaEnemigo) -> int
Calcula el daño de un ataque y lo devuelve (no hagas print dentro).

Duelo (bucle while)

Inicializa salud de cada dragón (p. ej., 30–50 puntos, a tu elección).

En un while que termine cuando uno llegue a salud ≤ 0:

Turno alterno: A golpea a B y luego B a A (usa un contador de turnos).

En cada golpe, llama a turnoDeAtaque(...) y resta salud al rival.

Si la salud cae por debajo de 0, ajústala a 0 y termina el bucle.

Puedes usar un for interno para contar “subturnos” o “intentos” del ataque (por ejemplo, 2 mordiscos por turno).

Manejo de errores

Cualquier entrada (edad, confirmaciones) debe pasar por try/except.

Aserciones

Incluye al menos 2 assert:

Que la salud nunca sea negativa tras un ajuste.

Que el daño devuelto por turnoDeAtaque sea numérico y ≥ 0.

Salida final

Muestra un resumen: nombres, categorías, fuerza final, resistencia final, y ganador del duelo.
```

### magos

```python
Descripción

Crea un programa por consola que simule un duelo relámpago entre un mago y un hechizo protector.

Entrada con validación

Pide la edad del mago. Convierte a int con try/except.

Si falla, usa edad 100 por defecto.

Clasificación y poder base (selección + función)

Clasifica al mago según su edad:

<30 → Aprendiz

30–99 → Hechicero

≥100 → Archimago

Implementa poderBase(edad) -> int que devuelva:

Aprendiz → 5

Hechicero → 8

Archimago → 10

(documenta la función con un docstring).

Rompimiento del hechizo (bucle + selección)

El escudo mágico empieza con 15 puntos de energía.

Recorre dos turnos con un for de 1 a 2:

Turno 1 → “Hechizo de Fuego” → daño = poderBase // 2

Turno 2 → “Hechizo de Rayo” → daño = poderBase // 3

Resta el daño al escudo.

Si la energía del escudo baja de 0, ajústala a 0 y sal del bucle.

Aserciones mínimas

Tras calcular cada daño: assert que el daño es numérico y ≥ 0.

Tras ajustar la energía: assert que la energía es ≥ 0.

Salida

Muestra: edad, rango del mago, poder base, energía final del escudo y resultado:

Si la energía es 0 → “¡El mago rompe el escudo mágico!”

Si no → “El escudo resiste al duelo relámpago.”


# pedir edad
edad_mago = input("Introduce la edad del mago: ")
# convertir a entero
try:
  edad_mago = int(edad_mago)
except: 
  # si falla, pon 100
  edad_mago = 100

# clasifica por edad
# menor que 30 es Aprendiz
# de 30 a 99 es Hechicero
# mas de 100 es Archimago

# funcion poderBase, recibe edad, devuelve entero
# si es aprendiz, devuelve 5
# si es hechicero, devuelve 8
# si es archimago, devuelve 10

# empezamos bucle
# escudo empieza con 15 puntos
# recorre dos turnos con for
# turno 1 fuego daño = poderBase // 2
# turno 2 hechizo rayo = daño = poderBase // 3
# resta el daño al escudo
# si energia escudo baja de cero, ajusta a cero

# tras cada daño, print de daño y mayor que cero
# tras ajuste energia, print y energia es mayor que cero

# salida: edad, rango, poder base, energia del escudo
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo
```

<a id="ejercicio-de-final-de-unidad-2"></a>
## Ejercicio de final de unidad

### Holamundo

```python
print("Hola mundo desde Python")
```

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```


<a id="desarrollo-de-clases"></a>
# Desarrollo de clases

<a id="concepto-de-clase"></a>
## Concepto de clase

En el vasto universo de la programación, las clases son como los bloques fundamentales que construyen edificios impresionantes. Un concepto tan esencial como este merece una exploración profunda y detallada, para entender su importancia y cómo se aplican en la creación de programas informáticos.

La clase es un molde abstracto que define las características y comportamientos comunes de un conjunto de objetos. Es el plano o la plantilla a partir del cual se crean instancias concretas de ese tipo. En términos simples, una clase es como un modelo para crear coches; cada coche que se fabrica a partir de este modelo tendrá las mismas características básicas (llantas, puertas, motor) pero puede variar en detalles específicos (color, marca).

La definición de una clase comienza con la palabra clave `class`, seguida del nombre de la clase. Este nombre debe ser descriptivo y seguir las convenciones de nomenclatura utilizadas en el lenguaje de programación que estés utilizando. Por ejemplo:

```python
class Coche:
    pass
```

En este ejemplo, `Coche` es el nombre de la clase. El bloque `pass` es simplemente un marcador de posición que indica que aquí se definirá el contenido de la clase.

Una vez creada una clase, puedes añadir atributos y métodos a ella. Los atributos son variables que almacenan datos específicos del objeto, mientras que los métodos son funciones que definen las acciones que puede realizar el objeto. Por ejemplo:

```python
class Coche:
    marca = "Toyota"
    
    def arrancar(self):
        print("El coche está arrancando")
```

En este caso, `marca` es un atributo de la clase `Coche`, y `arrancar` es un método que define una acción que puede realizar un objeto de esta clase.

La creación de instancias a partir de una clase se realiza mediante el uso del operador `new` (o simplemente el nombre de la clase seguido de paréntesis en algunos lenguajes). Por ejemplo:

```python
mi_coche = Coche()
```

Esta línea de código crea un nuevo objeto de la clase `Coche`, y lo asigna a la variable `mi_coche`. Ahora, puedes acceder a los atributos y métodos de este objeto mediante el punto (`.`):

```python
print(mi_coche.marca)  # Imprime: Toyota
mi_coche.arrancar()   # Imprime: El coche está arrancando
```

La programación orientada a objetos, que es la base del desarrollo de clases, permite organizar y estructurar el código de una manera más lógica y fácil de mantener. Al definir clases, puedes encapsular datos y comportamientos relacionados en un solo lugar, lo que facilita su reutilización y modificación.

Además, las clases permiten la herencia, que es un mecanismo que permite crear nuevas clases a partir de otras existentes. La clase hija puede heredar atributos y métodos de la clase padre, y además añadir nuevos o modificar los existentes. Esta característica es fundamental para crear jerarquías de objetos complejas y reutilizar código.

En resumen, las clases son una herramienta poderosa en el arsenal del programador. Son la base de la programación orientada a objetos y permiten organizar y estructurar el código de manera más lógica y eficiente. Al comprender completamente el concepto de clase, se abre un mundo de posibilidades para crear programas complejos y robustos que puedan adaptarse a las necesidades cambiantes del usuario.

### Introduccion

```markdown
Anteriormente hemos visto como las funciones permiten encapsular código
Cuando encapsulamos podemos

- Reutilizar 
- Externalizar

Las clases llevan esta metodología mucho más alla
```

### clase gato

```python
class Gato:
  pass
  
```

### instanciamos un gato

```python
class Gato:
  pass
  
gato1 = Gato()
print(gato1)
```

### ahora quiero crear otro gato

```python
class Gato:
  pass
  
gato1 = Gato()
print(gato1)

gato2 = Gato()
print(gato2)
```

### Elementos principales de las clases

```markdown
Los elementos principales de una clase son:

- Las propiedades: piezas de información estáticas (no se "mueven")

Son como variables

- Los métodos: piezas de información que "se mueven"

Son como funciones
```

### propiedades y metodos

```python
class Gato:
  def __init__(self):
    self.color = ""
  
jaegger = Gato()
jaegger.color = "crema"

lana = Gato()
lana.color = "gris"
```

### propiedades

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = 0
  
jaegger = Gato()
jaegger.color = "crema"
jaegger.edad = 9

lana = Gato()
lana.color = "gris"
lana.edad = 11
```

### introduccion a los metodos

```python
class Gato:
  def __init__(self):
    self.color = ""
    self.edad = 0
  def maulla(self):
    print("El gato está maullando")
  
jaegger = Gato()
jaegger.color = "crema"
jaegger.edad = 9
jaegger.maulla()

lana = Gato()
lana.color = "gris"
lana.edad = 11
lana.maulla()
```

### objeto cliente

```python
cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratala Sanchis"

cliente2_email = "info@cliente2.com"
cliente2_direccion = "La calle del cliente2"
cliente2_nombre = "Juan"
cliente2_apellidos = "García"
```

### clase cliente

```python
# Poco escalable - uso de muchas variables

cliente1_email = "info@jocarsa.com"
cliente1_direccion = "La calle de Jose Vicente"
cliente1_nombre = "Jose Vicente"
cliente1_apellidos = "Carratala Sanchis"

cliente2_email = "info@cliente2.com"
cliente2_direccion = "La calle del cliente2"
cliente2_nombre = "Juan"
cliente2_apellidos = "García"

# Mucho mejor: uso de clases

class Cliente:
  def __init__(self):
    self.email = ""
    self.direccion = "" 
    self.nombre = ""
    self.apellidos = ""
    
cliente1 = Cliente()
cliente1.email = "info@jocarsa.com"
cliente1.direccion = "La calle de Jose Vicente"
cliente1.nombre = "Jose Vicente"
cliente1.apellidos = "Carratala Sanchis"

cliente2 = Cliente()
cliente2.email = "info@cliente2.com"
cliente2.direccion = "La calle del cliente2"
cliente2.nombre = "Juan"
cliente2.apellidos = "García"
  
```

### Paradigmas en programacion

```markdown
Paradigma clásico: Estructurado

Listas de instrucciones que se ejecutan una detrás de la otra

Paradigma funcional:

Creas funciones, las almacenas en memoria y las usas cuando las necesitas

Paradigma orientado a objetos:

No solo creas funciones, sino que creas objetos, los almacenas en memoria, y luego los usas

Cada lenguaje puede adoptar uno o varios paradigmas

Los lenguajes que adoptan varios paradigmas, se llaman multiparadigma
Por ejemplo, Python es multiparadigma

Java es un lenguaje estrictamente orientado a objetos
Tienes que hacer objetos lo quieras o no

Los lenguajes estrictamente "algo" son mejores en el sentido de que "obligan" a tener buenas prácticas
Para hacer un programa sencilo es un rollo tener que hacer una clase

Años 60-70
Paradigma estructurado - Pascal - COBOL - BASIC

Años 70:
Paradigma funcional-estructurado - C

Años 80:
Aparece paradigma POO - C++ - SCALA

Años 90:
Se populariza el modelo estricto de POO - Java 1995 - C# 1998

2000's 
La época dorada de la programación orientada a objetos
La epoca dorada de Java y C#

2010's
No nos flipemos
Java, C# etc tienen su valor, y lo siguen teniendo
Pero hay un nicho para programas mas sencillos
Oracle se empieza a cargar Java
```

<a id="estructura-y-miembros-de-una-clase-visibilidad"></a>
## Estructura y miembros de una clase. Visibilidad

En el vasto terreno de la programación orientada a objetos, las clases son una construcción fundamental que nos permite modelar entidades del mundo real. Una clase es un molde o plantilla que define las características y comportamientos comunes de un conjunto de objetos. Cada objeto creado a partir de una clase se denomina instancia de esa clase.

La estructura y los miembros de una clase son elementos cruciales para definir su comportamiento y funcionalidad. Los miembros de una clase pueden ser atributos (también conocidos como variables) o métodos (funciones). Estos miembros definen las propiedades y capacidades que tendrán todas las instancias de la clase.

La visibilidad es un aspecto importante en el diseño de clases, ya que determina quién puede acceder a los atributos y métodos. En programación orientada a objetos, existen tres niveles de visibilidad: público (public), protegido (protected) y privado (private). Cada nivel tiene sus propias reglas sobre el acceso:

- **Público (public)**: Los miembros públicos son accesibles desde cualquier parte del programa. Son los que más a menudo se utilizan para exponer la funcionalidad de una clase.

- **Protegido (protected)**: Los miembros protegidos son accesibles dentro de la misma clase y en las clases derivadas. Esta visibilidad es útil cuando deseamos permitir el acceso a ciertos miembros solo dentro del paquete, pero no fuera de él.

- **Privado (private)**: Los miembros privados son accesibles solo dentro de la propia clase. Son los que se utilizan para ocultar detalles internos y proteger la integridad de los datos.

La estructura de una clase en programación orientada a objetos suele seguir un patrón común, aunque puede variar según el lenguaje de programación utilizado. Generalmente, comienza con la declaración de la clase seguida del nombre de la clase y las llaves que encierran su contenido.

Dentro de una clase, los miembros se declaran en orden: primero los atributos, luego los métodos. Cada miembro tiene un tipo de dato asociado y puede tener modificadores de acceso como public, protected o private.

La declaración de un método dentro de una clase es similar a la declaración de una función, pero está encapsulada dentro del contexto de la clase. Los métodos definen las acciones que los objetos pueden realizar y cómo interactúan entre sí.

La visibilidad juega un papel crucial en el diseño seguro y eficiente de clases. Al ocultar detalles internos y exponer solo lo necesario, podemos proteger contra modificaciones no deseadas y mantener la coherencia del estado de los objetos.

En resumen, las clases son la base de la programación orientada a objetos, y su estructura y miembros definen su comportamiento. La visibilidad es un mecanismo poderoso que nos permite controlar el acceso a estos miembros, lo que es fundamental para crear sistemas robustos y seguros. A través del uso adecuado de atributos y métodos con diferentes niveles de visibilidad, podemos modelar entidades del mundo real de manera precisa y eficiente.

### listas

```python
cliente1 = "Juan"
cliente2 = "Jorge"

clientes = ["Juan","Jorge","Jaime","Jose"]

print(clientes)
```

### operaciones con listas

```python
cliente1 = "Juan"
cliente2 = "Jorge"

clientes = ["Juan","Jorge","Jaime","Jose"]

print(clientes)

# Añadir un cliente

clientes.append("Julia")

print(clientes)

# Quito un elemento de la lista

clientes.pop()

print(clientes)
```

### clase cliente

```python
# Declaramos una clase
class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None
    
# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = "jose@empresa.com"
cliente1.nombre = "Jose"
cliente1.direccion = "La calle de Jose"



    
```

### le preguntamos al usuario

```python
# Declaramos una clase
class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None
    
# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la direccion del cliente: ")

print(cliente1)



    
```

### leemos los datos del cliente

```python
# Declaramos una clase
class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None
    
# Usamos la clase instanciando en un objeto
cliente1 = Cliente()
cliente1.email = input("Introduce el email del cliente: ")
cliente1.nombre = input("Introduce el nombre del cliente: ")
cliente1.direccion = input("Introduce la direccion del cliente: ")

print(cliente1)
print(cliente1.email)
print(cliente1.nombre)
print(cliente1.direccion)



    
```

### crud

```python
# CRUD
# Create 
# Read
# Update
# Delete

print("Programa de gestión de clientes v0.1 Jose Vicente Carratala")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

# Le permito escoger una opción
opcion = input("Escoge una opción: ")
opcion = int(opcion)   # Convierto a entero

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado
  if opcion == 1:
    print("Vamos a insertar un cliente")
  elif opcion == 2:
    print("Vamos a ver los clientes")
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
    
```

### crud insertar y listar

```python
# CRUD
# Create 
# Read
# Update
# Delete

print("Programa de gestión de clientes v0.1 Jose Vicente Carratala")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado

  # Le permito escoger una opción
  opcion = input("Escoge una opción: ")
  opcion = int(opcion)   # Convierto a entero
  
  if opcion == 1:
    print("Vamos a insertar un cliente")
    nuevocliente = input("Introduce el nombre del cliente: ")
    clientes.append(nuevocliente)
  elif opcion == 2:
    print("Vamos a ver los clientes")
    print(clientes)
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
    
```

### clase cliente

```python
# CRUD
# Create 
# Read
# Update
# Delete

class Cliente():
  def __init__(self):
    self.email = None
    self.nombre = None
    self.direccion = None

print("Programa de gestión de clientes v0.1 Jose Vicente Carratala")

# Muestro opciones en el menú para el usuario
print("Selecciona una opción: ")
print("1.-Insertar un cliente")
print("2.-Listar clientes")
print("3.-Actualizar clientes")
print("4.-Eliminar clientes")

clientes = []   # Creo una lista VACIA

while True: # Esto desata un bucle infinito pero controlado

  # Le permito escoger una opción
  opcion = input("Escoge una opción: ")
  opcion = int(opcion)   # Convierto a entero
  
  if opcion == 1:
    print("Vamos a insertar un cliente")
    # Primero creamos un nuevo cliente
    nuevocliente = Cliente()
    # Ahora le ponemos propiedades
    nuevocliente.nombre = input("Introduce el nombre del cliente: ")
    nuevocliente.email = input("Introduce el email del cliente: ")
    nuevocliente.direccion = input("Introduce la direccion del cliente: ")
    # A la lista de clientes añadimos nuestro cliente
    clientes.append(nuevocliente)
  elif opcion == 2:
    print("Vamos a ver los clientes")
    print(clientes)
  elif opcion == 3:
    print("Vamos a actualizar un cliente")
  elif opcion == 4:
    print("Vamos a eliminar un cliente")
  else:
    break
    
    
    
    
    
    
    
    
    
    
    
```

<a id="creacion-de-propiedades"></a>
## Creación de propiedades

En el vasto mundo de la programación, las clases son como moldeadores de objetos, creando estructuras que encapsulan datos y comportamientos. En esta subunidad didáctica, nos adentramos en la creación de propiedades dentro de estas clases, un paso esencial para dar forma a nuestros programas.

Las propiedades son atributos que definen las características de los objetos. Al igual que las variables, las propiedades almacenan datos, pero tienen una estructura más compleja y funcional. Cada propiedad tiene un nombre, un tipo de dato y puede tener métodos asociados para su acceso y modificación.

La creación de propiedades en una clase es fundamental porque permite encapsular los datos de manera segura y controlada. Esto significa que podemos definir cómo se accede a estos datos (lectura o escritura) y qué acciones se realizan cuando se intenta modificarlos, lo que ayuda a prevenir errores y mantener la integridad del objeto.

Además, las propiedades facilitan el acceso a los datos de manera más intuitiva y segura. En lugar de acceder directamente a una variable interna, podemos utilizar métodos getter y setter para controlar cómo se obtienen y modifican los valores de las propiedades. Esto no solo mejora la seguridad del objeto, sino que también facilita el mantenimiento y evolución del código.

La creación de propiedades también es clave para implementar la programación orientada a objetos (POO), una técnica poderosa que permite organizar y reutilizar el código de manera eficiente. Al definir las propiedades en una clase, podemos crear instancias de esa clase con diferentes valores para sus propiedades, lo que nos permite representar diversos estados del objeto.

En esta subunidad, aprenderemos a declarar propiedades en una clase, cómo definir métodos getter y setter para acceder y modificar sus valores, y cómo utilizar estas propiedades para encapsular los datos de nuestros objetos. A través de ejemplos prácticos, exploraremos cómo implementar las propiedades en diferentes contextos y cómo usarlas para mejorar la estructura y funcionalidad de nuestros programas.

La comprensión de cómo crear y utilizar propiedades es un paso crucial en el aprendizaje de la programación orientada a objetos. Al dominar este concepto, podremos construir clases más robustas y seguras, lo que nos permitirá desarrollar aplicaciones más complejas y eficientes.

### Repaso de propiedades

```python
# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    
```

### las propiedades pueden ser arrays

```python
# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = ['543534','5345345']
    
```

### escribir las propiedades de una clase

```python
# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = ['543534','5345345']
    
# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"

    
```

### leemos propiedad

```python
# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = ['543534','5345345']
    
# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"

print("El nombre del cliente es:",cliente1.nombre)
    
```

### los telefonos deben ser una lista

```python
# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
  def __init__(self):
    self.nombre = ""
    self.edad = 0
    self.telefonos = []
    
# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escribo una propiedad

cliente1.nombre = "Jose Vicente"

print("El nombre del cliente es:",cliente1.nombre)

cliente1.telefonos.append("63354333")
cliente1.telefonos.append("65436456")

print(cliente1.telefonos)
    
```

### aplicacion de productos

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías
    
```

### funciones y clases

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    

    
```

### creamos las variables globales

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []


    
```

### pseudocodigo

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
# Le mostramos al usuario las opciones que tiene
# En función de la opción que coja el usuario
  # O bien creamos un nuevo producto
  # O bien listamos los productos
  # O bien actualizamos los productos
  # O bien eliminamos los productos
    
```

### voy creando el codigo

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Le mostramos al usuario las opciones que tiene
# En función de la opción que coja el usuario
  # O bien creamos un nuevo producto
  # O bien listamos los productos
  # O bien actualizamos los productos
  # O bien eliminamos los productos
# Y volvemos a repetir
    
```

### le mostramos al usuario las opciones que tiene

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
# En función de la opción que coja el usuario
  # O bien creamos un nuevo producto
  # O bien listamos los productos
  # O bien actualizamos los productos
  # O bien eliminamos los productos
# Y volvemos a repetir
    
```

### tomamos la entrada de usuario

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
opcion = int(input("Escoge tu opción: "))
# En función de la opción que coja el usuario
  # O bien creamos un nuevo producto
  # O bien listamos los productos
  # O bien actualizamos los productos
  # O bien eliminamos los productos
# Y volvemos a repetir
    
```

### estructura if

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Le mostramos al usuario las opciones que tiene
print("Selecciona una opción:")
print("1.-Crear un nuevo producto")
print("2.-Listar productos")
print("3.-Actualizar productos")
print("4.-Eliminar productos")
opcion = int(input("Escoge tu opción: "))
# En función de la opción que coja el usuario
if opcion == 1:
  # O bien creamos un nuevo producto
  print("Creamos un nuevo producto")
elif opcion == 2:
  # O bien listamos los productos
  print("Vamos a listar los productos")
elif opcion == 3:
  # O bien actualizamos los productos
  print("Vamos a actualizar productos")
elif opcion == 4:
  # O bien eliminamos los productos
  print("Vamos a eliminar productos")
# Y volvemos a repetir
    
```

### bucle infinito

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Metemos al usuario en un bucle infinito
while True:
  # Le mostramos al usuario las opciones que tiene
  print("Selecciona una opción:")
  print("1.-Crear un nuevo producto")
  print("2.-Listar productos")
  print("3.-Actualizar productos")
  print("4.-Eliminar productos")
  opcion = int(input("Escoge tu opción: "))
  # En función de la opción que coja el usuario
  if opcion == 1:
    # O bien creamos un nuevo producto
    print("Creamos un nuevo producto")
  elif opcion == 2:
    # O bien listamos los productos
    print("Vamos a listar los productos")
  elif opcion == 3:
    # O bien actualizamos los productos
    print("Vamos a actualizar productos")
  elif opcion == 4:
    # O bien eliminamos los productos
    print("Vamos a eliminar productos")
  # Y volvemos a repetir
    
```

### desarrollo la insercion de producto

```python
'''
  Aplicación de gestión de productos
  (c) 2025 Jose Vicente Carratala
  Esta aplicación gestiona productos
'''

# En esta aplicación no aplica importar librerías

# Definimos clases y funciones

class Producto():
  def __init__(self):
    self.nombre = ""
    self.precio = 0
    
# Creamos las variables globales

productos = []

# Primero lanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Jose Vicente Carratala")
# Metemos al usuario en un bucle infinito
while True:
  # Le mostramos al usuario las opciones que tiene
  print("Selecciona una opción:")
  print("1.-Crear un nuevo producto")
  print("2.-Listar productos")
  print("3.-Actualizar productos")
  print("4.-Eliminar productos")
  opcion = int(input("Escoge tu opción: "))
  # En función de la opción que coja el usuario
  if opcion == 1:
    # O bien creamos un nuevo producto
    print("Creamos un nuevo producto")
    producto1 = Producto()           # Creo una nueva instancia de la clase
    producto1.nombre = input("Introduce el nombre del producto: ")   # Escribo la propiedad
    producto1.precio = input("Introduce el precio del producto: ")   # Escribo la propiedad
    productos.append(producto1)      # Y a la la lista de productos le añado el producto
  elif opcion == 2:
    # O bien listamos los productos
    print("Vamos a listar los productos")
  elif opcion == 3:
    # O bien actualizamos los productos
    print("Vamos a actualizar productos")
  elif opcion == 4:
    # O bien eliminamos los productos
    print("Vamos a eliminar productos")
  # Y volvemos a repetir
    
```

<a id="creacion-de-metodos"></a>
## Creación de métodos

En el vasto universo de la programación, los métodos son como las herramientas que nos permiten dar forma a nuestros objetos. Al igual que un carpintero necesita diferentes tipos de martillos para completar su trabajo, un programador necesita diversos métodos para manipular y gestionar los datos de sus clases.

El primer paso en el desarrollo de métodos es entender qué acción queremos que realice nuestro objeto. Un método puede ser tan simple como una función que imprime un mensaje o tan complejo como una operación matemática que procesa múltiples variables. Cada método tiene su propósito específico, y su definición se realiza dentro del cuerpo de la clase.

El nombre de cada método es crucial, ya que actúa como el identificador único que nos permite invocarlo cuando lo necesitemos. Es una buena práctica elegir nombres descriptivos que reflejen claramente la funcionalidad del método. Por ejemplo, si estamos trabajando con un objeto `Persona`, podríamos tener métodos como `cumplirAnios()` o `caminar(int pasos)`.

Además de su nombre, cada método tiene parámetros, que son los valores que necesita para realizar su tarea. Estos parámetros pueden ser de cualquier tipo y número, permitiendo una gran flexibilidad en cómo se utilizan los métodos. Por ejemplo, un método `calcularDescuento(double precioOriginal)` podría recibir el precio original de un producto como parámetro y devolver el precio con descuento aplicado.

El cuerpo del método es donde se define la lógica que ejecutará cuando el método sea invocado. Aquí es donde se realizan las operaciones necesarias para lograr el objetivo del método. Cada línea de código dentro del método debe ser clara y concisa, facilitando su lectura y depuración.

Es importante recordar que los métodos deben seguir un principio fundamental: la responsabilidad única. Un método debería tener una sola tarea y hacerla bien. Esto no solo hace que el código sea más fácil de mantener y entender, sino que también facilita la reutilización del código en diferentes partes del programa.

Además de definir métodos dentro de las clases, es común crear métodos estáticos. Los métodos estáticos son aquellos que pueden ser invocados sin necesidad de instanciar una clase. Son útiles para funciones utilitarias o operaciones que no dependen del estado de un objeto en particular.

La gestión adecuada de los métodos es esencial para mantener el orden y la claridad en nuestros proyectos de programación. Al seguir las mejores prácticas en la creación y uso de métodos, podemos construir sistemas más robustos y fáciles de mantener a lo largo del tiempo.

En resumen, los métodos son el corazón de cualquier programa orientado a objetos. Son herramientas poderosas que nos permiten dar forma a nuestros objetos y realizar tareas específicas. Al aprender a crear y utilizar métodos eficazmente, podemos desarrollar programas más complejos y funcionales, facilitando así la tarea del programador y mejorando la calidad de nuestro trabajo.

### repaso de los metodos

```python
class Gato():
  def __init__(self):
    self.color = ""     # Esto es una propiedad
  
  def maulla(self):     # Esto es un método (es una acción)
    return "miau"
    
    
gato1 = Gato()
gato1.color = "naranja"   # Aquí seteamos una propiedad
print(gato1.maulla())     # Aquí llamamos a un método
```

### metodo set

```python
class Gato():
  def __init__(self):
    self.color = ""     # Esto es una propiedad
  
  def maulla(self):     # Esto es un método (es una acción)
    return "miau"
    
  def setColor(self,nuevocolor):   # Defino un setter - el método es el responsable de cambiar la
    # Por ejemplo aquí podría validar si el color es un color válido para un gato
    self.color = nuevocolor         # Y cambio la propiedad
    
    
gato1 = Gato()
gato1.color = "naranja"   # Aquí seteamos una propiedad directamente (no es buena práctica)

gato1.setColor("naranja") # Esto es una práctica mucho mejor
```

### metodo getter

```python
class Gato():
  def __init__(self):
    self.color = ""     # Esto es una propiedad
  
  def maulla(self):     # Esto es un método (es una acción)
    return "miau"
    
  def setColor(self,nuevocolor):   # Defino un setter - el método es el responsable de cambiar la
    # Por ejemplo aquí podría validar si el color es un color válido para un gato
    self.color = nuevocolor         # Y cambio la propiedad
  
  def getColor(self):
    # Una vez más, aquí podría poner validaciones si lo quisiera
    return self.color
    
    
gato1 = Gato()
gato1.color = "naranja"   # Aquí seteamos una propiedad directamente (no es buena práctica)

gato1.setColor("naranja") # Esto es una práctica mucho mejor

print(gato1.color)      # Acceso directo, se puede pero no se recomienda

print(gato1.getColor()) # Acceso mediante método, se recomienda
```

### defino propiedad privada

```python
class Gato():
  def __init__(self):
    self.__color = "naranja"     # Esto es una propiedad privada (contrapuesta a pública)
    
gato1 = Gato()

print(gato1.__color)
  
```

### Clase cuenta bancaria

```python
class CuentaBancaria():
  def __init__(self):
    self.saldo = 0
    self.cliente = ""
    
```

### convertir en privadas

```python
class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    self.__saldo = nuevosaldo
    
cuentecliente1 = CuentaBancaria()
cuentecliente1.setSaldo(10000000000)


    
```

### get saldo

```python
class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    self.__saldo = nuevosaldo
  def getSaldo(self):
    return self.__saldo
    
cuentecliente1 = CuentaBancaria()
cuentecliente1.setSaldo(10000000000)
print(cuentecliente1.getSaldo())


    
```

### validacion

```python
limitediferenciasaldo = 1000

class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    # Establezco una condicion de que valida si el saldo nuevo es mayor de 1000 euros
    if nuevosaldo > self.__saldo + 1000:
      # Si salta la alarma, avisa y NO cambia el saldo
      print("Voy a avisar a la entidad de un ingreso muy grande")
    else
      # Si pasa el filtro, solo entonces se cambia el saldo
      self.__saldo = nuevosaldo
      
  def getSaldo(self):
    return self.__saldo
    
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(10000000000)
print(cuentacliente1.getSaldo())


    
```

### variable global

```python
limitediferenciasaldo = 1000

class CuentaBancaria():
  def __init__(self):
    self.__saldo = 0
    self.__cliente = ""
    
  # Defino setters y getters para el saldo
  def setSaldo(self,nuevosaldo):
    # Establezco una condicion de que valida si el saldo nuevo es mayor de 1000 euros
    if nuevosaldo > self.__saldo + limitediferenciasaldo:
      # Si salta la alarma, avisa y NO cambia el saldo
      print("Voy a avisar a la entidad de un ingreso muy grande")
    else
      # Si pasa el filtro, solo entonces se cambia el saldo
      self.__saldo = nuevosaldo
      
  def getSaldo(self):
    return self.__saldo
    
cuentacliente1 = CuentaBancaria()
cuentacliente1.setSaldo(10000000000)
print(cuentacliente1.getSaldo())


    
```

### creo setters y getters

```python
class Cliente():
  def __init__():
    self.nombrecompleto = ""
    self.email = ""
  
    


    
```

### ejemplo practico

```python
class Cliente():
  def __init__():
    self.nombrecompleto = ""
    self.email = ""
  
    


    
```

### creo setters y getters

```python
class Cliente():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE


    

    


    
```

### pequeño programa

```python
class Cliente():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE

print("Gestor de clientes v0.1 Jose Vicente Carratala")
print("Selecciona una opción:")
print("1.-Insertar un nuevo cliente")
print("2.-Obtener listado de clientes")
opcion = int(input("Indica tu opción (1,2): "))

if opcion == 1:
  print("Voy a insertar un cliente")
elif opcion == 2:
  print("Saco el listado de clientes")
  
  

    

    


    
```

### creo una lista de clientes

```python
class Cliente():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE

clientes = []             ############## Meto una lista de clientes vacia

print("Gestor de clientes v0.1 Jose Vicente Carratala")
print("Selecciona una opción:")
print("1.-Insertar un nuevo cliente")
print("2.-Obtener listado de clientes")
opcion = int(input("Indica tu opción (1,2): "))

if opcion == 1:     # Los SETTERS se usan en las operaciones de creación de nuevos elementos
  print("Voy a insertar un cliente")
  nuevocliente = Cliente()
  nombrecliente = input("Introduce el nombre del cliente: ")  # Tomo el dato
  nuevocliente.setNombreCompleto(nombrecliente) # Uso el metodo set para meter el dato en el objeto
  emailcliente = input("Introduce el email del cliente: ")  # Tomo el dato
  nuevocliente.setEmail(emailcliente) # Uso el metodo set para meter el dato en el objeto
elif opcion == 2:
  print("Saco el listado de clientes")
  

  
  

    

    


    
```

### getters

```python
class Cliente():
  # Este es el método constructor
  def __init__(self):
    self.nombrecompleto = ""
    self.email = ""
  # Estos son los setters y los getters
  def setNombreCompleto(self,nuevonombre):
    self.nombrecompleto = nuevonombre
  def setEmail(self,nuevoemail):
    self.email = nuevoemail
  def getNombreCompleto(self):
    return self.nombrecompleto
  def getEmail(self):
    return self.email
    
# CRUD - Create, Read, Update, Delete
# CRUD SQL - INSERT, SELECT, UPDATE, DELETE

clientes = []             ############## Meto una lista de clientes vacia

print("Gestor de clientes v0.1 Jose Vicente Carratala")
while True:
  print("Selecciona una opción:")
  print("1.-Insertar un nuevo cliente")
  print("2.-Obtener listado de clientes")
  opcion = int(input("Indica tu opción (1,2): "))

  if opcion == 1:     # Los SETTERS se usan en las operaciones de creación de nuevos elementos
    print("Voy a insertar un cliente")
    nuevocliente = Cliente()
    nombrecliente = input("Introduce el nombre del cliente: ")  # Tomo el dato
    nuevocliente.setNombreCompleto(nombrecliente) # Uso el metodo set para meter el dato en el objeto
    emailcliente = input("Introduce el email del cliente: ")  # Tomo el dato
    nuevocliente.setEmail(emailcliente) # Uso el metodo set para meter el dato en el objeto
    clientes.append(nuevocliente) # Y por ultimo añado el cliente a la lista de clientes
  elif opcion == 2:   # Los GETTERS se usan en las operaciones de listado
    print("Saco el listado de clientes")
    for cliente in clientes:
      print("-------------------------")
      print("Nombre: ",cliente.getNombreCompleto())
      print("email: ",cliente.getEmail())
      print("-------------------------")


  
  

  
  

    

    


    
```

<a id="creacion-de-constructores"></a>
## Creación de constructores

En el vasto y complejo mundo de la programación, los constructores son como las plantillas que nos permiten dar forma a nuestros objetos. Son métodos especiales dentro de una clase que se ejecutan automáticamente cuando un objeto es creado. Su principal objetivo es inicializar los atributos del objeto con valores específicos, preparándolo para su uso inmediato.

La creación de constructores es una práctica fundamental en la programación orientada a objetos (POO), ya que nos permite controlar cómo se instancian nuestros objetos y garantizar que estén en un estado válido desde el principio. Cada clase puede tener uno o más constructores, lo que proporciona flexibilidad para adaptarse a diferentes situaciones.

Los constructores son especialmente útiles cuando necesitamos asegurar que ciertos atributos no puedan estar nulos o vacíos al momento de la creación del objeto. Algunas clases pueden requerir que se especifiquen ciertos parámetros durante la instancia, lo que los constructores manejan con facilidad.

Además de los constructores predeterminados (que no requieren ningún parámetro), podemos definir constructores parametrizados, que permiten pasar valores específicos a los atributos del objeto al momento de su creación. Esta flexibilidad es crucial para crear objetos en estados deseados y evitar errores posteriores.

La creación de constructores también facilita la documentación y la comprensión del código. Al ver un constructor, podemos entender qué valores se esperan para inicializar los atributos del objeto, lo que nos ayuda a mantener el código limpio y fácil de mantener.

En resumen, la creación de constructores es una práctica esencial en la programación orientada a objetos. Nos permite controlar cómo se instancian nuestros objetos, garantizar su estado inicial válido y facilitar la documentación del código. A través de este proceso, podemos asegurar que nuestros programas sean más robustos, fáciles de mantener y menos propensos a errores.

### repaso gato

```python
class Gato():
  def __init__(self):    # El constructor se ejecuta sí o sí
    self.edad = 0
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato()
print(gato1.edad)

print(gato1.maulla())
    
```

### a un construtor se le pueden pasar parametros

```python
class Gato():
  def __init__(self):    # El constructor se ejecuta sí o sí
    self.edad = 0
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato()
print(gato1.edad)
gato1.edad = 5
print(gato1.edad)

print(gato1.maulla())
    
```

### constructor con parametros

```python
class Gato():
  def __init__(self,edad):    # El constructor se ejecuta sí o sí
    self.edad = edad
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato(5)

    
```

### mas parametros

```python
class Gato():
  def __init__(self,edad,nombre):    # El constructor se ejecuta sí o sí
    self.edad = edad
    self.nombre = nombre
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato(5,"micifu")

    
```

### tercera propiedad

```python
class Gato():
  def __init__(self,edad,nombre,raza):    # El constructor se ejecuta sí o sí
    self.edad = edad
    self.nombre = nombre
    self.raza = raza
    
  def maulla(self):     # El resto de métodos sólo se ejecutan si los llamas
    return "El gato está maullando"
    
    
gato1 = Gato(5,"micifu","mainecoon")

    
```

### ejemplo con cliente

```python
class Cliente():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
    
nombre = input("Introduce el nombre del cliente: ")
apellidos = input("Introduce los apellidos del cliente: ")
email = input("Introduce el email del cliente: ")
direccion = input("Introduce la dirección del cliente: ")

cliente1 = Cliente(nombre,apellidos,email,direccion)
print(cliente1)




    
```

### listado de clientes

```python
class Cliente():
  def __init__(self,nombre,apellidos,email,direccion):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
    self.direccion = direccion
 
clientes = []
while True:  
 
  nombre = input("Introduce el nombre del cliente: ")
  apellidos = input("Introduce los apellidos del cliente: ")
  email = input("Introduce el email del cliente: ")
  direccion = input("Introduce la dirección del cliente: ")

  clientes.append(Cliente(nombre,apellidos,email,direccion))





    
```

<a id="utilizacion-de-clases-y-objetos"></a>
## Utilización de clases y objetos

En el vasto terreno de la programación, las clases y los objetos son como las piezas fundamentales que conforman una estructura sólida. Comenzamos por entender qué son estas entidades esenciales antes de explorar cómo interactúan entre sí.

Las clases en programación son plantillas o modelos que definen las características comunes de un grupo de objetos. Son como moldeadores de cerámica, donde cada molde puede producir múltiples piezas idénticas pero con distintos atributos individuales. Cada clase tiene propiedades (variables) y métodos (funciones) que describen su comportamiento.

Los objetos, por otro lado, son instancias específicas de una clase. Al crear un objeto a partir de una clase, estamos creando una entidad concretas que posee las características definidas en la plantilla. Es como tomar un molde y hacerle una pieza de cerámica; cada pieza es única pero sigue el diseño del molde.

La relación entre clases y objetos es fundamental para la programación orientada a objetos (POO). Las clases actúan como contenedores que encapsulan datos y comportamientos, mientras que los objetos son las instancias concretas de estas clases. Esta distinción permite una organización jerárquica y modular del código, facilitando su mantenimiento y escalabilidad.

La creación de clases y objetos es un proceso iterativo. Primero se define la clase con sus propiedades y métodos, luego se crean los objetos basándose en esta definición. Cada objeto puede tener valores diferentes para las mismas propiedades, lo que permite representar múltiples entidades similares pero distintas.

La utilización de clases y objetos también facilita el reutilizar código. Una vez creada una clase, se pueden crear tantos objetos como sea necesario, cada uno con sus propias características específicas. Esto promueve la eficiencia y la consistencia en el desarrollo del software.

Además, las clases y los objetos permiten la abstracción, que es el proceso de simplificar complejidades reales del mundo real en conceptos más simples y manejables para el programa. Al definir una clase, se ocultan los detalles innecesarios y solo se expone lo necesario para su uso.

La programación orientada a objetos también fomenta la herencia, que es un mecanismo que permite crear nuevas clases basadas en clases existentes. Esta característica facilita el reutilizar código y organizar jerárquicamente las entidades del programa.

En resumen, las clases y los objetos son pilares fundamentales de la programación orientada a objetos. Permiten una organización eficiente, la reutilización de código y la abstracción, lo que resulta en software más robusto y fácil de mantener. Comprender cómo crear y utilizar clases y objetos es crucial para dominar el desarrollo de aplicaciones complejas y escalables.

### Mi propia clase

```python
class Matematicas():
  def __init__(self):
    self.PI = 3.14159265359
    
  def redondeo(self,numero):
    entero = int(numero)
    decimal = numero - entero
    if decimal < 0.5:
      redondeo = 0
    else:
      redondeo = 1
    return entero + redondeo
    
Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
```

### redondeos alza y baja

```python
class Matematicas():
  def __init__(self):
    self.PI = 3.14159265359
    
  def redondeo(self,numero):
    entero = int(numero)
    decimal = numero - entero
    if decimal < 0.5:
      redondeo = 0
    else:
      redondeo = 1
    return entero + redondeo
    
  def techo(self,numero):
    return int(numero)+1
  def suelo(self,numero):
    return int(numero)
    
Mate = Matematicas()
print(Mate.redondeo(4.7))
print(Mate.redondeo(4.2))
print(Mate.techo(4.7))
print(Mate.suelo(4.7))
```

### ahora uso la libreria estandar

```python
import math
    
print(round(4.7))
print(round(4.2))
print(math.ceil(4.7))
print(math.floor(4.7))
```

<a id="utilizacion-de-clases-heredadas"></a>
## Utilización de clases heredadas

En la etapa de desarrollo de clases, el concepto de herencia es un pilar fundamental que nos permite crear jerarquías de clases relacionadas. Esta técnica permite a una clase derivada (también conocida como subclase) heredar atributos y métodos de una clase base (superclase), lo que facilita la reutilización del código y la organización lógica.

La herencia nos permite definir relaciones "es un" entre clases. Por ejemplo, si tenemos una clase `Animal` con propiedades como `nombre` y `edad`, podemos crear subclases como `Perro` y `Gato` que hereden de `Animal`. De esta manera, las subclases pueden agregar o modificar atributos y métodos específicos, mientras mantienen los atributos y métodos comunes definidos en la superclase.

La utilización de clases heredadas no solo simplifica el código al evitar la duplicidad, sino que también promueve la cohesión del diseño. Cada subclase puede tener su propio comportamiento específico, pero compartirá funcionalidades básicas con otras clases relacionadas. Esta organización lógica facilita la comprensión y mantenimiento del código.

Además de la reutilización del código, la herencia también permite una mejor escalabilidad. Al crear nuevas clases que heredan de una superclase existente, podemos aprovechar el trabajo ya realizado en la superclase sin necesidad de reinventar la rueda. Esto es especialmente útil cuando se necesita agregar funcionalidades adicionales a un conjunto de objetos similares.

La herencia también facilita la gestión de cambios en el código. Si una funcionalidad común debe modificarse, solo es necesario hacerlo en la superclase, y esta modificación se reflejará automáticamente en todas las subclases que la hereden. Esto reduce significativamente el riesgo de errores y asegura un mantenimiento más eficiente.

En resumen, la utilización de clases heredadas es una práctica esencial en la programación orientada a objetos. Permite crear jerarquías lógicas, reutilizar código, mejorar la escalabilidad y facilitar la gestión de cambios. Esta técnica es fundamental para el diseño de sistemas complejos y eficientes, permitiendo una organización coherente y una estructura clara del código.

### gatos y perros

```python
class Gato():
  def __init__(self):
    self.edad = 0
    self.nombre = ""
    self.raza = ""
    
class Perro():
  def __init__(self):
    self.edad = 0
    self.nombre = ""
    self.raza = ""
```

### clase madre animal

```python
class Animal():
  def __init__(self):
    self.edad = 0
    self.nombre = ""
    self.raza = ""

class Gato(Animal):
  def __init__(self):
    super().__init__()    # Me traigo todo lo que tenga la clase superior
    
class Perro(Animal):      # Me traigo todo lo que tenga la clase superior
  def __init__(self):
    super().__init__()

gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)
    
```

### clase Roca

```python
class Animal():
  def __init__(self):
    self.edad = 0
    self.nombre = ""
    self.raza = ""

class Gato(Animal):
  def __init__(self):
    super().__init__()    # Me traigo todo lo que tenga la clase superior
    self.x = 0
    self.y = 0
    self.z = 0
    
class Perro(Animal):      
  def __init__(self):
    super().__init__()  # Me traigo todo lo que tenga la clase superior
    self.x = 0
    self.y = 0
    self.z = 0

class Roca():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0

gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)
    
```

### herencia o multinivel

```python
class Entidad():
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0

class Animal(Entidad):
  def __init__(self):
    super().__init__()
    self.edad = 0
    self.nombre = ""
    self.raza = ""

class Gato(Animal):
  def __init__(self):
    super().__init__()    # Me traigo todo lo que tenga la clase superior

    
class Perro(Animal):      
  def __init__(self):
    super().__init__()  # Me traigo todo lo que tenga la clase superior
    

class Roca(Entidad):
  def __init__(self):
    super().__init__()


gato1 = Gato()
print(gato1.edad)

perro1 = Perro()
print(perro1.edad)
    
```

<a id="ejercicio-de-final-de-unidad-3"></a>
## Ejercicio de final de unidad

### Holamundo

```python
print("Hola mundo desde Python")
```

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```


<a id="lectura-y-escritura-de-informacion"></a>
# Lectura y escritura de información

<a id="flujos-tipos-bytes-y-caracteres-clases-relacionadas"></a>
## Flujos. Tipos bytes y caracteres. Clases relacionadas

En el vasto mundo de la programación, los flujos de datos desempeñan un papel fundamental, ya que son la vía por la cual se transfieren información entre diferentes partes del programa. Los flujos pueden ser de dos tipos principales: bytes y caracteres, cada uno con sus propias características y clases relacionadas.

Los flujos de bytes representan los datos en su forma más básica, como una secuencia de ceros y unos. En la programación, estos flujos se manejan a través de las clases `InputStream` y `OutputStream`, que proporcionan métodos para leer y escribir datos en formatos binarios. Estas clases son fundamentales para operaciones como la lectura de archivos binarios o la transmisión de datos a través de sockets.

Por otro lado, los flujos de caracteres manejan los datos en su forma más legible, como texto. En este contexto, las clases `Reader` y `Writer` son esenciales. Estas clases proporcionan métodos para leer y escribir cadenas de texto, convirtiéndolas automáticamente entre bytes y caracteres según la codificación especificada. El uso de flujos de caracteres facilita el manejo de información textual en programas, ya que no requiere preocuparse por los detalles del formato binario.

La relación entre estos flujos es estrecha, ya que ambos pueden ser adaptados para funcionar juntos. Por ejemplo, la clase `BufferedReader` puede leer datos de un flujo de caracteres y proporcionar una interfaz más eficiente para la lectura de texto. De manera similar, la clase `BufferedWriter` puede escribir datos a un flujo de caracteres, optimizando el rendimiento al reducir el número de operaciones de escritura.

Además de las clases básicas, existen varias subclases que proporcionan funcionalidades adicionales y especializadas. Por ejemplo, la clase `FileInputStream` permite leer datos directamente desde un archivo en formato binario, mientras que la clase `FileWriter` permite escribir datos a un archivo en formato texto. Estas clases son útiles cuando se necesita trabajar con archivos específicos sin tener que preocuparse por los detalles del flujo de datos.

La gestión adecuada de flujos es crucial para el rendimiento y la eficiencia de cualquier programa. Al manejar correctamente los flujos, se puede evitar la pérdida de información o la corrupción de datos durante la lectura y escritura. Además, la optimización del uso de flujos puede mejorar significativamente el tiempo de ejecución de un programa.

En resumen, los flujos de bytes y caracteres son elementos esenciales en la programación, proporcionando las herramientas necesarias para manejar información textual y binaria de manera eficiente. A través de clases como `InputStream`, `OutputStream`, `Reader` y `Writer`, se puede realizar una amplia gama de operaciones de entrada y salida, desde la lectura de archivos hasta la transmisión de datos a través de redes.

La comprensión y el uso adecuado de flujos son fundamentales para cualquier programador que quiera crear aplicaciones robustas y eficientes. Al dominar estas técnicas, se puede asegurar que los programas funcionen correctamente y sean capaces de manejar grandes volúmenes de datos con eficiencia.

### escribir texto a archivo

```python
archivo = open("clientes.txt",'w') # W = Write

archivo.write("Esto es una prueba")

archivo.close()
```

### ahora leemos

```python
archivo = open("clientes.txt",'r') # R = Read

contenido = archivo.readline()
# También existe archivo.readlines()

print(contenido)

archivo.close()
```

### creador agenda

```python
while True:
  print("Dime lo que quieres hacer: ")
  print("1.-Introduce un nuevo contacto")
  print("2.-Leer todos los contactos")
  opcion = int(input("Escoge tu opción: "))
  if opcion == 1:
    nombre = input("Introduce el nombre de la persona: ")
    email = input("Introduce el email de la persona: ")
    archivo = open("agenda.txt",'a') # A = añadir
    archivo.write(nombre+","+email+"\n")
    archivo.close()
  elif opcion == 2:
    archivo = open("agenda.txt",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()
```

### agenda

```
Jorge,jorge@jocarsa.com
```

### clientes

```
Esto es una prueba
```

<a id="ficheros-de-datos-registros"></a>
## Ficheros de datos. Registros

En el vasto mundo de la programación, los ficheros de datos desempeñan un papel fundamental como almacenadores de información persistente. Al explorar esta subunidad didáctica, nos sumergimos en la comprensión del manejo de estos archivos, una habilidad esencial para cualquier desarrollador.

El primer paso hacia el dominio de los ficheros es entender su estructura básica: un fichero puede ser visto como una colección ordenada de registros. Cada registro, a su vez, está formado por campos individuales que contienen datos específicos. Esta organización permite una representación eficiente y accesible de la información.

La lectura y escritura de ficheros es un proceso bidireccional que implica el acceso y modificación de estos registros. La lectura nos permite recuperar los datos almacenados, mientras que la escritura nos brinda la capacidad de actualizar o agregar nueva información. Este flujo continuo entre el programa y el fichero es crucial para mantener la integridad y coherencia de los datos.

La manipulación de ficheros implica también la gestión de flujos de datos. Los flujos son canales que permiten la transmisión de información desde el programa hacia el fichero o viceversa. La comprensión de estos flujos es fundamental para optimizar el rendimiento del proceso de lectura y escritura.

Además, los ficheros pueden almacenar diferentes tipos de datos: bytes, caracteres, registros completos, entre otros. Cada tipo requiere un enfoque específico en la manipulación, desde la codificación hasta la deserialización. Esta diversidad añade complejidad pero también riqueza al manejo de información.

La seguridad es otro aspecto crucial a considerar cuando se trabaja con ficheros. La protección contra accesos no autorizados y la prevención de corrupciones son tareas que deben ser abordadas desde el diseño hasta la implementación del código. Herramientas y técnicas específicas pueden ayudar en esta tarea, pero es fundamental mantener un enfoque proactivo.

La eficiencia en la lectura y escritura de ficheros también es un objetivo importante. Algoritmos optimizados y estructuras de datos adecuadas pueden reducir significativamente el tiempo y recursos necesarios para manipular grandes volúmenes de información. Esta optimización no solo mejora el rendimiento del programa, sino que también lo hace más escalable.

En la práctica, los ficheros son utilizados en una amplia gama de aplicaciones. Desde bases de datos hasta sistemas operativos y aplicaciones web, su manejo es un componente fundamental. Comprender cómo trabajar con ellos nos proporciona las herramientas necesarias para desarrollar software robusto y eficiente.

La lectura y escritura de ficheros también implica la gestión de excepciones. Situaciones como errores de acceso o problemas de formato pueden surgir durante el proceso, y es crucial tener en cuenta estas posibilidades para mantener la estabilidad del programa.

Finalmente, la documentación es un aspecto no menos importante que el código mismo. Comentar adecuadamente las operaciones realizadas sobre los ficheros nos ayuda a entender su funcionamiento y facilita futuras modificaciones o mantenimiento.

En resumen, la lectura y escritura de ficheros es una habilidad multifacética y fundamental en la programación. Desde la comprensión de sus estructuras hasta la implementación de soluciones eficientes y seguras, cada paso requiere un enfoque cuidadoso y una comprensión profunda del contexto en el que se está trabajando.

### leer archivo

```python
archivo = open("blog.txt",'r')

lineas = archivo.readlines()

for linea in lineas:
  print(linea)
```

### leer json

```python
import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

print(contenido)
```

### leemos linea a linea

```python
import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
  print(linea)
```

### ahora accedemos a las parejas

```python
import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
  print(linea['titulo'])
  print(linea['fecha'])
  print(linea['autor'])
  print(linea['contenido'])
```

### una pequeña decoracion

```python
import json

archivo = open("blog.json",'r')

contenido = json.load(archivo)

for linea in contenido:
  print("####### ARTICULO ########")
  print(linea['titulo'])
  print(linea['fecha'])
  print(linea['autor'])
  print(linea['contenido'])
  print("#########################")
  print("")
```

### blog

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      
    </style>
  </head>
  <body>
    
  </body>
</html>
```

### secciones

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      
    </style>
  </head>
  <body>
    <header><h1>JOCARSAblog</h1></header>
    <main>
    
    </main>
    <footer>(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
```

### articulo

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      
    </style>
  </head>
  <body>
    <header><h1>JOCARSAblog</h1></header>
    <main>
      <article>
        <h3>Titulo del articulo</h3>
        <time>2025-10-16</time>
        <p>Jose Vicente Carratala</p>
        <p>Este es el contenido de un artículo ficticio</p>
      </article>
    </main>
    <footer>(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
```

### estilos minimos

```html
<!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>JOCARSAblog</h1></header>
    <main>
      <article>
        <h3>Titulo del articulo</h3>
        <time>2025-10-16</time>
        <p>Jose Vicente Carratala</p>
        <p>Este es el contenido de un artículo ficticio</p>
      </article>
    </main>
    <footer>(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
```

### Instalar servidor

```markdown
-Instalar un servidor web en entorno de desarrollo
(se entiende vuestro propio ordenador)

-Windows:
Se recomienda instalar el paquete XAMPP
https://www.apachefriends.org/es/index.html

Una vez instalado, la carpeta de publicación es c:/xampp/htdocs

-Linux:
Se instala Apache con el comando
sudo apt install apache2

Una vez instalado, la carpeta de publicación es: /var/www/html
```

### arranco flask

```python
# Abre una terminal e instala flask:
# pip install flask
# Flask es un microservidorweb que nos permite generar HTML desde Python

from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return "Esto es HTML desde Flask"
  
# Ahora arranco el servidor
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

### frankenstein

```python
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return '''
    <!doctype html>
<html lang="es">
  <head>
    <title>JOCARSAblog</title>
    <meta charset="utf-8">
    <style>
      body{background:steelblue;color:steelblue;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:600px;}
      header,footer{text-align:center;}
      main{color:black;}
    </style>
  </head>
  <body>
    <header><h1>JOCARSAblog</h1></header>
    <main>
      <article>
        <h3>Titulo del articulo</h3>
        <time>2025-10-16</time>
        <p>Jose Vicente Carratala</p>
        <p>Este es el contenido de un artículo ficticio</p>
      </article>
    </main>
    <footer>(c)2025 Jose Vicente Carratalá</footer>
  </body>
</html>
  '''
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

### blog

```json
[
  {
    "titulo":"Primer artículo",
    "fecha":"2025-10-16",
    "autor":"Jose Vicente Carratala",
    "contenido":"Este es el contenido del primer artículo"
  },
  {
    "titulo":"Segundo artículo",
    "fecha":"2025-10-17",
    "autor":"Jose Vicente Carratala",
    "contenido":"Este es el contenido del segundo artículo"
  },
  {
    "titulo":"Tercer artículo",
    "fecha":"2025-10-16",
    "autor":"Jose Vicente Carratala",
    "contenido":"Este es el contenido del tercer artículo"
  },
  {
    "titulo":"Cuarto artículo",
    "fecha":"2025-10-16",
    "autor":"Jose Vicente Carratala",
    "contenido":"Este es el contenido del cuarto artículo"
  }
]
```

### blog

```
Este es un primer articulo de blog
Este es un segundo artículo de blog
Y este es el tercero
Y por qué no, podemos tener un cuarto artículo
```

<a id="apertura-y-cierre-de-ficheros-modos-de-acceso-escritura-y-lectura-de-informacion-en-ficheros"></a>
## Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros

En el vasto mundo de la programación, la lectura y escritura de información son fundamentales para cualquier aplicación informática. En esta subunidad didáctica, nos adentramos en los aspectos cruciales de cómo interactuar con archivos en un programa, abordando desde la apertura y cierre de ficheros hasta las técnicas avanzadas de acceso y manipulación de datos.

La apertura y el cierre de ficheros son operaciones esenciales que permiten a nuestros programas acceder y modificar información persistente. Cada archivo se abre en un modo específico, determinado por la naturaleza de los datos que se quieren leer o escribir. Los modos más comunes incluyen lectura (`r`), escritura (`w`), anexión (`a`) y lectura-escritura (`rw`). Cada uno de estos modos tiene sus propias características y restricciones, lo que es crucial entender para evitar errores en la manipulación de archivos.

La apertura de un archivo implica establecer una conexión entre el programa y el dispositivo de almacenamiento. Este proceso puede implicar la asignación de recursos como memoria y espacio en disco, dependiendo del tamaño del archivo y las necesidades del programa. Es importante recordar que cada vez que se abre un archivo, debe cerrarse adecuadamente para liberar estos recursos y garantizar la integridad del sistema.

La escritura de información en ficheros es otro aspecto fundamental de la programación. Los programas pueden escribir datos en archivos de texto o binarios, dependiendo de las necesidades específicas del proyecto. La escritura puede ser sincrónica (el programa espera a que el dato sea escrito antes de continuar) o asíncrona (el programa continúa ejecutándose mientras se realiza la escritura). Cada método tiene sus ventajas y desventajas, y es importante elegir el más adecuado según las circunstancias.

Además de la apertura y cierre de ficheros, también es crucial manejar los errores que pueden surgir durante estas operaciones. Los archivos pueden no existir, puede faltar espacio en disco o puede haber problemas de permisos. Es por eso que los programas suelen implementar mecanismos para detectar y gestionar estos errores, asegurando la continuidad del proceso.

La lectura de información desde ficheros es otro aspecto fundamental de la programación. Los archivos pueden contener datos estructurados o no estructurados, y el programa debe ser capaz de leerlos correctamente. La lectura puede ser realizada línea por línea o en bloques más grandes, dependiendo del tamaño del archivo y las necesidades del programa.

La manipulación de información en ficheros es un aspecto avanzado que permite a los programas realizar operaciones complejas sobre datos persistentes. Esto puede incluir la búsqueda y reemplazo de texto, el ordenamiento de registros o la creación de copias de seguridad. La manipulación de ficheros requiere una comprensión profunda del formato y estructura de los datos almacenados.

La importancia de la lectura y escritura de información en programación no puede subestimarse. Estas operaciones son esenciales para el funcionamiento de aplicaciones que interactúan con el mundo exterior, desde sistemas empresariales hasta aplicaciones web y móviles. La capacidad de leer y escribir datos de manera eficiente y segura es un requisito fundamental para cualquier programador.

En conclusión, la lectura y escritura de información son operaciones fundamentales en la programación que permiten a los programas interactuar con el mundo exterior. A través de la apertura y cierre de ficheros, la escritura de datos y la manipulación avanzada de información, los programas pueden realizar tareas complejas y almacenar resultados persistentes. Comprender estos aspectos es crucial para cualquier programador que quiera crear aplicaciones robustas y eficientes.

### escribir

```python
archivo = open("basededatos.txt","w")
archivo.write("esto es otro contenido")
archivo.close()
```

### apendizar

```python
archivo = open("basededatos.txt","a")
archivo.write("esto es un contenido")
archivo.close()
```

### añadir salto de linea

```python
archivo = open("basededatos.txt","a")
archivo.write("esto es un contenido\n")
archivo.close()
```

### leer una linea

```python
archivo = open("basededatos.txt","r")
linea = archivo.readline()
print(linea)
archivo.close()
```

### leer varias lineas

```python
archivo = open("basededatos.txt","r")
lineas = archivo.readlines()
print(lineas)
archivo.close()
```

### recorrer la lista

```python
archivo = open("basededatos.txt","r")
lineas = archivo.readlines()
for linea in lineas:
  print(linea)
archivo.close()
```

### pickle escribir

```python
#pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin","wb")
cadena = "Jose Vicente"

pickle.dump(cadena,archivo)

archivo.close()
```

### leer pickle

```python
#pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin","rb")

cadena = pickle.load(archivo)
print(cadena)

archivo.close()
```

### crear cliente

```python
class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

clientes = []

clientes.append(Cliente("Jose Vicente","info@jocarsa.com"))
clientes.append(Cliente("Juan","juan@jocarsa.com"))

print(clientes)
```

### guardo con pickle a binario

```python
import pickle

class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

clientes = []

clientes.append(Cliente("Jose Vicente","info@jocarsa.com"))
clientes.append(Cliente("Juan","juan@jocarsa.com"))

archivo = open("clientes.bin","wb")
pickle.dump(clientes,archivo)
archivo.close()
```

### recupero los datos

```python
import pickle

class Cliente():
  def __init__(self,nuevonombre,nuevoemail):
    self.nombre = nuevonombre
    self.email = nuevoemail

archivo = open("clientes.bin","rb")
clientes = pickle.load(archivo)
archivo.close()

print(clientes)
```

### basededatos

```
esto es un contenido
esto es un contenido
esto es un contenido
```

<a id="utilizacion-de-los-sistemas-de-ficheros"></a>
## Utilización de los sistemas de ficheros.

### listar contenido de carpeta

```python
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
  print(elemento)
```

### atributos

```python
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
  ruta = os.path.join(carpeta, elemento)
  print(ruta)
  print(os.path.getsize(ruta))
  print(os.path.getmtime(ruta))
```

### formateo el resultado

```python
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

for elemento in elementos:
  ruta = os.path.join(carpeta, elemento)
  print(ruta)
  print(os.path.getsize(ruta)/(1024*1024),"MB")
  print(os.path.getmtime(ruta))
```

### suma del tamaño

```python
import os

carpeta = input("Indica una carpeta: ")

elementos = os.listdir(carpeta)

suma = 0

for elemento in elementos:
  ruta = os.path.join(carpeta, elemento)
  suma += os.path.getsize(ruta)

print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")
```

### recorrer

```python
import os

carpeta = input("Indica una carpeta: ")

for directorio,carpetas,archivo in os.walk(carpeta):
  print(directorio)
  print(carpetas)
  print(archivo)
```

### tamaño recursivo

```python
import os

carpeta = input("Indica una carpeta: ")

suma = 0

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            suma += os.path.getsize(ruta)
        except:
            pass  # Evita errores si un archivo no se puede leer
  
print("La carpeta ocupa:")
print(suma/(1024*1024),"MB")
```

### condicion

```python
import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        try:
            if os.path.getsize(ruta) > grande:
              print(ruta,os.path.getsize(ruta)/(1024*1024),"MB")
        except:
            pass  
    
```

### escribir en archivo el contenido de la carpeta

```python
import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

mapa = open("mapa.txt",'a') # Vaciamos los contenidos anteriores

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta+"\n")
        
mapa.close()
         
    
```

### sobreescribir cada vez

```python
import os

carpeta = input("Indica una carpeta: ")
grande = 1024*1024*1024 # 1 giga

mapa = open("mapa.txt",'w') # Vaciamos los contenidos anteriores

for directorio, carpetas, archivos in os.walk(carpeta):
    for archivo in archivos:
        ruta = os.path.join(directorio, archivo)
        mapa.write(ruta+"\n")
        
mapa.close()
         
    
```

### minibuscador

```python
cadena = "Esto es una cadena de prueba"
objetivo = "manzana"

if objetivo in cadena:
  print("Efectivamente está")
else:
  print("No está")
  
```

### busca en mapa

```python
archivo = open("mapa.txt",'r') # READ

lineas = archivo.readlines()

for linea in lineas:
  if "json" in linea:
    print("###########################")
    print("Encontrado!: ",linea)   
     
```

### usuario busca

```python
archivo = open("mapa.txt",'r') # READ
busca = input("Introduce el término a buscar: ")

lineas = archivo.readlines()

for linea in lineas:
  if busca in linea:
    print("###########################")
    print("Encontrado!: ",linea)   
     
```

### mapa

```
/var/www/html/programaciondam2526/001-Resumen.md
/var/www/html/programaciondam2526/README.md
/var/www/html/programaciondam2526/000-Resumen.md
/var/www/html/programaciondam2526/peticiones.py
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/000-Resumen.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/Criterios de evaluacion.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/001-Estructuras estáticas y dinámicas/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/001-Estructuras estáticas y dinámicas/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/004-Genericidad/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/004-Genericidad/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/003-Matrices (arrays) multidimensionales/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/003-Matrices (arrays) multidimensionales/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/005-Cadenas de caracteres. Expresiones regulares/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/005-Cadenas de caracteres. Expresiones regulares/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/002-Creación de matrices (arrays)/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/002-Creación de matrices (arrays)/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/006-Colecciones Listas, Conjuntos y Diccionarios/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/006-Colecciones Listas, Conjuntos y Diccionarios/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/007-Operaciones agregadas filtrado, reducción y recolección/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/006-Aplicación de las estructuras de almacenamiento/007-Operaciones agregadas filtrado, reducción y recolección/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/001-Introduccion.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/000-Resumen.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/Criterios de evaluacion.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/013-constantes.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/014-Diferencia.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/009-Entradas.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/014-operadores aritmeticos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/019-Calculadora.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/003-salidas.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/011-Cambio de tipo de dato.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/010-Entrada y problema.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/021-Calculo de IVA.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/017-operadores booleanos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/004-variar una variable.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/001-Holamundo.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/012-literales.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/020-Calculadora.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/005-identificadores permitidos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/007-Explicacion del codigo.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/008-Tipos de datos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/018-Ejercicio1-Calculadora de impuestos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/002-variables.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/006-comentarios.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/016-operadores arimeticos abreviados.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/101-Ejercicios/015-operadores de comparacion.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/101-Ejercicio de final de unidad/201-Criterios de evaluación/001-actividad.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/001-Estructura y bloques fundamentales/101-Ejercicios/001-Holamundo.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/001-Estructura y bloques fundamentales/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/001-Estructura y bloques fundamentales/001-Contenidos básicos/Introduccion.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/001-Estructura y bloques fundamentales/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/003-salidas.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/004-variar una variable.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/005-identificadores permitidos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/007-Explicacion del codigo.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/002-variables.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/101-Ejercicios/006-comentarios.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/002-Variables/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/005-Constantes/101-Ejercicios/013-constantes.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/005-Constantes/101-Ejercicios/014-Diferencia.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/005-Constantes/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/005-Constantes/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/004-Literales/101-Ejercicios/012-literales.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/004-Literales/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/004-Literales/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/014-operadores aritmeticos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/019-Calculadora.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/021-Calculo de IVA.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/017-operadores booleanos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/020-Calculadora.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/018-Ejercicio1-Calculadora de impuestos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/016-operadores arimeticos abreviados.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/101-Ejercicios/015-operadores de comparacion.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/006-Operadores y expresiones/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/101-Ejercicios/009-Entradas.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/101-Ejercicios/011-Cambio de tipo de dato.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/101-Ejercicios/010-Entrada y problema.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/101-Ejercicios/008-Tipos de datos.py
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/001-Identificación de los elementos de un programa informático/003-Tipos de datos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/000-Resumen.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/Criterios de evaluacion.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/002-Establecimiento de conexiones/101-Ejercicios/001-ejercicio.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/002-Establecimiento de conexiones/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/002-Establecimiento de conexiones/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/003-Almacenamiento, recuperación, actualización y eliminación de información en bases de datos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/003-Almacenamiento, recuperación, actualización y eliminación de información en bases de datos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/001-Acceso a bases de datos. Estándares. Características/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/009-Gestión de bases de datos/001-Acceso a bases de datos. Estándares. Características/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/000-Resumen.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/Criterios de evaluacion.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/006-Sobreescritura de métodos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/006-Sobreescritura de métodos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/005-Interfaces/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/005-Interfaces/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/001-Composición de clases/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/001-Composición de clases/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/007-Constructores y herencia/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/007-Constructores y herencia/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/003-Jerarquía de clases Superclases y subclases/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/003-Jerarquía de clases Superclases y subclases/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/004-Clases y métodos abstractos y finales/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/004-Clases y métodos abstractos y finales/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/002-Herencia y polimorfismo/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/007-Utilización avanzada de clases/002-Herencia y polimorfismo/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/000-Resumen.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/Criterios de evaluacion.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/006-ahora los impares.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/004-mas anidacion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/002-estructura for.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/001-ineficiente.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/007-while.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/0005-saltos.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/009-Ejercicio propuesto patitos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/008-incremento.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/101-Ejercicios/003-anidacion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/002-Estructuras de repetición/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/003-varios if.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/004-varios if.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/006-anidacion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/002-else.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/001-Condicional.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/007-Ejercicio en clase.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/101-Ejercicios/005-particula elif.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/001-Estructuras de selección/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/101-Ejercicios/004-combinacion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/101-Ejercicios/002-el chivato salta.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/101-Ejercicios/001-chivato.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/101-Ejercicios/003-ejemplo no tan traumatico.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/005-Aserciones/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/funcionsuma.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/008-llamada a la funcion de suma.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/002-uso de la funcion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/006-las funcione retornan.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/005-varios parametros.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/004-Llamada correcta.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/007-funcion de sumar.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/003-parametros.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/001-Funciones.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/101-Ejercicios/__pycache__/funcionsuma.cpython-312.pyc
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/003-Estructuras de salto/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/010-ejercicio propuesto.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/005-cadenas.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/008-documentacion de la funcion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/003-nuevo fallo.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/002-mejora.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/006-mejoro cadenas.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/009-extraccion de funcion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/004-nuevo fallo mas.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/001-funcion de division.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/011-tres en raya.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/funciondivision.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/101-Ejercicios/007-depuracion.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/006-Prueba, depuración y documentación de la aplicación/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/101-Ejercicios/002-error.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/101-Ejercicios/003-error con try except.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/101-Ejercicios/001-tryexcept.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/101-Ejercicios/004-pseudocodigo.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/004-Control de excepciones/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/001-ejercicio for.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/004-dragones.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/004-enunciado.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/005-magos.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/002-ejercicio escalones.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/101-Ejercicios/003-subir escalones de dos en dos.py
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/003-Uso de estructuras de control/007-Ejercicio/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/000-Resumen.md
/var/www/html/programaciondam2526/002-Utilización de objetos/Criterios de evaluacion.md
/var/www/html/programaciondam2526/002-Utilización de objetos/006-Constructores/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/006-Constructores/101-Ejercicios/007-propiedades de la fecha.py
/var/www/html/programaciondam2526/002-Utilización de objetos/006-Constructores/101-Ejercicios/006-fechas en python.py
/var/www/html/programaciondam2526/002-Utilización de objetos/006-Constructores/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/006-Constructores/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/011-entrada calculo y salida.py
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/012-libreria matematica.py
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/010-propiedades.py
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/008-destruccion de objetos.py
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/101-Ejercicios/009-caballos en la cuadra.py
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/007-Destrucción de objetos y liberación de memoria/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/001-Características de los objetos/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/001-Características de los objetos/101-Ejercicios/001-objeto math.py
/var/www/html/programaciondam2526/002-Utilización de objetos/001-Características de los objetos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/001-Características de los objetos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/101-Ejercicios/003-llamada a metodos.py
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/101-Ejercicios/004-sparse is better than dense.py
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/101-Ejercicios/004-sparse.py
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/003-Utilización de métodos. Parámetros/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/002-Instanciación de objetos/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/002-Instanciación de objetos/101-Ejercicios/002-namespace.py
/var/www/html/programaciondam2526/002-Utilización de objetos/002-Instanciación de objetos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/002-Instanciación de objetos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/005-Utilización de métodos estáticos/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/005-Utilización de métodos estáticos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/005-Utilización de métodos estáticos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/002-Utilización de objetos/004-Utilización de propiedades/101-Ejercicios/000-Nota importante.md
/var/www/html/programaciondam2526/002-Utilización de objetos/004-Utilización de propiedades/101-Ejercicios/005-propiedades.py
/var/www/html/programaciondam2526/002-Utilización de objetos/004-Utilización de propiedades/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/002-Utilización de objetos/004-Utilización de propiedades/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/000-Resumen.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/Criterios de evaluacion.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/Carpeta sin título/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/004-suma del tamaño.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/007-condicion.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/005-recorrer.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/001-listar contenido de carpeta.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/006-tamaño recursivo.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/008-escribir en archivo el contenido de la carpeta.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/003-formateo el resultado.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/010-minibuscador.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/009-sobreescribir cada vez.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/mapa.txt
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/011-busca en mapa.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/004-Utilización de los sistemas de ficheros./101-Ejercicios/002-atributos.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/009-Creación de controladores de eventos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/009-Creación de controladores de eventos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/007-Interfaces gráficas/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/007-Interfaces gráficas/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/005-Creación y eliminación de ficheros y directorios/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/005-Creación y eliminación de ficheros y directorios/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/006-Entrada desde teclado. Salida a pantalla. Formatos de visualización/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/006-Entrada desde teclado. Salida a pantalla. Formatos de visualización/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/001-escribir.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/007-pickle escribir.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/010-guardo con pickle a binario.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/009-crear cliente.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/basededatos.txt
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/002-apendizar.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/011-recupero los datos.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/datos.bin
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/004-leer una linea.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/005-leer varias lineas.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/003-añadir salto de linea.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/008-leer pickle.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/clientes.bin
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/101-Ejercicios/006-recorrer la lista.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/003-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/101-Ejercicios/003-creador agenda.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/101-Ejercicios/clientes.txt
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/101-Ejercicios/001-escribir texto a archivo.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/101-Ejercicios/002-ahora leemos.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/101-Ejercicios/agenda.txt
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/001-Flujos. Tipos bytes y caracteres. Clases relacionadas/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/005-una pequeña decoracion.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/004-ahora accedemos a las parejas.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/007-secciones.html
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/003-leemos linea a linea.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/001-leer archivo.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/012-frankenstein.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/008-articulo.html
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/blog.txt
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/011-arranco flask.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/002-leer json.py
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/blog.json
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/006-blog.html
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/010-Instalar servidor.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/101-Ejercicios/009-estilos minimos.html
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/002-Ficheros de datos. Registros/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/008-Concepto de evento/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/005-Lectura y escritura de información/008-Concepto de evento/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/.git/ORIG_HEAD
/var/www/html/programaciondam2526/.git/COMMIT_EDITMSG
/var/www/html/programaciondam2526/.git/FETCH_HEAD
/var/www/html/programaciondam2526/.git/packed-refs
/var/www/html/programaciondam2526/.git/description
/var/www/html/programaciondam2526/.git/index
/var/www/html/programaciondam2526/.git/HEAD
/var/www/html/programaciondam2526/.git/config
/var/www/html/programaciondam2526/.git/logs/HEAD
/var/www/html/programaciondam2526/.git/logs/refs/remotes/origin/HEAD
/var/www/html/programaciondam2526/.git/logs/refs/remotes/origin/main
/var/www/html/programaciondam2526/.git/logs/refs/heads/main
/var/www/html/programaciondam2526/.git/refs/remotes/origin/HEAD
/var/www/html/programaciondam2526/.git/refs/remotes/origin/main
/var/www/html/programaciondam2526/.git/refs/heads/main
/var/www/html/programaciondam2526/.git/info/exclude
/var/www/html/programaciondam2526/.git/hooks/pre-push.sample
/var/www/html/programaciondam2526/.git/hooks/pre-rebase.sample
/var/www/html/programaciondam2526/.git/hooks/pre-receive.sample
/var/www/html/programaciondam2526/.git/hooks/fsmonitor-watchman.sample
/var/www/html/programaciondam2526/.git/hooks/applypatch-msg.sample
/var/www/html/programaciondam2526/.git/hooks/push-to-checkout.sample
/var/www/html/programaciondam2526/.git/hooks/pre-merge-commit.sample
/var/www/html/programaciondam2526/.git/hooks/sendemail-validate.sample
/var/www/html/programaciondam2526/.git/hooks/post-update.sample
/var/www/html/programaciondam2526/.git/hooks/update.sample
/var/www/html/programaciondam2526/.git/hooks/pre-applypatch.sample
/var/www/html/programaciondam2526/.git/hooks/commit-msg.sample
/var/www/html/programaciondam2526/.git/hooks/prepare-commit-msg.sample
/var/www/html/programaciondam2526/.git/hooks/pre-commit.sample
/var/www/html/programaciondam2526/.git/objects/2b/cb2f1852b538bc8ce87ffeeb1c1e77930cb7c4
/var/www/html/programaciondam2526/.git/objects/69/34a7c4892afae9f5212aed2c144b18f9beca0f
/var/www/html/programaciondam2526/.git/objects/69/4ed2381c1215672796b5d15d4480d4c62997f2
/var/www/html/programaciondam2526/.git/objects/ff/c0b1ff8dd1931f841e231fab1442f3e2257a81
/var/www/html/programaciondam2526/.git/objects/ff/4803bc071937e5e3d5217ca976d697dfc046b1
/var/www/html/programaciondam2526/.git/objects/ff/72907a8b1ac4d2fd537fc01ddad70af28b1990
/var/www/html/programaciondam2526/.git/objects/46/252db27ed7930199159a6548d72b127380db15
/var/www/html/programaciondam2526/.git/objects/37/bed996f76d60c3cb8ca593e901eb84baabcf82
/var/www/html/programaciondam2526/.git/objects/37/7c1aa390898102acfb1496202c1525105cd551
/var/www/html/programaciondam2526/.git/objects/52/0967073acc2dff82f3a22b92f751377a2c228a
/var/www/html/programaciondam2526/.git/objects/52/c165ab90f3ee9b2bde62d023952117e114f3d2
/var/www/html/programaciondam2526/.git/objects/52/223b0aa2a1ae702b5cdb432cf3cec6aa7a0692
/var/www/html/programaciondam2526/.git/objects/52/0583ba4dea480e8a361321a6acee35c6869f7a
/var/www/html/programaciondam2526/.git/objects/52/891b4caec2346a0439d6384eff5c58ee3e4ace
/var/www/html/programaciondam2526/.git/objects/52/e7f90036998ec15bc529fe5ea5a4b09cc0e415
/var/www/html/programaciondam2526/.git/objects/a6/4e00e82920414fe955f186e49ca3d939773a54
/var/www/html/programaciondam2526/.git/objects/a6/ba63e47bd069661a8e7d0c56a6fbd27228c78a
/var/www/html/programaciondam2526/.git/objects/70/069d71010d60916be60a51995a3fca04cc4776
/var/www/html/programaciondam2526/.git/objects/70/b47da25c70e85f9f4ec6226747706a057c3d43
/var/www/html/programaciondam2526/.git/objects/70/b60c9be33184c59742ebde759d916c308c7b96
/var/www/html/programaciondam2526/.git/objects/10/2f526da2f3ed423efe29d01e98bb330507d9ee
/var/www/html/programaciondam2526/.git/objects/63/991ba4c0b5de03d04edd5d8cb77608624c763f
/var/www/html/programaciondam2526/.git/objects/63/67129a1591fedf3ed27e4191e356d6cedf54d4
/var/www/html/programaciondam2526/.git/objects/2d/4e2c38b2a766a008eac3cb6580f5ef93f10ed2
/var/www/html/programaciondam2526/.git/objects/2d/1daa01f1c49d9b1f4083919aa8a6ab8f2d622a
/var/www/html/programaciondam2526/.git/objects/d2/93fc8960a2996eca2e8ffd6af58677d4c18681
/var/www/html/programaciondam2526/.git/objects/d2/fbc53d6da413345624ed1ab6cd34dc108b2e69
/var/www/html/programaciondam2526/.git/objects/d2/0742a97ba026afe6b49a8b5bafb14b038e7d7d
/var/www/html/programaciondam2526/.git/objects/c8/31721b5664539fc8f1eea91002defab4a854b3
/var/www/html/programaciondam2526/.git/objects/c8/a647434c3d156ac49f4d785f526ed41af88d76
/var/www/html/programaciondam2526/.git/objects/c8/300b84d709e9462874bb924b44fc3e36442174
/var/www/html/programaciondam2526/.git/objects/c8/31ea66527f6399342f70b9ed91d1592ba02f6e
/var/www/html/programaciondam2526/.git/objects/af/f248886548afda5ea34d4abf95771913b35710
/var/www/html/programaciondam2526/.git/objects/af/6353671fdd6c538df68bc9cdef98e7fd8ddb38
/var/www/html/programaciondam2526/.git/objects/f1/a40b1dd7a010554f43c208af4f53edadbac64a
/var/www/html/programaciondam2526/.git/objects/8b/0828e0c18a8cd1bfc0a4e98c6c75ae8154e4d2
/var/www/html/programaciondam2526/.git/objects/8b/137891791fe96927ad78e64b0aad7bded08bdc
/var/www/html/programaciondam2526/.git/objects/13/27e66641678d49f91e9150ca745610b87dd3a7
/var/www/html/programaciondam2526/.git/objects/13/a30f50d5938c9903c6f6de6c80b495aa3b1604
/var/www/html/programaciondam2526/.git/objects/2f/a6511f4ee6520f1a9a329a436532dd64dd81a2
/var/www/html/programaciondam2526/.git/objects/2f/dfb97eea4cd79c468a464b5d06675202790c71
/var/www/html/programaciondam2526/.git/objects/97/a5640f59796fafa4a346745a176b171581ff0f
/var/www/html/programaciondam2526/.git/objects/97/2eac3233bcbe983dcc0e03089f7eb7d0ee7614
/var/www/html/programaciondam2526/.git/objects/3f/06047a35ca80ed4ebca72c78687ea4e66c7c17
/var/www/html/programaciondam2526/.git/objects/3f/d279c859e98a94d02e990756c28acd8d0f0161
/var/www/html/programaciondam2526/.git/objects/3f/48de1308cfdee7032ebd2ad62dd8b758d43140
/var/www/html/programaciondam2526/.git/objects/3f/eccc336453782979f2c3a078ebd78054737c9a
/var/www/html/programaciondam2526/.git/objects/82/cdd216ae199a67246c6d6863e81a8983ac3aff
/var/www/html/programaciondam2526/.git/objects/82/7a5563d7cdb9447e8a36cacc6516abb1eb51b2
/var/www/html/programaciondam2526/.git/objects/82/1bc66e0704feff1fe0b552361d268faace9c67
/var/www/html/programaciondam2526/.git/objects/55/0376c979fdf75c228b9a8a160ff1d8b7beafd4
/var/www/html/programaciondam2526/.git/objects/55/24797cb6603ef3d2134248ae71c4555402c157
/var/www/html/programaciondam2526/.git/objects/55/d760010c5249850011e22e979b485f9bd69150
/var/www/html/programaciondam2526/.git/objects/ad/f39835bd4d2a4c647bdc0fe6063652233d51af
/var/www/html/programaciondam2526/.git/objects/ad/eb7de7f144aa128ea8713019fa83c6ba3ec087
/var/www/html/programaciondam2526/.git/objects/0e/4c54bc6ae99b69ba5605c980c5e55480950f12
/var/www/html/programaciondam2526/.git/objects/0e/072209bc55116c28faa1b0aa24413dbb500f02
/var/www/html/programaciondam2526/.git/objects/26/1d107cc316f90cc0f700964e235f21b3a6e04f
/var/www/html/programaciondam2526/.git/objects/26/10e939551aef74d9b0768fac402a2e0209107b
/var/www/html/programaciondam2526/.git/objects/26/f07baad39e14b757269aa71f9523022b35532f
/var/www/html/programaciondam2526/.git/objects/7a/35f8d326923e8012cd6f289a6a21e205826184
/var/www/html/programaciondam2526/.git/objects/c0/8b5e48c85f0d20fa91a4dfe181b2eae1501144
/var/www/html/programaciondam2526/.git/objects/ec/c4a33ce949c150c2cb227feed70199b746b3ac
/var/www/html/programaciondam2526/.git/objects/ec/11c56d5863cff7f1deeac283257b05a2370d08
/var/www/html/programaciondam2526/.git/objects/62/390b8577ee22284b1ed1d0b4431e7524d3d9ef
/var/www/html/programaciondam2526/.git/objects/62/cf1f2111cf03d9b7f52a4572c8e2383d63b460
/var/www/html/programaciondam2526/.git/objects/62/7f35de26524a979168415ff7b562cea2389fcb
/var/www/html/programaciondam2526/.git/objects/62/e321012dc2186b31b4f6e15d5106499abf8cf9
/var/www/html/programaciondam2526/.git/objects/62/023618b51fc484143ecce141d705b1a8b77e23
/var/www/html/programaciondam2526/.git/objects/62/3cc6b5cfd4d510c4f1e0e987fb498c8215fe9d
/var/www/html/programaciondam2526/.git/objects/e2/038bf8c8b27a3c7f47c622902f32e40af8d27d
/var/www/html/programaciondam2526/.git/objects/e2/94a060e8f7a21d851d13a3d93f5b2b8bcbd2fa
/var/www/html/programaciondam2526/.git/objects/e2/82a33bb19148a016dcef43e5ef88b708ad0c3f
/var/www/html/programaciondam2526/.git/objects/9d/4b0f8c07d989c62504c9f7b83a9e04bc6a024e
/var/www/html/programaciondam2526/.git/objects/9d/01c25023360f559fe9550cb8b54cf0e999f6bf
/var/www/html/programaciondam2526/.git/objects/9d/d95d74273ce86895c0c4dc0dfef1be4aa3832f
/var/www/html/programaciondam2526/.git/objects/9d/ada280de6bef83d7a41f8af45dd2ee8a029ad1
/var/www/html/programaciondam2526/.git/objects/9d/1e2569a9b800ad1b9dab0ad5226b90761c750f
/var/www/html/programaciondam2526/.git/objects/9d/c6ba7de0377317e3a314b5d48417ac59f3faba
/var/www/html/programaciondam2526/.git/objects/9d/d9146fd9e87acc1b0a8f85ce0e97c1943591b0
/var/www/html/programaciondam2526/.git/objects/9d/46f7146a8481a54df904ef3cb8ec9c68dd4e0e
/var/www/html/programaciondam2526/.git/objects/27/16d902b81913b69c846643a4ff62e30f7473e7
/var/www/html/programaciondam2526/.git/objects/ba/89f99b969304ad2fe0bbab17b4edc1872b2429
/var/www/html/programaciondam2526/.git/objects/ba/7332583e65c6f44fb37517d6295f2e919c8799
/var/www/html/programaciondam2526/.git/objects/5b/135bb7d9d54f1621226ae92116eb4160fad130
/var/www/html/programaciondam2526/.git/objects/5b/f9907bbed3cc24d211005c71d3e2e42a10bc41
/var/www/html/programaciondam2526/.git/objects/5b/0c13a6998891c1ac473e6761c6b87db79c4ce8
/var/www/html/programaciondam2526/.git/objects/5b/c794d697b7d3bdc7ef8dab61cd765ee9e8ac4f
/var/www/html/programaciondam2526/.git/objects/5b/9a7de1e2988381635adde952e5c18afca91353
/var/www/html/programaciondam2526/.git/objects/5b/c2701980f74a501de06b17fcc2cdcfad3e5610
/var/www/html/programaciondam2526/.git/objects/7f/2be6d6704bed987241d72255cfa23cb9ddfa98
/var/www/html/programaciondam2526/.git/objects/7f/14cc16bb6cd93d691d60dc797cde876e58023f
/var/www/html/programaciondam2526/.git/objects/7f/a4af2f7e396661d5102ef43b2373226f150644
/var/www/html/programaciondam2526/.git/objects/7f/742d809cc157bf10a75096e394af3ac9776522
/var/www/html/programaciondam2526/.git/objects/9e/59a6ffd7273a2391bd421bfb1cefe981635637
/var/www/html/programaciondam2526/.git/objects/9e/2555bca40caa8f42c7baf7f64a8233d2eca276
/var/www/html/programaciondam2526/.git/objects/ce/e00be67c99b555806a1ca49f6eb94fbd419922
/var/www/html/programaciondam2526/.git/objects/ce/281723546f15914ce27ae745628428f0f1c559
/var/www/html/programaciondam2526/.git/objects/ce/0e710b9cc4152b39f5f4efcffc91696c5d3b87
/var/www/html/programaciondam2526/.git/objects/ce/a63e860adefac9c3d7c977c0b889e3a85c53f9
/var/www/html/programaciondam2526/.git/objects/db/3c69565595e7b6e5fccc459079732cdf191ffa
/var/www/html/programaciondam2526/.git/objects/db/0fd3ead4d9935483cc7aed3a74ef10680875cb
/var/www/html/programaciondam2526/.git/objects/db/f5427a54dd0836248f738720ca1def0392d637
/var/www/html/programaciondam2526/.git/objects/bf/74192b4f0efbd2aed3fe23a67be325319bff2d
/var/www/html/programaciondam2526/.git/objects/50/2db0e9dd438bc2b93b52e0a3ed656f741e4d22
/var/www/html/programaciondam2526/.git/objects/50/0ab02fe4a8aebd7206fbcbe2959772dffd7bad
/var/www/html/programaciondam2526/.git/objects/9b/69d6d24be3f33834a2e9a4b9784d0d16e0e738
/var/www/html/programaciondam2526/.git/objects/9b/0d0b33f5f9f002630187e3fd4bd06e9ea5b4b3
/var/www/html/programaciondam2526/.git/objects/9b/d91eecc9413deb229c1b228d184de08a030513
/var/www/html/programaciondam2526/.git/objects/b1/1c0b4b6f66d8c84b269d5842a86131ff810f0f
/var/www/html/programaciondam2526/.git/objects/b1/72ea56a82614bf155fc0ea8c125d5e2e232c3e
/var/www/html/programaciondam2526/.git/objects/b1/235e16f45b4201456951b5ff6e1cec4d715ee9
/var/www/html/programaciondam2526/.git/objects/b1/9729dbe01f2be9069e4af26b65a1757707582f
/var/www/html/programaciondam2526/.git/objects/f9/405c7565a83cd8730bf5ed414b6b203e1ef822
/var/www/html/programaciondam2526/.git/objects/f9/1d64b849d68b7f5b0a5a922dbf1028605f33eb
/var/www/html/programaciondam2526/.git/objects/f9/b29a377da0adf4ad9f44ecd65427117bb6669e
/var/www/html/programaciondam2526/.git/objects/86/3196b96c0f735dc7ffd164259b6be3667c6749
/var/www/html/programaciondam2526/.git/objects/86/680d5ad56a82372a5585ea6d51cdf856b0f9cb
/var/www/html/programaciondam2526/.git/objects/cc/7401584a1266d2cd4f0e98c217b398281cf81a
/var/www/html/programaciondam2526/.git/objects/44/e1e488ca1f73add95c437ff1dcd5ccf88e9451
/var/www/html/programaciondam2526/.git/objects/73/974291e016b119b99abfe40930fc34ddb34945
/var/www/html/programaciondam2526/.git/objects/73/0db11edac01b886205c801530fff72deb5f013
/var/www/html/programaciondam2526/.git/objects/73/6b8f20af2132af8d437ddc9774d56b0aab2bcb
/var/www/html/programaciondam2526/.git/objects/96/d3ebc0d18da7f2474fba880a8914e45fe54a85
/var/www/html/programaciondam2526/.git/objects/77/8d67993d3bb8c5a847e13ac749f71e98d26cd0
/var/www/html/programaciondam2526/.git/objects/77/498ebae145774c2391468344fd774e1c6c8463
/var/www/html/programaciondam2526/.git/objects/77/5c96611985a297a7cf7c41f5f5a92c0ce6d257
/var/www/html/programaciondam2526/.git/objects/77/7f8b58aed584f2437279e9626f99ae9420bdf1
/var/www/html/programaciondam2526/.git/objects/77/4cd922f1c49ac67a4bef2faf21261ead834c5d
/var/www/html/programaciondam2526/.git/objects/92/a664c8cf7b94f19248ff11158fe2c72a6145bd
/var/www/html/programaciondam2526/.git/objects/92/30f125f66f964100de65fc465f7b136c5713b1
/var/www/html/programaciondam2526/.git/objects/92/397fecf8398b1272a14318f5f386ccd776fe8c
/var/www/html/programaciondam2526/.git/objects/92/fcbffd6b3ee8e730d56b0f3e43dfc2fb469db3
/var/www/html/programaciondam2526/.git/objects/5e/3a1a601fe402f03d226287ff3317dc2a28f0d6
/var/www/html/programaciondam2526/.git/objects/5e/4b38156d1eaa3b3c34c9ad87c480162277ccd4
/var/www/html/programaciondam2526/.git/objects/5e/2e37977051e7e4a87f2c23917b3c79bc93e7d6
/var/www/html/programaciondam2526/.git/objects/b9/98954ad5eb42d8d3150cbc3e645f5c4d027cc4
/var/www/html/programaciondam2526/.git/objects/b9/3e998dc5a636207a1f5f9d8e081606b2d95177
/var/www/html/programaciondam2526/.git/objects/b9/8def76a80ab4511483c74be9ca0fe6a8acc1ab
/var/www/html/programaciondam2526/.git/objects/79/7ab8a457485348f1120abdcdd7bfa1dbc1adac
/var/www/html/programaciondam2526/.git/objects/79/f020098a8d2e83d2c703a583a25a8c64ca8a92
/var/www/html/programaciondam2526/.git/objects/79/e565f0633a497b885627c8423c89635407daad
/var/www/html/programaciondam2526/.git/objects/79/ae4940ab0b6ba539da0902706ae4a9b3b3af3f
/var/www/html/programaciondam2526/.git/objects/08/ed63d62e778cd7d89c4599572a83aef151fe14
/var/www/html/programaciondam2526/.git/objects/08/ede852c1b9d4f2a81cbf9a7dd468f12041635b
/var/www/html/programaciondam2526/.git/objects/31/47ce5cf2b32cf1066890c9347a496008f65961
/var/www/html/programaciondam2526/.git/objects/43/6cfa85b55cbcbfaa9a21bdf428ab54f881cc6c
/var/www/html/programaciondam2526/.git/objects/43/96b8aae598f50bd32c8965cff3ed08791b1b2b
/var/www/html/programaciondam2526/.git/objects/43/71fce4835eea777353a9e6e4c1f39f3d8b86bd
/var/www/html/programaciondam2526/.git/objects/bc/eba012c0fcbdfb16f636ef7f9b334a56fba468
/var/www/html/programaciondam2526/.git/objects/88/edea8228181a3b0410c88ce8141945a5e7734e
/var/www/html/programaciondam2526/.git/objects/88/71b65e63fe4be89ce8015614b45cded54178d3
/var/www/html/programaciondam2526/.git/objects/88/a1411c6141c445193c5ef5c7ccc2e035d7630a
/var/www/html/programaciondam2526/.git/objects/0a/ffbaa002e6b411f1cf13c7c7d3a100331dee29
/var/www/html/programaciondam2526/.git/objects/61/d2a4a6bb107f2c0b07ebfcb6002584385ccbee
/var/www/html/programaciondam2526/.git/objects/61/87e97e609415bd8780493befdaf4801adc293f
/var/www/html/programaciondam2526/.git/objects/d6/01a1f1b9a145311639d44fb006a8b5f2e904cd
/var/www/html/programaciondam2526/.git/objects/d6/43a463687b37f45ec01bdbdef7be87c2200ecd
/var/www/html/programaciondam2526/.git/objects/d6/0bd7855aaae5d240010156d868479a62a0f85b
/var/www/html/programaciondam2526/.git/objects/9a/b703bda9940db8a19c7e95423ea31541e10fea
/var/www/html/programaciondam2526/.git/objects/30/0439b9cb70bbeb13a01ca5dd608ff9165bc135
/var/www/html/programaciondam2526/.git/objects/30/25e30dea9fe5aea6ebf65ec384fa53a2a8d32d
/var/www/html/programaciondam2526/.git/objects/30/c426c9df54def4319b0f87bd13f76eb0972963
/var/www/html/programaciondam2526/.git/objects/30/a44bda449dbc9cf593ebf993f69c089553b0f4
/var/www/html/programaciondam2526/.git/objects/30/b93340deaf90970aa3799431160b7e18fb0459
/var/www/html/programaciondam2526/.git/objects/30/3bfe4e948e17e15cf28f458d821b0cf6548e72
/var/www/html/programaciondam2526/.git/objects/d5/e1bf0f3f4bf7bbba3874a3cb4cd18d4a7bcbdb
/var/www/html/programaciondam2526/.git/objects/d5/ad494001b8acc5d9c1561d24a092818355fc96
/var/www/html/programaciondam2526/.git/objects/d5/0880bba8203a309929fb2dc27991ab04be2d04
/var/www/html/programaciondam2526/.git/objects/d5/ed7bc232a31fa8dde8f8ce60bf00f864e43980
/var/www/html/programaciondam2526/.git/objects/b8/9bfbd239c90e59459d40f1881302d68cc2d496
/var/www/html/programaciondam2526/.git/objects/b8/11abc46553871553d1c308c4ab14910e1cc21d
/var/www/html/programaciondam2526/.git/objects/8d/19f776796d2fea36a3067f3c3cbd8980063cdb
/var/www/html/programaciondam2526/.git/objects/b7/0883045a00a6036c29a0562b93444df76806b4
/var/www/html/programaciondam2526/.git/objects/b7/ebd856517564baa47608a1c9b575fdfd155ae3
/var/www/html/programaciondam2526/.git/objects/b7/f11f34597aa0b0b13e97215d640449191cbc37
/var/www/html/programaciondam2526/.git/objects/b7/80a4df6297c90af5a1bf2614356dc4ca65e302
/var/www/html/programaciondam2526/.git/objects/83/d63bf32663fb7de6e014ae8de04cfd01cd4ee8
/var/www/html/programaciondam2526/.git/objects/bd/5d82786104fee2a3c4a488b57e8173eeddc3b5
/var/www/html/programaciondam2526/.git/objects/bd/15753a6d2e973c2c015c2556031ee8e746647e
/var/www/html/programaciondam2526/.git/objects/65/f9bf06eff504317a9c0ba578221d4b148024aa
/var/www/html/programaciondam2526/.git/objects/65/ae2c00fe81d673b8eac8f9fbee28a234bd7fd7
/var/www/html/programaciondam2526/.git/objects/65/34db183be09a6dbcd950358f6360da1098a38b
/var/www/html/programaciondam2526/.git/objects/65/c14fa15a377473e442d12eb3aabbb77bd06c82
/var/www/html/programaciondam2526/.git/objects/17/d101bfb07d0ef06e1d0f1d9cc1be0da02e59de
/var/www/html/programaciondam2526/.git/objects/17/c719591f89af9b903c4f11588efe015e5ae5fc
/var/www/html/programaciondam2526/.git/objects/17/66fe8ec6206b2928f26557eabaa6eac867aa90
/var/www/html/programaciondam2526/.git/objects/17/85496a3eb6e0e7ec8838886933edea83fed641
/var/www/html/programaciondam2526/.git/objects/29/a1578b6278d3678e7182eaad9332208fefd74d
/var/www/html/programaciondam2526/.git/objects/29/685712da8b4225a414a61145c4386a242a6dc8
/var/www/html/programaciondam2526/.git/objects/29/9c7cb53f89ecc4c97db6add5ab5aa99a44ab7c
/var/www/html/programaciondam2526/.git/objects/b3/c8abf391ae2d257e04b472189c1ecc03b10c1a
/var/www/html/programaciondam2526/.git/objects/e4/1e3f248d5cb7eebf1cb2e66dd6826350472b1f
/var/www/html/programaciondam2526/.git/objects/f3/b27c2e2768ee3d32863358f1a9afe143315645
/var/www/html/programaciondam2526/.git/objects/f3/4c46f042e834ec7c4cfdf70befbdb5711ec077
/var/www/html/programaciondam2526/.git/objects/8a/b6924f1f128b424f067f66539c3ca59780291e
/var/www/html/programaciondam2526/.git/objects/e3/0d8e21e41040a0b7209ee9c2bd18f39623e04f
/var/www/html/programaciondam2526/.git/objects/e3/a51edf5d66b5273d06dd21686610feafd0dc34
/var/www/html/programaciondam2526/.git/objects/e3/2e947037d6ba0fef39b54735a1e991ca8e76cd
/var/www/html/programaciondam2526/.git/objects/75/ab4babb0554d12361e5c89935ad21d91c63e35
/var/www/html/programaciondam2526/.git/objects/75/7f58361f110d526754fdc50ee81d1abfb06233
/var/www/html/programaciondam2526/.git/objects/75/8c358c9ab2fe036d16cc0126a016625e45ed50
/var/www/html/programaciondam2526/.git/objects/0d/95ebcef09b03a164adb0a5fe0dcbdc943c4249
/var/www/html/programaciondam2526/.git/objects/0d/3a61c1580e8b3b72d4f9c8677932fb8ced50f4
/var/www/html/programaciondam2526/.git/objects/f2/05eb323014470b8fd10179d816020f549c8d0c
/var/www/html/programaciondam2526/.git/objects/f2/b95612f43c365d03e3a3f7e10d27c08fad0814
/var/www/html/programaciondam2526/.git/objects/f2/4f78b1eeea7c0e7128effaea62b439292fe5e5
/var/www/html/programaciondam2526/.git/objects/f2/d44c4b75b45749ff626e07f52897504454e6c3
/var/www/html/programaciondam2526/.git/objects/f2/43c302d0d8cb3a930a77ae3a242062680fc097
/var/www/html/programaciondam2526/.git/objects/54/121e9f00c1baaa86cf982a7c0709669bc4a28f
/var/www/html/programaciondam2526/.git/objects/54/a4d05d0e13a1f68ed4cae7ebb6567ebe73eead
/var/www/html/programaciondam2526/.git/objects/54/210adb9999a3cd93adfb7d2b72381eb9acbb76
/var/www/html/programaciondam2526/.git/objects/48/61bc9e5d8114ee073487d9998e41f215ef64a0
/var/www/html/programaciondam2526/.git/objects/48/7dc094fa20193f5855d116c2f92b0ef4939a24
/var/www/html/programaciondam2526/.git/objects/48/e4f3c778ed93728a4fc9511f101f1452c99370
/var/www/html/programaciondam2526/.git/objects/48/757cdd567076e63fefe953f22aaefbb95f87b7
/var/www/html/programaciondam2526/.git/objects/48/a8ac132397574df217ac9a53d4f822543fc4fb
/var/www/html/programaciondam2526/.git/objects/48/4e6dae47121b946079644264fe6b06f2c29470
/var/www/html/programaciondam2526/.git/objects/d7/18f1f14426c720fce206b20343f1fd579289fb
/var/www/html/programaciondam2526/.git/objects/b2/c438705de0ec23072d79cddf64c154a7ca35c6
/var/www/html/programaciondam2526/.git/objects/b2/aa0aa7ff77c8cbd7107b01513bc57639b0c213
/var/www/html/programaciondam2526/.git/objects/ee/586e1c8a606cb746ac2c97023bdc4ab1ebdf90
/var/www/html/programaciondam2526/.git/objects/ee/b3d009efa72e7095f8e43012531010026a88e1
/var/www/html/programaciondam2526/.git/objects/ee/f19b14282f82323ab8f2f448e9e1ce85058703
/var/www/html/programaciondam2526/.git/objects/ee/dbf1122a917d00c765e47705b3a0da336adf38
/var/www/html/programaciondam2526/.git/objects/ee/b74d4fb999d934778b3442decd52f3f64db027
/var/www/html/programaciondam2526/.git/objects/38/3c40e6d68922508e3f1fa32bca6dbd1823c878
/var/www/html/programaciondam2526/.git/objects/38/b1f0a80f2f26c148b24fd0814cbae387a657c1
/var/www/html/programaciondam2526/.git/objects/38/476315d589175a8edcf80c1d9dc1068e461c3b
/var/www/html/programaciondam2526/.git/objects/38/c9f3b0b23a9d0f0be234a030efdd5941e3e50b
/var/www/html/programaciondam2526/.git/objects/38/66f3c163ad0dcf5bda280cd19b9372969267f7
/var/www/html/programaciondam2526/.git/objects/64/25868eef55de20bf6a70ca4e3b66fb7783a376
/var/www/html/programaciondam2526/.git/objects/64/c7ffe75cd4f5b772ef5d59362088792bb5e8c6
/var/www/html/programaciondam2526/.git/objects/64/a7e13ccada46e6e393a93c5c744e918110e6f2
/var/www/html/programaciondam2526/.git/objects/de/d4a26d20a4ec6b0faa541d0fcfd61326da552a
/var/www/html/programaciondam2526/.git/objects/0f/bfedfa8089a68f108dc244becff82c396dfa10
/var/www/html/programaciondam2526/.git/objects/0f/ef011b8ad3e482acb2223497191f40a15a5834
/var/www/html/programaciondam2526/.git/objects/0f/37587171eb870c1c570c61b79eeafa942900a8
/var/www/html/programaciondam2526/.git/objects/fd/5b47aa9eec6405cc7250f190012d161abb8c09
/var/www/html/programaciondam2526/.git/objects/fd/b31d1cf66bef7bb9f64ad5586f28e09ca53b2b
/var/www/html/programaciondam2526/.git/objects/09/dd7a1f6bb9a6c7c1455fc497014d6e3de10c66
/var/www/html/programaciondam2526/.git/objects/09/dc3405d4683b2f25a6ef5b9d9f1080d11ee046
/var/www/html/programaciondam2526/.git/objects/09/23169f80c4030115c1a66134148d919753f8e8
/var/www/html/programaciondam2526/.git/objects/dd/db6533d48388ee00649120900fea43abfab62a
/var/www/html/programaciondam2526/.git/objects/dd/a603b80bcc780cc251958afa54a8110ad33ba2
/var/www/html/programaciondam2526/.git/objects/dd/c45bc8b211fc933ab0202e7b9bc746d0eabfd8
/var/www/html/programaciondam2526/.git/objects/5a/dd0d1bb570dd98a714af4353225d33028a311b
/var/www/html/programaciondam2526/.git/objects/5a/8c31b35e88d0c21c3213cc12700e633acf537c
/var/www/html/programaciondam2526/.git/objects/03/45a2434702378e4c3d86fd48d8644cf884e450
/var/www/html/programaciondam2526/.git/objects/53/90895e7735c5e91b710d4cb80d7eeb970c10f4
/var/www/html/programaciondam2526/.git/objects/53/9e3dbf84340be05687442ce51b8fdc155f43ca
/var/www/html/programaciondam2526/.git/objects/02/3b5d66b0162d8b2947989553ee4a21f5b80013
/var/www/html/programaciondam2526/.git/objects/45/1cf007d89a562d828de1ab71c8b03e0c813d60
/var/www/html/programaciondam2526/.git/objects/45/64842856c63058029a4dcf99a465bc1acb83f3
/var/www/html/programaciondam2526/.git/objects/45/5c25527acb9a9129d8e0dc84e0d6e2ac54cdcf
/var/www/html/programaciondam2526/.git/objects/45/42ccba22ab6a6d73f51f2604e8c8aafbaccb62
/var/www/html/programaciondam2526/.git/objects/45/811145b200ab08508922335578e1664c850c61
/var/www/html/programaciondam2526/.git/objects/91/1433b44037404be4e3918fca0163a41070a4fe
/var/www/html/programaciondam2526/.git/objects/91/d209c7da06ab25f11320b800adb3b45cd0beb1
/var/www/html/programaciondam2526/.git/objects/87/0a6da161e2d598ac653ea20b8578f2f8597bc9
/var/www/html/programaciondam2526/.git/objects/fa/1f0f15658310877063d67c51bf4df6a22cbb57
/var/www/html/programaciondam2526/.git/objects/3c/1c39e49de27b86736f405c6957ee3dd9cfdd5e
/var/www/html/programaciondam2526/.git/objects/3c/28b8e295e08924aef8cbfd2b2b403a127991b8
/var/www/html/programaciondam2526/.git/objects/3c/ea5b84a2adeb13b77600766e763007e626a41b
/var/www/html/programaciondam2526/.git/objects/a2/c0faf57f1a8881a085aeabfc72c4f0047abc5b
/var/www/html/programaciondam2526/.git/objects/a2/e8365ce5788e3be23bf2164a7134721acc21e7
/var/www/html/programaciondam2526/.git/objects/a2/fe959017436ff0bc880f2c2706b626a5369b96
/var/www/html/programaciondam2526/.git/objects/a2/d9a3814c6c1b753047e4e68e341a31bcdcc069
/var/www/html/programaciondam2526/.git/objects/19/649f3d813c90c24986378e9fa9a9dad70190aa
/var/www/html/programaciondam2526/.git/objects/19/f647e31651e7848782356d76d21dc50713f952
/var/www/html/programaciondam2526/.git/objects/19/6dd1121301c24cbb4ed1484c3a276822f4d6d7
/var/www/html/programaciondam2526/.git/objects/19/b34366a32f3a69029e29af706748985e66a841
/var/www/html/programaciondam2526/.git/objects/19/d2d80b89ff5bbd35a8ea9a26f64d4da38ec9a2
/var/www/html/programaciondam2526/.git/objects/19/f4895aba14ca2c85ce7f1fcf7d3c1c60ba2659
/var/www/html/programaciondam2526/.git/objects/4a/e5181893d095ddf054be12e3f4311e9eb1f750
/var/www/html/programaciondam2526/.git/objects/4a/a2ea3d9cae831fb0084996cd8d8ebfb4803515
/var/www/html/programaciondam2526/.git/objects/4a/e2249b69cca655a575f79c7c1a3a458861d845
/var/www/html/programaciondam2526/.git/objects/41/addfa843c81549fd9ba6f04a0a2eaed3d8aa0e
/var/www/html/programaciondam2526/.git/objects/41/fa6282db7eebc94bfc9c5ecb72b2a3cd7a0c4e
/var/www/html/programaciondam2526/.git/objects/42/67b6071a276ca3cbf1c486bc20f0cae54445c5
/var/www/html/programaciondam2526/.git/objects/42/d0b0450e6a2406433751a72e1a9399464a36c0
/var/www/html/programaciondam2526/.git/objects/42/912ccde4361c76cead9a503e30bb9636a18a3e
/var/www/html/programaciondam2526/.git/objects/f8/ca83f62e7b5815ed67258cdced033c03a5fd76
/var/www/html/programaciondam2526/.git/objects/f8/2c5158df0aff9e5f200ddda23723e3ce9d59ec
/var/www/html/programaciondam2526/.git/objects/f8/ac85c9b203696e14cf7fa8044f0049e2f33b48
/var/www/html/programaciondam2526/.git/objects/8f/eaee63b3e7d712f3da62814f8702eb607fc83f
/var/www/html/programaciondam2526/.git/objects/8f/25fef1913937ec663903aa17334c2ece6eb74b
/var/www/html/programaciondam2526/.git/objects/04/2adb8e49490d2ee0ed622a92a469833804d9d0
/var/www/html/programaciondam2526/.git/objects/04/d87877b5a369c14bab8750b9a71e1658d01466
/var/www/html/programaciondam2526/.git/objects/da/d0077e9a4c18c78c03bde2ab8526a0b01f1d18
/var/www/html/programaciondam2526/.git/objects/da/9119fe169eefa2c1ec378b2e77a5854ec5464e
/var/www/html/programaciondam2526/.git/objects/95/8f2dcda50443fd718894b6bc7a0c650a2c8fcf
/var/www/html/programaciondam2526/.git/objects/95/661de9345c7b2e23f804f84ef86b4254abe69b
/var/www/html/programaciondam2526/.git/objects/95/8f25d38ebb09de20a632b257288d2c6092e46f
/var/www/html/programaciondam2526/.git/objects/7d/2339cc0f5c9cb7e1fa191b1b8d46a2915d03e3
/var/www/html/programaciondam2526/.git/objects/ca/41ad75a41a47bae52e702e14d8aaec2b41c264
/var/www/html/programaciondam2526/.git/objects/ca/e622c8ecd7f3787744bf6685897516001cb416
/var/www/html/programaciondam2526/.git/objects/ca/00f0137c95a4a857885b8a7644fa8264f45291
/var/www/html/programaciondam2526/.git/objects/ca/bf950be28f889d53b0d1d450c7228210cc8089
/var/www/html/programaciondam2526/.git/objects/pack/pack-274984f77d51a2155b5a472cdf2f0a7d4f2672d1.pack
/var/www/html/programaciondam2526/.git/objects/pack/pack-274984f77d51a2155b5a472cdf2f0a7d4f2672d1.rev
/var/www/html/programaciondam2526/.git/objects/pack/pack-274984f77d51a2155b5a472cdf2f0a7d4f2672d1.idx
/var/www/html/programaciondam2526/.git/objects/20/06f7f3cbdb7b2e0e66bbab41c179430b867660
/var/www/html/programaciondam2526/.git/objects/a8/984628a1371a04f3993cc3febeab1931aa93fd
/var/www/html/programaciondam2526/.git/objects/a8/6902b4389e367b226c7d8ccc291a9ba7ed7b7f
/var/www/html/programaciondam2526/.git/objects/a8/5e772e9fb84795507c4e1e86fdf925541438b8
/var/www/html/programaciondam2526/.git/objects/76/6b90626bd957ffdca005f7a4d51f3a19d17f71
/var/www/html/programaciondam2526/.git/objects/76/c45cf132d78cb3b65457ad4d287e85effa4e6f
/var/www/html/programaciondam2526/.git/objects/c3/278606b754157f866b523c2ffdddca73e9ff1f
/var/www/html/programaciondam2526/.git/objects/c3/f59da46e7aa0b9531c7f7db9fe76488817cef3
/var/www/html/programaciondam2526/.git/objects/c3/7e1b7d448aec128569d554ae62305b4129df58
/var/www/html/programaciondam2526/.git/objects/39/a6655ecb01d5b48994504ac6d26b0f5ab0a6d1
/var/www/html/programaciondam2526/.git/objects/11/93de59eca611f220e0ea53563e24271915f51c
/var/www/html/programaciondam2526/.git/objects/11/c89f8b7f0448b63b52ba5caebb2ce01717cb05
/var/www/html/programaciondam2526/.git/objects/11/865b58f8b856b89f289537a1eccbdd2e4fc2b9
/var/www/html/programaciondam2526/.git/objects/11/e1e6d05923a91d2a2bf7d3e0f415975e2cdc05
/var/www/html/programaciondam2526/.git/objects/ae/0f8672a305d2850d6a3d44f830495ec745c816
/var/www/html/programaciondam2526/.git/objects/84/5ee88aab2a531159401db8f81c8b7585fae3c3
/var/www/html/programaciondam2526/.git/objects/84/616cbe1c6e8d9d2efe5aee8ec5768fa5852cb1
/var/www/html/programaciondam2526/.git/objects/84/f1f73330bce92ffdf11ab71c4d0ed82a0e2e67
/var/www/html/programaciondam2526/.git/objects/a9/64cf0aec0248c781ef4509e64e685d0fb01033
/var/www/html/programaciondam2526/.git/objects/a9/36fb391c37ea2ae7ac32ef0155e121038995a5
/var/www/html/programaciondam2526/.git/objects/e0/11fb4b931079449782bb120dae83a577d01ddf
/var/www/html/programaciondam2526/.git/objects/e0/8ac68bab2a2ed0b116c5f1b113aa8d5ddf96b7
/var/www/html/programaciondam2526/.git/objects/e0/b4ebccd5984ddc56cce87aabc3db5fd2235726
/var/www/html/programaciondam2526/.git/objects/56/57237f217586911e5639f0ff1bfc6786ae33ea
/var/www/html/programaciondam2526/.git/objects/aa/c215911d3c157ae2cedba20c61ed9941b36f4b
/var/www/html/programaciondam2526/.git/objects/aa/7509de6fccd30c2cb814f9d7a27b48b4e13507
/var/www/html/programaciondam2526/.git/objects/d4/65b192c6bbe600e8ac788243e7b894f8b04965
/var/www/html/programaciondam2526/.git/objects/1a/3f694bc563d1e222d45a4ea2f3cfb71cbe327e
/var/www/html/programaciondam2526/.git/objects/1a/7b6fadb7293ce7043f007520448c9fa692a4d2
/var/www/html/programaciondam2526/.git/objects/b0/bdfe1951c22a441321fad68a2a0dc24a35afc6
/var/www/html/programaciondam2526/.git/objects/cf/a5a1790cefd824950d63229ac74b397fa6f0bf
/var/www/html/programaciondam2526/.git/objects/cf/da7b9f6f2a5d4ee6cd45ed6b03af77ea28881b
/var/www/html/programaciondam2526/.git/objects/cf/b36bc0c61ecf8b6415468e98780d5719656618
/var/www/html/programaciondam2526/.git/objects/8e/b40ccb87b839428f51e3de693b37dca7568b3e
/var/www/html/programaciondam2526/.git/objects/8e/ae24056c73515701dcdbb50bf85b3777e5df80
/var/www/html/programaciondam2526/.git/objects/e9/34027d11a4a5cab7b3863a269b12771fbc29bf
/var/www/html/programaciondam2526/.git/objects/e9/4aba73b09129093091a3f839569e47fe9eaeed
/var/www/html/programaciondam2526/.git/objects/e9/54a9453b1d6b24a681230202bdaa31e876082c
/var/www/html/programaciondam2526/.git/objects/18/ed742e6850c9434e9232f7f22844ecf4e91041
/var/www/html/programaciondam2526/.git/objects/4e/f1feb08c5bdb1ff45e674ceb5e8d470fd8ac1c
/var/www/html/programaciondam2526/.git/objects/4e/21e26411f7ef495a86d6c6de731f37bba36579
/var/www/html/programaciondam2526/.git/objects/4e/8fad9dfe00e8a3c2bbd4b6a7b065a5ba66d5e8
/var/www/html/programaciondam2526/.git/objects/4e/91c6ca49b51505a982a7b70d07ad1dad938e3c
/var/www/html/programaciondam2526/.git/objects/5c/e8caf6b8aa8f2e81611e2288a15fdd8dd02116
/var/www/html/programaciondam2526/.git/objects/5c/911630fd365075ac3d94247dc2efac66d3dc1e
/var/www/html/programaciondam2526/.git/objects/5c/2ef8a70d1e6d6a010e84fef13eac609744194a
/var/www/html/programaciondam2526/.git/objects/47/4347702b0844c2506efb2b0189fb92a500b04e
/var/www/html/programaciondam2526/.git/objects/34/71f70e0ba98befe5d918d28ac0293c8328d5f6
/var/www/html/programaciondam2526/.git/objects/34/ae0a783ab128b833d2c4749c3e3cff3eff92bb
/var/www/html/programaciondam2526/.git/objects/34/46fbac7db381bbc8c84d942d9bcbda2d17b07e
/var/www/html/programaciondam2526/.git/objects/3a/26c602b2cd9b1e0b7959d314f1ecb03e33b73d
/var/www/html/programaciondam2526/.git/objects/3a/ab3f79d1854a873991ab9030de0a2756459586
/var/www/html/programaciondam2526/.git/objects/3a/7a7218cf3046821f0ad83a427c106b600cb312
/var/www/html/programaciondam2526/.git/objects/c7/eef26d3654cf73d4e9ffaf5501025320045403
/var/www/html/programaciondam2526/.git/objects/c7/bd05fbb730a2eed69c2c8687f1bfb288c32057
/var/www/html/programaciondam2526/.git/objects/93/b4ccbf25bed23eb63f7a6be144c2f6ff444f7e
/var/www/html/programaciondam2526/.git/objects/93/2236b2eb4e2d6b725dee7a8f39e5d22854dbd0
/var/www/html/programaciondam2526/.git/objects/93/837d67872df816883a4cd32c30fc3c8797fd41
/var/www/html/programaciondam2526/.git/objects/93/aab3fe5b6bf41ee3711e65c3ff19a7c396ea1a
/var/www/html/programaciondam2526/.git/objects/93/f6f1498ad5d505eb80d3be4362ed2812c44351
/var/www/html/programaciondam2526/.git/objects/74/fa52b3974157b3870071f44e1438c823dbe744
/var/www/html/programaciondam2526/.git/objects/74/8af43b1d31768abcccb9205696b2043e5acadb
/var/www/html/programaciondam2526/.git/objects/66/4212ba14894242e9e9911f5f70a79a7b7033b8
/var/www/html/programaciondam2526/.git/objects/66/664024f3686b6597d3cfc8edb015a8ca1358b9
/var/www/html/programaciondam2526/.git/objects/5d/6c05b55824d8b6476c82d806a72d039e483fc3
/var/www/html/programaciondam2526/.git/objects/5d/6e30c668c8065c12453a572a48b93b0bd24ff6
/var/www/html/programaciondam2526/.git/objects/3d/f355713fce1ea9794a28ab51edefc1874f5a5d
/var/www/html/programaciondam2526/.git/objects/3d/2df20637468c43046735cc8ac565e5a53c3e44
/var/www/html/programaciondam2526/.git/objects/3d/8636c09d959fc4808569b03932a939b414498b
/var/www/html/programaciondam2526/.git/objects/36/6107c19814005755ba2855e7dc017a2798d33a
/var/www/html/programaciondam2526/.git/objects/36/4cb80082e3ef71a0ce8921f2914adb19d33258
/var/www/html/programaciondam2526/.git/objects/a7/c97167f36129cbc929189dd3dc45ee5a5e11b9
/var/www/html/programaciondam2526/.git/objects/2e/91f09ea85141190b201b364f755c070f00ac09
/var/www/html/programaciondam2526/.git/objects/1c/fb926de4ae307fe44fdf9cc9d77f14d692400a
/var/www/html/programaciondam2526/.git/objects/1c/e9f1acf5264d23b17e325f941679970289bb84
/var/www/html/programaciondam2526/.git/objects/80/e600e42241c16f74375a01aa40870dff18b396
/var/www/html/programaciondam2526/.git/objects/80/96e341d04b03483bc4fac02f36a75b0ec26e9d
/var/www/html/programaciondam2526/.git/objects/80/c89d3f6b6e374765c44f88dde057062b6ffa80
/var/www/html/programaciondam2526/.git/objects/80/ed99cc363c64540600632ce7dd8fb29c58fb44
/var/www/html/programaciondam2526/.git/objects/80/d6d325d69cf37dc629a229f28e6b3b8845b085
/var/www/html/programaciondam2526/.git/objects/85/e54c434ffcaee73b8659b02e52e227fd08911d
/var/www/html/programaciondam2526/.git/objects/85/e9f58fb67c8d72ab69a8129a298be1b4ff43db
/var/www/html/programaciondam2526/.git/objects/85/61ed7711223538dc8cc5425e9c5f4d1d875a21
/var/www/html/programaciondam2526/.git/objects/d3/03e2a574601db9fda6d8b068878126e69fa183
/var/www/html/programaciondam2526/.git/objects/d3/23e667070aff6f4561bf51066bf36c4c33c075
/var/www/html/programaciondam2526/.git/objects/4d/4d7102b88d10a9d57b68e31a40c2ffd0786506
/var/www/html/programaciondam2526/.git/objects/4d/84c60c2e1868c84288c0ae90859ea56784c346
/var/www/html/programaciondam2526/.git/objects/4d/7f237c9f731988bfed94141b9ecd02bcb443f2
/var/www/html/programaciondam2526/.git/objects/49/fd59645f3120ffdaf29c0f6b4a20d790281379
/var/www/html/programaciondam2526/.git/objects/df/535878552e9ee5d311272801d4198df077d28d
/var/www/html/programaciondam2526/.git/objects/df/8e78cd8b7bb5de55ec2f7cf27999263f7d8577
/var/www/html/programaciondam2526/.git/objects/df/183998b16b5c1641d9c4017a9a648fdd1e3606
/var/www/html/programaciondam2526/.git/objects/eb/4db2ba9ffefd6c0f5c124bc8e1a746357ca7ba
/var/www/html/programaciondam2526/.git/objects/eb/ea7c97d421ef5c78115aaa800e6254cf2e2914
/var/www/html/programaciondam2526/.git/objects/72/5d2eb6f538494e99b1f15e32bc82e908371ade
/var/www/html/programaciondam2526/.git/objects/72/c8bc998da5f70188fb0773fb74b80f890339a6
/var/www/html/programaciondam2526/.git/objects/72/d4d0634ccff3a9f89960940972841bf055e897
/var/www/html/programaciondam2526/.git/objects/72/0fca0a228ae43396bc84b734e16b1346128735
/var/www/html/programaciondam2526/.git/objects/72/c44ad8272610141e3226ce7975679e13758be6
/var/www/html/programaciondam2526/.git/objects/40/5a8c4a9fc6c2a6d7b4d96fad38017eef392b6f
/var/www/html/programaciondam2526/.git/objects/7e/e49fe0c83d13ff9ccc7e8900de04978e9fc3a5
/var/www/html/programaciondam2526/.git/objects/7e/f8bd44a7295d5b7e613a0da2f3e9bedcc9805a
/var/www/html/programaciondam2526/.git/objects/7e/b025c954bc5efd7094962912504ceb45041941
/var/www/html/programaciondam2526/.git/objects/7e/fc1950b9fa671d7fb759f8de81051bba5b2e0a
/var/www/html/programaciondam2526/.git/objects/f4/1e9fac32111f87f8db69b4cfcd30187d27b6fb
/var/www/html/programaciondam2526/.git/objects/f4/32a2f3f8bb30519bb88a97e4a396e48d5a2361
/var/www/html/programaciondam2526/.git/objects/ac/40adeb97a623de893d526c02f46633500fe7e4
/var/www/html/programaciondam2526/.git/objects/ac/324352877661b373286b5414771ddbb72eb0cf
/var/www/html/programaciondam2526/.git/objects/a1/0d9fd18745396681629ce671aafb9b61ff5cce
/var/www/html/programaciondam2526/.git/objects/a1/874b78f3b8e39ed1c40fdda74cf084d3fdb282
/var/www/html/programaciondam2526/.git/objects/a1/10729e95a38395be50e62dc5b3199c39e3b31f
/var/www/html/programaciondam2526/.git/objects/0b/31e8e817bc876a9a5dbfe3adcbbe0d915f1429
/var/www/html/programaciondam2526/.git/objects/0b/bf1108e40dc291f220a7dbe2d16daf4f637a34
/var/www/html/programaciondam2526/.git/objects/0b/222552dcbfd15e3d4c14de6eca455df62d483c
/var/www/html/programaciondam2526/.git/objects/0b/9e4be95b506747c5726d055434a016b049343a
/var/www/html/programaciondam2526/.git/objects/0b/4d8c765b3961099c08e67274a32ef49103d65b
/var/www/html/programaciondam2526/.git/objects/21/55b4e8139bfc9c1ca8c0d35204ffd686e3255b
/var/www/html/programaciondam2526/.git/objects/e6/8862b85ce720c5c95acb405e545df6609faee2
/var/www/html/programaciondam2526/.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
/var/www/html/programaciondam2526/.git/objects/e6/cefe17783008e3f95b763075921c95f095857e
/var/www/html/programaciondam2526/.git/objects/90/707d89828377bb44d7a72179b382239e1f4b71
/var/www/html/programaciondam2526/.git/objects/90/016c516562f56ea0d2f3c302bc47bc629a1b98
/var/www/html/programaciondam2526/.git/objects/90/e1925cd94673f113b823ed3581ce7def8e71c2
/var/www/html/programaciondam2526/.git/objects/6a/35b21a26d65989430a4eb1444a058e6e45bcee
/var/www/html/programaciondam2526/.git/objects/6a/8c0d53c9c967e1911bbed3cb4d5e8ddddd7b03
/var/www/html/programaciondam2526/.git/objects/6a/6b379624f1e10ba1a05783a5fa1700b16c7aec
/var/www/html/programaciondam2526/.git/objects/6a/0531878bf41b82ad3f500834edb253694eddaa
/var/www/html/programaciondam2526/.git/objects/78/d012c400d22a060a7c543fffc0f803c6623bc7
/var/www/html/programaciondam2526/.git/objects/78/530ccb582e365b32e0ef7356e109f4ee4a4bb7
/var/www/html/programaciondam2526/.git/objects/78/b152192e8bd024bafe324dae387eddb12cc315
/var/www/html/programaciondam2526/.git/objects/78/0380ee37c0651516c047425e0cecfec438a67e
/var/www/html/programaciondam2526/.git/objects/2a/77b7a25582f51afa42e6846430d794d31be7c8
/var/www/html/programaciondam2526/.git/objects/2a/bbf60f8cbcd1476b07768519b946a0e671cb48
/var/www/html/programaciondam2526/.git/objects/1f/89f43ed38769305dbd469aa340df75ff036a59
/var/www/html/programaciondam2526/.git/objects/1f/47ec295d246ce70768d40562f9dff1d4565a94
/var/www/html/programaciondam2526/.git/objects/1f/9065fd4ed5c1ed909c199294a5cbc144da1d06
/var/www/html/programaciondam2526/.git/objects/cd/42b4aa30fe8c8be5c789d9a1bc6c103437c4ba
/var/www/html/programaciondam2526/.git/objects/cd/6afacd3fbfe2ad2d47b13facb690d581c8eca4
/var/www/html/programaciondam2526/.git/objects/cd/6f5cb19c48eb0f80215f0b32f7e6f787eb74eb
/var/www/html/programaciondam2526/.git/objects/cd/9878d367f9199924b786346f1dea665f5acfeb
/var/www/html/programaciondam2526/.git/objects/1b/fbcff9718fec10bbd77a1c8ac9a269703b23f7
/var/www/html/programaciondam2526/.git/objects/1b/b9bce5cba16d293e2d5f9f11c688dddd4ae5d1
/var/www/html/programaciondam2526/.git/objects/2c/ba11b9ad8318c18246f417869d80cba58ea8a0
/var/www/html/programaciondam2526/.git/objects/2c/94213a76ada8196c6d506bd41f2294f0c9ae21
/var/www/html/programaciondam2526/.git/objects/9f/497ff1a228af84ef0f344a06d64ae1c73e2af6
/var/www/html/programaciondam2526/.git/objects/4b/b9582462dfc8f48e139f3e0154d0307ae22b70
/var/www/html/programaciondam2526/.git/objects/4b/bf591ce5f74ad6b72e7a5dec8aee988f35d98a
/var/www/html/programaciondam2526/.git/objects/6d/3ae8c2203ac2533ff29579d80ec4b26e96cc57
/var/www/html/programaciondam2526/.git/objects/6d/fb9f8855b35780af47a9b8df1c49a83d7cbc94
/var/www/html/programaciondam2526/.git/objects/6d/99820d963b0683dd1752c573f8d78782d8a94c
/var/www/html/programaciondam2526/.git/objects/6d/32a0588af2865c65ed6fe7c16127c6477a5643
/var/www/html/programaciondam2526/.git/objects/6d/de0147c7bf84e8de128db0831c7ce1f72773fe
/var/www/html/programaciondam2526/.git/objects/6c/954738f9de62b3586d40d7090d41c630dfa130
/var/www/html/programaciondam2526/.git/objects/3b/a4b9941bf04782455c228806635ff80c34f338
/var/www/html/programaciondam2526/.git/objects/67/0f38882dd35b114ec471d7ad10b0364a129d10
/var/www/html/programaciondam2526/.git/objects/67/14f44be8ed4b3ca2a7032b40b61afa74dddf14
/var/www/html/programaciondam2526/.git/objects/99/b71a74eea80c10a1e38b5a70178bdf3668f47e
/var/www/html/programaciondam2526/.git/objects/b4/4659e7bf116ee9013e45e9d5bb0dd53519e083
/var/www/html/programaciondam2526/.git/objects/b4/75d8ab7a2b1a0afd6d32c0d70f8ba3c0f8f99c
/var/www/html/programaciondam2526/.git/objects/b4/aad9a2942c418a0d6b3732ec83ea8d192756b9
/var/www/html/programaciondam2526/.git/objects/b4/62811b64a6b5fc241a1c59b3e6bed605098369
/var/www/html/programaciondam2526/.git/objects/4f/2a40c155fb2f95280abd631514830adea48234
/var/www/html/programaciondam2526/.git/objects/4f/9eccda329ef34d740335297c1beaf6261033b3
/var/www/html/programaciondam2526/.git/objects/4f/fa1b8db91ffa778d00535186747f96a9bf0033
/var/www/html/programaciondam2526/.git/objects/4f/fb90d77ab36fa203c99948b2f6fb8bc1bdffd9
/var/www/html/programaciondam2526/.git/objects/9c/03faaec8603f15cf39bd41fed6925c6e92dd8f
/var/www/html/programaciondam2526/.git/objects/1d/32f884cb2a31c0349bc01c007a77ca7b81cec9
/var/www/html/programaciondam2526/.git/objects/1d/967a21cfb096efa55a5af0ce07fd259b06e2bf
/var/www/html/programaciondam2526/.git/objects/d9/9986ccd3a47d1f5161cf7e8b697c1779c51a27
/var/www/html/programaciondam2526/.git/objects/05/aeec3ab353f4eb03a5a56529de56dfbb76c5c2
/var/www/html/programaciondam2526/.git/objects/05/98482b5d7f7fbfc82be933a89a91f4ff54bf23
/var/www/html/programaciondam2526/.git/objects/a0/91920f36f44374e27b0bce746f06689d7330eb
/var/www/html/programaciondam2526/.git/objects/a0/1bf65041c6c7e836e7b9ac8204c2d2512c478b
/var/www/html/programaciondam2526/.git/objects/a0/08ed62ad907114545dbfa0f42ea4b242973439
/var/www/html/programaciondam2526/.git/objects/a0/38ef3d428ba12d2c127490778bd9e4d8c62111
/var/www/html/programaciondam2526/.git/objects/b6/32d6d63a7c28a36a0be20010dfeceb2dd69959
/var/www/html/programaciondam2526/.git/objects/b6/cd4f6dfe2c6320cfefa2c822da09cc571ccb84
/var/www/html/programaciondam2526/.git/objects/f7/950b20a8bbc6527da9ae334517d33d4a453b24
/var/www/html/programaciondam2526/.git/objects/f7/528954ebc5dd9935879678dac65075e0d6ce60
/var/www/html/programaciondam2526/.git/objects/59/591f196b5bf70fc481e0495ac4cbdd183a50d6
/var/www/html/programaciondam2526/.git/objects/16/fce7e8c6f8ab53454ea4c9499f60e323dd28e2
/var/www/html/programaciondam2526/.git/objects/16/fa975cf94f941adf3d6571674d1dd3f1b256d0
/var/www/html/programaciondam2526/.git/objects/16/88fdc1ade53efda3503d75e8a750036f0786a7
/var/www/html/programaciondam2526/.git/objects/f0/9109b152c5d4ded93cb6cbfdaf31f209dc3ece
/var/www/html/programaciondam2526/.git/objects/f0/bee249fbace146d6942c111bbb9c74244e48e1
/var/www/html/programaciondam2526/.git/objects/bb/95a2d5d47d53e505807f725e089bdfac61df4c
/var/www/html/programaciondam2526/.git/objects/bb/4fc873d383343ff5e9369fc275b5c4877debcd
/var/www/html/programaciondam2526/.git/objects/3e/927bc386e357f8bcdc7ac59a6a49ced3e86ff7
/var/www/html/programaciondam2526/.git/objects/a5/a572dcb7e92013e90ee45d606cda6ecbb08271
/var/www/html/programaciondam2526/.git/objects/a5/e5b1d0e7229dfcb4ab37547ee48bc5ab1db161
/var/www/html/programaciondam2526/.git/objects/ed/575cf51df13927d5c639f8a0db22e9c1dae249
/var/www/html/programaciondam2526/.git/objects/ed/47eabd58ee303b2de149af3a43221a45344189
/var/www/html/programaciondam2526/.git/objects/33/4a3749a21b0b275065b5c294694aa350dfaddc
/var/www/html/programaciondam2526/.git/objects/01/ab91d9431c26600a11fc884491cd5e8261b974
/var/www/html/programaciondam2526/.git/objects/01/263a32d6a0b036a20981722a8337a0958c0166
/var/www/html/programaciondam2526/.git/objects/01/cee4624fc858d953eb6813d320b4dbe111b83b
/var/www/html/programaciondam2526/.git/objects/15/c7e3ecb73644c0f0376c66dc22405801a1e8fb
/var/www/html/programaciondam2526/.git/objects/15/c2e78c842e18ae6145bbd9f8346448f83ca8c7
/var/www/html/programaciondam2526/.git/objects/a3/7cd5baf4e52ee7866793b749687de15fb201be
/var/www/html/programaciondam2526/.git/objects/a3/8b7bc8e62766e92b40bebd0a172e5479a82daa
/var/www/html/programaciondam2526/.git/objects/a3/6ce66a05b908eeac1e87efcbe10b2c9d2cfd1a
/var/www/html/programaciondam2526/.git/objects/a3/b76e9beb9ce8703c6bb14ca55ff13298428b71
/var/www/html/programaciondam2526/.git/objects/22/3cf7f788066c4cefc32900b7dfd81d3c0ae995
/var/www/html/programaciondam2526/.git/objects/22/c05a3e0d6847ee951607b74af8fee47e6484e3
/var/www/html/programaciondam2526/.git/objects/00/b82a4d9be2b7d1bc53ec3bde32564f94de2716
/var/www/html/programaciondam2526/.git/objects/00/09eb8e24b8c2a5e6cc31a2d457418768c259c3
/var/www/html/programaciondam2526/.git/objects/35/ef16e53cf9271728cb7c5aeee4e1ae52de23bc
/var/www/html/programaciondam2526/.git/objects/35/ff20ffb4b31956f37d84ecca0f316381df60c8
/var/www/html/programaciondam2526/.git/objects/35/72fcfa0987e62fc686369881b360eb3684cd13
/var/www/html/programaciondam2526/.git/objects/35/89b539be622cbec73c6f2b67ad44a641c31be9
/var/www/html/programaciondam2526/.git/objects/35/3c980f9c3a2dfb41aa4c5aa2e565f86cfc9674
/var/www/html/programaciondam2526/.git/objects/35/3ef4d637cdaf3d79ed6ca46dff94bc77948c32
/var/www/html/programaciondam2526/.git/objects/c4/63ac01f88c426c9b8a6358e3f544d8c9b4aa05
/var/www/html/programaciondam2526/.git/objects/c4/f998db87069ad7254e847b4de43d8767a44562
/var/www/html/programaciondam2526/.git/objects/8c/213beea9fcd2db5852c0e4e8042d6dac73ee7e
/var/www/html/programaciondam2526/.git/objects/8c/a179d03587fe7bf2fa88bd5cd7674dfe1ae505
/var/www/html/programaciondam2526/.git/objects/8c/08fd3fd22988a528736002c665ff5487ee06bd
/var/www/html/programaciondam2526/.git/objects/8c/93691c900703cc65474b13925f32227d4c5d86
/var/www/html/programaciondam2526/.git/objects/c5/1dfbba3e5b81f72f867bb73bf2e9c4bc20e2d4
/var/www/html/programaciondam2526/.git/objects/06/e318d6b95f4853ebb453b94883cdf0632bc4c8
/var/www/html/programaciondam2526/.git/objects/06/c38788a579dfab048f05cd5be8cecbd8b5dd55
/var/www/html/programaciondam2526/.git/objects/06/8b53d8907c84b69822dd7acc8cc1e273369627
/var/www/html/programaciondam2526/.git/objects/06/28ff28ab9db1f8546eabb07ee1abb39466b3cc
/var/www/html/programaciondam2526/.git/objects/06/c07641ea823c49f5c682bd459cfc47b8996478
/var/www/html/programaciondam2526/.git/objects/06/c14926f200046123f1e4705bac90dc42740ad0
/var/www/html/programaciondam2526/.git/objects/c6/f2f65f262a816d96a5cb9a43d49378007f5d29
/var/www/html/programaciondam2526/.git/objects/81/918983325fcb1c564317cdfb4b8d9f23f04a3d
/var/www/html/programaciondam2526/.git/objects/1e/2a26d03b4ed038bc13e6c81fa8f60523bd009a
/var/www/html/programaciondam2526/.git/objects/1e/9bcaccb1a229c4ad6ab1121c2f524f104c9061
/var/www/html/programaciondam2526/.git/objects/1e/a1ab440e37f6c8b1ecc77737fccb558b9658d5
/var/www/html/programaciondam2526/.git/objects/28/5c129d063e85161e4531e49f320b43ab6fe6b6
/var/www/html/programaciondam2526/.git/objects/98/ecad0c56dff76910df0cc419c2c04c469690bf
/var/www/html/programaciondam2526/.git/objects/98/9021af1f8b15eba2519f0f53b215717b7258fd
/var/www/html/programaciondam2526/.git/objects/98/820ff75f7bfebf38e275406d9bac383f99acc2
/var/www/html/programaciondam2526/.git/objects/94/592749d1559c737355671491f7c88e4402a7c7
/var/www/html/programaciondam2526/.git/objects/94/628a2c12b1385d532641a19c6a4524d0c4e97a
/var/www/html/programaciondam2526/.git/objects/94/0ea58206eac9949370a6e1930adc7804dde5c0
/var/www/html/programaciondam2526/.git/objects/dc/e01cafc1a0ca5e6978c33c472149d859c0ad2d
/var/www/html/programaciondam2526/.git/objects/dc/ed79b1036447f1134da02aa4f8470ce9d29fbb
/var/www/html/programaciondam2526/.git/objects/24/daa5e42a71dac677d129760ddd9a7d9ad86be1
/var/www/html/programaciondam2526/.git/objects/24/4722a391c90125138c368a346aca61d16a914b
/var/www/html/programaciondam2526/.git/objects/24/646bde2f2a1d6e7fc0d235eab63ec67ee84efd
/var/www/html/programaciondam2526/.git/objects/71/40b2c88bc4154d15a8206e77e3edbd05a11f23
/var/www/html/programaciondam2526/.git/objects/71/0da1c1b0b69b99d3e83ae8185f882065efe147
/var/www/html/programaciondam2526/.git/objects/71/b0f0d2e2ed296373ef4913245264166c315908
/var/www/html/programaciondam2526/.git/objects/71/1c612351f684319938a7defcd8bc9e759c6aa7
/var/www/html/programaciondam2526/.git/objects/d1/fb293177557efd4f184cc9e192d8d4a107f0b1
/var/www/html/programaciondam2526/.git/objects/ea/08b34a406084b4f8dec53b0e652f5497bc7efe
/var/www/html/programaciondam2526/.git/objects/ea/873af148a57070133c6adba44c68273251e884
/var/www/html/programaciondam2526/.git/objects/ea/69c333990b764ca3c8a7248aa5c5282901e961
/var/www/html/programaciondam2526/.git/objects/ea/4c93b75a2902348586117cf018bba45b0b24f6
/var/www/html/programaciondam2526/.git/objects/a4/564eb5e18c8a5cb39be7c71b587ba6e18e1658
/var/www/html/programaciondam2526/.git/objects/a4/80b034a94363c30818cd58abd8b4455c3c6e39
/var/www/html/programaciondam2526/.git/objects/f6/c4c11a40492d6f5ccd0849d7709b833069604e
/var/www/html/programaciondam2526/.git/objects/51/e5f2a362d55d1b2192f5b40109c245987c3be9
/var/www/html/programaciondam2526/.git/objects/07/134b3002e83bb74e4d9297557d2803b05812a6
/var/www/html/programaciondam2526/.git/objects/07/11ee84cdb6be8fdc9ba21cb04704165a93c18c
/var/www/html/programaciondam2526/.git/objects/fc/8136c096643e4b00a58f60cbe9f9b02ae8fd85
/var/www/html/programaciondam2526/.git/objects/fc/09d14f0b2c28b38f9f8c5ccae692d3caba49cf
/var/www/html/programaciondam2526/.git/objects/fc/638d241c38ff6a1e5c4c9dcc1f0699adbd000b
/var/www/html/programaciondam2526/.git/objects/14/dab71047cda4716fcb69238e28d354cf67cc7a
/var/www/html/programaciondam2526/.git/objects/14/678b51cfaf8482c8be5a3c28062fdc823ec1fa
/var/www/html/programaciondam2526/.git/objects/14/bf2abdd399420218e109cb781e78b2e01e7558
/var/www/html/programaciondam2526/004-Desarrollo de clases/000-Resumen.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/Criterios de evaluacion.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/001-repaso gato.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/003-constructor con parametros.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/006-ejemplo con cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/002-a un construtor se le pueden pasar parametros.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/004-mas parametros.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/005-tercera propiedad.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/101-Ejercicios/007-listado de clientes.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/005-Creación de constructores/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/010-ejemplo practico.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/013-creo una lista de clientes.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/011-creo setters y getters.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/009-variable global.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/004-defino propiedad privada.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/005-Clase cuenta bancaria.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/008-validacion.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/012-pequeño programa.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/010-creo setters y getters.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/002-metodo set.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/007-get saldo.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/014-getters.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/003-metodo getter.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/006-convertir en privadas.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/101-Ejercicios/001-repaso de los metodos.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/004-Creación de métodos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/101-Ejercicios/002-clase madre animal.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/101-Ejercicios/004-herencia o multinivel.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/101-Ejercicios/003-clase Roca.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/101-Ejercicios/001-gatos y perros.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/007-Utilización de clases heredadas/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/002-las propiedades pueden ser arrays.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/011-le mostramos al usuario las opciones que tiene.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/004-leemos propiedad.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/013-estructura if.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/014-bucle infinito.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/003-escribir las propiedades de una clase.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/012-tomamos la entrada de usuario.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/001-Repaso de propiedades.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/006-aplicacion de productos.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/007-funciones y clases.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/009-pseudocodigo.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/008-creamos las variables globales.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/010-voy creando el codigo.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/005-los telefonos deben ser una lista.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/101-Ejercicios/015-desarrollo la insercion de producto.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/003-Creación de propiedades/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/006-Utilización de clases y objetos/101-Ejercicios/002-redondeos alza y baja.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/006-Utilización de clases y objetos/101-Ejercicios/001-Mi propia clase.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/006-Utilización de clases y objetos/101-Ejercicios/003-ahora uso la libreria estandar.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/006-Utilización de clases y objetos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/006-Utilización de clases y objetos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/004-le preguntamos al usuario.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/008-clase cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/001-listas.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/006-crud.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/005-leemos los datos del cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/007-crud insertar y listar.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/003-clase cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/101-Ejercicios/002-operaciones con listas.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/002-Estructura y miembros de una clase. Visibilidad/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/001-Introduccion.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/007-propiedades.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/004-ahora quiero crear otro gato.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/011-Paradigmas en programacion.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/009-objeto cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/008-introduccion a los metodos.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/002-clase gato.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/003-instanciamos un gato.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/005-Elementos principales de las clases.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/010-clase cliente.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/101-Ejercicios/006-propiedades y metodos.py
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/004-Desarrollo de clases/001-Concepto de clase/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/000-Resumen.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/Criterios de evaluacion.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/009-Tipos de datos colección/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/009-Tipos de datos colección/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/004-Creación de bases de datos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/004-Creación de bases de datos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/001-Bases de datos orientadas a objetos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/001-Bases de datos orientadas a objetos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/007-Recuperación, modificación y borrado de información/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/007-Recuperación, modificación y borrado de información/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/008-Tipos de datos objeto; atributos y métodos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/008-Tipos de datos objeto; atributos y métodos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/002-Características de las bases de datos orientadas a objetos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/002-Características de las bases de datos orientadas a objetos/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/006-El lenguaje de consultas sintaxis, expresiones, operadores/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/006-El lenguaje de consultas sintaxis, expresiones, operadores/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/005-Mecanismos de consulta/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/005-Mecanismos de consulta/001-Contenidos básicos/Contenidos básicos.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/003-Instalación del gestor de bases de datos/201-Criterios de evaluación/Criterios de evaluación.md
/var/www/html/programaciondam2526/008-Mantenimiento de la persistencia de los objetos/003-Instalación del gestor de bases de datos/001-Contenidos básicos/Contenidos básicos.md
```

<a id="creacion-y-eliminacion-de-ficheros-y-directorios"></a>
## Creación y eliminación de ficheros y directorios

En el mundo digital actual, la lectura y escritura de información son operaciones fundamentales que cualquier programa informático debe ser capaz de realizar con eficiencia. En esta subunidad didáctica, nos centramos en las técnicas específicas para crear y eliminar ficheros y directorios, dos aspectos cruciales del manejo de archivos en sistemas informáticos.

La creación de ficheros es un proceso que implica la generación de nuevos archivos con datos o información. En muchos lenguajes de programación, esta tarea se realiza mediante funciones o métodos específicos que permiten especificar el nombre y el contenido del archivo a crear. Por ejemplo, en Java, se puede utilizar la clase `FileWriter` para escribir texto en un nuevo fichero, mientras que en Python, la función incorporada `open()` con el modo 'w' permite crear un nuevo fichero y escribir en él.

Por otro lado, la eliminación de ficheros es una operación que requiere cuidado. Al eliminar un archivo, se pierde permanentemente su contenido a menos que se realice una copia previa. En Java, la clase `File` proporciona el método `delete()` para eliminar un fichero, mientras que en Python, la función `os.remove()` permite realizar esta tarea de manera sencilla.

La gestión de directorios es otro aspecto importante del manejo de archivos. Los directorios son contenedores que pueden almacenar otros directorios y ficheros, formando una estructura jerárquica. En Java, se puede utilizar la clase `File` para crear nuevos directorios con el método `mkdir()`, mientras que en Python, la función `os.mkdir()` cumple un papel similar.

Además de la creación y eliminación de archivos individuales, también es común trabajar con directorios enteros. En Java, la clase `File` ofrece métodos como `listFiles()` para obtener una lista de los ficheros y subdirectorios contenidos en un directorio, mientras que en Python, la función `os.listdir()` proporciona una funcionalidad similar.

La manipulación de directorios también implica la creación y eliminación de estructuras complejas. En Java, se puede utilizar la clase `File` para crear directorios anidados utilizando el método `mkdirs()`, mientras que en Python, la función `os.makedirs()` cumple un papel similar.

Es importante recordar que al trabajar con archivos y directorios, siempre es necesario manejar posibles excepciones. En Java, se pueden utilizar bloques try-catch para capturar y gestionar errores como la falta de permisos o el no existir del fichero o directorio. En Python, también se utilizan bloques try-except para manejar excepciones como `FileNotFoundError` o `PermissionError`.

La creación y eliminación de ficheros y directorios son operaciones esenciales que permiten la organización y gestión de información en sistemas informáticos. A través de estas técnicas, los programadores pueden crear estructuras de datos complejas, almacenar y recuperar información de manera eficiente, y mantener el orden en sus proyectos.

En resumen, la creación y eliminación de ficheros y directorios son habilidades fundamentales que cualquier programa informático debe dominar. A través de las funciones y métodos proporcionados por los lenguajes de programación, podemos realizar estas operaciones con facilidad y precisión, lo que nos permite organizar y gestionar información de manera eficiente en nuestros sistemas.

### crear carpeta

```python
import os

os.mkdir("micarpeta")
```

### eliminar carpeta

```python
import os

os.rmdir("micarpeta")
```

### no se puede crear una carpeta dos veces

```python
import os

os.mkdir("micarpeta")
```

### solucion al problema

```python
import os

try:
  os.mkdir("micarpeta")
except:
  print("Ha habido un error, continuamos")
```

### crear un archivo

```python
open("miarchivo.txt","w")
```

### eliminar archivo

```python
import os

# Hemos creado con:
# open("miarchivo.txt","w")

os.remove("miarchivo.txt")
```

### nuevo archivo con texto

```python
archivo = open("miarchivo.txt","w")

archivo.write("Esto es un texto de prueba que estoy escribiendo")
```

### comprimir

```python
import zipfile

origen = 'crmca_crmcapitol (1).sql'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w')
archivo.write(origen)
```

### algoritmo de compresion

```python
import zipfile

origen = 'crmca_crmcapitol (1).sql'

destino = 'basededatos.zip'

archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
archivo.write(origen)
```

### comprimir todos los arhivos de una carpeta

```python
import zipfile
import os

carpeta = "archivos"

for directorio, subcarpetas, archivos in os.walk(carpeta):
    for nombre_archivo in archivos:
        origen = os.path.join(directorio, nombre_archivo)
        destino = os.path.join(directorio, nombre_archivo + ".zip")
        archivo =  zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre_archivo)
```

### comprimir carpeta

```python
import os
import zipfile

origen = "archivos"
destino = "archivos.zip"

archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
for directorio, carpetas, archivos in os.walk(origen):
  for archivo in archivos:
    rutaarchivo = os.path.join(directorio, archivo)
    rutarelativa = os.path.relpath(rutaarchivo, origen)
    archivozip.write(rutaarchivo, rutarelativa)
    
archivozip.close()
```

### ejercicio final

```python
import os
import zipfile
import shutil

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales
'''

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Recorremos SOLO el primer nivel dentro de la ruta dada
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)

      # Evitar recomprimir ZIPs ya existentes
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue

      # Si es una carpeta: crear un ZIP con todo su contenido y luego eliminarla
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()
        shutil.rmtree(origen)

      # Si es un archivo: comprimirlo y luego eliminar el original
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()
        os.remove(origen)

except:
  print("Ha habido un error, continuamos")
```

### ampliacion

```python
import os
import zipfile
import shutil
import sys
import time

#### CUIDADO CON ESTE PROGRAMA
#### USALO BIEN
#### UN GRAN PODER CONLLEVA UNA GRAN RESPONSABILIDAD

'''
  Quiero:
  1.-Pedir al usuario una ruta de una carpeta con input
  2.-Repasar todas las subcarpetas y archivos dentro de esa carpeta
  3.-Para cada archivo o carpeta, quiero comprimirla en un ZIP
  4.-Una vez comprimido ese zip, quiero eliminar los contenidos originales (opcional con booleano)
  5.-Mostrar una barra de progreso en consola con porcentaje y estimación de tiempo
'''

# 1) Booleano para activar/desactivar el borrado de originales
borrar_originales = False  # ponlo a False para conservar los originales

# ---- Utilidades para la barra de progreso ----
def formatear_tiempo(segundos):
  segundos = int(segundos)
  h = segundos // 3600
  m = (segundos % 3600) // 60
  s = segundos % 60
  if h > 0:
    return f"{h:02d}:{m:02d}:{s:02d}"
  else:
    return f"{m:02d}:{s:02d}"

def mostrar_progreso(procesados, total, inicio):
  if total == 0:
    return
  porcentaje = (procesados / total)
  ancho_barra = 30
  rellenos = int(ancho_barra * porcentaje)
  barra = "[" + "#" * rellenos + "-" * (ancho_barra - rellenos) + "]"

  transcurrido = time.time() - inicio
  if procesados > 0:
    estimado_total = transcurrido / procesados * total
    restante = max(0, estimado_total - transcurrido)
  else:
    restante = 0

  texto = f"\r{barra} {porcentaje*100:6.2f}%  transcurrido: {formatear_tiempo(transcurrido)}  restante: {formatear_tiempo(restante)}"
  sys.stdout.write(texto)
  sys.stdout.flush()
# ---------------------------------------------

ruta = input("Introduce la ruta de la carpeta: ").strip()

try:
  # Comprobamos que la ruta existe y es una carpeta
  if not os.path.isdir(ruta):
    print("La ruta no es válida")
  else:
    # Preparamos la lista de ítems a procesar (solo primer nivel), excluyendo ZIPs
    items = []
    for nombre in os.listdir(ruta):
      origen = os.path.join(ruta, nombre)
      if os.path.isfile(origen) and origen.lower().endswith(".zip"):
        continue
      items.append(origen)

    total = len(items)
    procesados = 0
    inicio = time.time()
    mostrar_progreso(procesados, total, inicio)

    for origen in items:
      nombre = os.path.basename(origen)

      # Si es una carpeta: crear un ZIP con todo su contenido
      if os.path.isdir(origen):
        destino = origen + ".zip"
        archivozip = zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED)
        for directorio, subcarpetas, archivos in os.walk(origen):
          for archivo in archivos:
            rutaarchivo = os.path.join(directorio, archivo)
            rutarelativa = os.path.relpath(rutaarchivo, origen)
            archivozip.write(rutaarchivo, rutarelativa)
        archivozip.close()

        # Borrar carpeta original si está activado
        if borrar_originales:
          shutil.rmtree(origen)

      # Si es un archivo: comprimirlo
      elif os.path.isfile(origen):
        destino = origen + ".zip"
        archivo = zipfile.ZipFile(destino, 'w', compression=zipfile.ZIP_DEFLATED)
        archivo.write(origen, arcname=nombre)
        archivo.close()

        # Borrar archivo original si está activado
        if borrar_originales:
          os.remove(origen)

      # Actualizamos progreso
      procesados += 1
      mostrar_progreso(procesados, total, inicio)

    print()  # salto de línea al terminar la barra
    print("Proceso completado.")

except:
  print("\nHa habido un error, continuamos")
```

<a id="entrada-desde-teclado-salida-a-pantalla-formatos-de-visualizacion"></a>
## Entrada desde teclado. Salida a pantalla. Formatos de visualización

En el mundo digital, la capacidad de interactuar con los usuarios es fundamental para cualquier programa informático. La lectura desde teclado y la salida a pantalla son dos operaciones fundamentales que permiten esta comunicación. Comenzamos por entender cómo capturar información directamente del usuario, un proceso conocido como entrada.

La entrada desde teclado es una de las formas más comunes de interactuar con los usuarios en aplicaciones informáticas. Este proceso implica la recopilación de datos introducidos por el usuario a través del teclado y su posterior procesamiento por parte del programa. La lectura de datos desde el teclado puede ser realizada utilizando funciones específicas proporcionadas por diferentes lenguajes de programación, como `input()` en Python o `Scanner` en Java.

Es importante destacar que la entrada desde teclado no es solo una operación técnica; también implica un aspecto ético y legal. Los programas deben respetar la privacidad del usuario y garantizar que los datos introducidos sean seguros y confidenciales. Por lo tanto, es crucial implementar medidas de seguridad adecuadas para proteger la información proporcionada por el usuario.

La salida a pantalla, por otro lado, es el proceso inverso a la entrada. Consiste en mostrar información al usuario de manera visual, facilitando su comprensión y toma de decisiones. En Python, esta operación se realiza con la función `print()`, mientras que en Java se utiliza `System.out.println()`.

La forma en que se presenta la información en pantalla es crucial para la experiencia del usuario. Los formatos de visualización juegan un papel fundamental en cómo los datos son presentados y comprensibles. Por ejemplo, el uso de tablas, listas o gráficos puede facilitar la interpretación de grandes cantidades de información.

Además de mostrar información de manera clara y ordenada, es importante considerar la accesibilidad en la salida a pantalla. Esto significa asegurarse de que los usuarios con discapacidades visuales puedan interactuar con el programa sin dificultades. La utilización de colores contrastantes, leyendas legibles y elementos gráficos intuitivos son aspectos clave para garantizar una experiencia inclusiva.

La lectura desde teclado y la salida a pantalla no son solo operaciones técnicas; también son fundamentales para construir relaciones con los usuarios. Un programa que puede comunicarse eficazmente con el usuario es más probable de ser utilizado y satisfactorio. Por lo tanto, es crucial dedicar tiempo y esfuerzo a diseñar interfaces de usuario intuitivas y amigables.

En conclusión, la lectura desde teclado y la salida a pantalla son operaciones esenciales en cualquier programa informático. No solo permiten la interacción con los usuarios, sino que también contribuyen significativamente a su experiencia y satisfacción. Al entender estos conceptos y aplicarlos de manera efectiva, se puede crear software más robusto y accesible para todos los usuarios.

### Examen de final de trimestre

```markdown
CRUD en Python (No SQL)
Clases

1.-Presentará una pantalla de bienvenida
2.-Ofrecerá al usuario 4 opciones (Crear, Leer, Actualizar, Eliminar)
3.-Habrá que definir una clase en base a una entidad que os proporcionaré - no métodos set y get, acceso directo
4.-Las entidades se guardarán como objetos en memoria
5.-Las entidades persistirán en disco usando pickle
```

### creamos una clase

```python
class Cliente():
  
```

### creamos un constructor

```python
class Cliente():
  def __init__(self):
    
```

### el constructor tiene parametros

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email
```

### pantalla de bienvenida

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")
```

### bucle infinito

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

while True:
  
```

### creamos lista de entidades

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  
```

### creamos menu

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
```

### atrapamos las opciones con if

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
    
```

### desarrollamos insertar

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
    
```

### apendizamos

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
    
```

### pass de momento

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    pass
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### desarrollo leer

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    for cliente in clientes:
      print(cliente)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### imprimimos mejor el cliente

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    for cliente in clientes:
      print(cliente.nombre,cliente.apellidos,cliente.email)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### actualizar es como insertar pero con id

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    for cliente in clientes:
      print(cliente.nombre,cliente.apellidos,cliente.email)
  elif opcion == 3:
    identificador = input("Introduce el id para modificar: ")
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
    pass
  elif opcion == 4:
    pass
```

### chivamos el id

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    pass
```

### eliminar elemento

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    clientes.splice(identificador,1)
```

### confirmacion

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ")
    if confirmacion == "S":
      clientes.splice(identificador,1)
    elif confirmacion == "N":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### mayusculas minusculas

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ")
    if confirmacion == "S" or confirmacion == "s":
      clientes.splice(identificador,1)
    elif confirmacion == "N" or confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### lower

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      clientes.splice(identificador,1)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### cambiamos splice por pop

```python
class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      clientes.pop(identificador)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### guardamos con pickle

```python
import pickle

class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []


while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      clientes.pop(identificador)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### cargo registros si existen

```python
import pickle

class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

try:  #### Ojo que igual no existe el archivo ######
  archivo = open("clientes.dat",'rb')
  clientes = pickle.load(archivo)
except:
  print("No existe archivo de datos")

while True:
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      clientes.pop(identificador)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
```

### guardamos

```python
import pickle

class Cliente():
  def __init__(self,nombre,apellidos,email):
    self.nombre = nombre
    self.apellidos = apellidos
    self.email = email

print("###### Gestión de clientes v0.1 ######")
print("####### Jose Vicente Carratala  ######")

clientes = []

try:  #### Ojo que igual no existe el archivo ######
  archivo = open("clientes.bin",'rb')
  clientes = pickle.load(archivo)
  archivo.close()
except:
  print("No existe archivo de datos")

while True:
  archivo = open("clientes.bin",'wb')
  pickle.dump(clientes,archivo)
  archivo.close()
  
  print("Escoge una opción:")
  print("1.-Insertar un cliente")
  print("2.-Listar clientes")
  print("3.-Actualizar un cliente")
  print("4.-Eliminar un cliente")
  opcion = int(input("Escoge una opcion: "))
  
  if opcion == 1:
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes.append(Cliente(nombre,apellidos,email))
  elif opcion == 2:
    identificador = 0
    for cliente in clientes:
      print("Este es el cliente con ID:",identificador)
      print(cliente.nombre,cliente.apellidos,cliente.email)
      identificador += 1
  elif opcion == 3:
    identificador = int(input("Introduce el id para modificar: "))
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce los apellidos: ")
    email = input("Introduce el email: ")
    clientes[identificador].nombre = nombre
    clientes[identificador].apellidos = apellidos
    clientes[identificador].email = email
  elif opcion == 4:
    identificador = int(input("Introduce el id para eliminar: "))
    confirmacion = input("¿Estás seguro? (S/N): ").lower()
    if confirmacion == "s":
      clientes.pop(identificador)
    elif confirmacion == "n":
      print("Cancelado")
    else:
      print("Opción no válida")
  
```

### argumentos de terminal

```python
import sys

edad = int(sys.argv[1])
print("El doble de tu edad es:",(edad*2))
```

<a id="interfaces-graficas"></a>
## Interfaces gráficas

En el mundo digital actual, las interfaces gráficas desempeñan un papel crucial en la interacción entre los usuarios y los sistemas informáticos. Estas interfaces no solo facilitan la navegación y la manipulación de datos, sino que también contribuyen a mejorar significativamente la experiencia del usuario final.

La creación de interfaces gráficas es una habilidad fundamental para cualquier programador o desarrollador de software. Esta carpeta del contenido aborda los aspectos teóricos y prácticos necesarios para diseñar e implementar interfaces gráficas efectivas. Comenzamos por explorar los conceptos básicos, como las clases y propiedades que definen la estructura y el comportamiento de los componentes visuales.

A medida que avanzamos en esta sección, nos sumergimos en la creación de eventos y asociaciones de acciones a estos mismos. Los eventos son acciones específicas que ocurren dentro de la interfaz gráfica, como hacer clic en un botón o seleccionar un elemento del menú. Asociar acciones a estos eventos permite al programador responder de manera dinámica a las interacciones del usuario.

La persistencia es otro aspecto crucial en el desarrollo de interfaces gráficas. Es importante que los cambios realizados por el usuario se reflejen adecuadamente en la interfaz, y que esta pueda ser recuperada en caso de un reinicio o pérdida de datos. La carpeta también aborda técnicas avanzadas para gestionar la persistencia de componentes, asegurando que la información no se pierda.

Además, el contenido explora la creación de interfaces naturales de usuario (NUI), una área emergente que busca hacer que las interfaces sean más intuitivas y accesibles. Esto implica el uso de tecnologías como la voz y el movimiento del cuerpo para interactuar con los sistemas, así como la realidad aumentada.

La carpeta también incluye información sobre la documentación de aplicaciones, un aspecto fundamental para mantener el código legible y mantenible a largo plazo. Se abordan herramientas gráficas integradas en el IDE y externas al mismo, proporcionando una visión completa del proceso de creación de documentación.

Finalmente, se trata de la distribución de aplicaciones, un tema que aborda desde la empaquetación hasta la firma digital y las canales de distribución. La carpeta ofrece una guía práctica sobre cómo crear instaladores y paquetes autoinstalables, asegurando que los usuarios puedan instalar y usar la aplicación con facilidad.

En resumen, esta carpeta del contenido proporciona un enfoque integral al desarrollo de interfaces gráficas, desde sus fundamentos hasta técnicas avanzadas y prácticas recomendadas. Cada párrafo se desarrolla continuamente, ofreciendo una visión coherente y detallada del proceso de creación e implementación de interfaces gráficas en aplicaciones informáticas.

### tkinter

```python
# sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

ventana.mainloop() # No te salgas
```

### creamos un boton

```python
# sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves").pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### command en el boton

```python
# sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### definimos accion

```python
# sudo apt-get install python3-tk
import tkinter as tk

def accion():
  print("Has pulsado el boton")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### ponemos una etiqueta

```python
# sudo apt-get install python3-tk
import tkinter as tk

def accion():
  print("Has pulsado el boton")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el botón?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### salida en pantalla

```python
# sudo apt-get install python3-tk
import tkinter as tk

def accion():
  etiqueta.config(text="Pues sí que has pulsado el botón")

ventana = tk.Tk()

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el botón?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### microcalculadura

```python
# sudo apt-get install python3-tk
import tkinter as tk

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular!")
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Aqui va el resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

### calcular

```python
# sudo apt-get install python3-tk
import tkinter as tk

def calcular():
  op1valor = float(operando1.get())
  op2valor = float(operando2.get())
  suma = op1valor + op2valor
  resultado.config(text=str(suma))

ventana = tk.Tk()

operando1 = tk.Entry()
operando1.pack(padx=10,pady=10)

operando2 = tk.Entry()
operando2.pack(padx=10,pady=10)

boton = tk.Button(text="Calcular!",command=calcular)
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Aqui va el resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # No te salgas
```

<a id="concepto-de-evento"></a>
## Concepto de evento

En el vasto universo de la programación, los eventos son una parte fundamental que permite a las aplicaciones interactuar con el usuario y su entorno. Un evento es cualquier cosa que ocurre en un programa o en el sistema operativo que puede ser detectada por el software para realizar alguna acción. Estos pueden ser acciones del usuario como hacer clic en un botón, escribir texto en una caja de entrada o incluso cambios en la red.

La comprensión y manejo de eventos es crucial para desarrollar interfaces gráficas de usuario (GUI) interactivas y responsivas. Cada evento tiene asociado un manejador que define qué debe hacerse cuando el evento ocurre. Por ejemplo, si se hace clic en un botón, el manejador del evento puede ejecutar una función que cambia la interfaz o realiza alguna operación.

Los eventos pueden ser de diferentes tipos, como eventos de entrada (como teclas presionadas), eventos de salida (como el cierre de una ventana) y eventos de red (como la llegada de datos). Cada tipo de evento tiene sus propias características y manejadores específicos que permiten al programador controlar su comportamiento.

La gestión eficiente de los eventos es esencial para mantener la fluidez y la responsividad de las aplicaciones. Algunos lenguajes de programación, como Java o C#, tienen mecanismos incorporados para manejar eventos de manera sencilla y segura. Estas herramientas proporcionan clases y métodos que facilitan el registro de manejadores de eventos y la propagación de los mismos.

Además de los eventos generados por el usuario, también existen eventos internos del sistema operativo que pueden ser relevantes para una aplicación. Por ejemplo, un evento puede ocurrir cuando se cambia el tamaño de la ventana principal de una aplicación, lo cual puede requerir ajustes en la disposición de los elementos gráficos.

La programación orientada a objetos (OOP) es especialmente útil para manejar eventos, ya que permite encapsular el comportamiento relacionado con un evento dentro de una clase. Esto facilita la organización del código y hace más fácil mantener y escalar las aplicaciones.

En resumen, los eventos son un componente esencial en la programación moderna, permitiendo a las aplicaciones interactuar dinámicamente con el usuario y su entorno. La comprensión de cómo crear, manejar y propagar eventos es fundamental para desarrollar interfaces gráficas interactivas y responsivas. A través del uso adecuado de manejadores de eventos y técnicas orientadas a objetos, los programadores pueden crear aplicaciones que respondan eficazmente a las acciones del usuario y proporcionen una experiencia óptima.

### recordamos

```python
import tkinter as tk

ventana = tk.Tk()

ventana.mainloop()
```

### creo un marco

```python
import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=20,pady=20)

marco.pack(padx=20,pady=20)

ventana.mainloop()
```

### creo un entry

```python
import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

# DNI NIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)

# NOMBRE
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)

# APELLIDOS
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)

# EMAIL
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)

marco.pack(padx=20,pady=20)

ventana.mainloop()
```

### creo un boton

```python
import tkinter as tk

ventana = tk.Tk()

marco = tk.Frame(ventana)

# DNI NIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)

# NOMBRE
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)

# APELLIDOS
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)

# EMAIL
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)

# Boton
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)

marco.pack(padx=20,pady=20)

ventana.mainloop()
```

### funcion de insertar

```python
import tkinter as tk

ventana = tk.Tk()

def insertar():
  print("Vamos a insertar un cliente")

marco = tk.Frame(ventana)

# DNI NIE
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)

# NOMBRE
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)

# APELLIDOS
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)

# EMAIL
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)

# Boton
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)

marco.pack(padx=20,pady=20)

ventana.mainloop()
```

### mysql

```python
# pip3 install mysql-connector-python --break-system-packages
# sudo apt install libmysqlclient-dev python3-mysql.connector
# solo si da error de ssl en socket:
# pip3 install --user --upgrade mysql-connect-python --break-system-packages
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  INSERT INTO clientes
  VALUES(
    NULL,
    "12345678Z",
    "Jose Vicente",
    "Carratala Sanchis",
    "info@jocarsa.com"
  );
''')
conexion.commit()
cursor.close()
conexion.close()
```

### crear usuario

```sql
-- crea usuario nuevo con contraseña
CREATE USER 
'empresadam'@'localhost' 
IDENTIFIED  BY 'Empresadam123$';
-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'empresadam'@'localhost';
-- quitale todos los limites que tenga
ALTER USER 'empresadam'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON `empresadam`.* 
TO 'empresadam'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```

### seleccionar

```sql
SELECT * FROM clientes;
```

### insertar en base de datos

```python
import tkinter as tk
import mysql.connector
conexion = mysql.connector.connect(host="localhost",user="empresadam",password="Empresadam123$",database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
def insertar():
  cursor.execute('''
    INSERT INTO clientes
    VALUES(
      NULL,
      "'''+dninie.get()+'''",
      "'''+nombre.get()+'''",
      "'''+apellidos.get()+'''",
      "'''+email.get()+'''"
    );
  ''')
  conexion.commit()
marco = tk.Frame(ventana)
tk.Label(marco,text="Introduce el dni/nie del cliente").pack(padx=10,pady=10)
dninie = tk.Entry(marco)
dninie.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el nombre del cliente").pack(padx=10,pady=10)
nombre = tk.Entry(marco)
nombre.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce los apellidos del cliente").pack(padx=10,pady=10)
apellidos = tk.Entry(marco)
apellidos.pack(padx=10,pady=10)
tk.Label(marco,text="Introduce el email del cliente").pack(padx=10,pady=10)
email = tk.Entry(marco)
email.pack(padx=10,pady=10)
tk.Button(marco,text="Insertar cliente",command = insertar).pack(padx=10,pady=10)
marco.pack(padx=20,pady=20)
ventana.mainloop()
```

### leer de base de datos

```python
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()
cursor.execute('''
  SELECT * FROM clientes;
''')

filas = cursor.fetchall()

for fila in filas:
  print(fila)
  
cursor.close()
conexion.close()
```

### pintamos tablas

```python
import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()


arbol = ttk.Treeview(ventana, columns=("nombre", "apellidos"), show="headings")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")

arbol.insert("", "end", values=("Jose Vicente", "Carratala"))
arbol.insert("", "end", values=("Juan", "García Lopez"))

arbol.pack(padx=20,pady=20)

ventana.mainloop()
```

### frankenstein

```python
import tkinter as tk
from tkinter import ttk
import mysql.connector
conexion = mysql.connector.connect(host="localhost",user="empresadam",password="Empresadam123$",database="empresadam")
cursor = conexion.cursor()
ventana = tk.Tk()
arbol = ttk.Treeview(ventana, columns=("dninie","nombre", "apellidos","email"), show="headings")
arbol.heading("dninie", text="DNI del cliente")
arbol.heading("nombre", text="Nombre del cliente")
arbol.heading("apellidos", text="Apellidos del cliente")
arbol.heading("email", text="Email del cliente")
cursor.execute('''SELECT * FROM clientes;''')
filas = cursor.fetchall()
for fila in filas:
  arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

arbol.pack(padx=20,pady=20)

ventana.mainloop()
```

### unir con IA

```python
# pip3 install ttkbootsrap --break-system-packages
import tkinter as tk
from tkinter import ttk
import mysql.connector
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# --- Database connection ---
conexion = mysql.connector.connect(
    host="localhost",
    user="empresadam",
    password="Empresadam123$",
    database="empresadam"
)
cursor = conexion.cursor()

# --- Main window setup ---
ventana = tb.Window(themename="superhero")  # try also: "minty", "flatly", "darkly"
ventana.title("Gestión de Clientes")
ventana.geometry("800x600")

# --- Frames layout ---
frame_form = ttk.LabelFrame(ventana, text="Nuevo cliente", padding=20)
frame_form.pack(fill=X, padx=20, pady=10)

frame_tabla = ttk.LabelFrame(ventana, text="Lista de clientes", padding=20)
frame_tabla.pack(fill=BOTH, expand=True, padx=20, pady=10)

# --- Form fields ---
def insertar():
    dni = dninie.get()
    nom = nombre.get()
    ape = apellidos.get()
    ema = email.get()

    if dni == "" or nom == "" or ape == "" or ema == "":
        tb.dialogs.Messagebox.show_warning("Por favor, completa todos los campos", title="Atención")
        return

    cursor.execute('''
        INSERT INTO clientes VALUES (NULL, %s, %s, %s, %s);
    ''', (dni, nom, ape, ema))
    conexion.commit()
    cargar_datos()
    tb.dialogs.Messagebox.show_info("Cliente insertado correctamente", title="Éxito")

    # Limpiar campos
    dninie.delete(0, tk.END)
    nombre.delete(0, tk.END)
    apellidos.delete(0, tk.END)
    email.delete(0, tk.END)

# Form fields (left to right layout)
ttk.Label(frame_form, text="DNI/NIE:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
dninie = ttk.Entry(frame_form, width=20)
dninie.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=5, pady=5, sticky=W)
nombre = ttk.Entry(frame_form, width=20)
nombre.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_form, text="Apellidos:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
apellidos = ttk.Entry(frame_form, width=20)
apellidos.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Email:").grid(row=1, column=2, padx=5, pady=5, sticky=W)
email = ttk.Entry(frame_form, width=20)
email.grid(row=1, column=3, padx=5, pady=5)

ttk.Button(frame_form, text="Insertar cliente", command=insertar, bootstyle=SUCCESS).grid(
    row=0, column=4, rowspan=2, padx=10, pady=5, sticky=NS
)

# --- Treeview setup ---
columnas = ("dninie", "nombre", "apellidos", "email")
arbol = ttk.Treeview(frame_tabla, columns=columnas, show="headings", bootstyle=INFO)
for col in columnas:
    arbol.heading(col, text=col.capitalize())
    arbol.column(col, width=180, anchor=W)

# Scrollbars
scroll_y = ttk.Scrollbar(frame_tabla, orient=VERTICAL, command=arbol.yview)
scroll_x = ttk.Scrollbar(frame_tabla, orient=HORIZONTAL, command=arbol.xview)
arbol.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

arbol.grid(row=0, column=0, sticky=NSEW)
scroll_y.grid(row=0, column=1, sticky=NS)
scroll_x.grid(row=1, column=0, sticky=EW)

frame_tabla.rowconfigure(0, weight=1)
frame_tabla.columnconfigure(0, weight=1)

# --- Function to load data into the table ---
def cargar_datos():
    cursor.execute("SELECT * FROM clientes;")
    filas = cursor.fetchall()
    arbol.delete(*arbol.get_children())
    for fila in filas:
        arbol.insert("", "end", values=(fila[1], fila[2], fila[3], fila[4]))

# --- Initial load ---
cargar_datos()

ventana.mainloop()
```

<a id="creacion-de-controladores-de-eventos"></a>
## Creación de controladores de eventos

En el mundo digital, la interacción con los usuarios es fundamental para cualquier aplicación o sistema informático. La creación de controladores de eventos representa un paso crucial en este proceso, permitiendo que las aplicaciones respondan a acciones específicas realizadas por los usuarios, como clics de ratón, pulsaciones de teclado o cambios en el estado de una interfaz gráfica.

El concepto de controlador de eventos es sencillo pero poderoso. Es un mecanismo que permite asociar funciones o métodos con ciertas acciones dentro de la aplicación. Cada vez que ocurre un evento, como hacer clic en un botón, el sistema identifica cuál es el controlador asociado y ejecuta la función correspondiente.

La creación de controladores de eventos implica varios pasos. Primero, se debe definir la acción que desencadenará el evento. Esto puede ser algo tan simple como hacer clic en un botón o tan complejo como mover el cursor sobre una imagen. Luego, se necesita escribir la función que será ejecutada cuando ocurra este evento. Esta función puede realizar cualquier operación necesaria, desde actualizar los datos de una interfaz hasta enviar información a otro sistema.

La importancia de esta práctica radica en su capacidad para hacer que las aplicaciones sean interactivas y dinámicas. Sin controladores de eventos, las aplicaciones serían estáticas e ininteractivas, limitando significativamente su utilidad y experiencia del usuario. Por ejemplo, en una aplicación de gestión de tareas, el controlador de eventos asociado a un botón "Marcar como completada" permitiría que los usuarios cambien el estado de una tarea sin necesidad de recargar la página o navegar a otra sección.

Además, la creación de controladores de eventos es una práctica fundamental para el desarrollo orientado a objetos. En este paradigma, las clases pueden definir métodos que actúan como controladores de eventos, lo que permite una organización lógica y modular del código. Cada clase puede tener sus propios métodos que responden a eventos específicos, facilitando la mantenibilidad y escalabilidad del proyecto.

Es importante destacar que el proceso de creación de controladores de eventos no es siempre inmediato o intuitivo. Requiere una comprensión profunda de cómo funcionan los eventos en el contexto específico de la aplicación y las herramientas utilizadas para desarrollarla. Además, puede ser necesario manejar situaciones complejas, como eventos anidados o múltiples eventos asociados a un solo controlador.

En resumen, la creación de controladores de eventos es una habilidad esencial en el desarrollo de aplicaciones informáticas. Permite hacer que las interfaces sean interactivas y dinámicas, mejorando significativamente la experiencia del usuario. A través de este proceso, los desarrolladores pueden asociar acciones específicas con eventos, permitiendo que las aplicaciones respondan de manera eficiente a las interacciones del usuario, lo que es crucial para el éxito de cualquier proyecto informático.

<a id="simulacro-examen-miercoles"></a>
## - Simulacro examen miercoles

### comenzamos

```python
print("Bienvenidos a la aplicacion")

print("Selecciona una opcion:")
print("1.-Crear un registro")
print("2.-Listar registros")
print("3.-Actualiar registro")
print("4.-Eliminar registro")
```

### bucle infinito

```python
print("Bienvenidos a la aplicacion")

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
```

### if elif

```python
print("Bienvenidos a la aplicacion")

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
  
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
  
```

### mysql conexion

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
  
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
  
```

### conexion y cursor

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
  
  elif opcion == 2:
  
  elif opcion == 3:
  
  elif opcion == 4:
  
```

### seleccionamos

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    pass
  elif opcion == 2:
    cursor = conexion.cursor()
    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### ahora insertar

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas VALUES (
      NULL,
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+imagen+'''",
      "'''+url+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
  elif opcion == 2:

    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    pass
  elif opcion == 4:
    pass
```

### eliminar

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas VALUES (
      NULL,
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+imagen+'''",
      "'''+url+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
  elif opcion == 2:

    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    pass
  elif opcion == 4:
    identificador = input("Introduce el id a eliminar: ")
    cursor.execute('''
      DELETE FROM Piezas
      WHERE Identificador = '''+identificador+'''
    ''')
    conexion.commit()
```

### actualizar

```python
import mysql.connector

print("Bienvenidos a la aplicacion")

conexion = mysql.connector.connect(
  host="localhost",
  user="portafolioceac",
  password="portafolioceac",
  database="portafolioceac"
  )
cursor = conexion.cursor()

while True:
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      INSERT INTO Piezas VALUES (
      NULL,
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+imagen+'''",
      "'''+url+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
  elif opcion == 2:

    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    filas = cursor.fetchall()

    for fila in filas:
      print(fila)
  elif opcion == 3:
    identificador = input("Introduce el id a actualizar: ")
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    imagen = input("Introduce la imagen: ")
    url = input("Introduce la url: ")
    id_categoria = input("Introduce la categoria: ")
    cursor.execute('''
      UPDATE Piezas SET 
      titulo = "'''+titulo+'''",
      descripcion = "'''+descripcion+'''",
      imagen = "'''+imagen+'''",
      url = "'''+url+'''",
      id_categoria = '''+id_categoria+'''
      WHERE Identificador = '''+identificador+''';
    ''')
    conexion.commit()
  elif opcion == 4:
    identificador = input("Introduce el id a eliminar: ")
    cursor.execute('''
      DELETE FROM Piezas
      WHERE Identificador = '''+identificador+'''
    ''')
    conexion.commit()
```

<a id="ejercicio-de-final-de-unidad-4"></a>
## Ejercicio de final de unidad

### Holamundo

```python
print("Hola mundo desde Python")
```

### variables

```python
nombre = "Jose Vicente"
edad = 47
```

### salidas

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)
```

### variar una variable

```python
nombre = "Jose Vicente"
print("Mi nombre es",nombre)

nombre = "Juan"
print("Mi nombre es",nombre)
```

### identificadores permitidos

```python
nombre = "Jose"
nombre2 = "Vicente"
# 2nombre = "Jose Vicente"
nombre_completo = "Jose Vicente"
#nombre-completo = "Jose Vicente"
#nombre completo = "Jose Vicente"
nombreCompleto = "Jose Vicente" # Es legal pero no se recomienda
```

### comentarios

```python
# Esto es un comentario de una única línea

'''
    Esto es un comentario
    Esto sigue siendo un comentario
    Y esto también lo es
'''
```

### Explicacion del codigo

```python
edad = 47
# edad es el identificador
# = es el operador de asignación
# 47 es el valor literal que se es está asignando al identificador
```

### Tipos de datos

```python
nombre = "Jose Vicente" # Cadena
edad = 47 # Entero
altura = 1.78 # Decimal
vivo = True # Booleano
```

### Entradas

```python
nombre = input("Dime tu nombre: ")
print("Tu nombre es: ",nombre)
```

### Entrada y problema

```python
edad = input("Dime tu edad: ")
print("El doble de tu edad es: "+edad)
```

### Cambio de tipo de dato

```python
# Le pregunto al usuario por su edad
edad = input("Dime tu edad: ")
# Me aseguro de convertir la edad a un número entero
entero = int(edad)
# Calculo el doble de un número entero
doble = entero*2
# Saco el resultado por pantalla
print("El doble de tu edad es: "+doble)
```

### literales

```python
nombre = "Jose Vicente"
# Jose Vicente es el literal, y es de tipo cadena

edad = 47
# 47 es el literal, y es de tipo entero
```

### constantes

```python
PI = 3.1415

print("PI vale",PI)

PI = 4 # Le cambio el valor a PI

print("PI vale",PI)
# Las constantes deben formularse con mayúsculas
# Las variables deben formularse con minúsculas
```

### Diferencia

```python

# La constante es PI
# El literal es 3.1416

PI = 3.1416

PI = "unnumero"
```

### operadores aritmeticos

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores arimeticos abreviados

```python
edad = 47
# Le quiero sumar dos unidades
edad = edad + 2
edad += 2
#Le quiero restar dos unidades
edad = edad - 2
edad -= 2
# Lo quiero multiplicar por dos
edad = edad * 2
edad *= 2
# Lo quiero dividir por dos
edad = edad / 2
edad /= 2
```

### operadores booleanos

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### Ejercicio1-Calculadora de impuestos

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculadora

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = input("Introduce la base imponible de la factura: ")
```

### Calculo de IVA

```python
'''
    Calculadora de Impuestos
    v0.1 por Jose Vicente Carratalá
    Funcionamiento: Introduce una base imponible y se calcula IVA y total
'''

# Este programa no tiene importaciones

# Creo variables
base_imponible = 0
total_iva = 0
total_factura = 0

# Aquí pondría las funciones/clases

# Ahora calculamos

# Primero pido una entrada
print("Programa calculadora de impuestos")
print("(c) 2025 Jose Vicente Carratalá")
print("Introduce una base y te calculo el IVA y el total")
base_imponible = float(input("Introduce la base imponible de la factura: "))

# Luego realizo cálculos
total_iva = base_imponible*0.21
total_factura = base_imponible + total_iva

# Por último expreso una salida
print("El IVA de la factura es: ",total_iva)
print("El total de la factura es: ",total_factura)
```

<a id="examen-final"></a>
## Examen final

### crear tablas

```sql
CREATE DATABASE portafolioceac;

USE portafolioceac;


CREATE TABLE Piezas(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255),
  imagen VARCHAR(255),
  url VARCHAR(255),
  id_categoria INT
);

CREATE TABLE Categorias(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255)
);
```

### insertar

```sql
INSERT INTO Categorias VALUES(
  NULL,
  'General',
  'Esta es la categoria general'
);

INSERT INTO Piezas VALUES(
  NULL,
  'Primera pieza',
  'Esta es la descripcion de la primera pieza',
  'josevicente.jpg',
  'https://jocarsa.com',
  1
);
```

### fk

```sql
ALTER TABLE Piezas
ADD CONSTRAINT fk_piezas_categorias
FOREIGN KEY (id_categoria) REFERENCES Categorias(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

### selecciones

```sql
SELECT * FROM Categorias;

SELECT * FROM Piezas;
```

### left join

```sql
SELECT 
* 
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;
```

### ahora creo la vista

```sql
CREATE VIEW piezas_y_categorias AS 
SELECT 
Categorias.titulo AS categoriatitulo,
Categorias.descripcion AS categoriadescripcion,
Piezas.titulo AS piezatitulo,
Piezas.descripcion AS piezadescripcion,
imagen,
url
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;

SELECT * FROM piezas_y_categorias;
```

### usuario

```sql
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'portafolioceac'@'localhost' 
IDENTIFIED  BY 'portafolioceac';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolioceac.* 
TO 'portafolioceac'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```

<a id="carpeta-sin-titulo"></a>
## Carpeta sin título

En el vasto universo de la programación, una parte fundamental es la lectura y escritura de información, un proceso que permite a los programas interactuar con el mundo exterior. Esta carpeta del contenido nos guía a través de las técnicas y herramientas necesarias para manejar eficazmente estos flujos de datos.

Empezamos por entender los conceptos básicos de flujos de datos. En programación, un flujo es una secuencia de bytes que se mueven entre diferentes partes del sistema. Los flujos pueden ser de entrada (lectura) o salida (escritura), y son fundamentales para la interacción con dispositivos como archivos, dispositivos de red y dispositivos de entrada/salida.

La lectura de información es un proceso que implica abrir un flujo de entrada, leer los datos disponibles y luego cerrar el flujo. En programación, esto se realiza a través de clases y métodos específicos para manejar diferentes tipos de flujos. Por ejemplo, en Java, la clase `FileInputStream` se utiliza para leer bytes desde un archivo.

Por otro lado, la escritura de información es igualmente importante. Implica abrir un flujo de salida, escribir los datos deseados y luego cerrar el flujo. En Python, por ejemplo, la función `open()` con el modo 'w' (write) permite crear un nuevo archivo o truncar uno existente para escritura.

La manipulación de ficheros es una técnica poderosa que permite guardar y recuperar datos persistentemente. Los ficheros pueden ser de diferentes tipos: texto plano, binarios, XML, JSON, etc. Cada tipo tiene sus propias características y métodos de lectura y escritura específicos.

Además de los ficheros, las bases de datos también son un medio común para almacenar información persistente. La programación orientada a objetos permite interactuar con bases de datos mediante clases y objetos que representan tablas y registros. Herramientas como Hibernate en Java o Entity Framework en C# facilitan esta tarea, proporcionando métodos para insertar, actualizar y eliminar datos.

La lectura y escritura de información también se extiende a la manipulación de estructuras de datos complejas como matrices, listas y diccionarios. Estas estructuras permiten almacenar y recuperar grandes cantidades de datos de manera eficiente, utilizando métodos específicos para cada tipo.

La importancia de la lectura y escritura de información no se limita a los ficheros y las bases de datos. También es crucial en la comunicación entre aplicaciones, donde los datos se transmiten a través de sockets o interfaces web. En estos casos, el proceso de lectura y escritura se realiza a nivel de bytes, utilizando protocolos específicos para garantizar la integridad de los datos.

La optimización de la lectura y escritura es otro aspecto importante. Algunas técnicas incluyen el uso de buffers para reducir el número de operaciones de entrada/salida, la selección de algoritmos eficientes para la búsqueda y el ordenamiento de datos, y la gestión adecuada de los recursos.

Finalmente, la seguridad en la lectura y escritura de información es un tema crucial. Los programas deben implementar medidas para proteger los datos contra accesos no autorizados, modificaciones o pérdidas. Esto implica utilizar técnicas como el cifrado de datos, la autenticación de usuarios y la gestión adecuada de permisos.

En resumen, la lectura y escritura de información es una habilidad esencial en cualquier programa informático. Desde la manipulación de ficheros hasta la comunicación entre aplicaciones, este proceso permite a los programas interactuar con el mundo exterior y almacenar datos persistentemente. A través de técnicas eficientes y seguras, los programadores pueden crear sistemas que manejen grandes cantidades de información de manera efectiva y confiable.


<a id="aplicacion-de-las-estructuras-de-almacenamiento"></a>
# Aplicación de las estructuras de almacenamiento

<a id="estructuras-estaticas-y-dinamicas"></a>
## Estructuras estáticas y dinámicas

En el vasto y complejo mundo de la programación, las estructuras de almacenamiento desempeñan un papel fundamental como los pilares que sostienen una construcción. En esta subunidad didáctica, nos adentramos en el fascinante mundo de las estructuras estáticas y dinámicas, dos conceptos esenciales que permiten a los programadores organizar y manipular datos con eficiencia.

Las estructuras estáticas son como una casa construida con materiales fijos. Una vez que se ha definido su tamaño y forma, no puede cambiar. En la programación, esto significa que las estructuras estáticas tienen un tamaño fijo en memoria durante toda su vida útil. Son ideales para almacenar datos de tipos conocidos y fijos, como una lista de números enteros o una matriz de caracteres.

Por otro lado, las estructuras dinámicas son como una casa de Lego. Se pueden construir, modificar y cambiar a lo largo del tiempo. En la programación, esto significa que las estructuras dinámicas pueden crecer o disminuir en tamaño según sea necesario. Son ideales para almacenar datos de tipos variables o desconocidos, como una lista de cadenas de texto o un conjunto de objetos.

La elección entre usar estructuras estáticas y dinámicas depende del contexto específico del problema que se esté resolviendo. Las estructuras estáticas son más eficientes en términos de memoria y tiempo de ejecución, pero limitan la flexibilidad. Por otro lado, las estructuras dinámicas ofrecen mayor flexibilidad, pero pueden ser menos eficientes.

El concepto de estructura estática es fundamental para entender cómo se organizan los datos en la memoria del ordenador. Cada elemento de una estructura estática ocupa un espacio fijo y conocido en la memoria, lo que facilita el acceso y la manipulación de estos datos. Además, las estructuras estáticas pueden ser fácilmente iteradas y recorridas, lo que es útil para realizar operaciones como la búsqueda o la ordenación.

Por otro lado, las estructuras dinámicas son más complejas pero también más poderosas. Permiten el crecimiento y la disminución en tamaño durante la ejecución del programa, lo que significa que pueden adaptarse a situaciones cambiantes. Además, las estructuras dinámicas suelen ser más flexibles en cuanto al tipo de datos que pueden almacenar, ya que no están limitadas por un tamaño fijo.

La comprensión de estas diferencias es crucial para el diseño eficiente de programas. Al elegir la estructura adecuada, los programadores pueden optimizar el uso de memoria y mejorar el rendimiento del programa. Además, entender cómo funcionan las estructuras estáticas y dinámicas nos permite abordar problemas más complejos en el futuro.

En resumen, las estructuras estáticas y dinámicas son dos herramientas esenciales en la programación que permiten organizar y manipular datos de manera eficiente. Cada una tiene sus propias ventajas y desventajas, y su elección depende del contexto específico del problema que se esté resolviendo. A través de este estudio, hemos adquirido un nuevo nivel de comprensión sobre cómo funcionan estas estructuras fundamentales en la programación, lo que nos prepara para abordar problemas más complejos en el futuro.

### estructuras estaticas

```python
# x,y,z
coordenadas = (4,5,6)
```

### append a tupla

```python
# x,y,z
coordenadas = (4,5,6)
coordenadas.append(7)
```

### escribir datos

```python
# x,y,z
coordenadas = (4,5,6)

coordenadas[0] = 11 # esto es la "x"
coordenadas[1] = 12 # esto es la "y"
coordenadas[2] = 13 # esto es la "z"
```

### leer datos

```python
# x,y,z
coordenadas = (4,5,6)
coordenadas = (11,12,13)

print(coordenadas)

print(coordenadas[0])
```

### estructuras dinamicas

```python
agenda = [] # corchetes = lista

agenda.append("Jose Vicente")
agenda.append("Juan")

print(agenda)

agenda.append("Jorge")

print(agenda)
```

### acceso a un solo elemento

```python
agenda = [] # corchetes = lista

agenda.append("Jose Vicente")
agenda.append("Juan")

print(agenda)

agenda.append("Jorge")

print(agenda)
print(agenda[0])
```

### sobreescribir

```python
agenda = [
  'Jose Vicente',
  'Juan',
  'Jorge'
] # corchetes = lista

print(agenda)

agenda[0] = "Jaime"

print(agenda)
```

### eliminar elementos de la lista

```python
agenda = [
  'Jose Vicente',
  'Juan',
  'Jorge'
] # corchetes = lista

print(agenda)
agenda.pop()
print(agenda)
```

### quitar un elemento concreto

```python
agenda = [
  'Jose Vicente',
  'Juan',
  'Jorge'
] # corchetes = lista

print(agenda)
agenda.pop(1)
print(agenda)
```

### tupla de nuevo

```python
# x,y,z
coordenadas = (4,5,6)
```

### diccionario

```python
# x,y,z

coordenadas = {
  "x":"4",
  "y":"5",
  "z":"6"
}

print(coordenadas)
```

### acceso a un elemento

```python
# x,y,z

coordenadas = {
  "x":"4",
  "y":"5",
  "z":"6"
}

print(coordenadas)
print(coordenadas['x'])
```

### repaso

```markdown
# Tuplas ()

Estáticas, no pueden crecer ni decrecer
Índices numéricos

# Listas []

Dinámicas, pueden crecer y decrecer
Índices numéricos

# Diccionarios {}

Dinámicas, pueden crecer y decrecer
Índices alfanuméricos (letras, palabras, números)
```

### creamos una lista de la compra

```python
lista_de_la_compra = []

lista_de_la_compra.append("mangos")
lista_de_la_compra.append("chorizos")
lista_de_la_compra.append("cerveza")
lista_de_la_compra.append("patos")

print(lista_de_la_compra)
```

### lista con diccionario

```python
lista_de_la_compra = []

lista_de_la_compra.append(
  {
    "producto":"mangos",
    "cantidad":"4"
  }
)

print(lista_de_la_compra)
```

### un segundo elemento

```python
lista_de_la_compra = []

lista_de_la_compra.append(
  {
    "producto":"mangos",
    "cantidad":"4"
  }
)
lista_de_la_compra.append(
  {
    "producto":"manzanas",
    "cantidad":"7"
  }
)

print(lista_de_la_compra)
```

### carga inicial

```python
lista_de_la_compra = [
  {
    "producto":"mangos",
    "cantidad":"4"
  },
  {
    "producto":"manzanas",
    "cantidad":"7"
  }
]


print(lista_de_la_compra)
```

### el usuario se crea su lista

```python
print("Lista de la compra v0.1")

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  
```

### estructura if

```python
print("Lista de la compra v0.1")

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    
  elif opcion == 2:
    
```

### creamos la lista primero

```python
print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    
  elif opcion == 2:
    
```

### añado elemento a la lista

```python
print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    
  elif opcion == 2:
    
```

### vomito la lista

```python
print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
  elif opcion == 2:
    print("Listamos los elementos de la lista:")
    print(lista_de_la_compra)
```

### recorrer listas

```python
agenda = ["Jorge","Juan","Jose"]

print(agenda)
print(agenda[0])

for nombre in agenda:
  print(nombre)
```

### recorro la lista

```python
print("Lista de la compra v0.1")

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
  elif opcion == 2:
    print("Listamos los elementos de la lista:")
    for producto in lista_de_la_compra:
      print("Producto:",producto['nombre'])
      print("Cantidad:",producto['cantidad'])
      print("##############################") # Esto es estético, separador
```

### guardo en json

```python
print("Lista de la compra v0.1")
import json                   # Para usar la libreria tengo que importarla

lista_de_la_compra = []

while True:
  print("Selecciona una opcion")
  print("1.-Añadir elemento a la lista")
  print("2.-Leer la lista")
  opcion = int(input("Tu opción: "))
  
  if opcion == 1:
    print("Añadimos un elemento a la lista:")
    nombre = input("Indica el nombre del producto: ")
    cantidad = input("Indica la cantidad del producto: ")
    lista_de_la_compra.append({"nombre":nombre,"cantidad":cantidad})
    archivo = open("lista.json","w")         # Abro el archivo
    json.dump(lista_de_la_compra,archivo)    # Guardo en json
    archivo.close()                          # Cierro el archivo
  elif opcion == 2:
    print("Listamos los elementos de la lista:")
    for producto in lista_de_la_compra:
      print("Producto:",producto['nombre'])
      print("Cantidad:",producto['cantidad'])
      print("##############################") # Esto es estético, separador
```

### lista

```json
[{"nombre": "Manzanas", "cantidad": "2"}, {"nombre": "Peras", "cantidad": "4"}]
```

<a id="creacion-de-matrices-arrays"></a>
## Creación de matrices (arrays)

En el vasto y complejo mundo de la programación, las estructuras de almacenamiento desempeñan un papel fundamental como los pilares que sostienen una construcción. En esta subunidad didáctica, nos adentramos en el fascinante mundo de las matrices (arrays), una herramienta esencial para organizar y manipular datos de manera eficiente.

Las matrices son estructuras de datos bidimensionales que permiten almacenar un conjunto ordenado de elementos del mismo tipo. Imagina una tabla rectangular, donde cada celda contiene un valor específico. Esta organización permite acceder a cualquier elemento mediante dos índices: uno para la fila y otro para la columna. Este sistema de referencia es fundamental para realizar operaciones complejas sobre conjuntos de datos.

La creación de matrices es un concepto básico pero poderoso en programación. Para comenzar, debemos entender cómo declarar una matriz en nuestro código. En muchos lenguajes de programación, esto se realiza mediante la especificación del tipo de dato, el nombre de la matriz y su tamaño. Por ejemplo, en pseudocódigo, podríamos escribir algo como `int[][] miMatriz = new int[3][4];`, lo que crea una matriz de enteros con 3 filas y 4 columnas.

Una vez declarada, podemos inicializar los valores de la matriz utilizando bucles anidados. Cada iteración del bucle exterior corresponde a una fila, mientras que el bucle interior maneja las columnas. Este proceso es crucial para llenar la matriz con los datos deseados y prepararla para su uso en operaciones posteriores.

Las matrices también pueden ser utilizadas para representar tableros de juegos, gráficos bidimensionales o incluso sistemas de coordenadas. Su capacidad para almacenar múltiples valores en una sola estructura hace que sean ideales para resolver problemas que implican la manipulación de conjuntos de datos relacionados.

Además de su uso directo en el código, las matrices también son fundamentales en algoritmos y estructuras de datos más complejas. Por ejemplo, muchas operaciones matemáticas y científicas requieren la manipulación de matrices para realizar cálculos eficientes. En estos casos, las matrices se convierten en herramientas esenciales para el análisis y procesamiento de información.

La creación de matrices también implica comprender los conceptos de índices y dimensiones. Los índices son fundamentales para acceder a elementos específicos dentro de la matriz, mientras que las dimensiones indican cuántas filas y columnas contiene. Estos conceptos deben ser bien dominados para evitar errores comunes como el acceso fuera de rango o la confusión entre los índices.

En resumen, la creación de matrices es un tema fundamental en programación que nos permite organizar y manipular datos de manera eficiente. A través de esta estructura, podemos resolver problemas complejos y realizar operaciones matemáticas y científicas con mayor facilidad. Su dominio es esencial para cualquier desarrollador que quiera trabajar con conjuntos de datos relacionados o realizar cálculos avanzados en su código.

### comidas

```python
menu = []
```

### bucle infinito

```python
menu = []

while True:
  comida = input("Introduce el nombre de la comida: ")
  
```

### añado a la lista

```python
menu = []

while True:
  comida = input("Introduce el nombre de la comida: ")
  menu.append(comida)
```

### recorrer la lista

```python
menu = []

while True:
  comida = input("Introduce el nombre de la comida: ")
  menu.append(comida)
  print("Tu comida hasta el momento es:")
  for elemento in menu:
    print(elemento)
```

### acciones del menu

```python
menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  opcion = input("Selecciona una opción:")
  comida = input("Introduce el nombre de la comida: ")
  menu.append(comida)
  print("Tu comida hasta el momento es:")
  for elemento in menu:
    print(elemento)
```

### tomamos las opciones

```python
menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
```

### intentamos guardar

```python
menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.txt","w")
    archivo.write(menu)
    archivo.close()
    
    
    
```

### importamos pickle

```python
import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.txt","w")
    archivo.write(menu)
    archivo.close()
    
    
    
```

### abro el archivo en modo escritura binaria

```python
import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb") # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    
    
    
    
    
    
    
    
    
```

### print con exito

```python
import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb") # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    print("Se ha guardado con éxito ✅")
    
    
    
    
    
    
    
    
    
```

### cargar archivo

```python
import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  print("4.-Cargar datos de archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb") # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    print("Se ha guardado con éxito ✅")
  elif opcion == 4:
    archivo = open("datos.bin","rb")
    menu = pickle.load(archivo) # Volcamos el archivo a la lista
    archivo.close()
    
    
    
    
    
    
    
    
    
```

### cadena de ayuda

```python
import pickle

menu = []

while True:
  print("Opciones:")
  print("1.-Introducir nueva comida en el menú")
  print("2.-Listar comidas en el menú")
  print("3.-Guardar en archivo")
  print("4.-Cargar datos de archivo")
  opcion = int(input("Selecciona una opción:"))
  if opcion == 1:
    comida = input("Introduce el nombre de la comida: ")
    menu.append(comida)
  elif opcion == 2:
    print("Tu comida hasta el momento es:")
    for elemento in menu:
      print(elemento)
  elif opcion == 3:
    archivo = open("datos.bin","wb") # Write Binary
    pickle.dump(menu,archivo)
    archivo.close()
    print("Se ha guardado con éxito ✅")
  elif opcion == 4:
    archivo = open("datos.bin","rb")
    menu = pickle.load(archivo) # Volcamos el archivo a la lista
    archivo.close()
    print("Se ha cargado con éxito ✅")
    
    
    
    
    
    
    
    
```

<a id="matrices-arrays-multidimensionales"></a>
## Matrices (arrays) multidimensionales

Continuando con nuestra exploración del mundo de la programación, nos dirijimos a una subunidad crucial: la aplicación de las estructuras de almacenamiento. En esta sección, nos centraremos específicamente en las matrices (arrays) multidimensionales, un concepto fundamental que permite organizar y manejar datos de manera eficiente.

Las matrices multidimensionales son una extensión natural de los arrays unidimensionales, permitiendo almacenar datos en múltiples dimensiones. En lugar de tener solo filas o columnas, las matrices multidimensionales nos ofrecen la posibilidad de crear estructuras más complejas y ricas en información.

Para ilustrar su uso, consideremos una matriz bidimensional que representa una tabla de ventas. Cada fila podría representar un producto, mientras que cada columna podría representar diferentes meses del año. De esta manera, podemos almacenar fácilmente la cantidad vendida de cada producto durante cada mes, facilitando el análisis y la visualización de los datos.

La manipulación de matrices multidimensionales implica acceso a sus elementos mediante índices. En Python, por ejemplo, si tenemos una matriz bidimensional `ventas`, podemos acceder al valor de ventas del producto 3 en el mes 2 con la siguiente sintaxis: `ventas[2][1]`. Es importante recordar que los índices comienzan desde cero, lo que significa que el primer elemento está en la posición 0.

Además de las matrices bidimensionales, existen estructuras multidimensionales más complejas. Por ejemplo, una matriz tridimensional podría representar datos spaciales o temporales, donde cada dimensión representa un eje diferente. En este caso, podríamos tener una matriz que almacene temperaturas en diferentes ciudades a lo largo de los años.

La programación multidimensional no se limita a la manipulación de datos estáticos. También es común trabajar con matrices dinámicas, donde el tamaño puede cambiar durante la ejecución del programa. En estos casos, es crucial tener cuidado al manejar los índices y asegurarse de que siempre estén dentro del rango válido.

La eficiencia en la manipulación de matrices multidimensionales es un aspecto importante a considerar. Algunas operaciones pueden ser computacionalmente intensivas, lo que requiere una optimización cuidadosa para evitar problemas de rendimiento. Herramientas como NumPy en Python proporcionan funciones y métodos eficientes para trabajar con grandes conjuntos de datos multidimensionales.

En conclusión, las matrices multidimensionales son una herramienta poderosa en el arsenal del programador. Permiten organizar y manipular datos de manera estructurada, facilitando la realización de análisis complejos y la visualización de información. A medida que avanzamos en nuestro estudio de la programación, es crucial familiarizarnos con estas estructuras y aprender a utilizarlas eficazmente en nuestros proyectos.

### variable

```python
nombre = "Jose Vicente"
```

### lista

```python
nombre = "Jose Vicente"

nombres = [
  "Jose Vicente",
  "Juan",
  "Jorge",
  "Jaime",
  "Julia"
]
```

### matriz multidimensional

```python
agenda = []

# Una lista dentro de otra lista
agenda[0] = [
  "Jose Vicente",
  "Carratala",
  "info@jocarsa.com",
  "12345678"
]

agenda[1] = [
  "Jorge",
  "Martinez",
  "jorge@jocarsa.com",
  "123456787"
]
```

### otra formulacion

```python
agenda = [
  [
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "12345678"
  ],
  [
    "Jorge",
    "Martinez",
    "jorge@jocarsa.com",
    "123456787"
  ]
]

print(agenda)  
```

### acceso a un elemento de la primera dimension

```python
agenda = [
  [
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "12345678"
  ],
  [
    "Jorge",
    "Martinez",
    "jorge@jocarsa.com",
    "123456787"
  ]
]

print(agenda[0])  
```

### puedo acceder a la segunda dimension

```python
agenda = [
  [
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "12345678"
  ],
  [
    "Jorge",
    "Martinez",
    "jorge@jocarsa.com",
    "123456787"
  ]
]

print(agenda[0])  
print(agenda[0][0]) # Jose Vicente
```

### tambien podemos escribir

```python
agenda = [
  [
    "Jose Vicente",
    "Carratala",
    "info@jocarsa.com",
    "12345678"
  ],
  [
    "Jorge",
    "Martinez",
    "jorge@jocarsa.com",
    "123456787"
  ]
]

print(agenda[0])  
print(agenda[0][0]) # Jose Vicente
agenda[0][0] = "Jaime"
print(agenda[0][0]) # Jaime
```

### ejemplo palet

```python
palet = [ # x
          [ # y
            [1,2,3], # z 
            [4,5,6],
            [7,8,9]
          ],
          [
            [11,12,13], 
            [14,15,16],
            [17,18,19] 
          ],
          [
            [21,22,23], 
            [24,25,26],
            [27,28,29] 
          ]
        ]
print(palet)
```

### linea de palets

```python
palets = [ # linea de palets
           [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
          [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
        ]
print(palet)
```

### estanteria de palets

```python
palets = [ # estanteria de palets
          [ # linea de palets
           [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
          [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
        ],
        [ # linea de palets
           [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
          [ # x
            [ # y
              [1,2,3], # z 
              [4,5,6],
              [7,8,9]
            ],
            [
              [11,12,13], 
              [14,15,16],
              [17,18,19] 
            ],
            [
              [21,22,23], 
              [24,25,26],
              [27,28,29] 
            ]
          ],
        ],
       ]
print(palet)
```

### estanterias

```python
palets = [ # Estanterias de palets
           [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
         [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
        ]
print(palet)
```

### naves industriales

```python
naves = [ # Naves industriales
          [ # Estanterias de palets
           [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
         [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
        ],
        [ # Estanterias de palets
           [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
         [ # estanteria de palets
            [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
          [ # linea de palets
             [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
            [ # x
              [ # y
                [1,2,3], # z 
                [4,5,6],
                [7,8,9]
              ],
              [
                [11,12,13], 
                [14,15,16],
                [17,18,19] 
              ],
              [
                [21,22,23], 
                [24,25,26],
                [27,28,29] 
              ]
            ],
          ],
         ],
        ]
       ]
print(palet)
```

### agenda

```python
agenda = []

while True:
  nombre = input("Dime tu nombre: ")
  apellidos = input("Dime tus apellidos: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu teléfono: ")
  # Añado a la agenda
  agenda.append([nombre,apellidos,email,telefono])
  print(agenda)
  
  
  
```

### pickle para guardar

```python
import pickle
agenda = []

while True:
  nombre = input("Dime tu nombre: ")
  apellidos = input("Dime tus apellidos: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu teléfono: ")
  # Añado a la agenda
  agenda.append([nombre,apellidos,email,telefono])
  print(agenda)
  archivo = open("agenda.bin",'wb')
  pickle.dump(agenda,archivo)
  archivo.close()
  
  
  
```

### conversiones de datos conocidas

```python
edad = "47"

edad_en_numero = int(edad)

print(edad)
print(edad_en_numero)
```

### conversiones no posibles

```python
edad = "a"

edad_en_numero = int(edad)

print(edad)
print(edad_en_numero)
```

### tipo

```python
lista = ['manzanas','peras','platanos']
print(lista)
print(type(lista))

tupla = ('manzanas','peras','platanos')
print(tupla)
print(type(tupla))
```

### cambio de tipo de dato

```python
tupla = ('manzanas','peras','platanos')
# Necesito meter una fruta más
print(tupla)
lista = list(tupla) # convierto una tupla en una lista
print(lista)
lista.append("fresas")

# Ahora supongamos que tengo que volver a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)
```

### parto

```python
import pickle
agenda = []

while True:
  # Insertar
  nombre = input("Dime tu nombre: ")
  apellidos = input("Dime tus apellidos: ")
  email = input("Dime tu email: ")
  telefono = input("Dime tu teléfono: ")
  agenda.append([nombre,apellidos,email,telefono])
  # Imprimir
  print(agenda)
  # Guardar
  archivo = open("agenda.bin",'wb')
  pickle.dump(agenda,archivo)
  archivo.close()
  
  
  
```

### menu

```python
import pickle
agenda = []

while True:
  print("Selecciona una opcion: ")
  print("1.-Insertar un registro")
  print("2.-Leer registros")
  print("3.-Guardar registros")
  opcion = int(input("Opción escogida: "))
  if opcion == 1:
    # Insertar
    nombre = input("Dime tu nombre: ")
    apellidos = input("Dime tus apellidos: ")
    email = input("Dime tu email: ")
    telefono = input("Dime tu teléfono: ")
    agenda.append([nombre,apellidos,email,telefono])
  elif opcion == 2:
    # Imprimir
    print(agenda)
  elif opcion == 3:
    # Guardar
    archivo = open("agenda.bin",'wb')
    pickle.dump(agenda,archivo)
    archivo.close()
  
  
  
```

<a id="genericidad"></a>
## Genericidad

En el vasto mundo de la programación, una estructura de almacenamiento es como el esqueleto de un edificio; proporciona la base sobre la cual se construyen las aplicaciones. En esta subunidad didáctica, nos adentramos en el concepto fundamental de genericidad, que es una herramienta poderosa para mejorar la flexibilidad y reutilización del código.

La genericidad permite definir clases y métodos que pueden trabajar con diferentes tipos de datos sin necesidad de especificar estos tipos de antemano. Esta característica es especialmente valiosa en el desarrollo de bibliotecas y frameworks, donde se requiere una amplia gama de operaciones que puedan aplicarse a diversos tipos de objetos.

Comenzamos por entender cómo funciona la genericidad en Java, un lenguaje conocido por su soporte robusto para este concepto. A través del uso de parámetros de tipo genéricos, podemos crear clases y métodos que son independientes del tipo específico de datos con los que operan. Por ejemplo, una lista genérica puede almacenar cualquier tipo de objeto, desde cadenas hasta números enteros.

La ventaja de la genericidad radica en su capacidad para reducir el código repetitivo y mejorar la seguridad tipológica. Al definir clases y métodos genéricos, evitamos errores comunes como la conversión de tipos (ClassCastException) que pueden surgir cuando se trabaja con objetos de diferentes tipos.

Además, la genericidad facilita la creación de interfaces y clases más abstractas, permitiendo una mayor modularidad en el diseño de aplicaciones. Esto no solo hace que el código sea más fácil de mantener y escalar, sino que también promueve un mejor entendimiento del funcionamiento interno de las bibliotecas y frameworks.

En este contexto, es crucial entender cómo implementar la genericidad en diferentes situaciones. Por ejemplo, cuando se trabaja con colecciones como listas o conjuntos, el uso de tipos genéricos puede evitar problemas comunes relacionados con la pérdida de tipo (type erasure) que ocurre en Java.

La aplicabilidad de la genericidad no se limita a estructuras de datos; también es fundamental para la creación de métodos y funciones que pueden operar sobre cualquier tipo de dato. Esto incluye operaciones como comparaciones, filtrado y reducción, que son fundamentales en el procesamiento de grandes conjuntos de datos.

En resumen, la genericidad es una herramienta esencial en la programación moderna. Permite crear código más flexible, seguro y reusable, lo que a su vez facilita el desarrollo de aplicaciones complejas y escalables. A través de este concepto, los desarrolladores pueden abordar problemas de manera más eficiente, aprovechando al máximo las capacidades del lenguaje y las bibliotecas disponibles.

La comprensión y aplicación correcta de la genericidad son habilidades cruciales para cualquier programador que quiera escribir código limpio, mantenible y escalable. En esta subunidad didáctica, hemos explorado los fundamentos de este concepto y su importancia en el desarrollo de aplicaciones modernas. A medida que avanzamos en nuestro estudio de la programación, es importante mantenerse al tanto de estas técnicas avanzadas para mantenernos al día con las mejores prácticas del campo.

### genericidad en python

```python
numeros = [
  1,
  2,
  "3",
  4
]

print(numeros)
```

### funcion doble

```python
numeros = [
  1,
  2,
  "3",
  4
]

print(numeros)

def calculaDoble():
  for numero in numeros:
    print(numero*2)

calculaDoble()
```

### arreglo de genericidad

```python
numeros = [1,2,"3",4]

print(numeros)

def calculaDoble():
  for numero in numeros:
    numero = int(numero)   # Convierto en entero
    print(numero*2)

calculaDoble()
```

### meto un poco de presion

```python
numeros = [1,2,"3",4,"cinco"]

print(numeros)

def calculaDoble():
  for numero in numeros:
    numero = int(numero)   # Convierto en entero
    print(numero*2)

calculaDoble()
```

### try except

```python
numeros = [1,2,"3",4,"cinco"]

print(numeros)

def calculaDoble():
  for numero in numeros:
    try:
      numero = int(numero)   # Convierto en entero
      print(numero*2)
    except:
      print("(no válido)")

calculaDoble()
```

### estructura de datos

```python
numeros = [1,2,"3",4,"cinco"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                    # Primero intenta convertir
      numero = int(numero)
      print(numero * 2)
    except:                 # Si no puedes
      # Intenta busca el valor en la lista de numeros
      for i in range(0,len(numeros_etiquetas)):
        if numero == numeros_etiquetas[i]:
          print(i*2)
        
calculaDoble()
```

### la volvemos a fastidiar

```python
numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                    # Primero intenta convertir
      numero = int(numero)
      print(numero * 2)
    except:                 # Si no puedes
      # Intenta busca el valor en la lista de numeros
      for i in range(0,len(numeros_etiquetas)):
        if numero == numeros_etiquetas[i]:
          print(i*2)
        
calculaDoble()
```

### atrapamos el caso patata

```python
numeros = [1,2,"3",4,"cinco","patata"]

print(numeros)
numeros_etiquetas = ["cero","uno","dos","tres","cuatro","cinco"]
def calculaDoble():
  for numero in numeros:
    try:                    # Primero intenta convertir
      numero = int(numero)
      print(numero * 2)
    except:                 # Si no puedes
      centinela = False
      # Intenta busca el valor en la lista de numeros
      for i in range(0,len(numeros_etiquetas)):
        if numero == numeros_etiquetas[i]:
          print(i*2)
          centinela = True
      if centinela == False:
        print("Mira tio lo he intentado pero no he podido")
        
calculaDoble()
```

<a id="cadenas-de-caracteres-expresiones-regulares"></a>
## Cadenas de caracteres. Expresiones regulares

En el vasto mundo de la programación, las cadenas de caracteres son una construcción fundamental que nos permite almacenar y manipular texto. Son como los bloques con los que construimos nuestras aplicaciones, ya sea para mostrar información al usuario o para procesar datos internos.

Las expresiones regulares, por otro lado, son un poderoso lenguaje que nos permite definir patrones complejos de búsqueda dentro de estas cadenas. Es como tener una llave mágica que puede abrir puertas a cualquier texto que cumpla con ciertas características específicas.

La combinación de cadenas y expresiones regulares es como tener un jardín de flores, donde cada flor tiene su propio color y forma. Cada cadena es una flor única, mientras que las expresiones regulares son los jardineros que saben cómo identificar y agrupar estas flores según sus características.

En esta subunidad didáctica, nos adentramos en el fascinante mundo de las cadenas de caracteres y las expresiones regulares. Aprenderemos a crear y manipular cadenas con eficacia, así como a usar expresiones regulares para buscar y extraer información de ellas. Es un viaje lleno de descubrimientos y aplicaciones prácticas.

Comenzaremos por entender los conceptos básicos de las cadenas de caracteres, desde cómo se declaran hasta cómo se manipulan. Aprenderemos sobre diferentes tipos de cadenas y cómo realizar operaciones comunes como concatenación, búsqueda y reemplazo.

Luego, nos sumergiremos en el poderoso mundo de las expresiones regulares. Aprenderemos a definir patrones complejos que pueden coincidir con cualquier texto que cumpla ciertas condiciones. Estudiarémos cómo usar operadores y funciones para crear expresiones regulares versátiles y eficientes.

A lo largo del camino, veremos ejemplos prácticos de cómo aplicar estas técnicas en situaciones reales. Desde la validación de entradas de usuario hasta el procesamiento de datos complejos, aprenderemos a utilizar cadenas y expresiones regulares para resolver problemas con ingenio y eficiencia.

Finalmente, reflexionaremos sobre las mejores prácticas al trabajar con cadenas y expresiones regulares. Aprenderemos cómo optimizar nuestras soluciones, cómo manejar posibles errores y cómo mantener nuestro código limpio y legible.

Este viaje a través del mundo de las cadenas de caracteres y las expresiones regulares nos prepara para enfrentar desafíos más complejos en el campo de la programación. Es una habilidad fundamental que nos permitirá crear aplicaciones robustas, seguras y eficientes.

### las strings realmente son colecciones

```python
nombre = "Jose Vicente"
print(nombre)

print(nombre[0])
```

### recorrer una cadena

```python
nombre = "Jose Vicente"
for letra in nombre:
    print(letra)
```

### longitud de la cadena

```python
nombre = "Jose Vicente"
print("La longitud del nombre:")
print(len(nombre))
```

### explotar

```python
nombre = "Jose Vicente"
explotado = nombre.split(" ")
print(explotado)
```

### ejemplo csv

```python
datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena
print(datos)
# Ahora la parto
partido = datos.split(",")
# Ahora imprimo el partido
print(partido)
```

### unir

```python
datos = "uno,dos,tres,cuatro,cinco,seis"

# Primero imprimo la cadena
print(datos)
# Ahora la parto
partido = datos.split(",")
# Ahora imprimo el partido
print(partido)
# Ahora quiero unirlo todo de nuevo
nueva_cadena = "|".join(partido)
print(nueva_cadena)
```

### leer archivo csv

```python
archivo = open("clientes.csv","r")

lineas = archivo.readlines()

for linea in lineas:
	partido = linea.split(",")
	print(partido)
```

### convierto a matriz multidimensional

```
archivo = open("clientes.csv","r")

lineas = archivo.readlines()

conjunto_datos = []

for linea in lineas:
	partido = linea.split(",")
	conjunto_datos.append(partido)

print(conjunto_datos)
```

### reemplazar

```python
cadena = "Hoy es martes"

reemplazado = cadena.replace("martes","miercoles")

print(reemplazado)
```

### quitar saltos de linea

```python
# Esta cadena tiene algo que no quiero (\n)
linea_con_salto = "Esto es una prueba \n"
# Lo que quiero es QUITAR algo
# Quito |n con "nada"
limpiado = linea_con_salto.replace("\n","")
```

### expresiones regulares

```python

"""
Explicación del patrón:

^
    Indica el inicio de la cadena. La validación comienza desde el principio.

[a-zA-Z0-9_.+-]+
    Parte local del correo (antes de '@').
    Permite:
        - letras mayúsculas y minúsculas (a-zA-Z)
        - números (0-9)
        - guion bajo (_)
        - punto (.)
        - signo más (+)
        - guion (-)
    El símbolo '+' indica uno o más caracteres válidos.

@
    Caracter obligatorio que separa el usuario del dominio.

[a-zA-Z0-9-]+
    Nombre del dominio principal sin subdominios.
    Permite letras, números y guiones.
    Requiere al menos un carácter.

\.
    Un punto literal que separa el dominio del TLD.
    El backslash escapa el carácter '.' para que no actúe como comodín.

[a-zA-Z0-9-.]+
    Parte final del dominio (TLD o subdominios), por ejemplo:
        .com
        .co.uk
        .org
    Permite letras, números, guiones y puntos.
    El símbolo '+' indica uno o más caracteres.

$
    Indica el final de la cadena. La validación termina aquí.
"""
import re

patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email_mal = "algo"
email_bien = "info@jocarsa.com"

print(re.match(patron, email_mal))

print(re.match(patron, email_bien))
```

### regex direccion postal

```python
import re

patron = r'^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+ \d+[A-Za-z]? \d{5}$'
"""
Explicación del patrón:

^
    Inicio de la cadena.

[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+
    Nombre de la calle o vía.
    Permite:
        - letras mayúsculas y minúsculas
        - letras acentuadas y 'ñ'
        - espacios
    '+' indica uno o más caracteres.

␣ (espacio)
    Separador obligatorio.

\d+
    Número de portal.
    '\d' representa un dígito.
    '+' indica uno o más dígitos.
    Ejemplo: 5, 23, 104

[A-Za-z]?
    Letra opcional en el número (como 10B o 23A).
    '?' indica que puede aparecer cero o una vez.

␣ (espacio)
    Separador obligatorio.

\d{5}
    Código postal español estándar de 5 dígitos.

$
    Final de la cadena.
"""

direccion_mal = "Calle Mayor"
direccion_bien = "Calle Mayor 10 46001"

print(re.match(patron, direccion_mal))
print(re.match(patron, direccion_bien))
```

### validar telefono

```python

```

### ollama

```markdown
# Descargamos la instalacion de ollama

sudo apt install curl (si no tenéis curl)

curl -fsSL https://ollama.com/install.sh | sh

# Comprobar la versión instalada

ollama --version

Alternativa con snap:
sudo snap install ollama

# Quiero saber los modelos que tengo instalados

ollama list
```

### instalar un modelo

```markdown
ollama pull qwen2.5:3b-instruct
```

### ejecutar ollama

```markdown
ollama run qwen2.5:3b-instruct
```

### lista de modelos de ejemplo

```markdown
LLaMA / Meta

llama2

llama3

llama3.1

llama3.2

llama3.2-vision

codellama

Mistral / Mixtral

mistral

mistral-small

mistral-large (community ports)

mixtral-8x7b

mixtral-8x22b (community)

open-mistral-nemo (NVIDIA)

Phi / Microsoft

phi

phi2

phi3

phi3-mini

phi3-small

phi3-medium

Qwen / Alibaba

qwen

qwen2

qwen2.5

qwen2.5-coder

qwen2-audio

qwen2-vision

Nous Research

nous-hermes

nous-hermes-2-mistral

neural-chat

Gemma / Google

gemma

gemma2

Tiny / Lightweight models

tinyllama

orca-mini

dolphin-phi

stablelm-zephyr

✅ Vision-capable Models

(models that process images)

llama3.2-vision

qwen2-vision

moondream

bakllava

llava

llava-phi

chocovision (community)

✅ Code-specialized Models

codellama

granite-code

qwen2.5-coder

deepseek-coder

starcoder2

mistral-coder (community)

✅ Audio / Speech Models

whisper (speech-to-text)

qwen2-audio

salmonn (community)

✅ Embedding Models

nomic-embed-text

bge-base

bge-large

instructor-xl

✅ Tool / Function-calling Models

(many LLMs support tools depending on prompt)

No separate engine, but strongest:

llama3.1

llama3.2

qwen2.5

mixtral-8x7b
```

### ejecutar ollama desde python

```python
import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:3b-instruct",
    "prompt": "Explica qué es una lista en Python con un ejemplo. Responde en español.",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()
print(data["response"])
```

### clientes

```
id,nombre,apellidos,correo,telefono,direccion,ciudad,provincia,codigo_postal,empresa,NIF
1,Laura,García López,laura.garcia@example.com,612345678,Calle Mayor 12,Valencia,Valencia,46001,TecnoSol S.L.,B12345678
2,Miguel,Pérez Sánchez,miguel.perez@example.com,678901234,Avenida del Puerto 45,Madrid,Madrid,28002,InnovaWeb S.A.,A87654321
3,Ana,Martínez Ruiz,ana.martinez@example.com,634567890,Plaza España 3,Sevilla,Sevilla,41005,Servicon S.L.,B11223344
4,Carlos,Hernández Torres,carlos.hernandez@example.com,699112233,Calle Gran Vía 78,Barcelona,Barcelona,08010,SoftMarket S.L.,B99887766
5,Elena,Romero Díaz,elena.romero@example.com,622334455,Calle San Vicente 5,Zaragoza,Zaragoza,50004,ConsultingPro S.L.,B44556677
6,Javier,Navarro Gómez,javier.navarro@example.com,645667788,Avenida Constitución 23,Murcia,Murcia,30008,DataPlus S.A.,A33445566
7,María,Fuentes Ortega,maria.fuentes@example.com,633889900,Calle Sol 18,Málaga,Málaga,29007,Mercaplus S.L.,B22114455
8,Sergio,Rey Delgado,sergio.rey@example.com,671223344,Calle Libertad 9,Alicante,Alicante,03003,Logística Express S.L.,B77889900
9,Isabel,Vidal Castro,isabel.vidal@example.com,699554433,Paseo Colón 14,Bilbao,Bizkaia,48009,EcoEner S.A.,A99001122
10,Pablo,Santos Molina,pablo.santos@example.com,611223344,Calle Real 2,Valladolid,Valladolid,47003,Formática S.L.,B66778899
```

<a id="colecciones-listas-conjuntos-y-diccionarios"></a>
## Colecciones Listas, Conjuntos y Diccionarios

En el vasto mundo de la programación, las estructuras de almacenamiento desempeñan un papel fundamental como los pilares que sostienen una construcción. En esta subunidad didáctica, nos adentramos en el fascinante universo de las colecciones, específicamente en las listas, conjuntos y diccionarios, elementos esenciales para organizar y manipular datos de manera eficiente.

Las listas son como cajas mágicas que pueden contener cualquier tipo de dato, desde números hasta cadenas de texto. Cada elemento dentro de una lista tiene un índice único, lo que facilita su acceso y modificación. Imagina una lista como una fila de personas en una fila de comidas; puedes agregar o eliminar personas fácilmente, y cada persona tiene un lugar específico.

Los conjuntos, por otro lado, son colecciones desordenadas de elementos únicos. Es como tener un grupo de amigos donde nadie se repite. Los conjuntos son ideales para operaciones que requieren la eliminación de duplicados o la verificación de la pertenencia a un conjunto específico.

Los diccionarios son estructuras aún más poderosas, ya que asocian claves con valores. Piensa en ellos como una librería donde cada libro tiene un título único y puedes acceder directamente a él sin necesidad de buscarlo por toda la biblioteca. Los diccionarios son excelentes para almacenar información compleja y recuperarla rápidamente.

La comprensión y uso eficiente de estas estructuras es crucial en cualquier proyecto de programación. No solo facilitan el manejo de grandes cantidades de datos, sino que también optimizan el rendimiento al permitir operaciones como la búsqueda, inserción y eliminación de elementos con una eficiencia notable.

Además, las colecciones ofrecen métodos útiles para manipular los datos almacenados. Por ejemplo, puedes ordenar una lista, combinar dos conjuntos o buscar un valor específico en un diccionario. Estos métodos son como herramientas mágicas que transforman tus datos de manera inteligente.

Es importante recordar que cada estructura tiene sus propias ventajas y desventajas dependiendo del contexto en el que se utilice. Por ejemplo, si necesitas mantener la ordenación de los elementos, una lista podría ser la mejor opción. Sin embargo, si solo necesitas verificar la pertenencia a un conjunto sin importar su orden, un conjunto sería más eficiente.

En resumen, las listas, conjuntos y diccionarios son herramientas poderosas en el arsenal del programador. Cada una tiene su propio propósito y es esencial dominarlas para abordar problemas complejos de manera efectiva. Al aprender a utilizar estas estructuras con inteligencia, podemos crear programas más eficientes, escalables y fáciles de mantener.

La comprensión profunda de las colecciones nos abre el camino hacia la creación de aplicaciones sofisticadas que puedan manejar grandes volúmenes de datos con gracia. Es una habilidad fundamental en cualquier campo relacionado con la programación, y su dominio es un paso crucial hacia la maestría del arte digital.

Así, al explorar las listas, conjuntos y diccionarios, nos encontramos con una puerta que nos lleva a un mundo de posibilidades infinitas. Cada estructura es como una llave que abre una caja mágica, permitiéndonos almacenar, recuperar y manipular datos de manera inteligente y eficiente. Y así, en el vasto universo de la programación, continuamos aprendiendo y creciendo con cada paso que damos.

### diccionarios

```python
# Repaso de listas y tuplas
lista = ["platano","manzana","fresa"]

lista[0] # platano
lista[1] # manzana

tupla = ("platano","manzana","fresa")

tupla[0] # platano
tupla[1] # manzana 
```

### diccionarios ahora si

```python
# Esto sigue siendo una lista
persona = [
  "Jose Vicente",
  "Carratalá Sanchis",
  "info@jocarsa.com",
  47
]

# Ahora en formato diccionario

persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47
}
```

### lista en diccionario

```python
persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47,
  "telefonos":[
  	96345678,
    87654321
  ]
}
```

### lista de diccionarios en diccionario

```python
persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
```

### no argumentos archivo

```python
edad = input("Dime tu edad: ")
entero = int(edad)
doble = entero*2
print(doble)
```

### ahora con argumentos

```python
import sys

print(sys.argv)
```

### doble edad con argumentos

```python
import sys

argumentos = sys.argv
edad = argumentos[1]
entero = int(edad)
doble = entero*2
print(doble)
```

### ejemplo con dos argumentos

```python
import sys

argumentos = sys.argv
nombre = argumentos[1]
edad = argumentos[2]
entero = int(edad)
doble = entero*2
print("Hola, "+nombre+" tienes "+str(doble)+" años")
```

### argumentos con nombre

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--nombre")
parser.add_argument("--apellidos")

args = parser.parse_args()

diccionario = vars(args)
print(diccionario)
```

### instalar y usar ffmpeg

```markdown
sudo apt install ffmpeg

LLamarlo: ffmpeg
```

### acceder a diccionario

```python
persona = {
	"nombre":"Jose Vicente",
  "apellidos":"Carratalá Sanchis",
  "correo":"info@jocarsa.com",
  "edad":47,
  "telefonos":[
  	{	
      "tipo":"fijo",
    	"número":96123455
    },
    {	
      "tipo":"movil",
    	"número":65456546
    }
  ]
}

print(persona)
print(persona["telefonos"][0]["número"])
```

### diagrama

```json
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "389.188px",
      "top": "312px",
      "width": "",
      "height": "",
      "texto": "programa"
    },
    {
      "id": "forma-2",
      "tipo": "circle",
      "left": "356.135px",
      "top": "187px",
      "width": "",
      "height": "",
      "texto": "in"
    },
    {
      "id": "forma-3",
      "tipo": "circle",
      "left": "498.521px",
      "top": "187.333px",
      "width": "",
      "height": "",
      "texto": "out"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "378.521px",
      "top": "49.3229px",
      "width": "",
      "height": "",
      "texto": "html"
    }
  ],
  "flechas": [
    {
      "idInicio": "forma-2",
      "idFin": "forma-1",
      "tipo": "simple"
    },
    {
      "idInicio": "forma-1",
      "idFin": "forma-3",
      "tipo": "simple"
    },
    {
      "idInicio": "forma-4",
      "idFin": "forma-2",
      "tipo": "simple"
    },
    {
      "idInicio": "forma-3",
      "idFin": "forma-4",
      "tipo": "simple"
    }
  ]
}
```

<a id="operaciones-agregadas-filtrado-reduccion-y-recoleccion"></a>
## Operaciones agregadas filtrado, reducción y recolección

En el vasto terreno de la programación, las estructuras de almacenamiento desempeñan un papel fundamental como los pilares que sostienen una construcción. En esta subunidad didáctica, nos adentramos en el fascinante mundo de las operaciones agregadas, filtrado, reducción y recolección, explorando cómo estas técnicas pueden transformar nuestros datos con eficiencia y precisión.

La primera de estas técnicas es la **operación agregada**, que permite realizar cálculos sobre un conjunto de datos para obtener un valor único. Imagina una gran pileta de números; las operaciones agregadas son como los luchadores de sumas, multiplicaciones, promedios y conteos que nos permiten reducir esta multitud a un solo número, revelando patrones y tendencias ocultos.

El **filtrado** es otro poderoso aliado en este viaje. Este proceso selecciona elementos del conjunto original basándose en ciertas condiciones, como si estuviéramos recogiendo las flores de un jardín que cumplen con determinados criterios. El filtrado nos permite concentrarnos en lo relevante y descartar el resto, simplificando así la información a nuestro alcance.

La **reducción** es una técnica que lleva aún más lejos la idea del filtrado. No solo selecciona elementos, sino que también combina o reduce estos elementos hasta obtener un único resultado. Es como si estuviéramos juntando cientos de libros en una sola caja, reduciendo así su volumen y facilitando su manejo.

Finalmente, la **recolección** es el proceso inverso a la creación de estructuras de almacenamiento. Nos permite organizar y recuperar los datos que hemos procesado, asegurándonos de que estén disponibles cuando las necesitemos. Es como recoger los juguetes después del juego para poder jugar nuevamente.

Estas técnicas son esenciales en la programación moderna, ya que nos permiten manejar grandes volúmenes de datos con eficiencia y precisión. Al combinarlas, podemos realizar tareas complejas como análisis de datos, inteligencia artificial y aprendizaje automático, transformando información raw en conocimiento valioso.

En esta subunidad, hemos explorado cómo estas operaciones pueden ser aplicadas en diferentes contextos, desde la manipulación de listas simples hasta el procesamiento de grandes conjuntos de datos. Cada una de ellas es un puente que nos lleva a nuevas posibilidades y descubrimientos, demostrando que con las estructuras de almacenamiento y las operaciones adecuadas, podemos hacer de los datos una herramienta poderosa para resolver problemas complejos.

Así, al adentrarnos en el mundo de las operaciones agregadas, filtrado, reducción y recolección, nos encontramos con un conjunto de habilidades que nos permiten transformar nuestros datos con eficiencia y precisión. Cada una de estas técnicas es un paso importante en nuestro viaje por la programación, demostrando que con el conocimiento adecuado, podemos hacer de los datos una herramienta poderosa para resolver problemas complejos y descubrir patrones ocultos en la información.

### conjuntos

```python
frutas = {"manzanas","peras","platanos"}
print(frutas)
print(type(frutas))
```

### no repeticiones

```python
# No se aplica el concepto de orden
# No se pueden reordenar
# No admiten duplicados

frutas = {"manzanas","peras","platanos","manzanas"}
print(frutas)
print(type(frutas))
```

### dos conjuntos

```python
# No se aplica el concepto de orden
# No se pueden reordenar
# No admiten duplicados

frutas1 = {"manzanas","peras","platanos"}

frutas2 = {"peras","platanos","manzanas"}

if frutas1 == frutas2:
  print("Son iguales")
else:
  print("Son diferentes")
```

### comprobacion numeros

```python
patron = {1,2,3,4,5,6,7,8,9}

prueba = {6,4,3,5,7,8,2,1,9}

if prueba == patron:
  print("Se cumple la condicion")
else:
  print("no se cumple la condición")
```

### aleatorio

```python
import random

patron = {1,2,3,4,5,6,7,8,9}

lista = []
for i in range(1,10):
	lista.append(random.randint(1,9))
print(patron)
print(lista)
conjunto = set(lista)
print(conjunto)

if conjunto == patron:
  print("El conjunto es correcto")
else:
  print("El conjunto no es correcto")
```

### fuerza bruta

```python
import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
  lista = []
  for i in range(1,10):
    lista.append(random.randint(1,9))
    
  conjunto = set(lista)
  print(lista)
  
  if conjunto == patron:
    print("El conjunto es correcto")
    print(conjunto)
    print(lista)
    break # Fuerzo la finalizazión del bucle infinito
    

  
```

### elimino un numero

```python
import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
  lista = []
  for i in range(1,10):
    lista.append(random.randint(1,9))
  conjunto = set(lista)
  if conjunto == patron:
    print("El conjunto es correcto")
    print(conjunto)
    print(lista)
    # Ahora elimino un numero
    indice = random.randint(1,9)
    lista[indice] = "_"
    print(lista)
    break # Fuerzo la finalizazión del bucle infinito
    

  
```

### elimino X numeros

```python
import random

patron = {1,2,3,4,5,6,7,8,9}

while True:
  lista = []
  for i in range(1,10):
    lista.append(random.randint(1,9))
  conjunto = set(lista)
  if conjunto == patron:
    print("El conjunto es correcto")
    print(conjunto)
    print(lista)
    for i in range(1,5):
      # Ahora elimino un numero
      indice = random.randint(0,8)
      lista[indice] = "_" # Escoge un indice al azar y reemplaza su valor
    print(lista)
    break # Fuerzo la finalizazión del bucle infinito
    

  
```

### repito 9 veces

```python
import random

patron = {1,2,3,4,5,6,7,8,9}

for celda in range(1,10):
  while True:
    lista = []
    for i in range(1,10):
      lista.append(random.randint(1,9))
    conjunto = set(lista)
    if conjunto == patron:
      print("El conjunto es correcto")
      print(conjunto)
      print(lista)
      break # Fuerzo la finalizazión del bucle infinito
    

  
```

### matriz bidimensional

```python
import random

patron = {1,2,3,4,5,6,7,8,9}
sudoku = []
for celda in range(1,10):
  while True:
    lista = []
    for i in range(1,10):
      lista.append(random.randint(1,9))
    conjunto = set(lista)
    if conjunto == patron:
      sudoku.append(lista)
      break # Fuerzo la finalizazión del bucle infinito
    
print(sudoku)
  
```

### flask

```python
import random
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def inicio():
  patron = {1,2,3,4,5,6,7,8,9}
  sudoku = []
  for celda in range(1,10):
    while True:
      lista = []
      for i in range(1,10):
        lista.append(random.randint(1,9))
      conjunto = set(lista)
      if conjunto == patron:
        sudoku.append(lista)
        break # Fuerzo la finalizazión del bucle infinito

  return render_template("index.html",datos=sudoku)

if __name__ == "__main__":
  app.run(debug=True)
  
```

### flask con contador

```python
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    contador = 0
    patron = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    sudoku = []

    for celda in range(1, 10):
        while True:
            contador += 1
            lista = []
            for i in range(1, 10):
                lista.append(random.randint(1, 9))
            conjunto = set(lista)
            if conjunto == patron:
                sudoku.append(lista)
                break  # Fuerzo la finalización del bucle infinito

    print("He necesitado, con fuerza bruta, " + str(contador) + " intentos")
    return render_template("index.html", datos=sudoku)

if __name__ == "__main__":
    app.run(debug=True)
```

### calculo completo

```python
import random
from flask import Flask, render_template

app = Flask(__name__)

PATRON = set(range(1, 10))  # {1,2,3,4,5,6,7,8,9}


def generar_fila():
    """Genera una permutación aleatoria de 1..9."""
    fila = list(range(1, 10))
    random.shuffle(fila)
    return fila


def filas_validas(sudoku):
    """Todas las filas contienen exactamente los números 1..9."""
    for fila in sudoku:
        if set(fila) != PATRON:
            return False
    return True


def columnas_validas(sudoku):
    """Todas las columnas contienen exactamente los números 1..9."""
    for c in range(9):
        columna = [sudoku[f][c] for f in range(9)]
        if set(columna) != PATRON:
            return False
    return True


def sudoku_a_bloques(sudoku):
    """
    Convierte el sudoku (9 filas x 9 columnas) en 9 bloques 3x3.
    Cada bloque es una lista de 9 números, en orden de lectura.
    """
    bloques = []
    for br in range(3):          # bloque fila
        for bc in range(3):      # bloque columna
            bloque = []
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[r][c])
            bloques.append(bloque)
    return bloques


@app.route("/")
def inicio():
    intentos = 0

    # Fuerza bruta: generar tableros al azar hasta que filas y columnas sean válidas
    while True:
        intentos += 1
        sudoku = [generar_fila() for _ in range(9)]

        if filas_validas(sudoku) and columnas_validas(sudoku):
            break

    print(f"He necesitado, con fuerza bruta, {intentos} intentos")

    # Adaptamos a tu HTML: 9 bloques 3x3
    datos = sudoku_a_bloques(sudoku)

    return render_template("index.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
```

### mas eficiente

```python
import random
from flask import Flask, render_template

app = Flask(__name__)


def es_valido(grid, fila, col, num):
    """Comprueba si `num` puede ponerse en grid[fila][col]."""

    # Fila
    if num in grid[fila]:
        return False

    # Columna
    for f in range(9):
        if grid[f][col] == num:
            return False

    # Bloque 3x3
    bloque_fila = (fila // 3) * 3
    bloque_col = (col // 3) * 3
    for f in range(bloque_fila, bloque_fila + 3):
        for c in range(bloque_col, bloque_col + 3):
            if grid[f][c] == num:
                return False

    return True


def resolver_sudoku(grid):
    """
    Backtracking: intenta rellenar la cuadrícula.
    Devuelve True si se ha podido resolver, False si no.
    """

    # Buscar la siguiente celda vacía (0)
    for fila in range(9):
        for col in range(9):
            if grid[fila][col] == 0:
                # Probamos números del 1 al 9 en orden aleatorio
                candidatos = list(range(1, 10))
                random.shuffle(candidatos)

                for num in candidatos:
                    if es_valido(grid, fila, col, num):
                        grid[fila][col] = num
                        if resolver_sudoku(grid):
                            return True
                        # backtrack
                        grid[fila][col] = 0

                # Si ningún número sirve, devolvemos False
                return False

    # Si no quedan celdas vacías, está resuelto
    return True


def generar_sudoku_completo():
    """Genera un sudoku completo válido (9x9) usando backtracking."""
    grid = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(grid)
    return grid


def sudoku_a_bloques(sudoku):
    """
    Convierte el sudoku (9x9) en 9 bloques 3x3.
    Cada bloque es una lista de 9 números.
    """
    bloques = []
    for br in range(3):          # bloque fila
        for bc in range(3):      # bloque columna
            bloque = []
            for r in range(br * 3, br * 3 + 3):
                for c in range(bc * 3, bc * 3 + 3):
                    bloque.append(sudoku[r][c])
            bloques.append(bloque)
    return bloques


@app.route("/")
def inicio():
    sudoku = generar_sudoku_completo()
    datos = sudoku_a_bloques(sudoku)
    return render_template("index2.html", datos=datos)


if __name__ == "__main__":
    app.run(debug=True)
```


<a id="utilizacion-avanzada-de-clases"></a>
# Utilización avanzada de clases

<a id="repaso"></a>
## Repaso

### Npc

```python
# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personaje1 = Npc(4,3)
personaje2 = Npc(5,4)

print(personaje1)
print(personaje2)
```

### lista de npc

```python
# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []

personajes.append(Npc(4,3))
personajes.append(Npc(3,4))

print(personajes)
```

### ahora muchos personajes

```python
# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
	personajes.append(Npc(4,3))

print(personajes)
```

### posicion aleatoria

```python
# Non Playable Character
import random

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []
numero_personajes = 50

for i in range(0,numero_personajes):
	xaleatoria = random.randint(0,500)
	yaleatoria = random.randint(0,500)
	personajes.append(Npc(xaleatoria,yaleatoria))

print(personajes)
```

### imprimo como json

```python
import random
import json

class Npc():
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy}

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    personajes.append(Npc(xaleatoria, yaleatoria))

# Convertimos todos los NPC a diccionarios
personajes_json = [p.to_dict() for p in personajes]

# Lo imprimimos formateado
print(json.dumps(personajes_json, indent=2))
```

### flask

```python
import random
import json
from flask import Flask,render_template

class Npc():
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy}
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    personajes.append(Npc(xaleatoria, yaleatoria))

personajes_json = [p.to_dict() for p in personajes]

# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
```

### nuevo parametro

```python
import random
import json
from flask import Flask,render_template

class Npc():
    def __init__(self, x, y,radio):
        self.posx = x
        self.posy = y
        self.radio = radio

    # Método para convertir el objeto en diccionario
    def to_dict(self):
        return {"posx": self.posx, "posy": self.posy,"radio":self.radio}
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
    xaleatoria = random.randint(0, 500)
    yaleatoria = random.randint(0, 500)
    radioaleatorio = random.randint(10, 30)
    personajes.append(Npc(xaleatoria, yaleatoria,radioaleatorio))

personajes_json = [p.to_dict() for p in personajes]

# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
```

### muevo personajes

```python
import random
import json
from flask import Flask,render_template

class Npc():
	def __init__(self, x, y,radio):
		self.posx = x
		self.posy = y
		self.radio = radio

	def to_dict(self):
		return {"posx": self.posx, "posy": self.posy,"radio":self.radio}
	def mover(self):
		self.posx += random.randint(-5,5)	# Muevete un poco en X
		self.posy += random.randint(-5,5)	# Muevete un poco en Y
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	personajes.append(Npc(xaleatoria, yaleatoria,radioaleatorio))



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
```

### Muevo personajes pero con trigonometria

```python
import random
import json
from flask import Flask,render_template
import math # Para poder hacer trigonometria

class Npc():
	def __init__(self, x, y,radio,direccion):
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion # NUEVO

	def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion # NUEVO
    }
	def mover(self):
		self.posx += math.cos(self.direccion) # NUEVO
		self.posy += math.sin(self.direccion) # NUEVO
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2  # NUEVO
	personajes.append(
    Npc(xaleatoria, yaleatoria,radioaleatorio,direccionaleatoria) # NUEVO
  )



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
```

### creamos velocidad

```python
import random
import json
from flask import Flask,render_template
import math # Para poder hacer trigonometria

class Npc():
	def __init__(self, x, y,radio,direccion,velocidad): # NUEVO
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion 
		self.velocidad = velocidad # NUEVO

	def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion 
    }
	def mover(self):
		self.posx += math.cos(self.direccion)*self.velocidad # NUEVO
		self.posy += math.sin(self.direccion)*self.velocidad # NUEVO
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2 
	velocidadaleatoria = random.random()*5 # NUEVO
	personajes.append(
    Npc(
      xaleatoria, 
      yaleatoria,
      radioaleatorio,
      direccionaleatoria,
      velocidadaleatoria # NUEVO
    ) 
  )



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
```

### angulo cambia random

```python
import random
import json
from flask import Flask,render_template
import math # Para poder hacer trigonometria

class Npc():
	def __init__(self, x, y,radio,direccion,velocidad): 
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion 
		self.velocidad = velocidad 

	def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion 
    }
	def mover(self):
		# Aplicamos variacion de la direccion con el tiempo
		self.direccion += (random.random() - 0.5) * 0.2  # NUEVO
		self.posx += math.cos(self.direccion)*self.velocidad
		self.posy += math.sin(self.direccion)*self.velocidad 
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2 
	velocidadaleatoria = random.random()*5 
	personajes.append(
    Npc(
      xaleatoria, 
      yaleatoria,
      radioaleatorio,
      direccionaleatoria,
      velocidadaleatoria 
    ) 
  )



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
```

### colision

```python
import random
import json
from flask import Flask,render_template
import math # Para poder hacer trigonometria

class Npc():
	def __init__(self, x, y,radio,direccion,velocidad): 
		self.posx = x
		self.posy = y
		self.radio = radio
		self.direccion = direccion 
		self.velocidad = velocidad 

	def to_dict(self):
		return {
      "posx": self.posx, 
      "posy": self.posy,
      "radio": self.radio,
    	"direccion": self.direccion 
    }
	def mover(self):
		# Aplicamos variacion de la direccion con el tiempo
		self.direccion += (random.random() - 0.5) * 0.2
    # Colision con paredes en mover
		if self.posx > 500 or self.posx < 0 or self.posy > 500 or self.posy < 0: # NUEVO
      	# El personaje se da la vuelta
				self.direccion += math.pi # NUEVO
		self.posx += math.cos(self.direccion)*self.velocidad
		self.posy += math.sin(self.direccion)*self.velocidad 
# Preparo los personajes

personajes = []
numero_personajes = 50

for i in range(0, numero_personajes):
	xaleatoria = random.randint(0, 500)
	yaleatoria = random.randint(0, 500)
	radioaleatorio = random.randint(10, 30)
	direccionaleatoria = random.random()*math.pi*2 
	velocidadaleatoria = random.random()*5 
	personajes.append(
    Npc(
      xaleatoria, 
      yaleatoria,
      radioaleatorio,
      direccionaleatoria,
      velocidadaleatoria 
    ) 
  )



# Lanzo una web

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("juego.html")

@app.route("/api")
def api():
  # Primero muevo todos los personajes
  for personaje in personajes:	
    personaje.mover()
  personajes_json = [p.to_dict() for p in personajes]
  return json.dumps(personajes_json, indent=2)
  
if __name__ == "__main__":
  app.run(debug=True)
  
  
  
  
```

### diagrama (1)

```python
from typing import Optional

class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, apellidos: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r})"

class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"

class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"

    # FK1: cliente_id -> cliente.id

class Lineaspedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, pedido_id: Optional[int] = None, producto_id: Optional[int] = None, cantidad: Optional[str] = None):
        self.id = id
        self.fecha = fecha
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad

    def __repr__(self):
        return f"Lineaspedido(id={self.id!r}, fecha={self.fecha!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r}, cantidad={self.cantidad!r})"

    # FK1: pedido_id -> pedido.id
    # FK2: producto_id -> producto.id
```

### diagrama

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Diagrama exportado</title>
<style>
body {
  margin: 0;
  padding: 20px;
  background: #f3f3f7;
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}
.page {
  position: relative;
  background: #ffffff;
  border: 1px solid #d1d5db;
  box-shadow: 0 2px 4px rgba(0,0,0,.1);
  width: 374px;
  height: 248.69998168945307px;
  overflow: visible;
}

/* formas básicas */
.shape {
  position: absolute;
  min-width: 120px;
  min-height: 40px;
  padding: 6px 10px;
  background: #ffffff;
  border-radius: 4px;
  border: 1px solid #9ca3af;
  box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 13px;
}

.shape.rectangle {
  border-radius: 4px;
}

.shape.pill {
  border-radius: 999px;
}

.shape.circle {
  border-radius: 999px;
  width: 80px;
  height: 80px;
  padding: 0;
  justify-content: center;
}

/* base de datos */
.shape.db {
  min-width: 120px;
  min-height: 60px;
  padding-top: 20px;
  border-radius: 60px / 16px;
  background: linear-gradient(180deg, #e5e7eb 0%, #ffffff 40%, #e5e7eb 100%);
  position: absolute;
  overflow: hidden;
  text-align: center;
}
.shape.db::before {
  content: "";
  position: absolute;
  top: 0;
  left: 8px;
  right: 8px;
  height: 18px;
  border-radius: 999px;
  border: 1px solid #9ca3af;
  background: radial-gradient(circle at 50% 30%, #ffffff 0%, #e5e7eb 70%);
}
.shape.db::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 8px;
  right: 8px;
  height: 18px;
  border-radius: 999px;
  border: 1px solid rgba(156, 163, 175, 0.6);
  border-top: none;
  background: radial-gradient(circle at 50% 70%, #e5e7eb 0%, #d1d5db 70%);
}

/* entidades ER */
.shape.entity {
  width: 220px;
  min-height: 80px;
  background: #ffffff;
  border: 2px solid #111827;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0,0,0,.15);
  display: flex;
  flex-direction: column;
  font-size: 13px;
  overflow: hidden;
  padding: 0;
}
.entity-header {
  background: #f3f4f6;
  padding: 4px 8px;
  font-weight: 600;
  text-align: center;
  border-bottom: 1px solid #e5e7eb;
}
.entity-properties {
  flex: 1;
  padding: 4px 4px 0 4px;
}
.entity-property {
  display: grid;
  grid-template-columns: 14px 1fr 14px;
  align-items: center;
  column-gap: 4px;
  padding: 2px 0;
}
.entity-property .property-name {
  padding: 2px 4px;
  border-radius: 3px;
}

/* puertos */
.port {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  border: 1px solid #111827;
  background: #ffffff;
}
.port-left { justify-self: start; }
.port-right { justify-self: end; }

/* flechas rectas */
.arrow {
  position: absolute;
  height: 2px;
  background: #111827;
  transform-origin: 0 50%;
}
.arrow::after {
  content: "";
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}
.arrow-double::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%) rotate(180deg);
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}

/* flechas ortogonales */
.ortho-arrow {
  position: absolute;
  left: 0;
  top: 0;
}
.ortho-arrow .ortho-seg {
  position: absolute;
  background: #111827;
}
.ortho-seg.seg-horizontal { height: 2px; }
.ortho-seg.seg-vertical { width: 2px; }
.ortho-arrowhead {
  position: absolute;
  width: 0;
  height: 0;
}
.ortho-arrowhead.dir-right {
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-left: 8px solid #111827;
}
.ortho-arrowhead.dir-left {
  border-top: 5px solid transparent;
  border-bottom: 5px solid transparent;
  border-right: 8px solid #111827;
}
.ortho-arrowhead.dir-down {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 8px solid #111827;
}
.ortho-arrowhead.dir-up {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-bottom: 8px solid #111827;
}
</style>
</head>
<body>
<div class="page">

<div class="shape rectangle" style="left:133.43749999999994px;top:168.69998168945307px;width:119.99999999999994px;height:39.999999999999986px;">python</div>
<div class="shape rectangle" style="left:132.99999999999994px;top:128.49999999999994px;width:119.99999999999994px;height:39.99998855590819px;">flask</div>
<div class="shape rectangle" style="left:40px;top:41px;width:119.99999999999994px;height:39.999999999999986px;">html (en/)</div>
<div class="shape rectangle" style="left:214px;top:40px;width:119.99999999999994px;height:39.999999999999986px;">json (/api)</div>
<div class="arrow" style="left:171.742861834468px;top:128.49999999999994px;width:69.31852335628878px;transform:rotate(-2.386656011696309rad);"></div>
<div class="arrow" style="left:211.30508069216717px;top:128.49999999999994px;width:65.74729885991071px;transform:rotate(-0.829617075591497rad);"></div>
<div class="arrow" style="left:214px;top:60.34482758620686px;width:54.00089178811781px;transform:rotate(3.1358455904265896rad);"></div>
</div>
</body>
</html>
```

### diagrama

```json
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "466px",
      "top": "287.2px",
      "width": "",
      "height": "",
      "texto": "python"
    },
    {
      "id": "forma-2",
      "tipo": "rectangle",
      "left": "465.563px",
      "top": "247px",
      "width": "",
      "height": "",
      "texto": "flask"
    },
    {
      "id": "forma-3",
      "tipo": "rectangle",
      "left": "372.563px",
      "top": "159.5px",
      "width": "",
      "height": "",
      "texto": "html (en/)"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "546.563px",
      "top": "158.5px",
      "width": "",
      "height": "",
      "texto": "json (/api)"
    }
  ],
  "flechas": [
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-2",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-4",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    }
  ]
}
```

### diagrama

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int] = None
    nombre: Optional[str] = None
    apellidos: Optional[str] = None

@dataclass
class Producto:
    id: Optional[int] = None
    nombre: Optional[str] = None
    precio: Optional[str] = None

@dataclass
class Pedido:
    id: Optional[int] = None
    fecha: Optional[str] = None
    cliente_id: Optional[int] = None

    # FK1: cliente_id -> cliente.id

@dataclass
class Lineaspedido:
    id: Optional[int] = None
    fecha: Optional[str] = None
    pedido_id: Optional[int] = None
    producto_id: Optional[int] = None
    cantidad: Optional[str] = None

    # FK1: pedido_id -> pedido.id
    # FK2: producto_id -> producto.id
```

### diagrama

```
<svg xmlns="http://www.w3.org/2000/svg" width="374" height="248.69998168945307" viewBox="0 0 374 248.69998168945307">

  <defs>
    <style>
      text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; font-size: 12px; fill: #111827; }
      .shape-rect { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-entity { fill: #ffffff; stroke: #111827; stroke-width: 2; }
      .shape-circle { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-pill { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .shape-db { fill: #ffffff; stroke: #9ca3af; stroke-width: 1; }
      .conn { stroke: #111827; stroke-width: 2; fill: none; }
    </style>
    <marker id="arrow-end" markerWidth="10" markerHeight="7" refX="10" refY="3.5"
            orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 10 3.5, 0 7" fill="#111827"/>
    </marker>
    <marker id="arrow-start" markerWidth="10" markerHeight="7" refX="0" refY="3.5"
            orient="auto" markerUnits="strokeWidth">
      <polygon points="10 0, 0 3.5, 10 7" fill="#111827"/>
    </marker>
  </defs>
        
<rect class="shape-rect" x="133.43749999999994" y="168.69998168945307" width="119.99999999999994" height="39.999999999999986" rx="4" ry="4" />
<text x="193.43749999999991" y="192.69998168945307" text-anchor="middle">python</text>
<rect class="shape-rect" x="132.99999999999994" y="128.49999999999994" width="119.99999999999994" height="39.99998855590819" rx="4" ry="4" />
<text x="192.99999999999991" y="152.49999427795404" text-anchor="middle">flask</text>
<rect class="shape-rect" x="40" y="41" width="119.99999999999994" height="39.999999999999986" rx="4" ry="4" />
<text x="99.99999999999997" y="65" text-anchor="middle">html (en/)</text>
<rect class="shape-rect" x="214" y="40" width="119.99999999999994" height="39.999999999999986" rx="4" ry="4" />
<text x="274" y="63.99999999999999" text-anchor="middle">json (/api)</text>
<path class="conn" d="M 171.742861834468 128.49999999999994 L 121.25714424724976 80.99999999999997" marker-end="url(#arrow-end)" />
<path class="conn" d="M 211.30508069216717 128.49999999999994 L 255.69491407070575 79.99999999999997" marker-end="url(#arrow-end)" />
<path class="conn" d="M 214 60.34482758620686 L 160 60.65517241379308" marker-end="url(#arrow-end)" />
</svg>
```

<a id="composicion-de-clases"></a>
## Composición de clases

La composición de clases es una técnica poderosa que permite modelar relaciones complejas entre objetos, creando estructuras más ricas y realistas. En este submódulo, profundizaremos en cómo esta práctica puede ser aplicada para mejorar la modularidad y el reutilización del código.

Comenzamos por entender qué es la composición de clases. Esta relación se caracteriza por un objeto que contiene otros objetos como partes de sí mismo. Por ejemplo, podríamos tener una clase `Coche` que compone varios objetos internos como `Motor`, `Ruedas`, `Chofer` y `Pasajeros`. Cada uno de estos componentes es una instancia de otra clase, y juntos forman un objeto más complejo.

La composición nos permite crear jerarquías de clases más elaboradas. Por ejemplo, podríamos tener una clase `Empresa` que compone varias clases internas como `Departamento`, `Equipo`, `Proyecto` y `Colaborador`. Cada uno de estos componentes puede a su vez contener otros objetos, creando una estructura anidada y detallada.

La composición también nos permite implementar la responsabilidad única. En lugar de que un objeto haga todo el trabajo por sí mismo, lo delegamos a sus componentes internos. Esto hace que nuestro código sea más limpio, más fácil de mantener y más fácil de probar.

Además, la composición nos permite crear objetos más flexibles y adaptados a las necesidades cambiantes. Si necesitamos cambiar el comportamiento de un componente interno, podemos hacerlo sin afectar el objeto que lo contiene. Esto es especialmente útil en aplicaciones empresariales donde los requisitos pueden variar rápidamente.

La composición también nos permite implementar la inyección de dependencias. En lugar de crear objetos internos dentro del constructor de un objeto, podemos inyectarlos desde fuera. Esto hace que nuestro código sea más testable y más fácil de mantener.

En resumen, la composición de clases es una técnica poderosa que nos permite modelar relaciones complejas entre objetos, creando estructuras más ricas y realistas. Permite implementar la responsabilidad única, crear objetos más flexibles y adaptados a las necesidades cambiantes, e implementar la inyección de dependencias. Es una práctica fundamental en el diseño de software orientado a objetos y es esencial para crear aplicaciones empresariales robustas y escalables.

<a id="herencia-y-polimorfismo"></a>
## Herencia y polimorfismo

La herencia y el polimorfismo son pilares fundamentales de la programación orientada a objetos (POO), ofreciendo soluciones elegantes para organizar y reutilizar código. En esta subunidad didáctica, nos adentramos en estos conceptos con profundidad, explorando cómo permiten crear jerarquías de clases y cómo facilitan el desarrollo de aplicaciones más complejas.

La herencia es un principio que permite a una clase derivada (o subclase) heredar atributos y métodos de una clase base (o superclase). Esta relación natural entre clases, similar a la existente en la vida real, nos permite crear estructuras de datos más sofisticadas. Por ejemplo, si tenemos una clase `Animal` con propiedades comunes como `nombre` y `edad`, podemos derivar clases específicas como `Perro` y `Gato`, que heredan estas características pero también pueden añadir propiedades únicas.

El polimorfismo, por otro lado, se refiere a la capacidad de un objeto para responder a una misma llamada en diferentes formas. En el contexto de la POO, esto significa que podemos usar objetos de clases derivadas donde se espera un objeto de una clase base, siempre y cuando las clases derivadas implementen los métodos necesarios. Este concepto es crucial para crear código flexible y escalable, ya que nos permite tratar diferentes tipos de objetos de manera uniforme.

En esta subunidad, exploraremos cómo definir clases base y derivadas, cómo utilizar el operador `extends` para establecer relaciones de herencia, y cómo sobrescribir métodos en las clases derivadas. También aprenderemos sobre la visibilidad de los miembros de una clase (públicos, privados, protegidos) y cómo manejar la herencia múltiple, aunque con ciertas limitaciones.

Además, profundizaremos en el polimorfismo, aprendiendo a utilizar interfaces para definir contratos comunes entre clases, así como a implementar métodos abstractos en las clases base. También exploraremos cómo usar el operador `instanceof` para verificar la instancia de un objeto y cómo aplicar el polimorfismo en situaciones prácticas.

A lo largo de esta subunidad, trabajaremos con ejemplos prácticos que demuestran cómo aplicar la herencia y el polimorfismo en diferentes escenarios. Estos ejemplos nos ayudarán a entender cómo estos conceptos pueden ser utilizados para crear código más limpio, modular y fácil de mantener.

Finalmente, reflexionaremos sobre las ventajas y desventajas de utilizar la herencia y el polimorfismo en nuestro código. Aprenderemos cómo identificar situaciones en las que estos principios son especialmente útiles y cómo evitar abusar de ellos para mantener un diseño limpio y coherente.

En resumen, esta subunidad didáctica es una exploración profunda de la herencia y el polimorfismo en la programación orientada a objetos. A través de conceptos teóricos, ejemplos prácticos y reflexiones sobre su aplicación, nos prepararemos para abordar problemas más complejos y desarrollar aplicaciones más robustas y escalables.

<a id="jerarquia-de-clases-superclases-y-subclases"></a>
## Jerarquía de clases Superclases y subclases

La jerarquía de clases es un concepto fundamental en la programación orientada a objetos (POO), que permite organizar y reutilizar el código de manera eficiente. En esta subunidad, exploraremos cómo definir superclases y subclases, así como cómo utilizarlas para crear una estructura lógica y coherente en nuestros programas.

En primer lugar, es importante entender qué son las superclases y las subclases. Una superclase, también conocida como clase base o clase padre, es aquella que define un conjunto de atributos y métodos comunes para varias clases relacionadas. Por otro lado, una subclase, también llamada clase derivada o clase hija, hereda los atributos y métodos de la superclase y puede añadir nuevos o modificar los existentes.

La creación de una jerarquía de clases empieza con la definición de la superclase. Esta clase actúa como un molde que proporciona las características básicas que serán compartidas por todas las subclases. Por ejemplo, si estamos desarrollando un sistema para gestionar diferentes tipos de vehículos, podríamos crear una superclase llamada "Vehículo" con atributos como marca, modelo y año de fabricación.

Una vez definida la superclase, podemos crear subclases que hereden sus características. Por ejemplo, podríamos crear una subclase llamada "Coche" que herede de "Vehículo". La clase "Coche" podría añadir atributos específicos como número de puertas y color, o incluso sobrescribir métodos de la superclase para adaptarlos a las necesidades particulares del coche.

La jerarquía de clases no se limita a una sola nivel. Es posible tener subclases que hereden de otras subclases, creando así una estructura jerárquica. Por ejemplo, si tenemos una superclase "Automóvil" y dos subclases "Coche" y "Motocicleta", podríamos crear una subclase adicional llamada "SUV" que herede de "Coche". De esta manera, la clase "SUV" tendría todos los atributos y métodos de la superclase "Coche", además de los específicos de un SUV.

La utilización de jerarquías de clases ofrece varias ventajas. En primer lugar, permite una mayor reutilización del código, ya que las subclases pueden heredar los atributos y métodos comunes definidos en la superclase. Esto reduce la redundancia y facilita el mantenimiento del código.

Además, la jerarquía de clases mejora la organización lógica del programa. Al agrupar clases relacionadas bajo una superclase común, se facilita su comprensión y uso. Las subclases pueden ser vistas como extensiones o variaciones de la superclase, lo que hace que el código sea más intuitivo y fácil de navegar.

La herencia también permite la sobrescritura de métodos en las subclases. Esto significa que una subclase puede modificar el comportamiento de un método definido en su superclase para adaptarlo a sus necesidades específicas. Por ejemplo, si tenemos un método "arrancar" en la superclase "Vehículo", podemos sobrescribirlo en la subclase "Coche" para añadir funcionalidades adicionales como encender el aire acondicionado.

La utilización de jerarquías de clases también facilita la implementación de polimorfismo. El polimorfismo es un concepto que permite tratar objetos de diferentes clases de manera uniforme, siempre y cuando compartan una interfaz común definida en su superclase. Esto significa que podemos escribir código que funcione con cualquier objeto que herede de la superclase, independientemente del tipo específico de subclase.

En resumen, la jerarquía de clases es un poderoso mecanismo en la programación orientada a objetos que permite organizar y reutilizar el código de manera eficiente. Al definir superclases y subclases, podemos crear una estructura lógica y coherente que facilita la comprensión y uso del programa. La utilización de jerarquías de clases ofrece ventajas como la reutilización del código, la organización lógica del programa y el soporte para el polimorfismo, lo que hace que nuestro código sea más robusto, escalable y fácil de mantener.

<a id="clases-y-metodos-abstractos-y-finales"></a>
## Clases y métodos abstractos y finales

En la subunidad "Clases y métodos abstractos y finales", nos adentramos en conceptos avanzados de programación orientada a objetos que son fundamentales para el diseño robusto y escalable de aplicaciones. Comenzamos por entender los métodos abstractos, que son declaraciones de métodos sin implementación en la clase abstracta. Estos métodos deben ser implementados por cualquier subclase concreta, lo que asegura una interfaz común mientras permite la diversidad en las implementaciones específicas.

Continuando, exploramos los métodos finales, que son métodos declarados como finales dentro de una clase y no pueden ser sobrescritos por ninguna subclase. Esta característica es útil para proteger el comportamiento predefinido de un método, garantizando que ciertos aspectos del diseño sean inmutables y consistentes a lo largo de la jerarquía de clases.

La combinación de métodos abstractos y finales permite crear una estructura de clases donde se definen las interfaces necesarias para el comportamiento esperado, mientras se protegen ciertas implementaciones específicas. Este enfoque es especialmente útil en patrones de diseño como los Singleton o los Factory Methods, donde se requiere un control preciso sobre la creación y modificación de objetos.

Además, aprendemos que las clases abstractas pueden contener tanto métodos abstractos como finales, lo que permite una flexibilidad completa en el diseño. Las clases abstractas actúan como plantillas para sus subclases, proporcionando un esqueleto común mientras permiten la personalización necesaria.

Es importante destacar que los métodos abstractos y finales trabajan juntos para crear una jerarquía de clases coherente y segura. Los métodos abstractos aseguran que ciertos comportamientos sean implementados, mientras que los métodos finales protegen esos comportamientos contra modificaciones no deseadas.

En el contexto práctico, estos conceptos se aplican en la creación de frameworks y bibliotecas donde se requiere una estructura definida pero con la posibilidad de extensión. Por ejemplo, un framework puede proporcionar métodos abstractos para operaciones esenciales mientras permite a los desarrolladores sobrescribir solo las partes específicas que necesitan ser personalizadas.

Finalmente, reflexionamos sobre cómo estos conceptos pueden facilitar el mantenimiento y la evolución de software. Al definir interfaces claras con métodos abstractos y proteger comportamientos críticos con métodos finales, se reduce la complejidad del código y aumenta su resistencia a cambios.

En resumen, "Clases y métodos abstractos y finales" es una subunidad crucial en el aprendizaje de la programación orientada a objetos. A través de estos conceptos avanzados, los desarrolladores pueden crear sistemas más robustos, seguros y fácilmente mantenibles, lo que es fundamental para el éxito del desarrollo de software moderno.

<a id="interfaces"></a>
## Interfaces

Las interfaces en programación son una herramienta poderosa que permite definir un contrato común entre diferentes clases o componentes de software. En esta subunidad didáctica, exploraremos cómo las interfaces funcionan, cuándo deberíamos utilizarlas y cómo implementarlas de manera efectiva.

La primera parte del contenido se centra en la comprensión básica de qué es una interfaz. Se explica que una interfaz define un conjunto de métodos y propiedades que deben ser implementados por cualquier clase que quiera adoptar ese contrato. Esta definición abstracta permite a diferentes clases compartir comportamientos comunes sin necesidad de conocer su estructura interna.

A continuación, se aborda la importancia práctica de las interfaces en el diseño de software. Se destaca cómo permiten una mayor flexibilidad y reutilización del código, ya que cualquier clase puede implementar varias interfaces, lo que facilita la creación de sistemas modulares y escalables.

El contenido también incluye explicaciones sobre cómo declarar e implementar interfaces en diferentes lenguajes de programación. Se proporcionan ejemplos prácticos para mostrar cómo se pueden definir métodos abstractos y cómo las clases concretas deben proporcionar la implementación de estos métodos.

Además, se discute el concepto de polimorfismo a través de interfaces. Se explica que una interfaz puede ser utilizada como tipo de dato, lo que permite tratar diferentes objetos de manera uniforme en función del contrato definido por la interfaz, independientemente de su clase concreta.

El texto también aborda el uso de interfaces para crear sistemas decoupled (desacoplados), lo que facilita la mantenibilidad y la evolución del código. Se explican cómo las interfaces actúan como una barrera entre diferentes partes del sistema, reduciendo así la dependencia directa entre ellas.

Se proporcionan ejemplos de aplicaciones prácticas donde el uso de interfaces ha sido beneficioso, como en sistemas de plugins o en arquitecturas basadas en eventos. Se destaca cómo las interfaces permiten una mayor extensibilidad y personalización del software sin modificar su código base.

El contenido también incluye explicaciones sobre cómo manejar la implementación de interfaces en proyectos de equipo. Se discute el uso de herramientas como las interfaces gráficas para diseñar contratos de interfaz, así como prácticas recomendadas para la documentación y la revisión del código que implementa estas interfaces.

Finalmente, se aborda el tema de la evolución de interfaces a lo largo del tiempo. Se explica cómo las interfaces pueden ser modificadas o actualizadas sin afectar los componentes que las utilizan, siempre y cuando sigan cumpliendo con su contrato original.

En resumen, esta subunidad didáctica proporciona una visión completa y práctica de las interfaces en programación, desde su definición básica hasta sus aplicaciones en proyectos reales. Se enfoca en la comprensión profunda de cómo funcionan las interfaces y cómo pueden ser utilizadas para mejorar la estructura y el mantenimiento del código.

<a id="sobreescritura-de-metodos"></a>
## Sobreescritura de métodos

La sobreescritura de métodos es una técnica fundamental en la programación orientada a objetos que permite redefinir el comportamiento de un método heredado en una subclase. Este proceso es esencial para mantener la cohesión del diseño, permitiendo adaptar las funcionalidades específicas de cada clase sin alterar su estructura básica.

En el contexto de la programación orientada a objetos, cada objeto pertenece a una clase, que define sus atributos y métodos. Cuando una subclase hereda de una superclase, puede optar por redefinir los métodos de la superclase para adaptarlos a sus necesidades específicas. Esta práctica es conocida como sobreescritura o polimorfismo.

La sobreescritura se realiza mediante el uso del mismo nombre y firma (parámetros) que el método en la superclase, pero con un comportamiento diferente. Al llamar al método desde una instancia de la subclase, se ejecuta el método redefinido en lugar del original de la superclase.

Este mecanismo es poderoso porque permite mantener la jerarquía de clases y la cohesión del diseño, mientras que proporciona flexibilidad para adaptar las funcionalidades específicas de cada subclase. La sobreescritura es una herramienta fundamental en la programación orientada a objetos, permitiendo crear sistemas más modulares y escalables.

La sobreescritura también facilita la extensión del comportamiento de los métodos heredados. Al redefinir un método, se puede añadir nueva funcionalidad sin modificar el código original de la superclase. Esto es especialmente útil cuando se desea personalizar el comportamiento de una clase sin alterar su estructura básica.

Además, la sobreescritura permite la creación de métodos virtuales o abstractos en las superclases. Los métodos virtuales son aquellos que pueden ser redefinidos en subclases, mientras que los métodos abstractos no tienen implementación y deben ser redefinidos por todas las subclases. La sobreescritura es esencial para el correcto funcionamiento de estos métodos.

La sobreescritura también facilita la creación de interfaces gráficas y aplicaciones interactivas. Al redefinir métodos como `paint` o `actionPerformed`, se puede personalizar el comportamiento de componentes visuales, permitiendo crear interfaces más atractivas y funcionales.

En resumen, la sobreescritura es una técnica fundamental en la programación orientada a objetos que permite adaptar el comportamiento de los métodos heredados en subclases. Este mecanismo es esencial para mantener la cohesión del diseño, proporcionar flexibilidad y facilitar la extensión del comportamiento de las clases. La sobreescritura es una herramienta poderosa que permite crear sistemas más modulares, escalables y personalizables.

<a id="constructores-y-herencia"></a>
## Constructores y herencia

En el vasto terreno de la programación orientada a objetos, los constructores y la herencia son pilares fundamentales que permiten crear estructuras de datos complejas y reutilizables. Los constructores son métodos especiales que se ejecutan automáticamente cuando se crea un objeto, inicializando sus atributos en valores específicos o predeterminados. Esta fase es crucial para establecer el estado inicial del objeto, asegurando que esté listo para interactuar con el resto de la aplicación.

La herencia, por otro lado, es una característica poderosa que permite a las clases derivar propiedades y comportamientos de otras clases existentes. Al crear una clase hija, se puede aprovechar todo lo definido en la clase padre, extendiéndolo o modificándolo según sea necesario para adaptarse a nuevas necesidades. Esta práctica promueve la reutilización del código y facilita el mantenimiento al permitir cambios en un solo lugar.

La combinación de constructores y herencia permite crear jerarquías de clases que son más organizadas y fácilmente manejables. Cada nivel de la jerarquía puede añadir o modificar comportamientos específicos, mientras que los atributos y métodos comunes se mantienen en las clases superiores. Esta estructura facilita el diseño de sistemas complejos, donde diferentes partes pueden interactuar de manera coherente y eficiente.

El uso de constructores y herencia también implica la consideración de la encapsulación, una práctica que oculta los detalles internos de un objeto y expone solo lo necesario. Esto no solo protege el estado del objeto sino que también facilita su modificación y evolución en el futuro sin afectar a las partes que lo utilizan.

En la práctica, la creación de constructores y la implementación de herencia requieren una comprensión profunda de los conceptos básicos de programación orientada a objetos. Es importante entender cómo funcionan los métodos, cómo se manejan los tipos de datos y cómo se establecen las relaciones entre diferentes clases.

La utilización avanzada de constructores y herencia permite desarrollar aplicaciones más robustas y escalables. Al permitir la creación de clases genéricas que pueden adaptarse a múltiples contextos, estas características facilitan el desarrollo de software modular y reutilizable.

En resumen, los constructores y la herencia son herramientas esenciales en la programación orientada a objetos, proporcionando estructuras sólidas para organizar y gestionar el código. Su comprensión y uso adecuado son fundamentales para crear aplicaciones eficientes y mantenibles que puedan adaptarse a las necesidades cambiantes del usuario.


<a id="mantenimiento-de-la-persistencia-de-los-objetos"></a>
# Mantenimiento de la persistencia de los objetos

<a id="bases-de-datos-orientadas-a-objetos"></a>
## Bases de datos orientadas a objetos

En el vasto universo de la programación, una rama llamada "Mantenimiento de la persistencia de los objetos" destaca como un pilar fundamental. Esta sección explora cómo almacenar y recuperar datos en sistemas orientados a objetos, abordando conceptos cruciales que son esenciales para el desarrollo robusto y eficiente de aplicaciones.

La base de esta rama es la comprensión de las bases de datos orientadas a objetos (ODBs), sistemas que almacenan y gestionan los datos como objetos en lugar de registros. Este enfoque ofrece una representación natural de los datos dentro del contexto de un programa, facilitando su manipulación y acceso.

El primer paso hacia el mantenimiento de la persistencia de los objetos es entender cómo instalar y configurar un gestor de bases de datos orientadas a objetos. Esto implica familiarizarse con las herramientas disponibles y realizar una instalación segura y eficiente, asegurando que todos los requisitos técnicos sean cumplidos.

Una vez establecida la conexión con el gestor de base de datos, se procede a la creación de bases de datos. Este proceso requiere un diseño cuidadoso para garantizar la integridad y consistencia de los datos. La definición de tablas y relaciones adecuadas es crucial para optimizar el rendimiento y facilitar las consultas posteriores.

El mantenimiento de la persistencia de los objetos implica no solo la creación inicial, sino también la gestión continua de la información almacenada. Esto incluye la inserción de nuevos datos, la modificación existente y la eliminación de registros obsoletos o redundantes. Cada operación debe ser realizada con cuidado para mantener la coherencia de los datos.

La consulta de datos es otro aspecto fundamental del mantenimiento de la persistencia de los objetos. Los sistemas orientados a objetos proporcionan mecanismos eficientes para realizar búsquedas y recuperar información específica, lo que es esencial para el funcionamiento correcto de aplicaciones complejas.

Además de las operaciones básicas, el mantenimiento de la persistencia de los objetos implica la gestión de transacciones. Las transacciones son conjuntos de operaciones que deben ser ejecutadas como una unidad, asegurando que todas las modificaciones sean consistentes y completas o ninguna se aplique en caso de error.

El manejo de excepciones es otro aspecto crucial del mantenimiento de la persistencia de los objetos. Las bases de datos orientadas a objetos suelen presentar situaciones inesperadas durante el proceso de almacenamiento y recuperación de datos, por lo que es necesario implementar mecanismos robustos para capturar y manejar estas excepciones.

La optimización del rendimiento también es un aspecto importante en la persistencia de los objetos. Esto implica no solo mejorar la velocidad de acceso a los datos, sino también reducir el uso de recursos como memoria y espacio en disco.

Finalmente, el mantenimiento de la persistencia de los objetos debe incluir la documentación adecuada. La creación de documentación detallada sobre las estructuras de datos, las operaciones disponibles y los procedimientos recomendados es crucial para que otros desarrolladores puedan entender y trabajar con el sistema de manera eficiente.

En resumen, la persistencia de los objetos en sistemas orientados a objetos es un proceso complejo pero fundamental. Desde la instalación y configuración del gestor de base de datos hasta la optimización del rendimiento y la documentación, cada paso requiere una comprensión profunda y una atención meticulosa para garantizar el éxito del proyecto.

<a id="caracteristicas-de-las-bases-de-datos-orientadas-a-objetos"></a>
## Características de las bases de datos orientadas a objetos

La programación orientada a objetos (OOP) es una filosofía de diseño que busca representar los conceptos del mundo real mediante clases y objetos. En este contexto, el mantenimiento de la persistencia de los objetos es un aspecto crucial que permite almacenar y recuperar información de manera eficiente y segura.

Las bases de datos orientadas a objetos (ODB) son sistemas que almacenan y gestionan datos en forma de objetos, lo que facilita su acceso y manipulación. Estas bases de datos ofrecen una visión natural del mundo real, donde los datos se organizan en entidades relacionadas entre sí.

La característica más destacada de las ODB es su capacidad para almacenar directamente objetos como estructuras de datos complejas, sin necesidad de convertirlos a un formato plano. Esto permite una representación más precisa y natural de la realidad en el sistema de gestión de información.

Además, las ODB ofrecen funcionalidades avanzadas que facilitan el acceso y manipulación de los datos. Por ejemplo, permiten realizar consultas complejas sobre los objetos almacenados, lo que es especialmente útil para aplicaciones empresariales donde se requiere un análisis detallado de la información.

El mantenimiento de la persistencia en ODB implica la creación, actualización y eliminación de objetos en el sistema. Esta operación debe ser segura y eficiente, asegurando que los datos estén siempre disponibles y consistentes.

Las ODB también ofrecen mecanismos para gestionar las relaciones entre los objetos, lo que facilita la integración de diferentes partes del sistema. Por ejemplo, se pueden establecer relaciones entre clientes y pedidos, permitiendo una fácil consulta de todos los pedidos realizados por un cliente específico.

En resumen, el mantenimiento de la persistencia de los objetos en bases de datos orientadas a objetos es un aspecto fundamental que permite representar y gestionar información de manera natural y eficiente. Esta característica hace que las ODB sean una herramienta poderosa para aplicaciones empresariales y otras que requieren un alto nivel de integridad y accesibilidad de los datos.

<a id="instalacion-del-gestor-de-bases-de-datos"></a>
## Instalación del gestor de bases de datos

La instalación del gestor de bases de datos es un paso crucial en el desarrollo de aplicaciones que requieren almacenamiento persistente de información. Este proceso implica la configuración adecuada del software necesario para gestionar los datos de manera eficiente y segura, permitiendo a las aplicaciones acceder, modificar y recuperar información de forma rápida y precisa.

El primer paso en esta instalación es seleccionar el gestor de bases de datos que mejor se adapte a las necesidades específicas del proyecto. Algunos de los más populares incluyen MySQL, PostgreSQL, Oracle Database y Microsoft SQL Server. Cada uno tiene sus propias características y ventajas, por lo que es importante realizar una evaluación cuidadosa para elegir el más adecuado.

Una vez seleccionado el gestor de bases de datos, se procede a la instalación del software. Este proceso puede variar dependiendo del sistema operativo utilizado, pero generalmente implica descargar el instalador desde el sitio web oficial del gestor de bases de datos y seguir las instrucciones paso a paso proporcionadas por el mismo.

Durante la instalación, es crucial configurar correctamente los parámetros iniciales. Esto incluye establecer el nombre del servidor, la contraseña del administrador (root), y otros detalles específicos del sistema operativo. Además, se debe decidir si se desea instalar el gestor de bases de datos en modo seguro o no.

La instalación también puede implicar la configuración de opciones adicionales como el tamaño inicial de los archivos de datos, la configuración de seguridad avanzada y la selección de características específicas del software. Es importante realizar esta configuración con cuidado para evitar problemas posteriores.

Una vez completada la instalación, es necesario verificar que todo esté funcionando correctamente. Esto implica iniciar el servicio del gestor de bases de datos y comprobar que se puede acceder a él desde el sistema operativo. Además, se debe realizar una prueba básica para asegurarse de que los datos pueden ser insertados, recuperados y modificados sin problemas.

La instalación del gestor de bases de datos es un proceso fundamental en la creación de aplicaciones que requieren almacenamiento persistente de información. Aunque puede parecer complejo al principio, con una buena comprensión de los pasos involucrados y el uso de herramientas adecuadas, este proceso se vuelve relativamente sencillo y eficiente.

Es importante recordar que la instalación del gestor de bases de datos es solo el primer paso en el proceso de gestión de información. A lo largo del ciclo de vida de una aplicación, será necesario realizar actualizaciones periódicas, optimizar el rendimiento y asegurar la seguridad de los datos almacenados.

En conclusión, la instalación del gestor de bases de datos es un proceso crucial pero fundamental en el desarrollo de aplicaciones que requieren almacenamiento persistente. Con una buena comprensión de los pasos involucrados y el uso de herramientas adecuadas, este proceso se vuelve relativamente sencillo y eficiente.

<a id="creacion-de-bases-de-datos"></a>
## Creación de bases de datos

La creación de bases de datos es una etapa fundamental en el desarrollo de aplicaciones informáticas, ya que proporciona la estructura necesaria para almacenar, recuperar y gestionar los datos de manera eficiente. En esta subunidad didáctica, nos adentramos en los aspectos técnicos y prácticos de este proceso.

Comenzamos por entender las bases del concepto de base de datos. Una base de datos es una colección organizada de datos que se almacenan en un sistema informático para su acceso y gestión. Su principal objetivo es facilitar el almacenamiento, recuperación y manipulación de información de manera estructurada y eficiente.

Continuamos con la exploración de las herramientas y tecnologías utilizadas para crear bases de datos. En este contexto, destacan los gestores de bases de datos (DBMS), que son programas especializados en la creación, gestión y operación de las bases de datos. Algunos ejemplos populares incluyen MySQL, PostgreSQL y Microsoft SQL Server.

A medida que avanzamos, nos familiarizamos con el proceso de diseño de una base de datos. Este proceso implica definir la estructura de los datos a almacenar, determinar las relaciones entre ellos y seleccionar los tipos de datos adecuados para cada campo. El objetivo es crear un modelo de datos que sea funcional, eficiente y fácil de mantener.

El siguiente paso en el proceso de creación de bases de datos es la implementación del diseño. Esto implica la creación de las tablas físicas en el sistema de gestión de base de datos, definiendo las columnas, tipos de datos y restricciones necesarias para almacenar los datos de manera correcta.

Una vez creada la estructura física de la base de datos, es crucial definir las relaciones entre las tablas. Las relaciones permiten establecer conexiones entre diferentes conjuntos de datos, facilitando la recuperación de información relacionada y la creación de consultas complejas.

La optimización de una base de datos es otro aspecto importante a considerar en el proceso de su creación. Esto implica la selección de índices adecuados para mejorar el rendimiento de las consultas, así como la implementación de estrategias de almacenamiento y recuperación eficientes.

El diseño y creación de bases de datos también implican la consideración de aspectos de seguridad. Es fundamental establecer políticas de acceso controladas para proteger los datos sensibles y evitar accesos no autorizados.

Finalmente, en esta subunidad didáctica, exploramos técnicas avanzadas para la creación de bases de datos. Estas pueden incluir el uso de lenguajes de definición de datos (DDL) para crear esquemas complejos, la implementación de transacciones para garantizar la integridad de los datos y la utilización de herramientas de gestión de base de datos para facilitar el proceso.

En resumen, la creación de bases de datos es un proceso integral en el desarrollo de aplicaciones informáticas. A través de este proceso, podemos organizar y gestionar eficientemente grandes volúmenes de información, lo que permite a las empresas tomar decisiones basadas en datos precisos y actualizados. Este conocimiento es fundamental para cualquier profesional del campo de la programación y gestión de sistemas informáticos.

<a id="mecanismos-de-consulta"></a>
## Mecanismos de consulta

En el mundo digital de la programación, mantener la persistencia de los objetos es una tarea fundamental que permite a las aplicaciones almacenar y recuperar información con eficiencia. Este proceso implica la creación y gestión de mecanismos que permitan la manipulación de datos en un entorno persistente, como bases de datos o sistemas de archivos.

La carpeta `005-Mecanismos de consulta` del curso de programación se centra específicamente en cómo realizar estas operaciones. Aquí, los estudiantes aprenderán a formular y ejecutar consultas que permitan recuperar información almacenada de manera eficiente y segura. El contenido aborda desde la sintaxis básica hasta técnicas avanzadas, proporcionando una comprensión profunda del manejo de datos en aplicaciones.

La primera lección introduce los conceptos básicos de consulta, explicando cómo estructurar sentencias que permitan seleccionar, filtrar y ordenar información. Los estudiantes aprenderán a utilizar operadores lógicos y comparativos para crear consultas precisas y eficientes. Además, se discute la importancia de la optimización de consultas para mejorar el rendimiento de las aplicaciones.

La siguiente lección profundiza en los tipos de consultas más comunes, como las proyecciones y agrupamientos. Se explica cómo utilizar estas técnicas para obtener información resumida y estructurada, facilitando la toma de decisiones basadas en datos. Los estudiantes también aprenderán a combinar múltiples consultas para realizar tareas complejas.

La carpeta continúa con lecciones sobre el manejo de subconsultas, que son consultas anidadas dentro de otras. Esta técnica es crucial para resolver problemas complejos y obtener información detallada en aplicaciones empresariales y científicas. Los estudiantes aprenderán cómo utilizar subconsultas para realizar operaciones avanzadas y cómo optimizarlas para mejorar el rendimiento.

La lección sobre la combinación de múltiples selecciones es una extensión natural del tema anterior, enseñando a los estudiantes cómo combinar diferentes consultas para obtener información completa y precisa. Se discute la importancia de la coherencia en las consultas y cómo utilizar operadores lógicos para unir resultados de manera efectiva.

La carpeta también aborda el tema de la optimización de consultas, una cuestión crítica en cualquier sistema persistente. Los estudiantes aprenderán técnicas avanzadas para mejorar el rendimiento de las consultas, como el uso de índices y la minimización del uso de recursos. Se discute cómo analizar y optimizar consultas complejas para asegurar un rendimiento óptimo.

La lección final en esta carpeta se centra en el manejo de excepciones durante las consultas. Aprender a gestionar errores y excepciones es fundamental para la robustez de cualquier aplicación. Los estudiantes aprenderán cómo detectar, capturar y manejar excepciones que puedan surgir durante el proceso de consulta, asegurando una experiencia de usuario fluida y segura.

En resumen, la carpeta `005-Mecanismos de consulta` del curso de programación ofrece una visión completa y detallada del manejo de datos en aplicaciones. Desde los conceptos básicos hasta técnicas avanzadas, proporciona a los estudiantes las herramientas necesarias para realizar consultas eficientes y seguras. Este conocimiento es esencial para desarrollar aplicaciones robustas y escalables que puedan manejar grandes volúmenes de datos con facilidad y precisión.

<a id="el-lenguaje-de-consultas-sintaxis-expresiones-operadores"></a>
## El lenguaje de consultas sintaxis, expresiones, operadores

En el mundo de la programación, mantener la persistencia de los objetos es una tarea fundamental que requiere un lenguaje de consultas poderoso y flexible. Este lenguaje nos permite interactuar con las bases de datos de manera eficiente, recuperando, modificando y eliminando información de manera segura y precisa.

El primer paso para entender el mantenimiento de la persistencia es familiarizarse con el lenguaje de consultas que se utiliza en la base de datos. Este lenguaje, conocido como SQL (Structured Query Language), es un estándar internacional que permite a los programadores realizar operaciones complejas sobre las bases de datos.

La sintaxis de SQL es rica y detallada, permitiendo a los usuarios definir consultas precisas para acceder a la información necesaria. Desde la sencilla consulta SELECT hasta las complejas sentencias UPDATE y DELETE, cada una con su propia estructura y reglas específicas, SQL nos proporciona las herramientas necesarias para interactuar con los datos de manera eficiente.

Las expresiones en SQL son otro aspecto crucial del lenguaje. Las expresiones permiten realizar cálculos y manipulaciones sobre los datos antes de que sean recuperados o almacenados. Desde la suma de valores hasta el filtrado de resultados, las expresiones en SQL ofrecen una gran flexibilidad para procesar los datos según nuestras necesidades.

Los operadores son el núcleo del lenguaje de consultas. Son símbolos y palabras clave que nos permiten definir las condiciones y acciones a realizar en nuestras consultas. Desde los operadores relacionales (como =, >, <) hasta los operadores lógicos (AND, OR, NOT), cada uno con su propia funcionalidad y reglas de precedencia, los operadores son esenciales para construir consultas complejas.

La importancia de conocer bien el lenguaje de consultas no se limita a la recuperación de datos. También es fundamental para la modificación y eliminación de información en las bases de datos. Las sentencias UPDATE y DELETE, junto con los operadores y expresiones adecuados, nos permiten realizar cambios precisos en nuestros datos.

Además, el lenguaje de consultas también incluye funciones que pueden ser utilizadas dentro de nuestras consultas para realizar cálculos o manipulaciones adicionales. Desde las funciones agregadas (como SUM, AVG, COUNT) hasta las funciones de texto (como UPPER, LOWER, SUBSTRING), estas funciones ofrecen una gran potencia en el procesamiento de datos.

La comprensión del lenguaje de consultas es crucial para cualquier programador que trabaje con bases de datos. No solo nos permite interactuar eficientemente con los datos, sino que también nos proporciona la capacidad de realizar operaciones complejas y precisas sobre ellos. Con el conocimiento adecuado del lenguaje de consultas, podemos mantener la persistencia de los objetos de manera segura y efectiva, lo que es fundamental para el desarrollo de aplicaciones robustas y eficientes.

En resumen, el mantenimiento de la persistencia de los objetos en una base de datos requiere un lenguaje de consultas poderoso y flexible. Conocer bien el lenguaje de consultas nos permite interactuar con las bases de datos de manera eficiente, recuperando, modificando y eliminando información de manera segura y precisa. Desde la sencilla consulta SELECT hasta las complejas sentencias UPDATE y DELETE, cada una con su propia estructura y reglas específicas, el lenguaje de consultas nos proporciona las herramientas necesarias para interactuar con los datos de manera eficiente.

<a id="recuperacion-modificacion-y-borrado-de-informacion"></a>
## Recuperación, modificación y borrado de información

En el mundo digital, la persistencia de los objetos es una cuestión fundamental que abarca tanto la recuperación como la modificación y borrado de información. Este proceso es esencial para mantener la integridad y coherencia de los datos en aplicaciones informáticas.

La recuperación de información es un aspecto crucial del mantenimiento de la persistencia de los objetos. Consiste en el acceso a los datos almacenados previamente, lo que permite realizar consultas y operaciones sobre ellos. Este proceso requiere una comprensión profunda de las estructuras de datos utilizadas y las técnicas de acceso eficiente a estos datos.

La modificación de la información es otro elemento fundamental del mantenimiento de la persistencia de los objetos. Implica el cambio en los valores de los atributos de los objetos, lo que puede ser necesario para actualizar la información basada en nuevas entradas o cambios en las condiciones del sistema.

El borrado de información también forma parte integral del proceso de mantenimiento de la persistencia de los objetos. Es una operación delicada que debe realizarse con cuidado para evitar pérdidas de datos importantes y garantizar la integridad de la base de datos.

La recuperación, modificación y borrado de información son interrelacionados y deben manejarse de manera coherente para mantener el sistema informático funcional. Cada una de estas operaciones requiere un enfoque específico y técnicas adecuadas para garantizar su correcto funcionamiento.

El mantenimiento de la persistencia de los objetos es un proceso continuo que implica no solo la recuperación, modificación y borrado de información, sino también la gestión eficiente del almacenamiento y la optimización del rendimiento. Este proceso requiere una comprensión profunda de las bases de datos y las técnicas de programación adecuadas.

La persistencia de los objetos es un concepto fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo es esencial para garantizar la integridad, coherencia y eficiencia del sistema. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un tema complejo pero fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo requiere una comprensión profunda de las bases de datos y las técnicas de programación adecuadas. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un concepto fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo es esencial para garantizar la integridad, coherencia y eficiencia del sistema. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un tema complejo pero fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo requiere una comprensión profunda de las bases de datos y las técnicas de programación adecuadas. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un concepto fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo es esencial para garantizar la integridad, coherencia y eficiencia del sistema. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un tema complejo pero fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo requiere una comprensión profunda de las bases de datos y las técnicas de programación adecuadas. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un concepto fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo es esencial para garantizar la integridad, coherencia y eficiencia del sistema. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un tema complejo pero fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo requiere una comprensión profunda de las bases de datos y las técnicas de programación adecuadas. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

La persistencia de los objetos es un concepto fundamental en el desarrollo de aplicaciones informáticas. Su correcto manejo es esencial para garantizar la integridad, coherencia y eficiencia del sistema. A través del proceso de recuperación, modificación y borrado de información, se puede mantener la base de datos actualizada y relevante, lo que es crucial para el funcionamiento óptimo del sistema.

<a id="tipos-de-datos-objeto-atributos-y-metodos"></a>
## Tipos de datos objeto; atributos y métodos

En el vasto mundo de la programación, el concepto de persistencia de los objetos es una piedra angular que sostiene las estructuras de datos más complejas. Este proceso, que permite a los datos almacenados en memoria ser guardados permanentemente en un medio de almacenamiento externo como discos duros o bases de datos, es fundamental para mantener la integridad y consistencia de los sistemas informáticos.

La persistencia de los objetos implica no solo el almacenamiento de los datos, sino también su recuperación y manipulación. Este proceso se realiza a través de métodos específicamente diseñados para interactuar con el medio de almacenamiento. Estos métodos pueden ser directamente invocados por el programador o pueden ser utilizados automáticamente por frameworks y bibliotecas que facilitan la gestión del estado de los objetos.

Los tipos de datos objeto son una extensión natural del concepto de objetos en la programación orientada a objetos. Algunos ejemplos incluyen clases, estructuras y registros. Cada tipo de dato objeto tiene atributos, que representan las características o propiedades del objeto, y métodos, que definen las acciones que el objeto puede realizar.

Los atributos son variables asociadas con un objeto que almacenan su estado actual. Por ejemplo, en una clase `Persona`, los atributos podrían ser `nombre`, `edad` y `dirección`. Los métodos, por otro lado, son funciones definidas dentro de la clase que realizan operaciones sobre el objeto o manipulan sus atributos.

La persistencia de los objetos a través de tipos de datos objeto es un proceso que requiere cuidado. Es importante garantizar que los datos se almacenen y recuperen correctamente para evitar errores y mantener la coherencia del sistema. Además, la gestión adecuada de la memoria es crucial para evitar fugas de memoria y problemas de rendimiento.

En el contexto de bases de datos, la persistencia de los objetos a través de tipos de datos objeto puede realizarse mediante mapeo objeto-relacional (ORM). ORM es una técnica que permite a los desarrolladores interactuar con las bases de datos utilizando objetos en lugar de sentencias SQL. Esto facilita la programación y reduce el riesgo de errores.

La persistencia de los objetos también implica la gestión de transacciones. Una transacción es un conjunto de operaciones que se realizan como una unidad lógica. Si todas las operaciones dentro de una transacción son exitosas, entonces toda la transacción se considera exitosa y los cambios se aplican permanentemente al sistema. Si alguna operación falla, la transacción se cancela y no se aplican ningún cambio.

En resumen, la persistencia de los objetos es un concepto fundamental en la programación que permite a los datos ser almacenados, recuperados y manipulados de manera segura y eficiente. A través de tipos de datos objeto, métodos y técnicas como ORM y gestión de transacciones, los desarrolladores pueden crear sistemas informáticos robustos y confiables que puedan mantener su estado a lo largo del tiempo.

<a id="tipos-de-datos-coleccion"></a>
## Tipos de datos colección

En el vasto mundo de la programación, los objetos son las piezas fundamentales que conforman nuestra realidad digital. Sin embargo, para que estos objetos puedan interactuar eficazmente entre sí y con otros elementos del sistema, es necesario almacenarlos de manera persistente. Es aquí donde entra en juego el concepto de tipos de datos colección.

Los tipos de datos colección son estructuras de datos que nos permiten agrupar y organizar múltiples objetos bajo un solo nombre. Estas estructuras son esenciales para la programación orientada a objetos, ya que nos proporcionan una forma eficiente de almacenar, recuperar y manipular grandes cantidades de información.

La colección más básica y común en la programación es el array. Un array es una estructura de datos que permite almacenar un conjunto ordenado de elementos del mismo tipo. Cada elemento dentro del array se identifica por su índice, lo que facilita su acceso y manipulación. Los arrays son ideales para situaciones donde necesitamos trabajar con conjuntos homogéneos de datos.

Otro tipo de colección importante es el diccionario o mapa. A diferencia de los arrays, los diccionarios no están ordenados y cada elemento está asociado a una clave única. Este tipo de estructura es especialmente útil cuando necesitamos acceder a los elementos por su nombre o identificador en lugar de su posición.

Además de estos tipos básicos, existen colecciones más complejas como las listas enlazadas, las pilas y las colas. Cada una de estas estructuras tiene sus propias características y ventajas, lo que las hace útiles para diferentes situaciones dependiendo del problema que estemos tratando de resolver.

La elección del tipo de colección adecuado es crucial para el rendimiento y la eficiencia de nuestro código. Algunas colecciones ofrecen operaciones más rápidas en ciertas situaciones, mientras que otras son mejores para otros tipos de acceso o manipulación de datos.

Para trabajar con colecciones en programación, necesitamos conocer las operaciones básicas que se pueden realizar sobre ellas. Estas operaciones incluyen la inserción y eliminación de elementos, la búsqueda de un elemento específico y la recorrido de todos los elementos de la colección. Cada tipo de colección tiene sus propias implementaciones de estas operaciones, lo que puede afectar su rendimiento.

Además de las operaciones básicas, también es importante entender cómo manejar excepciones cuando se trabaja con colecciones. Por ejemplo, si intentamos acceder a un elemento fuera del rango válido de un array o diccionario, nuestro programa podría fallar. Es por eso que es crucial aprender a manejar estas situaciones de manera segura y eficiente.

La persistencia de los objetos en colecciones también implica la gestión de la memoria. Cuando insertamos objetos en una colección, debemos considerar cómo liberar la memoria cuando estos objetos ya no sean necesarios. Esto puede implicar el uso de técnicas como la recolección de basura o la gestión manual del ciclo de vida de los objetos.

En resumen, los tipos de datos colección son herramientas poderosas y versátiles en la programación orientada a objetos. Al comprender cómo funcionan y cuándo usar cada uno, podemos escribir programas más eficientes y robustos. Cada colección tiene sus propias ventajas y desventajas, lo que nos obliga a pensar cuidadosamente en nuestras necesidades específicas antes de elegir la estructura adecuada para nuestro problema.

La comprensión profunda de los tipos de datos colección es un paso crucial hacia el dominio del desarrollo de software. Al aprender a utilizar estas estructuras eficazmente, podemos crear aplicaciones que manejen grandes cantidades de información con facilidad y eficiencia. Este conocimiento nos permitirá construir sistemas complejos y escalables que respondan a las necesidades cambiantes de nuestros usuarios.

En el mundo de la programación, los objetos son como los bloques con los que construimos nuestras edificios digitales. Y las colecciones son las herramientas que nos permiten organizar y almacenar estos bloques de manera eficiente. Con un buen dominio de los tipos de datos colección, podemos crear estructuras de datos complejas y poderosas que nos ayuden a resolver problemas reales y significativos en el mundo digital.

La programación es una disciplina que requiere tanto conocimiento teórico como habilidad práctica. Y la comprensión de los tipos de datos colección es un aspecto fundamental del segundo, ya que nos permite trabajar con grandes cantidades de información de manera eficiente y segura. Con el tiempo y la práctica, podemos convertirnos en expertos en el uso de estas estructuras y aplicarlas en una variedad de situaciones.

En conclusión, los tipos de datos colección son herramientas esenciales en la programación orientada a objetos. Al aprender a utilizarlas eficazmente, podemos crear aplicaciones que manejen grandes cantidades de información con facilidad y eficiencia. Con un buen dominio de estos conceptos, podemos construir sistemas complejos y escalables que respondan a las necesidades cambiantes de nuestros usuarios. Y en el mundo digital, donde la cantidad de información es cada vez mayor, esta habilidad será más valiosa que nunca.


<a id="gestion-de-bases-de-datos"></a>
# Gestión de bases de datos

<a id="acceso-a-bases-de-datos-estandares-caracteristicas"></a>
## Acceso a bases de datos. Estándares. Características

En el vasto mundo de la programación, una base de datos es como un gran armario donde se almacenan los secretos digitales de nuestras aplicaciones. Este armario tiene reglas estrictas para mantener sus objetos en orden y garantizar su seguridad y eficiencia.

El acceso a bases de datos es el primer paso hacia la manipulación de estos secretos. Es como abrir una puerta que nos permite ver, modificar o eliminar lo que está dentro del armario. Para hacer esto, necesitamos seguir un conjunto de reglas establecidas por los estándares de la industria.

Estos estándares son como las normas de juego que todos deben seguir para que todo funcione sin problemas. Algunos de los más conocidos incluyen SQL (Structured Query Language), que es el idioma utilizado para comunicarse con las bases de datos, y JDBC (Java Database Connectivity), que es una API que permite a los programas Java interactuar con diferentes tipos de bases de datos.

Además de estos estándares, cada base de datos tiene sus propias características únicas. Algunas son más eficientes para almacenar grandes cantidades de información, mientras que otras son excelentes para manejar relaciones complejas entre los datos. Es importante conocer estas diferencias para elegir la herramienta adecuada para el trabajo.

El acceso a bases de datos no es solo una cuestión técnica; también implica seguridad y privacidad. Los sistemas deben estar diseñados para proteger la información sensible contra accesos no autorizados, lo que significa entender cómo funcionan los mecanismos de autenticación y autorización.

Además del acceso básico, las bases de datos modernas ofrecen una gama de funciones avanzadas. Desde el almacenamiento en caché hasta la replicación de datos para aumentar la disponibilidad, cada característica contribuye a hacer que nuestro armario digital sea más robusto y eficiente.

La gestión de transacciones es otro aspecto crucial del acceso a bases de datos. Una transacción es una serie de operaciones que se realizan juntas como un todo. Si alguna parte falla, todo debe revertirse para mantener la integridad de los datos. Es como asegurarse de que no se pierdan los juguetes cuando se está jugando con ellos.

El acceso a bases de datos también implica la optimización. Esto significa encontrar el camino más corto y eficiente para llegar al objetivo, ya sea consultando una base de datos grande o actualizando un registro específico. La optimización es como aprender a buscar en un armario lleno de juguetes sin perder el tiempo.

En resumen, el acceso a bases de datos es la puerta que nos permite interactuar con los secretos digitales almacenados en nuestros sistemas. Al seguir los estándares adecuados y conocer las características específicas de cada base de datos, podemos asegurarnos de que nuestra aplicación funcione eficientemente y seguramente. Y, como cualquier buen juego, el acceso a bases de datos requiere práctica y paciencia para dominarlo plenamente.

<a id="establecimiento-de-conexiones"></a>
## Establecimiento de conexiones

La gestión de bases de datos es una habilidad fundamental en el desarrollo de software moderno, ya que permite a los programadores almacenar, recuperar y gestionar grandes volúmenes de información de manera eficiente. En esta subunidad didáctica, nos centramos específicamente en el establecimiento de conexiones con bases de datos, un paso crucial antes de cualquier interacción con la información almacenada.

El primer concepto que abordamos es el concepto de conexión a una base de datos. Una conexión se establece entre el programa informático y la base de datos para permitir la comunicación bidireccional. Este proceso implica la especificación de detalles como el nombre del servidor, el puerto, el nombre de la base de datos, el usuario y la contraseña. La importancia de estos detalles no puede ser subestimada, ya que cualquier error en ellos puede llevar a fallas graves en la aplicación.

Continuamos con una explicación detallada sobre cómo establecer conexiones utilizando diferentes lenguajes de programación. Por ejemplo, en Java, se utiliza el objeto `Connection` del paquete `java.sql`, mientras que en Python, existen bibliotecas como `sqlite3` para bases de datos SQLite o `psycopg2` para PostgreSQL. Cada uno de estos métodos requiere un conjunto específico de parámetros y puede presentar desafíos propios dependiendo del tipo de base de datos utilizado.

El establecimiento de conexiones también implica la gestión de excepciones, ya que es posible que ocurran errores inesperados durante el proceso. Por ejemplo, si el servidor no está disponible o las credenciales son incorrectas, se producirá una excepción. Es crucial manejar estas situaciones adecuadamente para evitar que la aplicación falle y proporcionar un feedback útil al usuario.

Además de establecer conexiones, también es importante entender cómo cerrarlas correctamente. Una conexión abierta puede consumir recursos del servidor y limitar su capacidad para atender a otras solicitudes. Por lo tanto, es una buena práctica cerrar la conexión tan pronto como no sea necesaria, utilizando métodos específicos proporcionados por cada lenguaje o biblioteca.

El proceso de establecimiento de conexiones también implica la configuración del entorno de desarrollo. Esto puede incluir la instalación y configuración de drivers o controladores para el tipo específico de base de datos utilizado. Por ejemplo, si se está utilizando una base de datos MySQL, es necesario instalar el driver JDBC correspondiente.

En este contexto, también es útil conocer las mejores prácticas en cuanto a la seguridad de las conexiones. Esto incluye el uso de contraseñas seguras y la implementación de políticas de acceso controlados para evitar accesos no autorizados. Además, es recomendable utilizar métodos como la autenticación dual-factor o la autenticación basada en tokens para mejorar la seguridad.

Finalmente, esta subunidad también aborda el tema de la gestión de transacciones. Una transacción es una serie de operaciones que se realizan juntas y deben completarse completamente o no realizarse en absoluto. Si alguna operación falla, toda la transacción debe revertirse para mantener la integridad de los datos.

En resumen, el establecimiento de conexiones con bases de datos es un paso fundamental en cualquier aplicación que interactúe con información persistente. A través de este proceso, se permite la comunicación entre el programa y la base de datos, lo que facilita la almacenamiento, recuperación y gestión de grandes volúmenes de información. Es crucial entender los detalles del establecimiento de conexiones, manejar excepciones adecuadamente, cerrar las conexiones correctamente y seguir mejores prácticas en cuanto a seguridad y transacciones para asegurar el funcionamiento eficiente y seguro de la aplicación.

### ejercicio

```markdown
Ejercicio
```

<a id="almacenamiento-recuperacion-actualizacion-y-eliminacion-de-informacion-en-bases-de-datos"></a>
## Almacenamiento, recuperación, actualización y eliminación de información en bases de datos

En la vastedad del océano digital, donde los datos son las rocas fundamentales de nuestra era, se encuentra el concepto de gestión de bases de datos. Este es un dominio que abarca desde la creación hasta la eliminación de información en sistemas de almacenamiento persistente. Comenzamos nuestro viaje por esta temática con una visión general del proceso de almacenamiento y recuperación de datos.

El primer paso en el manejo de bases de datos es su almacenamiento, un acto que requiere inteligencia y precisión para garantizar la integridad y seguridad de los datos. Este proceso implica la creación de tablas o colecciones donde se organizarán los datos según ciertas reglas definidas por el modelo de datos utilizado. La elección del modelo de datos adecuado es crucial, ya que determinará cómo se estructuran y relacionan los datos dentro de la base.

La recuperación de información es otro aspecto fundamental de la gestión de bases de datos. Este proceso implica la búsqueda y acceso a los datos almacenados en la base de datos. La eficiencia de esta operación depende del diseño de índices y la optimización de las consultas SQL, que son herramientas clave para extraer información de manera rápida y precisa.

La actualización de información es un proceso que permite modificar los datos existentes en la base de datos. Este acto es esencial para mantener los datos actualizados y reflejar los cambios en el mundo real. La gestión adecuada de las transacciones durante este proceso es crucial, ya que garantiza la consistencia y coherencia de los datos.

Por último, pero no menos importante, está el proceso de eliminación de información. Este acto implica la borrado de registros o datos específicos de la base de datos. La seguridad y la privacidad son factores clave en este proceso, ya que debe garantizar que solo se eliminen los datos autorizados y necesarios.

A lo largo de este recorrido por el mundo de la gestión de bases de datos, hemos explorado desde la creación hasta la eliminación de información. Cada paso requiere una comprensión profunda del modelo de datos, las consultas SQL y las transacciones para garantizar que los datos sean manejados de manera eficiente y segura.

Este proceso no es solo técnico; también implica habilidades de planificación y organización. Es necesario tener en cuenta el rendimiento de la base de datos, la seguridad de los datos y la facilidad con la que se pueden realizar operaciones de recuperación y actualización.

En conclusión, la gestión de bases de datos es un campo complejo pero fundamental para cualquier sistema informático moderno. Desde su creación hasta su eliminación, cada paso requiere una comprensión profunda y habilidades técnicas avanzadas. A través del estudio y práctica constante, podemos mejorar nuestra capacidad para manejar eficazmente los datos en nuestro mundo digital.


<a id="programacion-en-el-lado-del-servidor"></a>
# Programación en el lado del servidor

<a id="fundamentos"></a>
## Fundamentos

### diagrama

```json
{
  "formas": [
    {
      "id": "forma-1",
      "tipo": "rectangle",
      "left": "366.413px",
      "top": "203.832px",
      "width": "",
      "height": "",
      "texto": "PHP"
    },
    {
      "id": "forma-2",
      "tipo": "rectangle",
      "left": "366.566px",
      "top": "162.493px",
      "width": "",
      "height": "",
      "texto": "HTML"
    },
    {
      "id": "forma-3",
      "tipo": "rectangle",
      "left": "545.524px",
      "top": "330.509px",
      "width": "",
      "height": "",
      "texto": "PHP"
    },
    {
      "id": "forma-4",
      "tipo": "rectangle",
      "left": "547.995px",
      "top": "129.995px",
      "width": "",
      "height": "",
      "texto": "HTML"
    },
    {
      "id": "forma-5",
      "tipo": "rectangle",
      "left": "548.352px",
      "top": "169.63px",
      "width": "",
      "height": "",
      "texto": "JS"
    },
    {
      "id": "forma-6",
      "tipo": "circle",
      "left": "546.189px",
      "top": "229.623px",
      "width": "",
      "height": "",
      "texto": "JSON"
    }
  ],
  "flechas": [
    {
      "desde": {
        "shapeId": "forma-3",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-6",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    },
    {
      "desde": {
        "shapeId": "forma-6",
        "propId": null,
        "side": null
      },
      "hasta": {
        "shapeId": "forma-5",
        "propId": null,
        "side": null
      },
      "tipo": "simple",
      "estilo": "straight"
    }
  ]
}
```

### Preparatorio

```markdown

```

### cuota de mercado

```markdown
Python es actualmente el lenguaje de programación general más utilizado
https://www.tiobe.com/tiobe-index/

Resumen: Python es guay

En los servidores web:
PHP reina desde los años 90
Todo el mundo despotrica
Todo el mundo lo quiere matar
Todo el mundo dice que es una mierda
https://w3techs.com/technologies/overview/programming_language

PHP = Personal Home Page

Sintaxis:
Los archivos que contienen PHP, tienen que tener la extensión .php
```

### html en php

```
Un archivo PHP puede tener HTML
<p>No, en serio, puede realmente tener HMTL</p>
<p>Un archivo PHP no te obliga a poner PHP</p>

Este archivo debe estar

Linux: /var/www/html/(carpeta que queráis)

Windows: C:/xampp/htdocs/(carpeta que queráis)

Y luego en el navegador:
http://localhost/(carpeta que queráis)

En mi caso concreto:
http://localhost/programaciondam2526/010-Programaci%c3%b3n%20en%20el%20lado%20del%20servidor/001-Fundamentos/101-Ejercicios/003-html%20en%20php.php
```

### Probamos PHP

```
Esto no es PHP

<?php
	echo "Esto si que es php";
?>

Esto ya no es PHP
```

### Que pasa con el repositorio

```markdown
Todos estáis queriendo meter vuestro repositorio 
en la carpeta de publicación

Eso me parece muy bien

No debéis mover la carpeta de GitHub, porque a GitHub no le gustará
Deberíais romper el clon, y volver a clonar de nuevo en la carpeta de publicación

Eso es deseable a largo plazo, pero no ahora mismo

De momento hoy:
Trabajad en la carpeta de apache
Al final de la clase copiais el contenido a vuestra carpeta real

Y estos proximos dias, lo hacemos "bien"
```

### comentarios en php

```
<?php
	echo "Hola mundo en PHP"; 
  // echo en PHP es como print en Python
  // Esto es un comentario de una única línea
  
  /*
  	Esto es una linea de comentario
    Esto tambien es una linea de comentario
  */
?>
```

### operadores

```
<?php
	echo 4+3;
  echo 4-3;
  echo 4*3;
  echo 4/3;
  echo 4%3;
?>
```

### romper linea

```
Esto es HTML<br>
<?php
	echo "Esto es PHP<br>";
?>	
Esto vuelve a ser HTML<br>
```

### operadores de comparacion

```
<?php
	echo 4<3;
  echo 4<=3;
  echo 4>3;
  echo 4>=3;
  echo 4==3;
  echo 4!=3;
?>
```

### operadores booleanos

```
<?php
	echo 4 == 4 && 3 == 3 && 2 == 2; // Verdadero
  echo 4 == 4 && 3 == 3 && 2 == 1; // Falso
  
  echo 4 == 4 || 3 == 3 || 2 == 2; // Verdadero
  echo 4 == 4 || 3 == 3 || 2 == 1; // Verdadero
  echo 4 == 4 || 3 == 2 || 2 == 1; // Verdadero
  echo 4 == 3 || 3 == 2 || 2 == 1; // Falso
?>
```

### variables

```
<?php
	$edad = 47; // Las variables se declaran con dolar
  echo $edad; // Podemos hacer echo de variables
  echo "<br>"; // salto de linea
  $edad = 48; // Podemos cambiar el valor de una variable
  echo $edad;
?>
```

### estructura for y calendario

```
<!doctype html>
<html>
	<head>
  	<style>
    	.dia{border:1px solid black;padding:10px;width:50px;
      height:50px;display:inline-block;}
    </style>
  </head>
  <body>
    <?php
      // El signo de encadenamiento es el . (y eso es superguay)

      for($dia = 1;$dia < 31;$dia++){
        echo "<div class='dia'>".$dia."</div>";
      }
    ?>
  </body>
</html>
```

### if

```
<?php

	$edad = 47;
  if($edad < 30){
  	echo "Eres un joven";
  }
  
?>
```

### else

```
<?php

	$edad = 47;
  if($edad < 30){
  	echo "Eres un joven";
  }else{
  	echo "Ya no eres un joven";
  }
  
?>
```

### else if

```
<?php

	$edad = 47;
  
  if($edad < 10){
  	echo "Eres un niño";
  }else if($edad >= 10 && $edad < 20){
  	echo "Eres un adolescente";
  }else if($edad >= 20 && $edad < 30){
  	echo "Eres un joven";
  }else{
  	echo "Ya no eres joven";
  }
  
?>
```

### switch

```
<?php
	$dia_de_la_semana = "martes";
	switch($dia_de_la_semana){
  	case "lunes":
    	echo "hoy es el peor dia de la semana";
      break;
    case "martes":
    	echo "hoy es el segundo peor día de la semana";
      break;
    case "miercoles":
    	echo "hoy ya estamos a mitad de semana";
      break;
    case "jueves":
    	echo "Ya casi es viernes";
      break;
    case "viernes":
    	echo "Por fin es viernes";
      break;
    case "sábado":
    	echo "Este es el mejor dia de la semana";
      break;
    case "domingo":
    	echo "Parece mentira que mañana ya sea lunes";
      break;
  }

?>
```

### arrays

```
<?php
	$frutas = ['manzana','pera','platano'];
  
  var_dump($frutas);
?>
```

### arrays multidimensionales

```
<?php

	$agenda = [
  	["Jose Vicente","Carratala",47],
    ["Juan","Martinez",45],
    ["Jaime","Lopez",46]
  ];
  
  var_dump($agenda);
  
?>
```

### declarar una funcion

```
<?php
	function diHola(){
  	echo "Hola como estás";
  }
?>
```

### usar la funcion

```
<?php
	function diHola(){
  	echo "Hola como estás";
  }
  
  diHola();
?>
```

### funciones con parametros

```
<?php
	function diHola($nombre){
  	echo "Hola, ".$nombre." como estás";
  }
  
  diHola("Jose Vicente");
?>
```

### varios parametros

```
<?php
	function diHola($nombre,$edad){
  	echo "Hola, ".$nombre." tienes ".$edad." años, como estás";
  }
  
  diHola("Jose Vicente",47);
?>
```

### return en la funcion

```
<?php
	function diHola($nombre,$edad){
  	return "Hola, ".$nombre." tienes ".$edad." años, como estás";
  }
  
  echo diHola("Jose Vicente",47);
?>
```

### vamos con los gatos

```
<?php

	class Gato{
  	function __construct($color,$edad){
    	$this->color = $color;
      $this->edad = $edad;
    }
  }
  
  $gato1 = new Gato("Naranja",1);
  $gato2 = new Gato("Blanco",2);
  
  var_dump($gato1);

?>
```

<a id="get-y-post"></a>
## get y post

### repaso de los verbos

```markdown
Los verbos http son:

GET (dame) "SELECT"
POST (toma) "INSERT"
PUT (modificamos) "UPDATE"
DELETE (eliminamos) "DELETE"

PATCH (también modificamos) "UPDATE"
```

### get

```
<?php
	// Espera que en la URL haya un parametro llamado nombre
	echo $_GET['nombre'];
?>
```

### formularcion de url

```markdown
A una URL se le pueden pasar parámetros

script.php?parametro1=valor1&parametro2=valor2&...

script.php = es el script principal
? = a partir de aqui, empiezan los parámetros
clave=valor = clave es la clave del parámetro, valor es el valor del parámetro
& = espera que te paso más
```

### dos parametros get

```
<?php
	echo $_GET['nombre'];
  echo "<br>";
  echo $_GET['apellidos'];
?>
```

### formulario

```html
<form action="006-post.php" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>

006-post.php = quien te procesa
POST = como se va a enviar y recibir la informacion
name="nombre" = la clave que se va a enviar
```

### post

```
<?php
	echo $_POST['nombre'];
?>

$_POST porque me envían la información por POST
Y la tengo que recoger por la misma vía

'nombre' porque es la clave que se ha enviado desde HTML
```

### autoprocesamiento

```
<?php
	echo $_POST['nombre'];
?>

<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>
```

### php.ini

```markdown
php.ini en Windows:
C:/xampp/php/php.ini
(Espero que no sea vuestro caso)

En Ubuntu está en:
/etc/php/8.3/apache2/php.ini

Si no os deja modificar con gedit

sudo nano /etc/php/8.3/apache2/php.ini

Comandos:
(Parece que si que deja hacer scroll)
Control + W = Buscar (where)
Control + O = Guardar
Control + X = Salir
Tenéis la ayuda bajo del editor

display_errors = On (cambiad de Off a On)

Cuando se toca el php.ini hay que reiniciar apache

sudo service apache2 restart
```

### comprobacion

```
<?php
	esto da error si o si
?>
```

### retomamos

```
<?php
	echo $_POST['nombre'];
?>

<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>
```

### comprobacion de existencia

```
<?php
	// Comprobación de existencia isset
	if(isset($_POST['nombre'])){
		echo $_POST['nombre'];
  }
?>

<form action="?" method="POST">
  <p>Introduce tu nombre</p>
  <input type="text" name="nombre">
  <input type="submit">
</form>
```

### preguntas y respuestas

```
<!doctype html>
<html>
	<head>
  	<style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{
      	display:flex;align-items:center;justify-content:center;
        background:lightgray;flex-direction:column;}
      header,footer,main{
      	width:400px;padding:20px;background:white;
        text-align:center;
        }
      form{display:flex;flex-direction:column;gap:10px;}
      input{padding:10px;}
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
    	(c) 2025 Jose Vicente Carratala
    </footer>
  </body>
</html>
```

### atrapamos la informacion

```
<!doctype html>
<html>
	<head>
  	<style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{
      	display:flex;align-items:center;justify-content:center;
        background:lightgray;flex-direction:column;}
      header,footer,main{
      	width:400px;padding:20px;background:white;
        text-align:center;
        }
      form{display:flex;flex-direction:column;gap:10px;}
      input{padding:10px;}
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
    	(c) 2025 Jose Vicente Carratala
      <?php
      	echo $_POST['pregunta'];
        echo "<br>";
        echo $_POST['respuesta'];
      ?>
    </footer>
  </body>
</html>
```

### isset

```
<!doctype html>
<html>
	<head>
  	<style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{
      	display:flex;align-items:center;justify-content:center;
        background:lightgray;flex-direction:column;}
      header,footer,main{
      	width:400px;padding:20px;background:white;
        text-align:center;
        }
      form{display:flex;flex-direction:column;gap:10px;}
      input{padding:10px;}
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
    	(c) 2025 Jose Vicente Carratala
      <?php
      	if(isset($_POST['pregunta']) && isset($_POST['respuesta'])){
          echo $_POST['pregunta'];
          echo "<br>";
          echo $_POST['respuesta'];
        }
      ?>
    </footer>
  </body>
</html>
```

<a id="persistencia"></a>
## Persistencia

### escribir texto

```
<?php
  $archivo = fopen("archivo.txt", "a"); // "a" = append
  fwrite($archivo, "Nuevo texto escrito desde PHP\n");
  fclose($archivo);
?>
```

### voy a hacer una barbaridad

```markdown
Terminal:

sudo chmod 777 -R /var/www/html/programaciondam2526

sudo = Realizo acción como administrador

chmod = cambio permisos

777 = le doy permiso a todo el mundo

-R = Lo quiero aplicar recursivo (a todo el contenido)

/var/www.... = la carpeta afectada

En el sistema de permisos UNIX (Linux,macOS)

1 numero para el usuario
1 numero para el grupo al que pertenece el usuario
1 numero para todo el resto


0 - ningún permiso
1 = solo ejectar
2 = solo escribir
3 = escribir y ejecutar
4 = solo leer
5 = leer y ejecutar
6 = leer y escribir
7 = leer, escribir y ejecutar

777 = permisible en tu maquina, no recomendable en produccion
usuario leer, escribir y ejecutar
grupo leer, escribir y ejecutar
todo el mundo leer, escribir y ejecutar

755 = posible para produccion
usuario leer, escribir y ejecutar
grupo leer y ejecutar
todo el mundo leer y ejecutar

644 = mas restrictivo para produccion
usuario leer y escribir
grupo solo leer
todo el mundo solo leer
```

### leer

```
<?php
  $archivo = fopen("archivo.txt", "r"); // "r" = leer/read
  
  // Parámetros 1.-Lo que lees 2.-Longitud de lo que lees
  $contenido = fread($archivo,filesize("archivo.txt"));
  
  echo $contenido;
  fclose($archivo);
?>
```

### array nombrado en php

```
<?php
  $cliente = [];
  $cliente['nombre'] = "Jose Vicente";
  $cliente['apellidos'] = "Carratala Sanchis";
  $cliente['email'] = "info@jocarsa.com";
  
  var_dump($cliente);
?>
```

### saco el array como json

```
<?php
  $cliente = [];
  $cliente['nombre'] = "Jose Vicente";
  $cliente['apellidos'] = "Carratala Sanchis";
  $cliente['email'] = "info@jocarsa.com";
  
  $json = json_encode($cliente);
  echo $json;  
?>
```

### recuperamos el formulario

```
<!doctype html>
<html>
	<head>
  	<style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{
      	display:flex;align-items:center;justify-content:center;
        background:lightgray;flex-direction:column;}
      header,footer,main{
      	width:400px;padding:20px;background:white;
        text-align:center;
        }
      form{display:flex;flex-direction:column;gap:10px;}
      input{padding:10px;}
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
    	(c) 2025 Jose Vicente Carratala
      <?php
      	$json = json_encode($_POST); 	// Convierte post a JSON
        echo $json;										// Y lo saca por pantalla
      ?>
    </footer>
  </body>
</html>
```

### y lo guardamos en el disco

```
<!doctype html>
<html>
	<head>
  	<style>
    	body,html{width:100%;height:100%;padding:0px;margin:0px;}
      body{
      	display:flex;align-items:center;justify-content:center;
        background:lightgray;flex-direction:column;}
      header,footer,main{
      	width:400px;padding:20px;background:white;
        text-align:center;
        }
      form{display:flex;flex-direction:column;gap:10px;}
      input{padding:10px;}
    </style>
  </head>
  <body>
  	<header>
  		<h1>Preguntas y respuestas</h1>
    </header>
    <main>
    	<form action="?" method="POST">
      	<label for="pregunta">Introduce la pregunta</label>
      	<input type="text" name="pregunta" id="pregunta">
        <label for="respuesta">Introduce la respuesta</label>
      	<input type="text" name="respuesta" id="respuesta">
        <input type="submit">
      </form>
    </main>
    <footer>
    	(c) 2025 Jose Vicente Carratala
      <?php
      	if(isset($_POST['respuesta'])){
          $json = json_encode($_POST); 	// Convierte post a JSON
          $archivo = fopen(date('U').".json",'w');	// Abre un arhivo
          fwrite($archivo,$json);										// Guarda el json
          fclose($archivo);													// Cierra el archivo
        }
      ?>
    </footer>
  </body>
</html>
```

### 1764753558

```json
[]
```

### 1764753566

```json
{"pregunta":"que dia es hoy","respuesta":"miercoles"}
```

### archivo

```
Nuevo texto escrito desde PHP
```

<a id="proyecto-ana"></a>
## Proyecto Ana

### Analisis de tecnologias

```markdown
Necesitamos 
HTML, CSS, JS - Esto sin problema

Necesitamos PHP - GitHub pages descartado
Solución?

Contratación de un alojamiento (hosting) que tenga soporte para
HTML
CSS
JS
PHP

Ejemplo: hostinger
Via Render - servicio en la nube que os dé soporte o bien para 
```

### front

```html
<!doctype html>
<html lang="es">
  <head>
  </head>
  <body>
    	<header>
    </header>
    <main>
      <div id="terminal" contenteditable=true>
      </div>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### estilizamos un poco

```html
<!doctype html>
<html lang="es">
  <head>
    <style>
      #editor{
      	font-family:monospace;
        background:lightgray;color:black;padding:20px;
        width:400px;
        height:100px;margin:auto;
        margin-bottom:10px;
      }
      #terminal{
      	font-family:monospace;
        background:black;color:white;padding:20px;
        width:400px;
        height:50px;margin:auto;
      }
      .ventana{
      	border:1px solid grey;
        border-top:30px solid grey;
        border-radius:5px;
        box-shadow:0px 5px 10px rgba(0,0,0,0.3);
      }
      button{
        margin:auto;background:green;
        color:white;padding:10px;border-radius:5px;border:none;
      margin:auto;margin-bottom:10px;display:block;}
    </style>
  </head>
  <body>
    	<header>
    </header>
    <main>
      <div id="editor" contenteditable=true class="ventana"></div>
      <button>Compilar</button>
      <div id="terminal" contenteditable=true class="ventana"></div>
    </main>
    <footer>
    </footer>
  </body>
</html>
```

### javascript

```html
<!doctype html>
<html lang="es">
  <head>
    <style>
      #editor{
      	font-family:monospace;
        background:lightgray;color:black;padding:20px;
        width:400px;
        height:100px;margin:auto;
        margin-bottom:10px;
      }
      #terminal{
      	font-family:monospace;
        background:black;color:white;padding:20px;
        width:400px;
        height:50px;margin:auto;
      }
      .ventana{
      	border:1px solid grey;
        border-top:30px solid grey;
        border-radius:5px;
        box-shadow:0px 5px 10px rgba(0,0,0,0.3);
      }
      button{
        margin:auto;background:green;
        color:white;padding:10px;border-radius:5px;border:none;
      margin:auto;margin-bottom:10px;display:block;}
    </style>
  </head>
  <body>
    	<header>
    </header>
    <main>
      <div id="editor" contenteditable=true class="ventana"></div>
      <button>Compilar</button>
      <div id="terminal" contenteditable=true class="ventana"></div>
    </main>
    <footer>
    </footer>
    <script>
      let boton = document.querySelector("button")
      boton.onclick = function(){
      	console.log("Vamos a enviar algo al servidor")
        let codigo = document.querySelector("#editor").textContent
        console.log(codigo)
      }
    </script>
  </body>
</html>
```

### flask

```python
from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

if __name__ == "__main__":
  app.run(debug=True)
```

### nuevo endpoint

```python
from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

@app.route("/api")
def api():
  print("He recibido algo")
  return "ok"

if __name__ == "__main__":
  app.run(debug=True)
```

### estamos obligados a metodo

```python
from flask import Flask, render_template, request
import io
import contextlib


app = Flask(__name__)

@app.route("/")
def inicio():
  return render_template("frente.html")

@app.route("/api", methods=['POST'])
def api():
    codigo = request.data.decode("utf-8")

    buffer = io.StringIO()
    try:
        # Ejecuta el código y captura todo lo que se imprima
        with contextlib.redirect_stdout(buffer):
            exec(codigo, {})   # entorno global vacío (peligroso igualmente si no controlas el código)
    except Exception as e:
        return str(e), 400

    salida = buffer.getvalue()
    # Si no ha habido nada por pantalla, puedes devolver algo por defecto
    return salida if salida else "OK"

if __name__ == "__main__":
  app.run(debug=True)
```

### soporte multilinea

```python
from flask import Flask, render_template, request
import io
import contextlib

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("frente.html")

@app.route("/api", methods=['POST'])
def api():
    codigo = request.data.decode("utf-8")

    buffer = io.StringIO()
    try:
        # Ejecuta el código y captura todo lo que se imprima
        with contextlib.redirect_stdout(buffer):
            exec(codigo, {})
    except Exception as e:
        # devolvemos el error como texto y código 400
        return str(e), 400

    salida = buffer.getvalue()
    return salida if salida else "OK"

if __name__ == "__main__":
    app.run(debug=True)
```


<a id="git"></a>
# .git

<a id="branches"></a>
## branches

<a id="hooks"></a>
## hooks

<a id="info"></a>
## info

<a id="logs"></a>
## logs

<a id="objects"></a>
## objects

<a id="refs"></a>
## refs
