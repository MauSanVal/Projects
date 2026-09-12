# Proceso de Gram-Schmidt Ponderado (Weighted Gram-Schmidt Process)

Una implementación analítica en Python utilizando **SymPy** del proceso de ortogonalización y normalización de Gram-Schmidt bajo un **producto interno ponderado**.

##  Descripción General

El algoritmo extienda el proceso tradicional de Gram-Schmidt redefiniendo el espacio euclidiano con un producto interno ponderado por una matriz diagonal de pesos positivos $w = [1, 4, 9, 16, 25]$:

$$\langle x, y \rangle_w = \sum_{i=1}^{n} w_i x_i y_i$$

El módulo calcula una base ortonormal $E = \{e_1, e_2, e_3, e_4, e_5\}$ exacta mediante cálculo simbólico.

---

##  Formulación Matemática

1. **Producto Interno Ponderado:**
   $$\langle x, y \rangle_w = x^T W y$$

2. **Vectores Ortogonales ($u_k$):**
   $$u_k = v_k - \sum_{j=1}^{k-1} \frac{\langle v_k, u_j \rangle_w}{\langle u_j, u_j \rangle_w} u_j$$

3. **Vectores Ortonormales ($e_k$):**
   $$e_k = \frac{u_k}{\sqrt{\langle u_k, u_k \rangle_w}}$$

---

##  Estructura de la Carpeta

```text
Projects/numerical_linear_algebra/weighted_gram_schmidt/
├── README.md                  # Documentación teórica
└── weighted_gram_schmidt.py   # Algoritmo en SymPy con producto interno ponderado
