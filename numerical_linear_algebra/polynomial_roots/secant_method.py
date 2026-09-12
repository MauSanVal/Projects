# Definimos la función (puedes cambiarla)
def f(x):
    return x**4 -3*x**3 + x**2 +x +1  # ejemplo: x^3 - x - 2 = 0


# Valores iniciales
x0 = 1.0
x1 = 2.0

# Parámetros
tolerancia = 1e-6
max_iter = 100

for i in range(max_iter):
    if f(x1) - f(x0) == 0:
        print("División entre cero, el método falla")
        break

    # Fórmula de la secante
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

    print(f"Iteración {i + 1}: x = {x2}")

    # Criterio de paro
    if abs(x2 - x1) < tolerancia:
        print("\nRaíz aproximada:", x2)
        break

    # Actualizar valores
    x0 = x1
    x1 = x2
else:
    print("No convergió en el número     máximo de iteraciones")