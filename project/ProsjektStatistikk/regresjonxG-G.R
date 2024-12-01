library(ggplot2)

# Messi data
messi_data <- data.frame(
  sesong = 1:8,
  xG = c(9.8, 26.66, 20.86, 25.97, 29.94, 26.94, 27.11, 35.89),
  Goals = c(11, 38, 31, 51, 45, 54, 41, 58)
)

# Ronaldo data
ronaldo_data <- data.frame(
  sesong = 1:8,
  xG = c(17.42, 29.84, 29.44, 23.33, 26.97, 25.41, 35.56, 39.33),
  Goals = c(24, 36, 37, 28, 44, 42, 51, 61)
)

# Plot for Messi med xG
ggplot(messi_data, aes(x=xG, y=Goals)) +
  geom_point() +
  geom_smooth(method="lm", col="blue") +
  ggtitle("Messi: Forventede mål (xG) vs Antall faktiske mål") +
  xlab("Forventede mål (xG)") +
  ylab("Antall faktiske mål")

# Plot for Ronaldo med xG
ggplot(ronaldo_data, aes(x=xG, y=Goals)) +
  geom_point() +
  geom_smooth(method="lm", col="red") +
  ggtitle("Ronaldo: Forventede mål (xG) vs Antall faktiske mål") +
  xlab("Forventede mål (xG)") +
  ylab("Antall faktiske mål")


# Regresjonsanalyse for Messi
messi_lm <- lm(Goals ~ xG, data = messi_data)
summary(messi_lm)

# Regresjonsanalyse for Ronaldo
ronaldo_lm <- lm(Goals ~ xG, data = ronaldo_data)
summary(ronaldo_lm)

