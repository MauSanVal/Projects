# Stochastic Processes & Markov Chain Applications

This repository contains numerical and analytical solutions for classic probability and stochastic modeling problems using **Discrete-Time Markov Chains (DTMC)** and **Absorbing Markov Chains**.

Each project combines **exact symbolic computation** in Python (`sympy`) with **empirical Monte Carlo simulations** (`numpy`) to evaluate key metrics such as expected absorption times, fundamental matrices, and transition probabilities.

---

## 1. Projects Included

###  01. Snakes and Ladders (`/01_snakes_and_ladders`)
* **Model:** Absorbing Markov Chain on a 20-square game board with jumps (ladders) and falls (snakes).
* **Objective:** Calculate the exact expected number of dice rolls required to reach the winning square starting from square 1.
* **Key Concepts:** State space reduction (occupiable states), canonical transition matrix decomposition, fundamental matrix $N = (I - Q)^{-1}$, and simulation-based statistical verification.

###  02. The Maze Problem (`/02_maze_problem`)
* **Model:** Random walk on a bounded graph / grid representing a maze with boundary absorbing states (exits or traps).
* **Objective:** Determine absorption probabilities (probability of escaping vs. hitting a trap) and the expected time to reach an exit from any starting cell.
* **Key Concepts:** Discrete-time random walks, boundary condition solving, absorbing probabilities matrix $B = N R$, and escape time estimation.

---

## 2. Mathematical Framework

Both projects leverage the canonical formulation of **Absorbing Markov Chains**.

### Canonical Form of Transition Matrix $P$
For a system with $t$ transient states and $r$ absorbing states, the transition matrix $P$ is partitioned as:

$$P = \begin{pmatrix} Q & R \\ \mathbf{0} & I_r \end{pmatrix}$$

where:
* $Q \in \mathbb{R}^{t \times t}$: Transition probabilities between transient states.
* $R \in \mathbb{R}^{t \times r}$: Transition probabilities from transient states to absorbing states.
* $I_r \in \mathbb{R}^{r \times r}$: Identity matrix for absorbing states.
* $\mathbf{0}$: Zero matrix.

### Fundamental Matrix $N$
The fundamental matrix $N$ yields the expected number of visits to transient state $j$ starting from transient state $i$ before absorption:

$$N = (I_t - Q)^{-1} = \sum_{k=0}^{\infty} Q^k$$

### Expected Time to Absorption $\mathbf{t}$
The expected number of steps to reach an absorbing state starting from transient state $i$ is given by:

$$\mathbf{t} = N \mathbf{1}$$

where $\mathbf{1}$ is a column vector of ones.

---

## 3. Repository Structure

```text
.
├── 01_snakes_and_ladders/
│   ├── board.png                  # Game board schematic
│   ├── snakes_and_ladders.ipynb   # Exact symbolic & Monte Carlo analysis
│   └── README.md                  # Detailed project documentation
│
├── 02_maze_problem/
│   ├── maze_grid.png              # Maze graph / grid topology diagram
│   ├── maze_solver.ipynb          # Random walk analysis & escape probabilities
│   └── README.md                  # Detailed project documentation
│
└── README.md                      # Repository root overview
