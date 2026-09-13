# CTMC Uniformization — Jensen's Method

This project studies the numerical computation of transition probability matrices for a **continuous-time Markov chain (CTMC)** using the **uniformization method**, also known as Jensen's method.

The implementation uses matrix operations and truncated infinite series to approximate the transition probability matrix $P(t)$ at different times.

## Mathematical Background

Consider a continuous-time Markov chain with transition-rate matrix $R$ and row rates

```math
r_i = \sum_{j=1}^{N} r_{ij}
```

Let

```math
r \geq \max_i r_i
```

The corresponding uniformized transition matrix is defined by

```math
\hat{P}
=
I+\frac{Q}{r}
```

where $Q$ is the infinitesimal generator of the chain.

Equivalently, its entries can be written as

```math
\hat{p}_{ij}
=
\begin{cases}
1-\frac{r_i}{r}, & i=j,\\
\frac{r_{ij}}{r}, & i\neq j.
\end{cases}
```

The transition probability matrix of the continuous-time Markov chain can then be expressed through the uniformization formula

```math
P(t)
=
\sum_{k=0}^{\infty}
e^{-rt}
\frac{(rt)^k}{k!}
\hat{P}^{\,k}
```

This representation expresses the CTMC transition probabilities as a Poisson-weighted combination of powers of the discrete transition matrix $\hat{P}$.

## Numerical Approximation

Since the series is infinite, it must be truncated.

The first implementation uses the truncation suggested in the activity:

```math
M
=
\max
\left\{
\left\lceil rt+5\sqrt{rt}\right\rceil,
20
\right\}
```

The transition matrix is then approximated by

```math
P^M(t)
=
\sum_{k=0}^{M}
e^{-rt}
\frac{(rt)^k}{k!}
\hat{P}^{\,k}
```

The notebook evaluates this approximation for

```text
t = 0.5, 1, 5.
```

## Error-Controlled Uniformization

The project also implements an alternative procedure in which the truncation point $M$ is determined automatically from a prescribed tolerance $\epsilon$.

For a fixed $t\geq0$,

```math
\left|
p_{ij}(t)-p^M_{ij}(t)
\right|
\leq
\sum_{k=M+1}^{\infty}
e^{-rt}
\frac{(rt)^k}{k!}
```

The implementation increases the number of terms until the accumulated Poisson probability reaches the required accuracy.

In the numerical experiment, the tolerance is set to

```math
\epsilon=10^{-5}
```

This allows the truncation level $M$ to depend on the chosen time $t$.

## Chapman-Kolmogorov Verification

A fundamental property of a continuous-time Markov chain is the Chapman-Kolmogorov equation

```math
P(s+t)=P(s)P(t),
\qquad s,t\geq0
```

The notebook verifies this numerically using

```math
P(1)
\approx
P(0.5)P(0.5)
```

The difference between both matrices is computed to verify that the numerical approximation preserves this property up to the expected truncation error.

## Comparison of Methods

The notebook compares two approaches:

1. A fixed truncation based on

```math
M
=
\max
\left\{
\left\lceil rt+5\sqrt{rt}\right\rceil,
20
\right\}
```

2. An adaptive truncation based on a prescribed tolerance $\epsilon$.

The resulting transition matrices are numerically very close, showing that the tolerance-based procedure produces results consistent with the fixed truncation.

## Implementation

The project uses **SymPy** for matrix operations and numerical evaluation.

The implementation includes:

- Construction of the uniformization matrix $\hat{P}$.
- Approximation of $P(t)$ using a fixed truncation.
- Approximation using an error-based truncation.
- Numerical verification of the Chapman-Kolmogorov equations.
- Comparison of the results obtained by both procedures.

## Topics

- Continuous-time Markov chains
- Markov transition matrices
- Infinitesimal generators
- Uniformization
- Jensen's method
- Poisson distributions
- Matrix powers
- Infinite series truncation
- Chapman-Kolmogorov equations
- Numerical probability
- SymPy
