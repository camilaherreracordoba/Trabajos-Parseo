import ply.lex as lex

reserved = {
    'INICIO': 'INICIO',
    'FIN': 'FIN',
    'VAR': 'VAR',
    'TABLA': 'TABLA',
    'ASIGNAR': 'ASIGNAR',
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
}


tokens = [
    'IDENTIFICADOR',
    'ENTERO',
    'CADENA',

    'IGUAL', 'PUNTOYCOMA', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'LLAVE_IZQ', 'LLAVE_DER', 'COMA', 'DOSPUNTOS',

    'MAS', 'MENOS', 'MULT', 'DIV', 'MOD',

    'IGUALIGUAL', 'DISTINTO', 'MAYOR', 'MENOR',

    'AND', 'OR', 'NOT',
] + list(reserved.values())

t_PUNTOYCOMA   = r';'
t_IGUAL        = r'='
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_IZQ    = r'\{'
t_LLAVE_DER    = r'\}'
t_COMA         = r','
t_DOSPUNTOS    = r':'


t_IGUALIGUAL   = r'=='
t_DISTINTO     = r'!='
t_MAYOR        = r'>'
t_MENOR        = r'<'
t_AND          = r'&'
t_OR           = r'\|'
t_NOT          = r'!'
t_MAS          = r'\+'
t_MENOS        = r'-'
t_MULT         = r'\*'
t_DIV          = r'/'
t_MOD          = r'%'


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9_-]*'
    t.type = reserved.get(t.value.upper(), 'IDENTIFICADOR')
    return t


t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()


data = '''
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

'''

lexer.input(data)
for tok in lexer:
    print(tok)