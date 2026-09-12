import numpy as np


def qr_decomposition2(A):
    A = A.astype(float)
    n = A.shape[0]

    Q = np.eye(n)
    R = A.copy()

    for k in range(n - 1):
        x = R[k:, k]

        norm_x = np.linalg.norm(x)

        if norm_x == 0:
            continue

        e1 = np.zeros_like(x)
        e1[0] = 1.0

        sign = 1 if x[0] >= 0 else -1

        v = x + sign * norm_x * e1
        v = v / np.linalg.norm(v)

        Hk = np.eye(n)
        Hk[k:, k:] -= 2 * np.outer(v, v)

        R = Hk @ R
        Q = Q @ Hk.T

    return Q, R