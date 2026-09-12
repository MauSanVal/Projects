# concavidad.py

import sympy as sp
from raices import raices_complejas

x = sp.Symbol('x')


def concavidad(poly):

    f = poly.as_expr()

    # Segunda derivada
    f2 = sp.diff(f, x, 2)

    # Convertir a Poly
    poly_f2 = sp.Poly(f2, x)

    # Raíces usando TU algoritmo QR
    puntos = raices_complejas(poly_f2)

    # Conservar solo raíces reales
    puntos_reales = []

    for r in puntos:

        if abs(r.imag) < 1e-8:
            puntos_reales.append(r.real)

    puntos_reales.sort()

    intervalos = []

    regiones = [-sp.oo] + puntos_reales + [sp.oo]

    for i in range(len(regiones) - 1):

        a = regiones[i]
        b = regiones[i + 1]

        # Punto de prueba
        if a == -sp.oo:

            test = b - 1

        elif b == sp.oo:

            test = a + 1

        else:

            test = (a + b) / 2

        val = f2.subs(x, test)

        if val > 0:
            tipo = "Cóncava hacia arriba"

        elif val < 0:
            tipo = "Cóncava hacia abajo"

        else:
            tipo = "Concavidad indefinida"

        intervalos.append(((a, b), tipo))

    return intervalos