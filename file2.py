import numpy as np
from scipy.integrate import trapezoid, simpson, fixed_quad
n = 100

# 3a: ∫₀² eˣ/(1+x²) dx
def f_a(x):
    return np.exp(x)/(1 + x**2)

x_a = np.linspace(0, 2, n+1)
y_a = f_a(x_a)

trap_a = trapezoid(y_a, x_a)
mid_a = fixed_quad(f_a, 0, 2, n=n)[0]
simp_a = simpson(y_a, x_a)

print(f"3a Trapezoidal: {trap_a:.6f}")
print(f"3a Midpoint: {mid_a:.6f}")
print(f"3a Simpson's: {simp_a:.6f}")

# 3b: ∫₀^(π/2) (1+cos x)^(1/3) dx
def f_b(x):
    return (1 + np.cos(x))**(1/3)

x_b = np.linspace(0, np.pi/2, n+1)
y_b = f_b(x_b)

trap_b = trapezoid(y_b, x_b)
mid_b = fixed_quad(f_b, 0, np.pi/2, n=n)[0]
simp_b = simpson(y_b, x_b)

print(f"3b Trapezoidal: {trap_b:.6f}")
print(f"3b Midpoint: {mid_b:.6f}")
print(f"3b Simpson's: {simp_b:.6f}")