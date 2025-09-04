<programa> ::= "INICIO:" <bloque> "FIN"

<bloque> ::= <sentencia> | <sentencia> <bloque>

<sentencia> ::= <declaracion_tabla> ";"
              | <declaracion_var> ";"
              | <asignacion> ";"
              | <salida> ";"
              | <condicional>
              | <bucle>

<declaracion_tabla> ::= "VAR" <identificador> "TABLA" "=" "[" <filas> "]"
<filas> ::= <fila> | <fila> "," <filas>
<fila> ::= "{" <pares> "}"
<pares> ::= <par> | <par> "," <pares>
<par> ::= <identificador> ":" <literal>

<declaracion_var> ::= "VAR" <identificador> "=" <expresion>
<asignacion> ::= "ASIGNAR" <identificador> "=" <expresion>
<salida> ::= "SALIDA:" <expresion>

<condicional> ::= "SI:" <expresion_booleana> "ENTONCES:" <bloque>
                | "SI:" <expresion_booleana> "ENTONCES:" <bloque> "SINO:" <bloque>

<bucle> ::= "MIENTRAS:" <expresion_booleana> "HACER:" <bloque>

<expresion> ::= <literal>
              | <identificador>
              | <expresion_aritmetica>
              | <expresion_booleana>
              | <consulta>

<consulta> ::= "SELECCIONAR" <columnas> "DE" <identificador> <opciones_consulta>
<opciones_consulta> ::= 
                      | "DONDE" <expresion_booleana>
                      | "AGRUPAR POR" <columnas>
                      | "ORDENAR POR" <columnas>

<columnas> ::= <identificador> | <identificador> "," <columnas>

<expresion_aritmetica> ::= <op_aritmetico> <expresion> <expresion>
<expresion_booleana>   ::= <booleano>
                         | <identificador>
                         | <op_logico> <expresion_booleana> <expresion_booleana>
                         | <op_negacion> <expresion_booleana>
                         | <expresion_comparacion>

<expresion_comparacion> ::= <op_comparacion> <expresion> <expresion>

<literal> ::= <entero> | <booleano> | <cadena>
<entero> ::= <digito> | <digito> <entero>
<booleano> ::= "VERDADERO" | "FALSO"
<cadena> ::= "\"" <caracteres> "\""

<op_aritmetico> ::= "+" | "-" | "*" | "/" | "%"
<op_comparacion> ::= "==" | "!=" | ">" | "<"
<op_logico> ::= "&" | "|"
<op_negacion> ::= "!"

<identificador> ::= <letra> | <letra> <identificador>
<caracteres> ::= <caracter> | <caracter> <caracteres>
<caracter> ::= <letra> | <digito> | "-" | "_"
<letra> ::= "a" | ... | "z" | "A" | ... | "Z"
<digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
