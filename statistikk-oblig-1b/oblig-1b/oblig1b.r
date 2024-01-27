# Assuming you have already installed and loaded ggplot2 and read the data
# Install necessary packages if not already installed
if (!require(ggplot2)) install.packages("ggplot2")

# Read CSV data
df <- read.csv("./terningDroppXY.csv")

# 2a
# Linear Regression on the first 5 measurements
lm_first5 <- lm(Lengde ~ Dropp, data=df[1:5, ])
summary(lm_first5)

#2c
# Linear Regression on the entire dataset
lm_full <- lm(Lengde ~ Dropp, data=df)

#2d
# Plotting the (x, y) data points for the entire dataset
plot(df$Dropp, df$Lengde, main="Scatterplot of Dropp vs Lengde", xlab="Dropp", ylab="Lengde")

#2e
# Adding regression line to the plot
abline(lm_full, col="blue")

#2g
# Sum of Squared Residuals for the first 5 measurements
ssr_first5 <- sum(residuals(lm_first5)^2)
cat("Sum of Squared Residuals (First 5 Measurements):", ssr_first5, "\n")

# Sum of Squared Residuals for the entire dataset
ssr_full <- sum(residuals(lm_full)^2)
cat("Sum of Squared Residuals (Entire Dataset):", ssr_full, "\n")

#2h
# Standard Error for the first 5 measurements
se_first5 <- sqrt(ssr_first5 / lm_first5$df.residual)
cat("Standard Error (First 5 Measurements):", se_first5, "\n")

# Standard Error for the entire dataset
se_full <- sqrt(ssr_full / lm_full$df.residual)
cat("Standard Error (Entire Dataset):", se_full, "\n")

#2i