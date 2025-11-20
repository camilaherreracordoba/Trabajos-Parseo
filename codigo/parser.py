import ply.lex as lex
import ply.yacc as yacc
from lexer import tokens
# --------------------------
#  Reglas sintácticas
# --------------------------
# <programa> ::= "INICIO:" <bloque> "FIN"
def p_programa(p):
    'programa : INICIO DOSPUNTOS bloque FIN'
    p[0] = ("programa", p[3])

#<bloque> ::= <sentencia> <bloque> | λ
def p_bloque(p):
    '''bloque : sentencia
              | sentencia bloque'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_bloque_vacio(p):
    '''bloque : vacio'''
    p[0] = []

#<sentencia> ::= <declaracion_tabla> ";"
#               | <declaracion_var> ";"
#               | <asignacion> ";"
#               | <salida> ";"
#               | <consulta> ";"
#               | <condicional>
#               | <bucle>
def p_sentencia(p):
    '''sentencia : declaracion_var PUNTOYCOMA
                 | declaracion_tabla PUNTOYCOMA
                 | asignacion PUNTOYCOMA
                 | salida PUNTOYCOMA
                 | consulta PUNTOYCOMA
                 | condicional
                 | bucle'''
    p[0] = p[1]

# -----------------------------
#   Declaraciones
# ------------------------------

# <declaracion_var> ::= "VAR" <identificador> "=" <expresion>
def p_declaracion_var(p):
    'declaracion_var : VAR IDENTIFICADOR IGUAL expresion'
    p[0] = ("declaracion_var", p[2], p[4])

# <declaracion_tabla> ::= "VAR" "TABLA" <identificador> "=" "[" <lista_filas> "]"
def p_declaracion_tabla(p):
    'declaracion_tabla : VAR TABLA IDENTIFICADOR IGUAL CORCHETE_IZQ filas CORCHETE_DER'
    p[0] = ("declaracion_tabla", p[3], p[6])

# <lista_filas> ::= <fila> <lista_filas> | λ
def p_lista_filas(p):
    '''filas : fila
             | fila COMA filas
             | vacio'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

# <fila> ::= "{" <atributo_fila> <atributos> "}"
def p_fila(p):
    '''fila : LLAVE_IZQ atributo_fila atributos LLAVE_DER'''
    p[0] = dict([p[2]] + p[3])

# <atributos> ::= "," <atributo_fila> <atributos> | λ
def p_atributos(p):
    '''atributos : COMA atributo_fila atributos
                 | vacio'''
    if len(p) == 4:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

# <atributo_fila> ::= <identificador> ":" <dato_literal>
def p_atributo_fila(p):
    'atributo_fila : IDENTIFICADOR DOSPUNTOS dato_literal'
    p[0] = (p[1], p[3])


# -----------------------------
#   Asignación y salida
# -----------------------------
# <asignacion> ::= <identificador> "=" <expresion>
def p_asignacion(p):
    'asignacion : IDENTIFICADOR IGUAL expresion'
    p[0] = ("asignacion", p[1], p[3])

# <salida> ::= "SALIDA:" <expresion>
def p_salida(p):
    'salida : SALIDA DOSPUNTOS expresion'
    p[0] = ("salida", p[3])


# -----------------------------
#   Condicionales y bucles
# -----------------------------

# <condicional> ::= "SI:" <expresion> "ENTONCES:" <bloque> 
#                | "SI:" <expresion> "ENTONCES:" <bloque> "SINO:" <bloque>
def p_condicional(p):
    '''condicional : SI DOSPUNTOS expresion ENTONCES DOSPUNTOS bloque
                   | SI DOSPUNTOS expresion ENTONCES DOSPUNTOS bloque SINO DOSPUNTOS bloque'''
    if len(p) == 7:
        p[0] = ("si", p[3], p[6])
    else:
        p[0] = ("si_sino", p[3], p[6], p[9])

# <bucle> ::= "MIENTRAS:" <expresion> "HACER:" <bloque>
def p_bucle(p):
    'bucle : MIENTRAS DOSPUNTOS expresion HACER DOSPUNTOS bloque'
    p[0] = ("mientras", p[3], p[6])


