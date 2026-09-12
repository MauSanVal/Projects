import math
# Definimos la función g(x)
def g(x):
    return math.sqrt(10/(x+4))
#f(x) = x**3 +4x**2 -10 = 0
# Valor inicial
x0 = 5

# Parámetros
tolerancia = 1e-3
max_iter = 100

print("Iteración\t x")

for i in range(max_iter):
    x1 = g(x0)
    print(f"{i+1}\t\t {x1}")

    # Criterio de convergencia
    if abs(x1 - x0) < tolerancia:
        print("\nRaíz aproximada:", x1)
        break

    x0 = x1
else:
    print("\nNo convergió en el número máximo de iteraciones")