# QR Algorithm

This project studies the **QR factorization** and the **QR algorithm for eigenvalue computation**, with applications to polynomial root finding.

Two approaches to QR factorization are implemented explicitly:

- Gram-Schmidt orthogonalization
- Householder reflections

The resulting QR factorization is then used within the QR iteration to approximate the eigenvalues of a matrix.

## Mathematical Background

### QR Factorization

For a suitable matrix $A$, the QR factorization has the form

```math
A=QR
```

where:

- $Q$ is orthogonal.
- $R$ is upper triangular.

### Gram-Schmidt

Given the columns $a_1,\dots,a_n$ of $A$, Gram-Schmidt constructs an orthonormal basis by repeatedly removing projections onto previously computed vectors.

For example,

```math
v_j
=
a_j
-
\sum_{i=1}^{j-1}
\langle q_i,a_j\rangle q_i
```

followed by

```math
q_j=\frac{v_j}{\|v_j\|}
```

### Householder Reflections

Householder transformations construct orthogonal reflections that eliminate entries below the diagonal.

A Householder matrix has the form

```math
H=I-2vv^T
```

for a normalized vector $v$.

Successive transformations reduce $A$ to an upper triangular matrix $R$, while the product of the transformations gives $Q$.

## QR Eigenvalue Algorithm

Starting from a matrix $A_0=A$, the QR iteration computes

```math
A_k-\mu_k I = Q_kR_k
```

and then forms

```math
A_{k+1}=R_kQ_k+\mu_k I
```

The shift $\mu_k$ is used to improve convergence.

When the iteration converges, the resulting matrix approaches an upper triangular or Schur-like form, whose diagonal and $2\times2$ blocks contain information about the eigenvalues.

## Polynomial Root Finding

A particularly interesting application is the computation of polynomial roots through a **companion matrix**.

For a monic polynomial

```math
p(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0
```

the companion matrix is

```math
C=
\begin{pmatrix}
0&0&\cdots&0&-a_0\\
1&0&\cdots&0&-a_1\\
0&1&\cdots&0&-a_2\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\cdots&1&-a_{n-1}
\end{pmatrix}
```

The eigenvalues of $C$ are precisely the roots of $p(x)$.

Therefore, the project connects

```math
\text{polynomial}
\rightarrow
\text{companion matrix}
\rightarrow
\text{eigenvalues}
\rightarrow
\text{polynomial roots}
```

## Complex Eigenvalues

When the computation is performed using real arithmetic, conjugate complex eigenvalue pairs can appear through $2\times2$ blocks of the final quasi-triangular matrix.

For a block

```math
B=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
```

the associated eigenvalues satisfy

```math
\lambda^2-(a+d)\lambda+(ad-bc)=0
```

Thus,

```math
\lambda
=
\frac{
(a+d)\pm\sqrt{(a+d)^2-4(ad-bc)}
}{2}
```

## Numerical Considerations

The QR algorithm is an iterative numerical method, so convergence depends on the matrix and the chosen implementation.

Important considerations include:

- repeated or closely spaced eigenvalues,
- convergence rate,
- numerical rounding,
- the choice of shifts,
- the stability of the QR factorization.

Householder QR is generally preferred over classical Gram-Schmidt when numerical stability is important.

## Implementation

The project contains:

```text
qr_algorithm/
├── README.md
├── qr_grandschmidt.py
├── qr_householder.py
└── polynomial_roots_qr.py
```

`qr_grandschmidt.py` implements QR factorization using Gram-Schmidt.

`qr_householder.py` implements QR factorization using Householder reflections.

`polynomial_roots_qr.py` combines the QR factorization, QR iteration, companion matrices, and root extraction into a complete numerical experiment.

## Topics

- QR factorization
- Gram-Schmidt orthogonalization
- Householder reflections
- Eigenvalue computation
- Companion matrices
- Polynomial root finding
- Numerical stability# Algoritmo QR para el Cálculo de Raíces (QR Algorithm Suite)

Una suite en Python para la factorización matricial $QR$ (vía **Gram-Schmidt** y **Reflexiones de Householder**) aplicada al cálculo de autovalores sobre la matriz compañera para la obtención de raíces reales y complejas de polinomios.

##  Módulos y Métodos Implementados

| Archivo | Método / Algoritmo | Descripción |
| :--- | :--- | :--- |
| `qr_grandschmidt.py` | **Descomposición QR (Gram-Schmidt)** | Implementación de ortogonalización de Gram-Schmidt para factorizar $A = QR$. |
| `qr_householder.py` | **Descomposición QR (Householder)** | Factorización matricial mediante transformaciones ortogonales de Householder (mayor estabilidad numérica). |
| `roots.py` | **Algoritmo QR e Integración** | Construcción de matriz compañera, iteración $A_{k+1} = R_k Q_k$, extracción de bloques $2 \times 2$ (raíces complejas) y verificación. |

---

##  Formulación Matemática

### 1. Descomposición $A = QR$
- **Gram-Schmidt:** Ortogonaliza recursivamente las columnas de $A$:
  $$v_j = a_j - \sum_{i=0}^{j-1} \langle q_i, a_j \rangle q_i, \quad q_j = \frac{v_j}{\Vert{}v_j\Vert{}}$$
- **Householder:** Aplica matrices ortogonales de reflexión $H_k = I - 2v_k v_k^T$ para anular elementos subdiagonales:
  $$R = H_{n-1} \dots H_1 A, \quad Q = H_1^T \dots H_{n-1}^T$$

### 2. Matriz Compañera y Autovalores
Para un polinomio mónico $P(x) = x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0$, la matriz compañera $C$ se define como:

$$C = \begin{bmatrix}  0 & 0 & \dots & 0 & -a_0 \\ 1 & 0 & \dots & 0 & -a_1 \\ 0 & 1 & \dots & 0 & -a_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & -a_{n-1} \end{bmatrix}$$

Los autovalores de $C$ coinciden exactamente con las raíces de $P(x) = 0$.

### 3. Extracción de Raíces Complejas (Bloques $2 \times 2$)
Al converger a la forma de Schur real, los pares de raíces complejas conjugadas aparecen como submatrices $2 \times 2$ en la diagonal de la matriz $T$:

$$\begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies \text{Traza } = a + d, \quad \text{Det } = ad - bc$$
$$\lambda = \frac{\text{Traza} \pm \sqrt{\text{Traza}^2 - 4\text{Det}}}{2}$$

---

##  Limitaciones de Convergencia

- **Raíces Múltiples:** La tasa de convergencia decrece considerablemente cuando existen raíces de multiplicidad mayor a 1.
- **Módulos Iguales:** En presencia de autovalores complejos con magnitudes iguales, la matriz puede mantener subbloques persistentes requiriendo desplazamientos de origen (*shifts*).
- **Sensibilidad Numérica:** Si el algoritmo QR no converge en el número máximo de iteraciones, la aproximación de raíces no será precisa.

---

##  Estructura del Repositorio

```text
Projects/numerical_linear_algebra/qr_algorithm/
├── README.md             # Documentación matemática y técnica
├── qr_grandschmidt.py    # Factorización QR por Gram-Schmidt
├── qr_householder.py     # Factorización QR por Reflexiones de Householder
└── roots.py              # Matriz compañera, iteración QR y extractor de raíces
