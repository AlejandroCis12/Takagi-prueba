def j_newton(fun, q, x0, tol, nmax):
    """
    Newton-Jackson method to find roots of a function.

    Parameters:
    fun: Callable function f(x)
    q: Jackson derivative parameter (float)
    x0: Initial guess (float)
    tol: Tolerance for convergence (float)
    nmax: Maximum number of iterations (int)

    Returns:
    zero: Approximate root (float)
    res: Residual (float)
    niter: Number of iterations (int)
    curve: List of tuples [(x_i, f(x_i))]
    """
    curve = []
    x = x0
    fx = fun(x)
    fqx = fun(q * x)
    curve.append((x, fx))
    niter = 0
    diff = tol + 1

    while diff >= tol and niter <= nmax:
        niter += 1
        dfqx = fx / fqx if fqx != 0 else float('inf')  # Avoid division by zero
        denominator = 1 - dfqx
        if denominator == 0:
            print("Denominator zero. Method stopped to avoid division by zero.")
            break
        x = x * (1 - q * dfqx) / denominator
        fx = fun(x)
        fqx = fun(q * x)
        diff = abs(fx)
        curve.append((x, fx))

    if niter > nmax:
        print("Newton method stopped without convergence.")

    zero = x
    res = fx
    return zero, res, niter, curve
