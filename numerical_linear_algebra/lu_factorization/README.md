# Factorización LU (Método de Crout) y Resolución de Sistemas Lineales

Una implementación explícita en Python nativo (sin dependencias externas) de la **factorización LU mediante el algoritmo de Crout** para resolver sistemas de ecuaciones lineales $Ax = b$.

##  Descripción General

El programa descompone una matriz cuadrada de coeficientes $A \in \mathbb{R}^{n \times n}$ en el producto de dos matrices triangulares:
- Una matriz triangular inferior $L$ (donde los elementos de la diagonal principal son calculados).
- Una matriz triangular superior unitaria $U$ (donde $U_{i,i} = 1$).

$$\mathbf{A} = \mathbf{L} \mathbf{U}$$

El algoritmo optimiza el espacio en memoria almacenando ambas matrices $L$ y $U$ de forma compacta en la misma matriz original durante el proceso de factorización, procediendo luego a la resolución del sistema mediante dos etapas de sustitución.

---

##  Algoritmo y Resolución

Dado el sistema $\mathbf{A}\mathbf{x} = \mathbf{b}$, tras factorizar $\mathbf{A} = \mathbf{L}\mathbf{U}$ el problema se resuelve en dos pasos:

1. **Sustitución hacia adelante (*Forward Substitution*):**
   Resuelve el sistema triangular inferior $\mathbf{L}\mathbf{y} = \mathbf{b}$ para hallar el vector auxiliar $\mathbf{y}$:
   $$y_i = \frac{b_i - \sum_{j=0}^{i-1} L_{i,j} y_j}{L_{i,i}}$$

2. **Sustitución hacia atrás (*Backward Substitution*):**
   Resuelve el sistema triangular superior unitario $\mathbf{U}\mathbf{x} = \mathbf{y}$ para determinar el vector solución $\mathbf{x}$:
   $$x_i = y_i - \sum_{j=i+1}^{n-1} U_{i,j} x_j$$

---

##  Estructura del Repositorio

```text
Projects/numerical_linear_algebra/lu_factorization/
├── README.md             # Documentación y fundamentos teóricos
└── lu_factorization.py   # Implementación del método de Crout en Python puro
