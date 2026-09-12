# Búsqueda de Raíces de Polinomios (Polynomial Roots)

Una colección de métodos numéricos y analíticos en Python para la localización y solución de ceros y raíces de funciones polinomiales y no lineales ($f(x) = 0$).

##  Métodos Implementados

| Archivo | Método | Descripción |
| :--- | :--- | :--- |
| `cuadratic_solver.py` | **Fórmula Cuadrática Compleja** | Solución analítica exacta para ecuaciones cuadráticas $ax^2 + bx + c = 0$ permitiendo coeficientes en el plano complejo ($\mathbb{C}$). |
| `fixed_point_iteration.py` | **Iteración de Punto Fijo** | Método numérico abierto que convierte $f(x) = 0$ en $x = g(x)$ para encontrar puntos fijos iterativos con control de tolerancia. |
| `secant_method.py` | **Método de la Secante** | Algoritmo numérico abierto de convergencia superlineal que aproxima la derivada mediante rectas secantes a partir de dos puntos iniciales. |

---

##  Formulación Matemática

### 1. Ecuación Cuadrática en $\mathbb{C}$
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}, \quad a, b, c \in \mathbb{C}$$

### 2. Iteración de Punto Fijo
Dado $x_0$, evalúa iterativamente:
$$x_{k+1} = g(x_k)$$
hasta satisfacer $\vert{}x_{k+1} - x_k\vert{} < \text{tol}$.

### 3. Método de la Secante
Aproxima la raíz mediante la fórmula de actualización:
$$x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$$

---

##  Estructura de la Carpeta

```text
Projects/numerical_linear_algebra/polynomial_roots/
├── README.md                   # Documentación teórica y técnica del módulo
├── cuadratic_solver.py         # Solver analítico para coeficientes complejos
├── fixed_point_iteration.py    # Algoritmo de iteración de punto fijo
└── secant_method.py            # Método abierto de la secante
