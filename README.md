# goit-algo-hw-10

## Task 1

Two approaches for coin change problem were implemented:
- Greedy algorithm
- Dynamic programming

### Conclusions

The greedy algorithm works much faster because it always selects the largest possible coin first.

Dynamic programming guarantees the optimal solution for any coin system but requires more memory and execution time.

For standard coin systems greedy algorithms are usually more efficient.

---

## Task 2

The definite integral of the function f(x) = x² on the interval [0, 2] was calculated using:
- Monte Carlo method
- scipy.integrate.quad

### Results

Monte Carlo result was very close to the analytical result calculated using the `quad` function.

Example:
- Monte Carlo result ≈ 2.67
- quad result = 2.666666666666667

### Conclusions

Monte Carlo integration provides approximate results that become more accurate as the number of random samples increases.

The `quad` function from SciPy produces a more precise analytical result.

The comparison confirms that the Monte Carlo method is effective for numerical approximation of integrals.
