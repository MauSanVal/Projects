import sympy as sp

# Pesos del producto interno
pesos = [1, 4, 9, 16, 25]

# Vectores de la base original
v1 = sp.Matrix([1, 4, -1, 3, 2])
v2 = sp.Matrix([1, 3, 0, 0, 7])
v3 = sp.Matrix([-6, 4, 3, 6, 0])
v4 = sp.Matrix([6, 2, -2, -1, 5])
v5 = sp.Matrix([0, 0, 2, 8, 4])
V = [v1, v2, v3, v4, v5]

# Producto interno ponderado
def prod(x, y):
    return sum(pesos[i]*x[i]*y[i] for i in range(5))

# Proceso de Gram–Schmidt corregido
U = []
for k in range(5):
    u = V[k]
    for j in range(k):
        u -= (prod(u, U[j]) / prod(U[j], U[j])) * U[j]
    U.append(sp.simplify(u))

# Normalización (base ortonormal)
E = [u / sp.sqrt(prod(u, u)) for u in U]

# Mostrar resultados
for i, e in enumerate(E, start=1):
    print(f"e{i} = ")
    sp.pprint(sp.simplify(e))
    print()

print("Ejemplo: ",prod(E[4], E[0]))
print("Ejemplo: ",prod(E[4], E[1]))
print("Ejemplo: ",prod(E[4], E[2]))
print("Ejemplo: ",prod(E[4], E[3]))
print("Ejemplo: ",prod(E[4], E[4]))