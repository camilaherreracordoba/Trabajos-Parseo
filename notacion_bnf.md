```bnf
<programa> ::= "INICIO:" <bloque> "FIN"

<bloque> ::= <vacio>
           | <sentencia> <bloque>

<sentencia> ::= <declaracion_tabla> ";"
              | <declaracion_var> ";"
              | <asignacion> ";"
              | <salida> ";"
              | <condicional>
              | <bucle>

<declaracion_var> ::= "VAR" <identificador> "=" <expresion>
<declaracion_tabla> ::= "VAR" "TABLA" <identificador> "=" "[" <filas> "]"

<filas> ::= <vacio>
         | <fila> <filas>
<fila> ::= "{" <pares> "}"
<pares> ::= <vacio>
         | <par> <pares_rest>
<pares_rest> ::= <vacio> | "," <par> <pares_rest>
<par> ::= <identificador> ":" <literal>

<asignacion> ::= "ASIGNAR" <identificador> "=" <expresion>

<salida> ::= "SALIDA:" <expresion>

<condicional> ::= "SI:" <expresion> "ENTONCES:" <bloque> <sino_opt>
<sino_opt> ::= <vacio> | "SINO:" <bloque>

<bucle> ::= "MIENTRAS:" <expresion> "HACER:" <bloque>

<consulta> ::= "SELECCIONAR" <columnas> "DE" <identificador> <opciones_consulta>
<opciones_consulta> ::= <vacio>
                      | "DONDE" <expresion>
                      | "AGRUPAR" "POR" <columnas>
                      | "ORDENAR" "POR" <columnas>

<columnas> ::= <identificador>
             | <identificador> "," <columnas>

<expresion> ::= <literal>
              | <identificador>
              | <consulta>
              | <arit_pref>
              | <comp_pref>
              | <log_pref>
              | <neg_pref>

<arit_pref> ::= <op_aritmetico> <expresion> <expresion>
<comp_pref> ::= <op_comparacion> <expresion> <expresion>
<log_pref>  ::= <op_logico> <expresion> <expresion>
<neg_pref>  ::= <op_negacion> <expresion>

<literal> ::= <entero> | <booleano> | <cadena>
<entero> ::= <digito> | <entero> <digito>
<booleano> ::= "VERDADERO" | "FALSO"
<cadena> ::= "\"" <caracteres> "\""
<caracteres> ::= <vacio> | <caracteres> <caracter>
<caracter> ::= <letra> | <digito> | "-" | "_"

<op_aritmetico> ::= "+" | "-" | "*" | "/" | "%"
<op_comparacion> ::= "==" | "!=" | ">" | "<"
<op_logico> ::= "&" | "|"
<op_negacion> ::= "!"


<identificador> ::= <letra> <resto_identificador>
<resto_identificador> ::= <vacio> | <resto_identificador> <letra_digito_guion>
<letra_digito_guion> ::= <letra> | <digito> | "_" | "-"

<letra> ::= "a" | ... | "z" | "A" | ... | "Z"
<digito> ::= "0" | "1" | ... | "9"

<vacio> ::= λ
```