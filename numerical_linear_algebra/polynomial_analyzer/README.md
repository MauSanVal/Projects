# Polynomial Analyzer

This project is a modular tool for the symbolic and numerical analysis of real polynomial functions.

Given a polynomial, the program provides several classical calculus analyses, including derivatives, critical points, monotonicity, concavity, integration, roots, and visualization.

The project combines **SymPy** for symbolic manipulation with numerical methods for root finding and graphical representation.

## Features

The program currently provides:

- Polynomial expression parsing
- Domain identification
- Root computation
- Derivatives
- Critical points and local extrema
- Increasing and decreasing intervals
- Concavity
- Numerical integration
- Graphing

## Mathematical Analysis

### Domain

A polynomial with real coefficients is defined for every real number:

```math
\operatorname{Dom}(p)=\mathbb{R}
```

The project nevertheless includes a domain module as part of the general analysis workflow.

### Derivatives

The program computes successive symbolic derivatives using SymPy.

For a polynomial $f(x)$, it obtains

```math
f'(x),\quad f''(x),\quad \dots
```

until the derivative becomes constant.

### Roots

The root module represents the polynomial through its companion matrix.

For a polynomial

```math
p(x)=a_nx^n+\cdots+a_1x+a_0,
\qquad a_n\neq0
```

the coefficients are normalized and used to construct a companion matrix whose eigenvalues correspond to the roots of the polynomial.

The eigenvalues are approximated through the QR algorithm with a simple shift.

The current implementation of the QR factorization uses NumPy's

```python
numpy.linalg.qr
```

inside the root-analysis module.

### Critical Points and Extrema

The critical points are obtained from the roots of

```math
f'(x)=0
```

The second derivative is then used to classify the corresponding real critical points:

```math
f''(c)>0
\quad\Rightarrow\quad
\text{local minimum}
```

```math
f''(c)<0
\quad\Rightarrow\quad
\text{local maximum}
```

When

```math
f''(c)=0
```

the classification is left inconclusive by the current implementation.

### Monotonicity

The program studies the sign of

```math
f'(x)
```

between consecutive real critical points.

If

```math
f'(x)>0
```

the function is classified as increasing on the corresponding interval.

If

```math
f'(x)<0
```

it is classified as decreasing.

### Concavity

The sign of

```math
f''(x)
```

is analyzed between consecutive real zeros of the second derivative.

Thus,

```math
f''(x)>0
```

corresponds to concavity upward, while

```math
f''(x)<0
```

corresponds to concavity downward.

### Numerical Integration

The project approximates definite integrals using the **composite trapezoidal rule**.

For

```math
\int_a^b f(x)\,dx
```

the step size is

```math
h=\frac{b-a}{n}
```

and the approximation is

```math
\int_a^b f(x)\,dx
\approx
\frac{h}{2}
\left[
f(a)
+
2\sum_{i=1}^{n-1}f(a+ih)
+
f(b)
\right]
```

The user specifies $a$, $b$, and the number of subintervals $n$.

### Visualization

The graphing module evaluates the polynomial numerically over a fixed interval and displays the resulting curve using Matplotlib.

## Architecture

The project is divided into separate modules according to the mathematical task:

```text
polynomial_analyzer/
├── main.py
├── parser_poly.py
├── dominio.py
├── raices.py
├── derivadas.py
├── crecimiento.py
├── extremos.py
├── concavidad.py
├── integral.py
└── grafica.py
```

This structure separates parsing, symbolic analysis, numerical root finding, integration, and visualization.

## Topics

- Polynomial functions
- Symbolic computation
- Numerical root finding
- Companion matrices
- QR algorithm
- Differential calculus
- Monotonicity
- Extrema
- Concavity
- Numerical integration
- Scientific visualization
