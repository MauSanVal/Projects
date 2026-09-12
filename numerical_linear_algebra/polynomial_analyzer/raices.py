import numpy as np
import cmath
import sympy as sp


# ============================
# Matriz compañera
# ============================
def companion_matrix(coeffs):

    # ==========================================
    # corección:
    # usar complejos para manejar correctamente
    # raíces complejas
    # ==========================================
    coeffs = np.array(coeffs, dtype=complex)

    if coeffs[0] == 0:
        raise ValueError("El coeficiente principal no puede ser cero.")

    coeffs = coeffs / coeffs[0]

    n = len(coeffs) - 1

    # ==========================================
    # corrección:
    # matriz compleja
    # ==========================================
    C = np.zeros((n, n), dtype=complex)

    C[1:, :-1] = np.eye(n - 1)

    C[:, -1] = -coeffs[:0:-1]

    return C


# ============================
# Iteración QR
# ============================
def qr_algorithm(A, max_iter=100000, tol=1e-12):

    A = A.copy()

    n = A.shape[0]

    for k in range(max_iter):

        # ==========================================
        # correción:
        # shift simple
        #
        # sin shifts el QR converge muy mal
        # para raíces complejas
        # ==========================================
        mu = A[-1, -1]

        Q, R = np.linalg.qr(A - mu * np.eye(n))

        A = R @ Q + mu * np.eye(n)

        # ==========================================
        # correción:
        # criterio de convergencia
        #
        # verificamos que la parte debajo
        # de la diagonal sea pequeña
        # ==========================================
        subdiag = np.abs(np.tril(A, -1))

        if np.all(subdiag < tol):
            return A

    raise RuntimeError("El algoritmo QR no convergió.")


# ============================
# Obtener raíces desde
# matriz casi triangular
# ============================
def extract_roots(T, tol=1e-8):

    n = T.shape[0]

    roots = []

    i = 0

    while i < n:

        # ==========================================
        # eigenvalor aislado
        # ==========================================
        if i == n - 1 or abs(T[i + 1, i]) < tol:

            roots.append(complex(T[i, i]))

            i += 1

        else:

            # ==========================================
            # bloque 2x2
            # ==========================================
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


# ============================
# Limpiar errores numéricos
# ============================
def clean_root(z, tol=1e-10):

    real = z.real
    imag = z.imag

    if abs(real - round(real)) < tol:
        real = round(real)

    if abs(imag) < tol:
        imag = 0

    if imag == 0:
        return float(real)

    return complex(real, imag)

# ============================
# FUNCIÓN PRINCIPAL
# ============================
def raices_complejas(poly):

    x = sp.Symbol('x')

    # ==========================================
    # correción:
    # expandir expresiones simbólicas
    #
    # esto permite manejar cosas como:
    # (x-2)*(x^4+4)
    # ==========================================
    if not isinstance(poly, sp.Poly):

        poly = sp.expand(poly)

        poly = sp.Poly(poly, x)

    # Coeficientes en orden descendente
    coeffs = [complex(c) for c in poly.all_coeffs()]

    # Caso constante
    if poly.degree() == 0:
        return []

    # Construir matriz compañera
    C = companion_matrix(coeffs)

    # Aplicar QR
    T = qr_algorithm(C)

    # Extraer raíces
    roots = extract_roots(T)

    # ==========================================
    #  corrección:
    # limpiar errores numéricos
    # ==========================================
    roots = [clean_root(r) for r in roots]

    # ==========================================
    # corrección:
    # ordenar raíces para visualización
    # ==========================================
    roots.sort(
        key=lambda z: (
            z.real if isinstance(z, complex) else z,
            z.imag if isinstance(z, complex) else 0
        )
    )

    return roots