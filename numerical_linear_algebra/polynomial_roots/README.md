# Polynomial Roots

This project contains several approaches to solving equations of the form

```math
f(x)=0
```

with an emphasis on comparing analytical and iterative numerical methods.

The current implementation includes:

- the quadratic formula,
- fixed-point iteration,
- the secant method.

The examples illustrate different ideas used in numerical root finding.

## 1. Quadratic Formula

For a quadratic equation

```math
ax^2+bx+c=0
```

the roots are

```math
x=
\frac{-b\pm\sqrt{b^2-4ac}}{2a}
```

The implementation uses Python's `cmath` module, allowing the coefficients and resulting roots to be complex.

## 2. Fixed-Point Iteration

The fixed-point method rewrites an equation

```math
f(x)=0
```

in the form

```math
x=g(x)
```

Starting from an initial approximation $x_0$, the iteration is

```math
x_{k+1}=g(x_k)
```

The current example uses

```math
g(x)=\sqrt{\frac{10}{x+4}}
```

which corresponds to the equation

```math
x^3+4x^2-10=0
```

The iteration stops when

```math
|x_{k+1}-x_k|<\text{tol}
```

## 3. Secant Method

The secant method is an open root-finding method that approximates the derivative using two previous points.

The iteration is

```math
x_{k+1}
=
x_k
-
f(x_k)
\frac{x_k-x_{k-1}}
{f(x_k)-f(x_{k-1})}
```

Unlike Newton's method, the secant method does not require the analytical derivative of $f$.

The current example uses

```math
f(x)=x^4-3x^3+x^2+x+1
```

The method stops when consecutive approximations satisfy

```math
|x_{k+1}-x_k|<\text{tol}
```

## Comparison

The three methods illustrate different approaches to solving nonlinear equations:

| Method | Type | Main idea |
|---|---|---|
| Quadratic formula | Analytical | Direct closed-form solution |
| Fixed-point iteration | Iterative | Repeated application of $g(x)$ |
| Secant method | Iterative | Approximate Newton-like updates without $f'(x)$ |

The convergence of the iterative methods depends on the initial values, the function, and the mathematical conditions of the method.

## Topics

- Nonlinear equations
- Polynomial roots
- Fixed-point iteration
- Secant method
- Convergence
- Numerical methods
- Complex arithmetic

## File Structure

```text
polynomial_roots/
├── README.md
├── cuadratic_solver.py
├── fixed_point_iteration.py
└── secant_method.py
```
