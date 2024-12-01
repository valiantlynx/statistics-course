library(ggplot2)

# Messi data
messi_mål <- c(11, 38, 31, 51, 45, 54, 41, 58, 41, 60, 73, 31, 47)
messi_skudd <- c(39, 111, 86, 113, 120, 93, 89, 120, 81, 100, 135, 115, 119)

# Ronaldo data
ronaldo_mål <- c(24, 36, 37, 28, 44, 42, 51, 61, 51, 55, 60, 40, 35)
ronaldo_skudd <- c(55, 80, 95, 82, 111, 88, 137, 129, 131, 137, 131, 127, 109)

data_messi <- data.frame(Skudd=messi_skudd, Mål=messi_mål)
data_ronaldo <- data.frame(Skudd=ronaldo_skudd, Mål=ronaldo_mål)

# Plot for Messi
ggplot(data_messi, aes(x=Skudd, y=Mål)) +
  geom_point() +
  geom_smooth(method="lm", col="blue") +
  ggtitle("Messi: Skudd på mål vs Mål") +
  xlab("Skudd på mål") +
  ylab("Mål")

# Plot for Ronaldo
ggplot(data_ronaldo, aes(x=Skudd, y=Mål)) +
  geom_point() +
  geom_smooth(method="lm", col="red") +
  ggtitle("Ronaldo: Skudd på mål vs Mål") +
  xlab("Skudd på mål") +
  ylab("Mål")

# Regresjonsanalyse for Messi
modell_messi <- lm(Mål ~ Skudd, data=data_messi)
summary(modell_messi)

# Regresjonsanalyse for Ronaldo
modell_ronaldo <- lm(Mål ~ Skudd, data=data_ronaldo)
summary(modell_ronaldo)

# Forutsi mål for Messi med 100 skudd på mål
ny_data_messi <- data.frame(Skudd=100)
forutsi_mål_messi <- predict(modell_messi, newdata=ny_data_messi)
print(forutsi_mål_messi)

# Forutsi mål for Ronaldo med 100 skudd på mål
ny_data_ronaldo <- data.frame(Skudd=100)
forutsi_mål_ronaldo <- predict(modell_ronaldo, newdata=ny_data_ronaldo)
print(forutsi_mål_ronaldo)

# Konfidensintervaller for Messi
confint(modell_messi)

# Konfidensintervaller for Ronaldo
confint(modell_ronaldo)