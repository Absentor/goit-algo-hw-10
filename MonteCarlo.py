import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# =========================
# Function
# =========================

def f(x):
    return x ** 2


# Integration limits
a = 0
b = 2


# =========================
# Monte Carlo Method
# =========================

def monte_carlo_integral(func, a, b, samples=100000):

    max_y = max(func(a), func(b))

    inside_points = 0

    for _ in range(samples):

        x = random.uniform(a, b)
        y = random.uniform(0, max_y)

        if y <= func(x):
            inside_points += 1

    rectangle_area = (b - a) * max_y

    return rectangle_area * (inside_points / samples)


# Monte Carlo result
mc_result = monte_carlo_integral(f, a, b)


# =========================
# quad result
# =========================

quad_result, error = spi.quad(f, a, b)


# =========================
# Output
# =========================

print(f"Monte Carlo result: {mc_result}")
print(f"quad result: {quad_result}")
print(f"Error estimate: {error}")


# =========================
# Plot
# =========================

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])

ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_title('Monte Carlo Integration')

plt.grid()
plt.show()
