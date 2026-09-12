import sympy as sp

x = sp.symbols('x')


def integral_definida(poly):

    a = float(input("Introduce el límite inferior a: "))
    b = float(input("Introduce el límite superior b: "))
    n = int(input("Introduce el número de subintervalos n: "))

    if n <= 0:
        raise ValueError("El número de subintervalos debe ser positivo.")

    # Convertir Poly -> Expr
    expr = poly.as_expr()

    # Convertir expresión simbólica a función numérica
    f = sp.lambdify(x, expr, "numpy")

    # Método del trapecio compuesto
    h = (b - a) / n

    suma = 0

    for i in range(1, n):
        suma += f(a + i*h)

    integral = (h/2) * (f(a) + 2*suma + f(b))

    return integral