# -----------------------------
#   Expresiones
# -----------------------------
#<expresion> ::= <literal>
#              | <identificador>
#              | <consulta>
#              | <expresion_prefija>
def p_expresion(p):
    '''expresion : literal
                 | IDENTIFICADOR
                 | consulta
                 | expresion_prefija'''
    p[0] = p[1]

#<expresion_prefija> ::= <op_aritmetico> <operando> <operando>
#                      | <op_comparacion> <operando> <operando>
#                      | <op_logico> <operando> <operando>
#                      | <op_negacion> <operando>

def p_expresion_prefija(p):
    '''expresion_prefija : op_aritmetico operando operando
                         | op_comparacion operando operando
                         | op_logico operando operando
                         | op_negacion operando'''
    if len(p) == 4:
        p[0] = ("expr_prefija_binaria", p[1], p[2], p[3])
    else:
        p[0] = ("expr_prefija_unaria", p[1], p[2])

# <operando> ::= <literal> | <identificador> | <consulta> | <expresion_prefija>
def p_operando(p):
    '''operando : literal
                | IDENTIFICADOR
                | consulta
                | expresion_prefija'''
    p[0] = p[1]


# --------------------------------------
#   Consultas 
# --------------------------------------
# <consulta> ::= "SELECCIONAR" <columnas> "DE" <identificador> | "SELECCIONAR" <columnas> "DE" <identificador> <opciones_consulta>
def p_consulta(p):
    '''consulta : SELECCIONAR columnas DE IDENTIFICADOR
                | SELECCIONAR columnas DE IDENTIFICADOR opciones_consulta'''
    if len(p) == 5:
        p[0] = ("consulta", p[2], p[4])
    else:
        p[0] = ("consulta_opciones", p[2], p[4], p[5])

# <opciones_consulta> ::= "DONDE" <expresion>
#                      | "AGRUPAR" "POR" <columnas> 
#                      | "ORDENAR" "POR" <columnas>

def p_opciones_consulta(p):
    '''opciones_consulta : DONDE expresion
                         | AGRUPAR POR columnas
                         | ORDENAR POR columnas'''
    if p[1] == 'DONDE':
        p[0] = ("donde", p[2])
    elif p[1] == 'AGRUPAR':
        p[0] = ("agrupar", p[3])
    else:
        p[0] = ("ordenar", p[3])

# <columnas> ::= <identificador> "," <columnas> | <identificador>
def p_columnas(p):
    '''columnas : IDENTIFICADOR COMA columnas
                | IDENTIFICADOR'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

# -----------------------------
#   Literales
# -----------------------------
# <literal> ::= <entero> | <booleano> | <cadena>
def p_literal(p):
    '''literal : ENTERO
               | booleano
               | CADENA'''
    p[0] = p[1]

# <booleano> ::= "VERDADERO" | "FALSO"
def p_booleano(p):
    '''booleano : VERDADERO
                | FALSO'''
    p[0] = (p[1] == "VERDADERO")

# <dato_literal> ::= <booleano> | <cadena> | <entero>
def p_dato_literal(p):
    '''dato_literal : booleano
                    | CADENA
                    | ENTERO'''
    p[0] = p[1]

# -----------------------------
#   Operadores
# -----------------------------
# <op_aritmetico> ::= "+" | "-" | "*" | "/" | "%"
def p_op_aritmetico(p):
    '''op_aritmetico : MAS
                     | MENOS
                     | MULT
                     | DIV
                     | MOD'''
    p[0] = p[1]

# <op_comparacion> ::= "==" | "!=" | ">" | "<"
def p_op_comparacion(p):
    '''op_comparacion : IGUALIGUAL
                      | DISTINTO
                      | MAYOR
                      | MENOR'''
    p[0] = p[1]

# <op_logico> ::= "&" | "|" | "IGUALES"
def p_op_logico(p):
    '''op_logico : AND
                 | OR
                 | IGUALES'''
    p[0] = p[1]

# <op_negacion> ::= "!"
def p_op_negacion(p):
    'op_negacion : NOT'
    p[0] = p[1]


# -----------------------------
#   Vacío
# -----------------------------

def p_vacio(p):
    '''vacio :'''
    pass


# -----------------------------
#   Manejo de errores
# -----------------------------

def p_error(p):
    if p:
        print(f"Error sintáctico en '{p.value}' (línea {p.lineno})")
    else:
        print("Error sintáctico: fin de archivo inesperado") 

parser = yacc.yacc()