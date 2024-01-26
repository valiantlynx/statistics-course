set.seed(314)
# vi har et tall med 100 sider, og har farget 27 røde. Men vi vet at ikke dette og skal utelukede basert påå slå terningen  gjetatte ganger
n = 10 # antall gjetninger
(newRed = rbinom(n, 100, 0.27)) # antall røde i hver gjetning

