from scipy.stats import nbinom

r = 7  # Antall suksesser
p = 0.5  # Sannsynlighet for suksess

# Beregn P(4 < X ≤ 18) som P(X ≤ 18) - P(X ≤ 4)
probability = nbinom.cdf(18, r, p) - nbinom.cdf(4, r, p)
print(f"P(4 < X ≤ 18) = {probability}")
