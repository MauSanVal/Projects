# Algoritmo QR para el Cálculo de Raíces (QR Algorithm Suite)

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
