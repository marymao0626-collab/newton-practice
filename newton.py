def first_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def second_derivative(f, x, h=1e-5):
    return derivative (lambda y : deriative(f, y, h), x, h)

def optimize(f, x0, tol=1e-6):
    x = x0

    while True:
        first = first_derivative(f, x)
        second = second_derivative(f, x)

        x_new = x - first / second

        if abs(x_new - x) < tol:
            return x_new

        x = x_new
        


    