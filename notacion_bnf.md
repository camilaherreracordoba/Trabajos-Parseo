### Notación BNF
```bnf
<programa> ::= "INICIO:" <bloque> "FIN"

<bloque> ::= <sentencia> | <sentencia> <bloque> | λ

<sentencia> ::= <declaracion> ";" | <condicional> | <bucle> | <asignacion> ";" | <salida> ";"

<salida> ::= "SALIDA:" <expresion>

<condicional> ::= "SI:" <expresion_booleana> "ENTONCES:" <bloque>
                | "SI:" <expresion_booleana> "ENTONCES:" <bloque> "SINO:" <bloque>

<bucle> ::= "MIENTRAS:" <expresion_booleana> "HACER:" <bloque>

<asignacion> ::= <identificador> <op_asignacion> <expresion>

<expresion> ::= <expresion_numerica> | <expresion_booleana>

<declaracion> ::= "VAR" <identificador> <declaracion_entero>
                | "VAR" <identificador> <declaracion_booleano>

<declaracion_entero> ::= "ENTERO" <op_asignacion> <expresion_numerica>

<declaracion_booleano> ::= "BOOLEANO" <op_asignacion> <expresion_booleana>

<expresion_booleana> ::= <booleano>
                       | <identificador>
                       | <op_logico> <expresion_booleana> <expresion_booleana>
                       | <op_negacion> <expresion_booleana>
                       | <expresion_comparacion>

<expresion_numerica> ::= <entero>
                       | <identificador>
                       | <op_aritmetico> <expresion_numerica> <expresion_numerica>

<expresion_comparacion> ::= <op_comparacion> <expresion_numerica> <expresion_numerica>

<identificador> ::= <letra> | <letra> <identificador_otros> | <letra> <identificador>
<identificador_otros> ::= <digito> | <digito> <identificador_otros> | <digito> <identificador>
                        | <guion> | <guion> <identificador_otros> | <guion> <identificador>
 
<op_asignacion> ::= "="
<op_comparacion> ::= "==" | "!=" | ">" | "<" 
<op_logico> ::= "&" | "|"
<op_negacion> ::= "!"
<op_aritmetico> ::= "+" | "-" | "/" | "*" | "%"
<booleano> ::= "VERDADERO" | "FALSO"
<entero> ::= <digito> | <digito> <entero>
<digito> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<letra> ::= "a" | ... | "z" | "A" | ... | "Z"
<guion> ::= "-" | "_"

```