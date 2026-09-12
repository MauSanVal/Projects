# crecimiento.py

import sympy as sp
from raices import raices_complejas

x = sp.Symbol('x')


def crecimiento_decrecimiento(poly):

    # Función simbólica
    f = poly.as_expr()

    # Primera derivada
    f1 = sp.diff(f, x)

    # Convertir derivada a Poly
    poly_f1 = sp.Poly(f1, x)

    # ======================================
    # Raíces críticas usando tu método QR
    # ======================================

    raices = raices_complejas(poly_f1)

    criticos_reales = []

    for r in raices:

        try:

            real = float(sp.re(r))
            imag = float(sp.im(r))

            # Aceptar raíces casi reales
            if abs(imag) < 1e-8:

                criticos_reales.append(real)

        except:

            pass

    # Ordenar y eliminar repetidas
    criticos_reales = sorted(set(criticos_reales))

    # ======================================
    # Construcción de intervalos
    # ======================================

    puntos = [-sp.oo] + criticos_reales + [sp.oo]

    intervalos = []

    for i in range(len(puntos) - 1):

        a = puntos[i]
        b = puntos[i + 1]

        # ======================================
        # Elegir punto de prueba
        # ======================================

        # Caso (-∞, ∞)
        if a == -sp.oo and b == sp.oo:

            test = 0

        # Caso (-∞, b)
        elif a == -sp.oo:

            test = b - 1

        # Caso (a, ∞)
        elif b == sp.oo:

            test = a + 1

        # Caso finito
        else:

            test = (a + b) / 2

        # ======================================
        # Evaluar derivada
        # ======================================

        valor = float(f1.subs(x, test).evalf())

        # ======================================
        # Clasificar intervalo
        # ======================================

        if valor > 0:

            tipo = "Creciente"

        elif valor < 0:

            tipo = "Decreciente"

        else:

            tipo = "Constante"

        intervalos.append(
            {
                "intervalo": f"({sp.pretty(a)}, {sp.pretty(b)})",
                "tipo": tipo
            }
        )

    return intervalos