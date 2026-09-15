# Absorbing Markov Chains — 3x3 Rat Maze Simulation (Food vs. Shock)

This project models and numerically simulates a classic 9-compartment maze navigation problem using **Absorbing Markov Chains**. An agent (e.g., a rat) moves randomly through a $3 \times 3$ grid of interconnected rooms until it reaches one of two terminal absorbing states: obtaining **Food** (State 7) or receiving an electric **Shock** (State 8).

The analytical framework computes exact expected escape times, fundamental matrix occupancy metrics, and absorption probabilities ($P_{\text{food}}$ vs. $P_{\text{shock}}$) from any starting position, validating linear algebra solutions against empirical **Monte Carlo** random walk simulations.

## Mathematical Background

Let $\mathcal{S} = \{0, 1, 2, 3, 4, 5, 6, 7, 8\}$ be the discrete state space partitioned into $t = 7$ transient states $\mathcal{S}_T = \{0, 1, 2, 3, 4, 5, 6\}$ and $r = 2$ absorbing states $\mathcal{S}_A = \{7 \text{ (Food)}, 8 \text{ (Shock)}\}$.

### Canonical Transition Matrix Form

The single-step transition probability matrix $P \in \mathbb{R}^{9 \times 9}$ organized in canonical block form is defined as:

$$P = \begin{pmatrix} Q & R \\ \mathbf{0} & I_2 \end{pmatrix}$$

where:
- $Q \in \mathbb{R}^{7 \times 7}$ contains transition probabilities between transient states $\{0, \dots, 6\}$.
- $R \in \mathbb{R}^{7 \times 2}$ contains transition probabilities from transient states to absorbing states $\{7, 8\}$.
- $\mathbf{0} \in \mathbb{R}^{2 \times 7}$ is the zero matrix.
- $I_2 \in \mathbb{R}^{2 \times 2}$ is the identity matrix ($P_{7,7} = 1, P_{8,8} = 1$).

### Fundamental Matrix $N$

The fundamental matrix $N \in \mathbb{R}^{7 \times 7}$ calculates the expected number of visits to transient state $j$ starting from transient state $i$ before absorption:

$$N = \sum_{k=0}^{\infty} Q^k = (I_7 - Q)^{-1}$$

### Expected Time to Absorption

The expected number of steps $\tau_i$ required to end the simulation (reach Food or Shock) starting from compartment $i \in \mathcal{S}_T$ is given by vector $\boldsymbol{\tau} \in \mathbb{R}^7$:

$$\boldsymbol{\tau} = N \mathbf{1}_7$$

where $\mathbf{1}_7 \in \mathbb{R}^7$ is a column vector of ones.

### Absorption Probabilities (Food vs. Shock)

The matrix $B \in \mathbb{R}^{7 \times 2}$ defines the exact probability of reaching a specific absorbing state ($B_{i, 7}$ for Food, $B_{i, 8}$ for Shock) when starting from state $i$:

$$B = N R$$

where $B_{i, 7} + B_{i, 8} = 1$ for all $i \in \{0, \dots, 6\}$.

---

## Maze Topology & Adjacency Graph

The $3 \times 3$ maze layout is mapped as follows:

```text
+-----------+-----------+-----------+
|     0     |     1     |  7 (FOOD) |
| (Top-L)   | (Top-Mid) | (Absorbing|
+-----------+-----------+-----------+
|     2     |     3     |     4     |
| (Mid-L)   | (Center)  | (Mid-R)   |
+-----------+-----------+-----------+
| 8 (SHOCK) |     5     |     6     |
|(Absorbing)|(Bot-Mid)  | (Bot-R)   |
+-----------+-----------+-----------+
