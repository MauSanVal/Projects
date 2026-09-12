# Numerical Linear Algebra

This directory contains implementations and experiments in numerical linear algebra, focusing on matrix factorizations, orthogonalization, eigenvalue computation, and numerical methods for solving polynomial equations.

The projects are developed to connect theoretical concepts from linear algebra with their computational implementation.

## Projects

### LU Factorization

Implementation of LU factorization using the Crout algorithm, together with forward and backward substitution for solving linear systems.

**Topics:**

* LU factorization
* Crout algorithm
* Forward substitution
* Backward substitution
* Linear systems

---

### LDLᵀ Factorization

Implementation of the LDLᵀ factorization for symmetric matrices.

Given a suitable symmetric matrix \(A\), the method computes

$$
A = LDL^T,
$$

where \(L\) is lower triangular and \(D\) is diagonal.

**Topics:**

* Matrix factorization
* Symmetric matrices
* Triangular systems

---

### QR Algorithm

Implementation of QR factorization using two different orthogonalization techniques:

* Gram-Schmidt orthogonalization
* Householder reflections

The QR factorization is then used in the QR algorithm for numerical eigenvalue computation.

The project also explores the connection between polynomial roots and eigenvalues through companion matrices.

**Topics:**

* QR factorization
* Gram-Schmidt orthogonalization
* Householder reflections
* Eigenvalue computation
* Companion matrices
* Numerical algorithms

---

### Weighted Gram-Schmidt

Implementation of the Gram-Schmidt process with respect to a weighted inner product.

For a positive-definite weight matrix \(W\), the inner product is defined by

$$
\langle x,y\rangle_W = x^T W y.
$$

The project constructs an orthogonal basis with respect to this inner product.

**Topics:**

* Inner products
* Orthogonality
* Gram-Schmidt process
* Weighted inner products

---

### Polynomial Roots

Implementation of several methods for finding polynomial roots, including analytical and numerical approaches.

**Methods:**

* Quadratic formula
* Fixed-point iteration
* Secant method

The project illustrates the difference between analytical solutions and iterative numerical methods.

**Topics:**

* Polynomial equations
* Fixed-point iteration
* Secant method
* Numerical root finding

---

### Polynomial Analyzer

A modular tool for analyzing real polynomials using symbolic and numerical methods.

The program includes functionality for:

* Domain analysis
* Root finding
* Derivatives
* Critical points
* Extrema
* Monotonicity
* Concavity
* Integration
* Graphing

The root-finding component also makes use of numerical linear algebra techniques through companion matrices and the QR algorithm.

**Topics:**

* Symbolic computation
* Numerical root finding
* Polynomial analysis
* Numerical linear algebra
* Visualization

---

## Goals

The main goal of these projects is to study how concepts from linear algebra and numerical analysis can be translated into computational algorithms.

Particular emphasis is placed on understanding the mathematical structure behind each method, implementing the algorithms explicitly, and exploring their numerical behavior.
