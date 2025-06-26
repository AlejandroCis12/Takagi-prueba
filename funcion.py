import numpy as np
import matplotlib.pyplot as plt

def T(x, N=500):
    suma = 0
    for n in range(N):
        tx = 2**n * x
        diente = 2 * min(tx - np.floor(tx), np.ceil(tx) - tx)
        suma += (1/2)**n * diente
    return suma

def j_newton(fun, a, x0, tol, nmax):
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
    fx = fun(x)-a
    curve.append((x, fx))
    niter = 0
    diff = tol + 1

    while diff >= tol and niter <= nmax:
        niter += 1
        denominator = fun(x)-x
        if denominator == 0:
            print("Denominator zero. Method stopped to avoid division by zero.")
            break
        x = x * (1-((fun(x)-a)/denominator))
        fx = fun(x)-a
        diff = abs(fun(x))
        curve.append((x, fx))

    if niter > nmax:
        print("Newton method stopped without convergence.")

    zero = x
    res = fx
    return zero, res, niter, curve

a=0.34

Jz, Jr, Jn, Jc = j_newton(fun=T, a = 0.34, x0=.2, tol=1e-5, nmax=500)
Lx = np.linspace(0, 1, 1000)
Ly = [T(x)-a for x in Lx]
plt.figure(figsize=(8, 6))
plt.plot(Lx, Ly, linewidth=1.2, label='f(x)')
Jc = np.array(Jc)
plt.plot(Jc[:, 0], Jc[:, 1], '.-', linewidth=1.2, markersize=8, label='Iteraciones')
plt.grid(True)
plt.title("Convergence of Newton method with Jackson derivative")
plt.legend()
print(f"\nCon la derivada de jackson se encontró la raíz {Jz:.6f} en {Jn} iteraciones f({Jz:.6f}) = {Jr:.6e}")
plt.show()