def first_derivative(f, x, h=1e-5):
    """Approximate the first derivative of f at x."""
    return (f(x + h) - f(x)) / h

def second_derivative(f, x, h=1e-5):
    """Approximate the second derivative of f at x."""
    return first_derivative (lambda y : first_derivative(f, y, h), x, h)

def optimize(f, x0, tol=1e-6):
    """Find a local minimum of f using Newton's method."""

    if not callable(f):
        raise TypeError(f"Argument is not a function, it is of type {type(f)}")

    x = x0

    iteration = 0

    while True:
        iteration += 1

        if abs(x) > 1e7:
            raise RuntimeError(
                f"At iteration {iteration}, optimization appears to be diverging"
            )

        first = first_derivative(f, x)
        second = second_derivative(f, x)

        if second == 0:
            raise RuntimeError("Second derivative is zero; optimization failed.")

        x_new = x - first / second

        if abs(x_new - x) < tol:
            return x_new

        x = x_new



import numpy as np


def gradient(f, x, h=1e-5):
    """Approximate the gradient of f at x."""
    grad = np.zeros(len(x))

    for i in range(len(x)):
        x_step = x.copy()
        x_step[i] += h
        grad[i] = (f(x_step) - f(x)) / h

    return grad


def hessian(f, x, h=1e-5):
    """Approximate the Hessian matrix of f at x."""
    n = len(x)
    H = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            x_ij = x.copy()
            x_i = x.copy()
            x_j = x.copy()

            x_ij[i] += h
            x_ij[j] += h
            x_i[i] += h
            x_j[j] += h

            H[i, j] = (
                f(x_ij)
                - f(x_i)
                - f(x_j)
                + f(x)
            ) / h**2

    return H


def optimize_multivariate(f, x0, tol=1e-6):
    """Find a local minimum using multivariate Newton's method."""
    x = np.array(x0, dtype=float)

    while True:
        grad = gradient(f, x)
        H = hessian(f, x)

        eachstep = np.linalg.solve(H, grad)
        x_new = x - eachstep

        if np.linalg.norm(x_new - x) < tol:
            return x_new

        x = x_new
    