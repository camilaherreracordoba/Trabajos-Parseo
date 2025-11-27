from lexer import lexer
from parser import parser
from pprint import pprint
from graphviz import Digraph

def ast_to_graph(node, graph=None, parent=None):
    from graphviz import Digraph

    if graph is None:
        graph = Digraph("AST")
        graph.attr("node", shape="box", fontsize="10")

    if node is None:
        nid = str(id(node))
        graph.node(nid, "None")
        if parent:
            graph.edge(parent, nid)
        return graph

    nid = str(id(node))


    if isinstance(node, tuple):
        label = node[0] 
        graph.node(nid, label)

        if parent:
            graph.edge(parent, nid)

        for i, elemento in enumerate(node[1:], start=1):
            ast_to_graph(elemento, graph, nid)

        return graph


    if isinstance(node, list):
        graph.node(nid, "lista")  
        if parent:
            graph.edge(parent, nid)

        for elemento in node:
            ast_to_graph(elemento, graph, nid)

        return graph

    graph.node(nid, repr(node))
    if parent:
        graph.edge(parent, nid)

    return graph

codigo = """
INICIO:
VAR x = 7;
VAR y = 9;
SALIDA: + x y;
FIN
"""

codigo0 = """ 
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
        ORDENAR POR departamento;
FIN
"""

codigo1 = """
INICIO: VAR entrada = 10; 
VAR umbral = > 4 entrada;
MIENTRAS: umbral 
HACER: SALIDA: entrada; 
entrada = - entrada 1; 
FIN
"""

actual = codigo

print("tokens")
lexer.input(actual)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{tok.type:<15} {tok.value}")

print("\ resultados parser")
resultado = parser.parse(actual, lexer=lexer)
pprint(resultado)

g = ast_to_graph(resultado)
g.render("arbol", view=True)