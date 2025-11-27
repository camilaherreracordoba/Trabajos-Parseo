import ply.lex as lex

# ------------------palabras reservadas ----------------------
reserved = {
    'INICIO': 'INICIO',
    'FIN': 'FIN',
    'VAR': 'VAR',
    'TABLA': 'TABLA',
    'SALIDA': 'SALIDA',
    'SI': 'SI',
    'ENTONCES': 'ENTONCES',
    'SINO': 'SINO',
    'MIENTRAS': 'MIENTRAS',
    'HACER': 'HACER',
    'SELECCIONAR': 'SELECCIONAR',
    'DE': 'DE',
    'DONDE': 'DONDE',
    'AGRUPAR': 'AGRUPAR',
    'POR': 'POR',
    'ORDENAR': 'ORDENAR',
    'VERDADERO': 'VERDADERO',
    'FALSO': 'FALSO',
    'IGUALES': 'IGUALES',
}
# ---------------- tokens ----------------------------------
tokens = [
    'IDENTIFICADOR',
    'ENTERO',
    'CADENA',
    'IGUAL', 
    'PUNTOYCOMA', 
    'CORCHETE_IZQ', 'CORCHETE_DER',
    'LLAVE_IZQ', 'LLAVE_DER', 
    'COMA', 'DOSPUNTOS',
    'MAS', 'MENOS', 'MULT', 'DIV', 'MOD',
    'IGUALIGUAL', 'DISTINTO', 'MAYOR', 'MENOR',
    'AND', 'OR', 'NOT',
] + list(reserved.values())

# ----------- simbolos --------------------------------------
t_PUNTOYCOMA = r';'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_COMA = r','
t_DOSPUNTOS = r':'
# --------- operadores ------------------
# comparacion
t_IGUALIGUAL = r'=='
t_DISTINTO = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
# asignacion
t_IGUAL = r'='
# logicos
t_AND = r'&'
t_OR = r'\|'
t_NOT = r'!'
# aritmeticos
t_MAS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
# --------------------------------------
#-------------- Literales ----------------- 
# enteros
def t_ENTERO(t):
    r'\d+'
    # castea a int
    t.value = int(t.value)
    return t
# cadenas
def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    # se excluyen las comillas del resto de la cadena
    t.value = t.value[1:-1]
    t.lexer.lineno += t.value.count('\\n')
    return t

# verificacion de Identificador o palabra reservada (en mayuscula)
def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9_-]*'
    if t.value in reserved: 
        t.type = reserved[t.value]
    return t

# tabulaciones
t_ignore = " \t"
# salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# errores
def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
# comentarios (no especificado en la gramatica pero sirve)
def t_comment(t):
    r'//.*'
    pass

lexer = lex.lex()
