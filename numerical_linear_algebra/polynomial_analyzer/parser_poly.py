# parser_poly.py
# Convierte notación Wolfram (*^) a Python y genera un Poly de sympy

import re
import sympy as sp

x = sp.Symbol('x')

def parse_polynomial(expr):

    # Wolfram -> Python
    expr = re.sub(r'(\d+(?:\.\d+)?)\*\^([+-]?\d+)', r'\1e\2', expr)

    # Agregar * entre número y x
    expr = re.sub(r'(\d)\s*x', r'\1*x', expr)

    # Convertir a expresión sympy
    expr = sp.sympify(expr)

    poly = sp.Poly(expr, x)

    if poly.degree() > 5:
        raise ValueError("El grado del polinomio debe ser <= 5")

    return poly