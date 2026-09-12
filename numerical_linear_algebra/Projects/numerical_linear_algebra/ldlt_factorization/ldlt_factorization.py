import numpy as np

# Matriz simétrica hardcodeada
A = np.array([
    [4, -1, 1],
    [-1, 4.25, 2.75],
    [1, 2.75, 3.5]
], dtype=float)

n = A.shape[0]

# Inicializar L y D
L = np.eye(n)
D = np.zeros((n, n))

# Factorización LDL^T
for j in range(n):
    # Calcular D[j,j]
    suma = 0
    for k in range(j):
        suma += L[j, k] ** 2 * D[k, k]
    D[j, j] = A[j, j] - suma

    # Calcular columna j de L
    for i in range(j + 1, n):
        suma = 0
        for k in range(j):
            suma += L[i, k] * L[j, k] * D[k, k]
        L[i, j] = (A[i, j] - suma) / D[j, j]

# Resultados
print("Matriz A:")
print(A)

print("\nL:")
print(L)

print("\nD:")
print(D)

print("\nVerificación (L @ D @ L.T):")
print(L @ D @ L.T)