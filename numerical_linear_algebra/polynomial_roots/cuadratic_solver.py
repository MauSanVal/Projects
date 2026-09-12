import cmath

# Coeficientes (pueden ser reales o complejos)
a = 1j
b = -7 - 3j
c = -5 -21j

# Discriminante
d = b**2 - 4*a*c

# Fórmula general
x1 = (-b + cmath.sqrt(d)) / (2*a)
x2 = (-b - cmath.sqrt(d)) / (2*a)

print("Raíz 1:", x1)
print("Raíz 2:", x2)