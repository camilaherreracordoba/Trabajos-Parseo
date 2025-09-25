# Trabajos-Parseo

### TP1: Mapa conceptual
```mermaid
flowchart
    A[Traductores]
    A --> F[Función]
    F --> G[Reciben instrucciones dadas en un lenguaje fuente de alto nivel]
    G --> G1[Convierten el código a un lenguaje objeto comprensible para el procesador]
    A --> B[Tipos]
    B --> C[Intérpretes]
    B --> D[Ensambladores]
    B --> E[Compiladores]

    C --> J[Ejecutan directamente las intrucciones de un lenguaje dado]
    D --> H[Convierten el lenguaje ensamblador al código de una maquina determinada]
    E --> K[Transforman un código a una versión equivalente en un lenguaje de bajo nivel]
    

    E --> L[Herramientas]
        L --> L1[Editores]
        L1 --> L11[Permiten leer, escribir y modificar programas]
        L1 --> L12[Conforman entorno de desarrollo integrado con el compilador]
        L --> L2[Preprocesadores]
        L2 --> L21[Modifican el programa antes del proceso de compilación]
        L2 --> L22[Pueden eliminar comentarios, incluir librerías y sustituyen las macro instrucciones con las sentencias por las que estan compuestas]
        L --> L3[Enlazadores]
        L3 --> L31[Unen los modulos del código para crear un archivo ejecutable]
        L3 --> L32[Hacen llamadas a las funciones referenciadas de librerias]
        L --> L4[Cargadores]
        L4 --> L41[Asignan el espacio de memoria y las direcciones necesarias para el programa]
        L --> L5[Depuradores]
        L5 --> L51[Herramientas que facilitan la detección de errores]
        L5 --> L52[permiten ejecutar el programa paso a paso y seleccionar variables para visualizar sus cambios]
        L --> L6[Desensambladores]
        L6 --> L61[Herramientas de ingeniería inversa que traducen el lenguaje máquina a ensamblador]
        L --> L7[Decompiladores]
        L7 --> L71[Traducen código máquina a un lenguaje de alto nivel]

    
        L --> L8[Transpiladores]
        L8 --> L81[Leen un código fuente en un lenguaje dado y generan un código equivalente en otro lenguaje]
```


### TP2: Lenguaje a crear 

#### Objetivo
El lenguaje a desarrollar es un lenguaje de dominio específico procedural para la manipulación de **bases de datos**. Cuenta con soporte de estructuras de control (condicionales y bucles). Permite definir variables, tablas de datos y realiza también consultas básicas. Las operaciones aritméticas y lógicas se usan con notación polaca (prefija), y las palabras claves están en español.
#### Alcance
Su función es simular operaciones de SQL procedural en memoria y ejecutar consultas con expresiones booleanas y aritméticas en notación prefija.

No soporta joins complejos, subconsultas anidadas, recursión ni concurrencia. No interactúa con archivos ni bases de datos externas (datos en memoria únicamente)

#### Especificaciones léxicas
##### Palabras reservadas

Palabra |  Significado
--------|-------
INICIO:| Indica el inicio de un programa
FIN | Indica el fin de un programa
SALIDA:| Imprime una expresion númerica o booleana.
SI: | Inicia una estructura condicional (If)
ENTONCES:| Indica el inicio del bloque a ejecutar si la condición es VERDADERA
SINO:| Indica el bloque a ejecutar si la condición es FALSA
MIENTRAS:| Define la condición a cumplir para ejecutar un bucle (While)
HACER: | Indica el bloque de sentencias a ejecutar si la condición del bucle es verdadera
VAR | Inicia la declaración de una variable
ENTERO | Indica que el tipo de dato de la variable declarada es entero
BOOLEANO | Indica que el tipo de dato de la variable declarada es booleano
TABLA | Indica que la variable declarada es una tabla en memoria

#### Palabra reservadas operaciones procedurales

Palabra |  Significado
--------|-------
SELECCIONAR	| Inicia una consulta sobre una tabla declarada
DE | Indica la tabla fuente de la consulta
DONDE | Especifica una condición de filtrado (equivalente a WHERE)
AGRUPAR POR | Agrupa los resultados de la consulta según una o más columnas
ORDENAR POR | Ordena los resultados según una o más columnas

##### Identificadores

