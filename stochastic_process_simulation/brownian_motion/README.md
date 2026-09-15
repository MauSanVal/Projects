# Brownian Motion and Related Processes

This notebook studies the simulation and basic properties of **Brownian motion** and several related stochastic processes. The main objective is to connect the mathematical definition of these processes with numerical simulation and visualization.

The notebook develops the simulation of standard Brownian motion, explores its distribution and typical scale, introduces conditional midpoint refinement, constructs Brownian bridges, extends the model to include drift and volatility, and concludes with an empirical comparison using Apple stock data.

The mathematical explanations are accompanied by reproducible Python implementations and visualizations.

---

## Contents

1. [Standard Brownian Motion](#1-standard-brownian-motion)
2. [Several Brownian Paths and Typical Scale](#2-several-brownian-paths-and-typical-scale)
3. [Midpoint Refinement](#3-midpoint-refinement)
4. [Brownian Bridge](#4-brownian-bridge)
5. [Brownian Motion with Drift and Volatility](#5-brownian-motion-with-drift-and-volatility)
6. [Empirical Comparison with Apple Stock Data](#6-empirical-comparison-with-apple-stock-data)
7. [Main Takeaways](#7-main-takeaways)
8. [Requirements](#requirements)

---

## 1. Standard Brownian Motion

A **standard Brownian motion** is a stochastic process $W = (W_t)_{t \geq 0}$ satisfying, in particular,

$$
W_0 = 0,
$$

and

$$
W_t - W_s \sim \mathcal{N}(0,t-s), \qquad 0 \leq s < t,
$$

with independent increments over disjoint time intervals.

To simulate a Brownian path on an interval $[0,T]$, the interval is divided into $n$ subintervals of length

$$
\Delta t = \frac{T}{n}.
$$

If $Z_k \sim \mathcal{N}(0,1)$ are independent, the simulation is based on

$$
W_{t_{k+1}} = W_{t_k} + \sqrt{\Delta t}\,Z_k.
$$

The notebook implements this construction through:

```python
brownian_motion(T, n, seed=None)
```

which returns both the time grid and the simulated path.

A backward-compatible function,

```python
brown(T, n, seed=None)
```

is also included and returns only the simulated path.

The notebook first visualizes a single realization of standard Brownian motion.

---

## 2. Several Brownian Paths and Typical Scale

A Brownian motion satisfies

$$
W_t \sim \mathcal{N}(0,t),
$$

so its standard deviation at time $t$ is

$$
\sqrt{t}.
$$

The notebook therefore plots several independent Brownian paths together with the curves

$$
\pm\sqrt{t},
$$

which provide a useful reference for the typical scale of the process.

These curves are **not bounds** for Brownian motion. Brownian paths can cross them.

The notebook also studies the distribution at a fixed terminal time $T$. Since

$$
W_T \sim \mathcal{N}(0,T),
$$

a large number of simulated terminal values is used to compare the empirical mean and variance with their theoretical values.

This provides a numerical verification of one of the fundamental distributional properties of Brownian motion.

---

## 3. Midpoint Refinement

The notebook introduces a conditional midpoint construction for refining a previously simulated Brownian path.

A midpoint should not simply be taken as the deterministic average of the two endpoints. If

$$
m = \frac{t_i+t_{i+1}}{2},
$$

then, conditioned on the values at the endpoints,

$$
W_m \mid W_{t_i}, W_{t_{i+1}}
\sim
\mathcal{N}
\left(
\frac{W_{t_i}+W_{t_{i+1}}}{2},
\frac{t_{i+1}-t_i}{4}
\right).
$$

This conditional distribution allows new points to be inserted while preserving the stochastic structure of Brownian motion.

The notebook implements this through:

```python
refine_with_midpoints(time, path, seed=None)
```

The resulting path is compared with the original coarse discretization, illustrating how Brownian paths can be refined by adding conditionally sampled intermediate points.

---

## 4. Brownian Bridge

A **Brownian bridge** is obtained by conditioning a Brownian motion on a prescribed endpoint.

For a bridge from $0$ to $0$ over $[0,T]$,

$$
B_t = W_t - \frac{t}{T}W_T.
$$

This construction guarantees

$$
B_0 = 0, \qquad B_T = 0.
$$

More generally, a bridge from $0$ to a prescribed endpoint $b$ can be constructed as

$$
B_t = W_t + \frac{t}{T}(b-W_T).
$$

The notebook implements this with:

```python
brownian_bridge(T, n, endpoint=0.0, seed=None)
```

Several independent Brownian bridges are also simulated to visualize how the paths fluctuate while remaining pinned to the required endpoint values.

A backward-compatible helper function,

```python
BrownBridge(path)
```

is included to convert an existing Brownian path into a bridge ending at zero.

---

## 5. Brownian Motion with Drift and Volatility

The standard Brownian motion can be extended to the process

$$
X_t = \mu t + \sigma W_t,
$$

where:

* $\mu$ is the **drift**,
* $\sigma > 0$ is the **volatility**.

The resulting process satisfies

$$
X_t \sim \mathcal{N}(\mu t,\sigma^2 t).
$$

The notebook implements this model through:

```python
brownian_with_drift(T, n, mu, sigma, seed=None)
```

The simulation is visualized together with the deterministic drift component

$$
\mu t,
$$

which makes the effect of the parameters easier to interpret.

This section provides a simple connection between standard Brownian motion and stochastic models in which a systematic trend and a random component are both present.

---

## 6. Empirical Comparison with Apple Stock Data

The final section applies the ideas to real financial data.

The notebook downloads **Apple (AAPL)** historical data from January 1, 2020 to January 1, 2025 using the `yfinance` library.

The closing-price series is first visualized. The notebook then computes daily log-returns using

$$
r_t = \log\left(\frac{P_t}{P_{t-1}}\right),
$$

where $P_t$ denotes the closing price.

The mean daily log-return and daily volatility are calculated, and the empirical distribution of the log-returns is visualized.

An important distinction is emphasized in the notebook:

> A stock-price series is not itself a Brownian motion.

Instead, Brownian-motion-based models can be used as mathematical models for quantities such as returns or log-prices. The comparison in this notebook is therefore intended as an empirical illustration rather than as a claim that the Apple stock price follows Brownian motion exactly.

---

## 7. Main Takeaways

The notebook develops several fundamental ideas related to Brownian motion:

* Brownian motion can be simulated by adding independent normal increments with variance $\Delta t$.

* At a fixed time $T$,

  $$
  W_T \sim \mathcal{N}(0,T).
  $$

* The standard deviation of $W_t$ is $\sqrt{t}$, which describes the typical scale of the process.

* Conditional midpoint sampling provides a mathematically consistent way to refine a Brownian path.

* Brownian bridges can be constructed by conditioning Brownian motion on a prescribed endpoint.

* Adding drift and volatility leads to the model

  $$
  X_t = \mu t + \sigma W_t.
  $$

* Numerical simulations can be compared with theoretical distributions and with empirical financial data.

Overall, the notebook illustrates how probabilistic definitions can be translated into computational procedures and visualized through simulation.

---

## Requirements

The notebook primarily uses:

* **Python 3**
* **NumPy**
* **Matplotlib**

The final section additionally uses:

* **yfinance**

Install the required packages with:

```bash
pip install numpy matplotlib yfinance
```

The `yfinance` dependency is only necessary for the Apple stock-data section.

---


