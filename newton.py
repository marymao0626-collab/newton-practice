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


    