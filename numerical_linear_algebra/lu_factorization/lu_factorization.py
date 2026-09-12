# Matriz aumentada (n x n+1)
A = [
    [2.1756, 4.0231, -2.1732, 5.1967, 17.102],
    [-4.0231, 6, 0, 1.1973, -6.1593],
    [-1, -5.2107, 1.1111, 0, 3.0004],
    [6.0235, 7, 0, -4.1561,0]
]

n = len(A)

# separar matriz de coeficientes y vector b
a = [fila[:n] for fila in A]
b = [fila[n] for fila in A]

if a[0][0] == 0:
    print("a11 = 0")

# ----------------
# FACTORIZACION LU (Crout)
# ----------------

j = 0
while j < n:

    # calcular columna de L
    i = j
    while i < n:
        suma = 0
        k = 0

        while k < j:
            suma += a[i][k] * a[k][j]
            k += 1

        a[i][j] = a[i][j] - suma
        i += 1

    # calcular fila de U
    if j < n - 1:
        i = j + 1

        while i < n:
            suma = 0
            k = 0

            while k < j:
                suma += a[j][k] * a[k][i]
                k += 1

            a[j][i] = (a[j][i] - suma) / a[j][j]
            i += 1

    j += 1

if a[n-1][n-1] == 0:
    print("Error: pivote cero")

print("Matriz LU almacenada:")
for fila in a:
    print(fila)

# --------------------------
# SUSTITUCION HACIA ADELANTE
# Resolver Ly = b
# --------------------------

y = [0.0] * n

i = 0
while i < n:
    suma = 0
    j = 0

    while j < i:
        suma += a[i][j] * y[j]
        j += 1

    y[i] = (b[i] - suma) / a[i][i]
    i += 1

# -------------------------
# SUSTITUCION HACIA ATRAS
# Resolver Ux = y
# -------------------------

x = [0.0] * n

i = n - 1
while i >= 0:
    suma = 0
    j = i + 1

    while j < n:
        suma += a[i][j] * x[j]
        j += 1

    # U tiene 1 en la diagonal
    x[i] = y[i] - suma

    i -= 1

print("\nSolucion del sistema:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")