Los identificadores minimamente estan compuestos por una letra en minúscula (a-z), o mayúscula (A-Z) y pueden ser sucedidos por otra letra, un numero (0 - 9) o un guion bajo o medio (_/-). 

##### Operadores
|Tipo | Operador |
|-----|----------|
| Aritmetico | "+", "-", "/", "*", "%" |
| Logico | "&", "\|" |
| Comparación | "==", "!=", ">", "<" | 
| Asignación | "=" |
| Negación | "!" | 
| Fin de sentencia | ";" |
##### Tipos de datos 
| Tipo | Valores |
------------------|--------------
| Booleano | "VERDADERO", "FALSO" |
|Entero | (0-9)+ |
|Cadena | Secuencias de caracteres entre comillas "..."|
| Tabla | conjunto de filas en memoria
#### Especificaciones sintácticas
[Notación BNF del lenguaje](notacion_bnf_v2.md)

Regla | Especificación
-------------|------------
Estructura del programa | El programa siempre empieza con la palabra INICIO, seguida por un bloque de sentencias y finaliza con FIN.
Bloque | Está compuesto por cero o más sentencias
Sentencia | Puede ser la declaracion o asignación de una variable, una estructura condicional, un bucle o una salida por pantalla. Todas, menos las sentencias condicionales y los bucles, deben terminar con ";".
Declaración | Inicializa una variable iniciando con la palabra VAR y luego indicando su tipo, su identificador y su valor inicial.
Asignación | Asigna un valor a una variable ya declarada, indicando su identificador seguido por "=" y su nuevo valor.
Salida | Imprime una expresion númerica o booleana.
Condicional | Estructura de control que selecciona un bloque dependiendo de una expresión booleana
Bucle | Ejecuta un bloque en caso de que una condición sea verdadera
Expresión | Operaciones o identificadores que reprensentan o producen valores numericos o booleanos.

#### Especificaciones semánticas

- **Declaraciones**: Cada variable debe ser declarada una única vez. Las variables definidas dentro del programa son de ámbito local, mientras que las definidas dentro de las estructuras condicionales o de bucle corresponden a un subambito y por lo tanto solamente pueden ser usadas dentro de esa estructura.
- **Asignaciones**: Deben realizarse sobre una variable existente con un identificador válido. El valor asignado tiene que ser del mismo tipo que la variable.
- **Operaciones**: todas las operaciones aritméticas o booleanas son realizadas con notación prefija, de forma que el operador precede a los operandos. 
     - **Aritméticas**: "+", "-", "*", "/", "%" solamente entre enteros.
     - **Comparaciones**: "==", "!=",">" y "<" solo entre enteros.
     - **Booleanas**: "&", "|", "!" solamente sobre valores booleanos.

- **Condicional**: las condiciones deben ser expresiones booleanas válidas. Todas las variables definidas previamente pueden ser usadas dentro del bloque de sentencias, mientras que las definidas dentro del bloque solamente pueden usarse dentro del mismo.
- **Bucle**: las condiciones deben ser expresiones booleanas válidas. Todas las variables definidas previamente pueden ser usadas dentro del bloque de sentencias, mientras que las definidas dentro del bloque solamente pueden usarse dentro del mismo.
- **Salida**: Solamente imprime expresiones válidas bien tipadas.
- **Errores**: en caso de no respetarse las especificaciones correspondietnes a cada caso, se debe lanzar un mensaje de error dando detalle para cada uno.
- **Consultas**: filtran datos en memoria según la expresión booleana en DONDE.


#### Ejemplo del lenguaje
```lisp
INICIO:

VAR empleados TABLA = [
	{ nombre: "Ana", edad: 30, salario: 2000, departamento: "Ventas" },
	{ nombre: "Luis", edad: 45, salario: 3000, departamento: "Ventas" },
	{ nombre: "Marta", edad: 29, salario: 2500, departamento: "IT" },
	{ nombre: "Pedro", edad: 35, salario: 2800, departamento: "IT" }
];

VAR bono = + 500 200;

ASIGNAR bono = * bono 2;

SALIDA: bono;

SI: > bono 1000 ENTONCES:
	SALIDA: "Bono mayor a mil"
SINO:
	SALIDA: "Bono menor o igual a mil";

MIENTRAS: < bono 3000 HACER:
	ASIGNAR bono = + bono 100;
	SALIDA: bono;

SALIDA: SELECCIONAR nombre, salario DE empleados DONDE > salario 2500;

SALIDA: SELECCIONAR departamento, salario DE empleados 
        AGRUPAR POR departamento 
        ORDENAR POR salario;

FIN

```

