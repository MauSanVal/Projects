# Stochastic Process Simulation

This directory contains computational projects focused on the **simulation, analysis, and numerical approximation of stochastic processes**.

The projects combine mathematical theory with Python implementations to study discrete-time and continuous-time Markov chains, Brownian motion, and related probabilistic models.

The main goal is to connect theoretical concepts from probability and stochastic processes with numerical experiments, simulations, and computational methods.

---

## Projects

### 1. Absorbing Markov Chains

**Directory:** [`absorving_markov_chains`](./absorving_markov_chains)

This project studies **absorbing discrete-time Markov chains** through two applications:

- **Snakes and Ladders**
- **Random walks in a maze**

The project combines exact matrix-based calculations with Monte Carlo simulation.

The main mathematical tools include the canonical decomposition

$$
P =
\begin{pmatrix}
Q & R \\
0 & I
\end{pmatrix},
$$

the **fundamental matrix**

$$
N = (I-Q)^{-1},
$$

and the expected absorption time

$$
\mathbf{t} = N\mathbf{1}.
$$

The simulations are used to compare empirical results with the corresponding theoretical quantities.

**Main topics:**

- Discrete-time Markov chains
- Absorbing states
- Random walks
- Transition matrices
- Fundamental matrices
- Absorption probabilities
- Expected absorption times
- Monte Carlo simulation

---

### 2. Brownian Motion

**Directory:** [`brownian_motion`](./brownian_motion)

This project studies the simulation and basic properties of **Brownian motion** and several related stochastic processes.

The notebook begins with the simulation of standard Brownian motion using independent Gaussian increments:

$$W_{t_{k+1}}=W_{t_k}+\sqrt{\Delta t}\,Z_k,$$

where

$$
Z_k \sim \mathcal{N}(0,1).
$$

It then explores several extensions and related constructions, including:

- Multiple Brownian paths
- The typical scale of Brownian motion
- Conditional midpoint refinement
- Brownian bridges
- Brownian motion with drift and volatility
- An empirical comparison with financial data

For a Brownian motion,

$$
W_t \sim \mathcal{N}(0,t),
$$

so its standard deviation grows as

$$
\sqrt{t}.
$$

The project emphasizes the connection between these theoretical properties and their numerical manifestations.

**Main topics:**

- Brownian motion
- Gaussian processes
- Brownian bridges
- Stochastic simulation
- Conditional distributions
- Drift and volatility
- Numerical experiments
- Financial data

---

### 3. CTMC Uniformization — Jensen's Method

**Directory:** [`ctmc_uniformization_jensen_method`](./ctmc_uniformization_jensen_method)

This project studies the numerical computation of transition probability matrices for **continuous-time Markov chains (CTMCs)** using the **uniformization method**, also known as **Jensen's method**.

Given an infinitesimal generator $Q$ and a uniformization rate $r$, the uniformized transition matrix is

$$\hat{P}=I+\frac{Q}{r}$$

The transition probability matrix of the CTMC can then be represented as

$$P(t) = \sum_{k=0}^{\infty}e^{-rt} \frac{(rt)^k}{k!} \hat{P}^{k}$$

Since the series is infinite, the implementation requires a numerical truncation.

The project compares:

1. A fixed truncation based on the Poisson distribution.
2. An adaptive truncation based on a prescribed error tolerance.

It also verifies the Chapman-Kolmogorov property numerically:

$$
P(s+t) = P(s)P(t).
$$

**Main topics:**

- Continuous-time Markov chains
- Infinitesimal generators
- Uniformization
- Jensen's method
- Poisson distributions
- Matrix powers
- Infinite series truncation
- Error control
- Chapman-Kolmogorov equations
- Numerical probability

---

## Repository Structure

```text
stochastic_process_simulation/
│
├── absorving_markov_chains/
│   ├── maze/
│   │   ├── absorbing_markov_chain_maze.ipynb
│   │   └── README.md
│   │
│   ├── snakes_and_stairs/
│   │   ├── absorving_markov_chains_snakes_and_stairs.ipynb
│   │   ├── board.png
│   │   └── README.md
│   │
│   └── README.md
│
├── brownian_motion/
│   ├── brownian_motion.ipynb
│   └── README.md
│
├── ctmc_uniformization_jensen_method/
│   ├── ctmc_uniformization_jensen_method.ipynb
│   └── README.md
│
└── README.md
```

Each project contains its own README with a more detailed explanation of the mathematical framework, implementation, and numerical experiments.

---

## Mathematical Scope

The projects in this directory cover several levels of stochastic-process modeling.

### Discrete-Time Markov Chains

The absorbing Markov chain projects work with transition matrices of the form

$$P_{ij} = \mathbb{P}(X_{n+1}=j \mid X_n=i)$$

The evolution of the distribution of the chain can be studied through powers of the transition matrix:

$$ P^n $$

For absorbing chains, matrix decompositions provide exact expressions for quantities such as absorption probabilities and expected absorption times.

### Continuous-Time Markov Chains

The CTMC project considers a generator matrix $Q$ and transition matrices

$$ P(t)$$

The uniformization method transforms the continuous-time problem into a weighted sum involving powers of a discrete transition matrix:

$$ P(t) = \sum_{k=0}^{\infty} e^{-rt} \frac{(rt)^k}{k!} \hat{P}^{k}$$

This provides a computational approach for approximating the transition probabilities of a CTMC.

### Brownian Motion

The Brownian-motion project moves from jump processes to continuous sample paths.

Standard Brownian motion satisfies

$$ W_0 = 0 $$

and has independent Gaussian increments with

$$ W_t-W_s \sim \mathcal{N}(0,t-s),\qquad s < t $$

Its simulation can therefore be constructed from independent normal random variables.

---

## Computational Approach

The projects use numerical computation to investigate stochastic models in several complementary ways.

### Exact and Numerical Calculations

Matrix-based methods are used whenever theoretical expressions can be evaluated directly, including:

- Matrix inversion
- Matrix multiplication
- Matrix powers
- Numerical series
- Error-controlled approximations

### Monte Carlo Simulation

Random simulations are used to estimate quantities such as:

- Absorption times
- Absorption probabilities
- Distributions
- Sample paths
- Empirical moments

The simulated results can then be compared with theoretical predictions.

### Visualization

Plots are used throughout the projects to make stochastic behavior visible, including:

- Markov-chain trajectories
- Brownian paths
- Empirical distributions
- Convergence behavior
- Numerical comparisons

---

## Python Libraries

The projects primarily use the following Python libraries:

- **NumPy** for numerical computation and random simulation
- **SymPy** for symbolic and matrix calculations
- **Matplotlib** for visualization
- **yfinance** for the financial-data section of the Brownian motion project

The exact dependencies may vary between individual projects. See the README inside each project for its specific requirements.

---

## Learning Objectives

These projects are intended to develop both the mathematical and computational aspects of stochastic processes.

In particular, they provide practice with:

- Translating probabilistic models into algorithms
- Constructing and manipulating transition matrices
- Simulating random processes
- Comparing theoretical and empirical results
- Approximating infinite series numerically
- Controlling numerical errors
- Visualizing stochastic behavior
- Connecting mathematical models with real data

---

## Further Documentation

Each project contains a dedicated README with its mathematical development and implementation details.

- [Absorbing Markov Chains](./absorving_markov_chains/README.md)
- [Brownian Motion](./brownian_motion/README.md)
- [CTMC Uniformization — Jensen's Method](./ctmc_uniformization_jensen_method/README.md)
