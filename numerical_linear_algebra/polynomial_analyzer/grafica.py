# grafica.py

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')

def graficar(poly):

    f = sp.lambdify(x, poly.as_expr(), 'numpy')

    xs = np.linspace(-10, 10, 2000)
    ys = f(xs)

    plt.axhline(0)
    plt.axvline(0)

    plt.plot(xs, ys)

    plt.grid(True)

    plt.show()