### ejemplo de derivación por izquierda

```
INICIO:
VAR x = 7;
VAR y = 9;
SALIDA: + 7 9;
FIN
```

| Cadena actual                                    | Regla a aplicar |
|----------------------------------------------------|----------------|
| `<programa>`                                        | `<programa> ::= INICIO: <bloque> FIN` |
| `INICIO: <bloque> FIN`                              | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: <sentencia> <bloque> FIN`                 | `<sentencia> ::= <declaracion_var> ;` |
| `INICIO: <declaracion_var> ; <bloque> FIN`         | `<declaracion_var> ::= VAR <identificador> = <expresion>` |
| `INICIO: VAR <identificador> = <expresion> ; <bloque> FIN` | `<identificador> ::= <letra> <resto_identificador>` |
| `INICIO: VAR x = <expresion> ; <bloque> FIN`       | `<expresion> ::= <literal>` |
| `INICIO: VAR x = <literal> ; <bloque> FIN`         | `<literal> ::= <entero>` |
| `INICIO: VAR x = 7 ; <bloque> FIN`                 | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: VAR x = 7 ; <sentencia> <bloque> FIN`     | `<sentencia> ::= <declaracion_var> ;` |
| `INICIO: VAR x = 7 ; VAR <identificador> = <expresion> ; <bloque> FIN` | `<identificador> ::= <letra>` |
| `INICIO: VAR x = 7 ; VAR y = <expresion> ; <bloque> FIN` | `<expresion> ::= <literal>` |
| `INICIO: VAR x = 7 ; VAR y = <literal> ; <bloque> FIN` | `<literal> ::= <entero>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; <bloque> FIN`     | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; <sentencia> <bloque> FIN` | `<sentencia> ::= <salida> ;` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: <expresion> ; <bloque> FIN` | `<expresion> ::= <arit_pref>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: <arit_pref> ; <bloque> FIN` | `<arit_pref> ::= <op_aritmetico> <expresion> <expresion>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: + <expresion> <expresion> ; <bloque> FIN` | `<expresion> ::= <literal>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: + 7 <expresion> ; <bloque> FIN` | `<expresion> ::= <literal>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: + 7 9 ; <bloque> FIN` | `<bloque> ::= <vacio>` |
| `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: + 7 9 ; FIN` | `<vacio> ::= λ` |

### ejemplo de derivacion por derecha
```
INICIO:
VAR x = 7;
VAR y = 9;
SALIDA: + 7 9;
FIN
```

| Cadena Actual                                   | Regla a aplicar |
|----------------------------------------------------|----------------|
| `<programa>`                                        | `<programa> ::= INICIO: <bloque> FIN` |
| `INICIO: <bloque> FIN`                              | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: <sentencia> <bloque> FIN`                 | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: <sentencia> <sentencia> <bloque> FIN`     | `<bloque> ::= <sentencia> <bloque>` |
| `INICIO: <sentencia> <sentencia> <sentencia> <vacio> FIN` | `<bloque> ::= <vacio>` |
| Última sentencia: `SALIDA: <expresion> ;`          | `<sentencia> ::= <salida> ;` |
| `<expresion> ::= <arit_pref>`                       | `<arit_pref> ::= <op_aritmetico> <expresion> <expresion>` |
| `<expresion> ::= <literal>`                          | `<literal> ::= <entero>` |
| Resultado: `SALIDA: + 7 9 ;`                        | - |
| Segunda sentencia: `VAR y = <expresion> ;`         | `<sentencia> ::= <declaracion_var> ;` |
| `<expresion> ::= <literal>`                          | `<literal> ::= <entero>` |
| Resultado: `VAR y = 9 ;`                            | - |
| Primera sentencia: `VAR x = <expresion> ;`         | `<sentencia> ::= <declaracion_var> ;` |
| `<expresion> ::= <literal>`                          | `<literal> ::= <entero>` |
| Resultado: `VAR x = 7 ;`                            | - |
| `<vacio> ::= λ`                                     | `<bloque> ::= <vacio>` |
| Combinación final: `INICIO: VAR x = 7 ; VAR y = 9 ; SALIDA: + 7 9 ; FIN` | - |
