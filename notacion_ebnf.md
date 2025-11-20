```bnf
<programa> ::= "INICIO:" <bloque> "FIN"

<bloque> ::= <sentencia> <bloque> | λ

<sentencia> ::= <declaracion_tabla> ";"
               | <declaracion_var> ";"
               | <asignacion> ";"
               | <salida> ";"
               | <consulta> ";"
               | <condicional>
               | <bucle>

<declaracion_var> ::= "VAR" <identificador> "=" <expresion>

<declaracion_tabla> ::= "VAR" "TABLA" <identificador> "=" "[" <lista_filas> "]"
<lista_filas> ::= <fila> <lista_filas> | λ

<fila> ::= "{" <atributo_fila> <atributos> "}"
<atributos> ::= "," <atributo_fila> <atributos> | λ

<atributo_fila> ::= <identificador> ":" <dato_literal>
<dato_literal> ::= <booleano> | <cadena> | <entero>

<asignacion> ::= <identificador> "=" <expresion>
<salida> ::= "SALIDA:" <expresion>

<condicional> ::= "SI:" <expresion> "ENTONCES:" <bloque> 
                | "SI:" <expresion> "ENTONCES:" <bloque> "SINO:" <bloque>
<bucle> ::= "MIENTRAS:" <expresion> "HACER:" <bloque>

<consulta> ::= "SELECCIONAR" <columnas> "DE" <identificador> | "SELECCIONAR" <columnas> "DE" <identificador> <opciones_consulta>
<opciones_consulta> ::= "DONDE" <expresion>
                      | "AGRUPAR" "POR" <columnas> 
                      | "ORDENAR" "POR" <columnas>

<columnas> ::= <identificador> "," <columnas> | <identificador>


<expresion> ::= <literal>
              | <identificador>
              | <consulta>
              | <expresion_prefija>

<expresion_prefija> ::= <op_aritmetico> <operando> <operando>
                      | <op_comparacion> <operando> <operando>
                      | <op_logico> <operando> <operando>
                      | <op_negacion> <operando>

<operando> ::= <literal> | <identificador> | <consulta> | <expresion_prefija>

<literal> ::= <entero> | <booleano> | <cadena>
<entero> ::= <digito> | <digito> <entero>
<booleano> ::= "VERDADERO" | "FALSO"
<cadena> ::= """ <caracteres> """


<op_aritmetico> ::= "+" | "-" | "*" | "/" | "%"
<op_comparacion> ::= "==" | "!=" | ">" | "<"
<op_logico> ::= "&" | "|" | "IGUALES"
<op_negacion> ::= "!"

<identificador> ::= <letra> <caracteres>
<caracteres> ::= <caracter> <caracteres> | λ
<caracter> ::= <letra> | <digito> | "-" | "_"
<letra> ::= "a" | ... | "z" | "A" | ... | "Z"
<digito> ::= "0" | "1" | ... | "9"
```