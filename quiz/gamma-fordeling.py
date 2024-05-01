from scipy.stats import gamma

# Spørsmål 1: X ~ γ(14, 7.23). P(X≥1.64)
k1 = 14
theta1 = 7.23
P_ge_1_64_corrected = 1 - gamma.cdf(1.64, k1, scale=theta1)

# Spørsmål 2: X ~ γ(6, 0.91). Finn x slik at P(X≥x) =0.99
k2 = 6
theta2 = 0.91
x2_corrected = gamma.ppf(1 - 0.99, k2, scale=theta2)

# Spørsmål 3: X ~ γ(0.5, 12.15). P(X=0.123401711143927)
# Siden X er kontinuerlig, er sannsynligheten for en spesifikk verdi nøyaktig 0.

print(P_ge_1_64_corrected, x2_corrected)
