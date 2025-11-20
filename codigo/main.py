# main.py
from lexer import lexer
from parser import parser

# Ejemplo a analizar
codigo0 = """
INICIO:
VAR x = 7;
VAR y = 9;
SALIDA: + x y;
FIN
"""

codigo = """ 
INICIO:

VAR TABLA empleados = [
	{ nombre: "Ana", edad: 30, salario: 2000, departamento: "Ventas" },
	{ nombre: "Luis", edad: 45, salario: 3000, departamento: "Ventas" },
	{ nombre: "Marta", edad: 29, salario: 2500, departamento: "IT" },
	{ nombre: "Pedro", edad: 35, salario: 2800, departamento: "IT" }
];

VAR bono = + 500 200;

bono = * bono 2;

SALIDA: bono;

SI: > bono 1000 ENTONCES:
	SALIDA: "Bono mayor a mil";
SINO:
	SALIDA: "Bono menor o igual a mil";

MIENTRAS: < bono 3000 HACER:
	bono = + bono 100;
	SALIDA: bono;

SALIDA: SELECCIONAR nombre, salario DE empleados DONDE > salario 2500;

SALIDA: SELECCIONAR departamento, salario DE empleados 
        AGRUPAR POR departamento;

FIN
"""

print("tokens")
lexer.input(codigo)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{tok.type:<15} {tok.value}")

print("\ resultados parser")
resultado = parser.parse(codigo, lexer=lexer)
print(resultado)