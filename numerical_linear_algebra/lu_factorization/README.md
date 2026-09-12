# LU Factorization — Crout Method

This project implements the LU factorization of a square matrix using the **Crout algorithm**, together with forward and backward substitution for solving linear systems.

The implementation focuses on making the computational steps of the factorization explicit rather than relying on a library routine that performs the decomposition automatically.

## Mathematical Background

Given a square matrix \(A\), the LU factorization seeks matrices \(L\) and \(U\) such that

$$
A = LU,
$$

where:

* \(L\) is lower triangular.
* \(U\) is upper triangular with ones on its main diagonal.

In the Crout convention, the diagonal entries belong to \(L\), while

$$
U_{ii}=1.
$$

Once the factorization is obtained, a linear system

$$
Ax=b
$$

can be rewritten as

$$
LUx=b.
$$

Introducing an intermediate vector \(y\),

$$
Ly=b,
$$

followed by

$$
Ux=y.
$$

This reduces the original problem to two triangular systems.

## Algorithm

The implementation computes the columns of \(L\) and the rows of \(U\) successively.

For the entries of \(L\),

$$
L_{ij}
=
A_{ij}
-
\sum_{k=0}^{j-1}L_{ik}U_{kj},
\qquad i\geq j.
$$

For the entries of \(U\),

$$
U_{ij}
=
\frac{
A_{ij}
-
\sum_{k=0}^{j-1}L_{ik}U_{kj}
}{
L_{ii}
},
\qquad i<j.
$$

After the factorization, the system is solved by:

### Forward substitution

$$
y_i=
\frac{
b_i-\sum_{j=0}^{i-1}L_{ij}y_j
}{
L_{ii}
}.
$$

### Backward substitution

Since \(U\) has a unit diagonal,

$$
x_i=
y_i-\sum_{j=i+1}^{n-1}U_{ij}x_j.
$$

## Implementation

The program stores the factors \(L\) and \(U\) compactly in the same matrix used during the factorization.

The current example uses a \(4\times4\) system and prints the resulting factorization together with the computed solution.

## Topics

* LU factorization
* Crout algorithm
* Triangular systems
* Forward substitution
* Backward substitution
* Numerical linear algebra

## File Structure

```text
lu_factorization/
├── README.md
└── lu_factorization.py
```
