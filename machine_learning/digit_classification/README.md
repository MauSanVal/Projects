# Handwritten Digit Classification — Dense Neural Network

This project implements a **Multi-Layer Perceptron (MLP)** / **Dense Neural Network** using **TensorFlow / Keras** to solve a multi-class image classification task on the **Optical Recognition of Handwritten Digits** dataset (`scikit-learn`).

The implementation covers data preprocessing, feature normalization, neural network architecture definition, optimization using Stochastic Gradient Descent (SGD), and quantitative performance evaluation.

## Mathematical Background

Consider an input feature vector $x \in \mathbb{R}^{64}$ representing an $8 \times 8$ grayscale image normalized such that $x_i \in [0, 1]$.

### Activation Functions

1. **Rectified Linear Unit (ReLU)** in the hidden layer:

$$f(z) = \max(0, z)$$

2. **Softmax Function** in the output layer for class $i \in \{0, 1, \dots, 9\}$:

$$p_i = \text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=0}^{9} e^{z_j}}$$

where $z = W_2 \cdot f(W_1 x + b_1) + b_2$ denotes the logit output vector.

### Optimization & Loss Function

The network is trained using **Sparse Categorical Cross-Entropy loss**:

$$\mathcal{L}(y, p) = -\log(p_y)$$

where $y \in \{0, \dots, 9\}$ is the true integer class label and $p_y$ is the predicted probability for class $y$.

Parameters are updated via **Stochastic Gradient Descent (SGD)** with learning rate $\eta$:

$$\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}$$

## Dataset

The project uses the UCI ML Optical Recognition of Handwritten Digits dataset (`sklearn.datasets.load_digits`):

- **Number of Instances**: 1,797 samples
- **Image Dimensions**: $8 \times 8$ grayscale pixels
- **Features**: 64 continuous features normalized to $[0, 1]$
- **Target Classes**: 10 distinct classes ($0$ through $9$)
- **Data Split**: 80% Training set (1,437 samples), 20% Test set (360 samples)

## Model Architecture

The deep learning model is built using Keras's `Sequential` API:

| Layer | Type | Output Shape | Param # | Activation |
|---|---|---|---|---|
| Input | Flatten | (None, 64) | 0 | None |
| Hidden | Dense | (None, 128) | 8,320 | ReLU |
| Output | Dense | (None, 10) | 1,290 | Softmax |

- **Total Parameters**: 9,610 trainable parameters.

## Numerical Experiment & Training

The training process is configured with the following hyperparameters:

```text
Optimizer:     SGD (learning_rate = 0.01)
Loss Function: Sparse Categorical Cross-Entropy
Epochs:        100
Batch Size:    32 (default)
