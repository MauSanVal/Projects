# LDLᵀ Factorization

This project implements the **$LDL^T$ factorization** for real symmetric matrices.

The purpose is to study how the structure of a symmetric matrix can be exploited to obtain a factorization into triangular and diagonal factors.

## Mathematical Background

For a suitable symmetric matrix $A$,

```math
A = LDL^T
```

where:

- $L$ is lower triangular with ones on the diagonal.
- $D$ is diagonal.
- $L^T$ is the transpose of $L$.

Unlike the standard Cholesky factorization,

```math
A = LL^T
```

the $LDL^T$ factorization does not require square roots during the factorization process.

## Algorithm

The implementation computes the diagonal entries of $D$ using

```math
D_{jj}
=
A_{jj}
-
\sum_{k=0}^{j-1}
L_{jk}^2D_{kk}
```

For $i>j$, the entries of $L$ are computed from

```math
L_{ij}
=
\frac{
A_{ij}
-
\sum_{k=0}^{j-1}
L_{ik}L_{jk}D_{kk}
}{
D_{jj}
}
```

The process is carried out column by column.

## Verification

After computing $L$ and $D$, the implementation reconstructs the original matrix through

```math
LDL^T
```

and compares the result with $A$.

This provides a direct numerical verification of the factorization.

## Example

The current implementation uses a real symmetric matrix and prints:

- the original matrix $A$,
- the lower triangular matrix $L$,
- the diagonal matrix $D$,
- the reconstructed matrix $LDL^T$.

## Topics

- Symmetric matrices
- Matrix factorization
- $LDL^T$ decomposition
- Triangular matrices
- Numerical linear algebra

## File Structure

```text
ldlt_factorization/
├── README.md
└── ldlt_factorization.py
```

## Note

The $LDL^T$ factorization is closely related to Cholesky factorization, but it is a distinct factorization and should not be identified simply as a "modified Cholesky" algorithm.
