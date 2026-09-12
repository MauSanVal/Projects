# Descomposición Matricial $LDL^T$

Una implementación explicita en Python del algoritmo de **factorización $LDL^T$** (Cholesky modificada) para matrices simétricas reales.

##  Descripción General

La descomposición $LDL^T$ factoriza una matriz simétrica real $A \in \mathbb{R}^{n \times n}$ en el producto de:
- Una matriz triangular inferior unitaria $L$ ($L_{i,i} = 1$).
- Una matriz diagonal $D$.
- La traspuesta de la matriz triangular inferior $L^T$.

$$\mathbf{A} = \mathbf{L} \mathbf{D} \mathbf{L}^T$$

A diferencia de la descomposición estándar de Cholesky ($LL^T$), este método **evita el cálculo de raíces cuadradas**, reduciendo la carga computacional y permitiendo trabajar con matrices definidas o semidefinidas positivas.

---

##  Formulación Matemática

El algoritmo evalúa las siguientes relaciones iterativas columna por columna para $j = 0, 1, \dots, n-1$:

1. **Elementos diagonales de $D$:**
   $$D_{j,j} = A_{j,j} - \sum_{k=0}^{j-1} L_{j,k}^2 D_{k,k}$$

2. **Elementos subdiagonales de $L$ ($i > j$):**
   $$L_{i,j} = \frac{1}{D_{j,j}} \left( A_{i,j} - \sum_{k=0}^{j-1} L_{i,k} L_{j,k} D_{k,k} \right)$$

---

##  Estructura del Repositorio

```text
Projects/numerical_linear_algebra/ldlt_factorization/
├── README.md               # Documentación y fundamentos teóricos
└── ldlt_factorization.py   # Implementación del algoritmo y comprobación matricial
