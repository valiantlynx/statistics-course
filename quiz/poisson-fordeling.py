from scipy.stats import poisson

# Parametere for Poisson-fordeling
lambd = 9  # Gjennomsnittsverdi

# Beregn P(3 < X ≤ 9)
P_4_to_9 = poisson.cdf(9, lambd) - poisson.cdf(3, lambd)
print("P(3 < X ≤ 9) =", P_4_to_9)
