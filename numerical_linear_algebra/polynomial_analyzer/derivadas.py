# derivadas.py

import sympy as sp

x = sp.Symbol('x')


def derivada(poly):

    derivadas_lista = []

    actual = poly.as_expr()

    while True:

        # Calcular derivada
        actual = sp.diff(actual, x)

        derivadas_lista.append(actual)

        # Detener si es constante
        if actual.is_number:

            break

    return derivadas_lista