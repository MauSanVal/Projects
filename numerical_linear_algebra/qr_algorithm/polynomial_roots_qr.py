import numpy as np
import cmath
from qr_grandschmidt import qr_decomposition1
from qr_householder import qr_decomposition2

# coeficientes del polinomio en orden descendente:
# [1, -5, 8, -4, 4] -> x⁴ - 5x³ + 8x² - 4x + 4

coeffs = [1, 2, 0, 3, 0, 0, 1, 4, 5, 7, 4, 4]


# ============================
# Matriz compañera
# ============================
def companion_matrix(coeffs):
    coeffs = np.array(coeffs, dtype=float)

    if coeffs[0] == 0:
        raise ValueError("El coeficiente principal no puede ser cero.")

    coeffs = coeffs / coeffs[0]

    n = len(coeffs) - 1
    C = np.zeros((n, n))

    C[1:, :-1] = np.eye(n - 1)
    C[:, -1] = -coeffs[:0:-1]

    return C


# ============================
# Iteración QR
# ============================
def qr_algorithm(A, max_iter=5000):
    A = A.copy()

    for k in range(max_iter):
        #Q, R = np.linalg.qr(A)         #Para usar numpy
        #Q, R = qr_decomposition1(A)    #Para usar Grand-Schmidt
        Q, R = qr_decomposition2(A)     #Para usar Householder
        A = R @ Q

    return A, max_iter

# ============================
# Obtener eigenvalores
# (raíces)
# ============================
def extract_roots(T, tol=1e-8):
    n = T.shape[0]
    roots = []
    i = 0

    while i < n:
        if i == n - 1 or abs(T[i + 1, i]) < tol:
            # raíz real
            roots.append(T[i, i])
            i += 1
        else:
            # bloque 2x2 -> raíces complejas conjugadas
            a = T[i, i]
            b = T[i, i + 1]
            c = T[i + 1, i]
            d = T[i + 1, i + 1]

            trace = a + d
            det = a * d - b * c

            disc = trace**2 - 4 * det

            root1 = (trace + cmath.sqrt(disc)) / 2
            root2 = (trace - cmath.sqrt(disc)) / 2

            roots.extend([root1, root2])
            i += 2

    return roots

def evaluar_polinomio(coeffs, x):
    resultado = 0

    for c in coeffs:
        resultado = resultado * x + c

    return resultado

# ============================
# Main
# ============================
def main():
    print("Coeficientes:", coeffs)

    C = companion_matrix(coeffs)

    print("\nMatriz compañera:")
    print(C)

    T, iters = qr_algorithm(C)

    print(f"\nIteraciones realizadas: {iters}")

    print("\nForma casi triangular final:")
    print(T)

    roots = extract_roots(T)

    print("\nRaíces encontradas:")
    for r in roots:
        if abs(r.imag) < 1e-10:
            print(float(r.real))
        else:
            print(r)

    print("\nVerificación:")

    for r in roots:
        valor = evaluar_polinomio(coeffs, r)
        print(f"P({r}) = {valor}")

if __name__ == "__main__":
    main()

