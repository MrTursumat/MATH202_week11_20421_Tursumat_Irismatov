import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# 1. Approximating integral using Trapezoidal, Midpoint, and Simpson's Rule
def f(x):
    return np.exp(-x**2)  # Example function, update based on the actual integral

a, b = 0, 1  # Define integral limits
n = 10  # Number of subintervals

# Trapezoidal Rule
x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)
trap_result = np.trapz(y_trap, x_trap)

# Midpoint Rule
x_mid = (x_trap[:-1] + x_trap[1:]) / 2
y_mid = f(x_mid)
mid_result = np.sum(y_mid) * (b-a)/n

# Simpson's Rule
simp_result = spi.simpson(y_trap, x_trap)

print(f"Trapezoidal Rule Approximation: {trap_result:.6f}")
print(f"Midpoint Rule Approximation: {mid_result:.6f}")
print(f"Simpson's Rule Approximation: {simp_result:.6f}")

# 2. Estimating values for t = [2,5,10,100,1000,10000]
def series_sum(t):
    return np.sum([1/(1 + n**2) for n in range(1, t+1)])

t_values = [2, 5, 10, 100, 1000, 10000]
series_results = [series_sum(t) for t in t_values]

for t, result in zip(t_values, series_results):
    print(f"Sum for t={t}: {result:.6f}")

# 3. Graphing functions for Comparison Theorem
def g(x):
    return 1/(1 + x**2)

def h(x):
    return 1/x**2

x_vals = np.linspace(1, 10, 100)
y_g = g(x_vals)
y_h = h(x_vals)

plt.figure(figsize=(8,6))
plt.plot(x_vals, y_g, label='f(x) = 1/(1+x^2)', color='blue')
plt.plot(x_vals, y_h, label='g(x) = 1/x^2', linestyle='dashed', color='red')
plt.xlabel('x')
plt.ylabel('Function Values')
plt.legend()
plt.title('Comparison of f(x) and g(x)')
plt.grid()
plt.show()
