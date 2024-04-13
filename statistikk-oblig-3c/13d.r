# R kode for å beregne posterior fordeling av lambda
kappa_0 <- 3
theta_0 <- 73
n <- 6
t <- 119

# Oppdatere parametrene for den posterior fordelingen
kappa_n <- kappa_0 + n
theta_n <- theta_0 / (1 + theta_0 * t)

# Den posterior fordelingen for lambda
kappa_n
theta_n
