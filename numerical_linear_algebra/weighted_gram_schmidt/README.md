# Weighted Gram-Schmidt

This project implements the **Gram-Schmidt orthogonalization process with respect to a weighted inner product**.

The implementation uses SymPy so that the resulting orthogonal and orthonormal vectors can be computed symbolically.

## Mathematical Background

The standard Euclidean inner product is

```math
\langle x,y\rangle=x^Ty
```

Here, the inner product is modified using a positive weight matrix $W$:

```math
\langle x,y\rangle_W=x^TWy
```

For the current example,

```math
W=
\mathrm{diag}(1,4,9,16,25)
```

Equivalently,

```math
\langle x,y\rangle_W
=
\sum_{i=1}^{5}w_i x_i y_i
```

The weighted inner product changes the notion of orthogonality and therefore produces a different orthogonal basis from the standard Euclidean Gram-Schmidt process.

## Weighted Gram-Schmidt Process

Given linearly independent vectors $v_1,\dots,v_n$, the orthogonal vectors are computed recursively by

```math
u_k
=
v_k
-
\sum_{j=1}^{k-1}
\frac{
\langle v_k,u_j\rangle_W
}{
\langle u_j,u_j\rangle_W
}
u_j
```

The vectors are then normalized:

```math
e_k
=
\frac{u_k}{
\sqrt{\langle u_k,u_k\rangle_W}
}
```

The resulting set

```math
\{e_1,\dots,e_n\}
```

satisfies

```math
\langle e_i,e_j\rangle_W=0
\qquad
(i\neq j)
```

and

```math
\langle e_i,e_i\rangle_W=1
```

## Implementation

The current example uses five vectors in $\mathbb{R}^5$ and the weight vector

```math
(1,4,9,16,25)
```

SymPy is used to preserve exact symbolic expressions during orthogonalization and normalization.

The program also evaluates selected weighted inner products to verify orthonormality.

## Topics

- Inner products
- Weighted inner products
- Orthogonality
- Orthonormal bases
- Gram-Schmidt process
- Symbolic computation
- Linear algebra

## File Structure

```text
weighted_gram_schmidt/
├── README.md
└── weighted_gram_schmidt.py
```
