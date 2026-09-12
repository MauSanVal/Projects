import numpy as np


def qr_decomposition1(A):
    A = A.astype(float)
    n = A.shape[0]

    Q = np.zeros((n, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = A[:, j].copy()

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]

        R[j, j] = np.linalg.norm(v)

        if R[j, j] != 0:
            Q[:, j] = v / R[j, j]

    return Q, R
