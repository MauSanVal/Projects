# extremos.py

import sympy as sp
from raices import raices_complejas

x = sp.Symbol('x')


def maximos_minimos(poly):

    f = poly.as_expr()

    # Primera y segunda derivada
    f1 = sp.diff(f, x)
    f2 = sp.diff(f1, x)

    # Convertir derivada a Poly
    poly_f1 = sp.Poly(f1, x)

    # Calcular raíces usando TU algoritmo
    criticos = raices_complejas(poly_f1)

    resultado = []

    for c in criticos:

        # Ignorar raíces complejas no reales
        if abs(c.imag) > 1e-8:
            continue

        c_real = c.real

        val = float(f2.subs(x, c_real).evalf())

        if val > 0:
            tipo = "Mínimo local"

        elif val < 0:
            tipo = "Máximo local"

        else:
            tipo = "Punto crítico inconcluso"

        resultado.append((c_real, tipo))

    return resultado