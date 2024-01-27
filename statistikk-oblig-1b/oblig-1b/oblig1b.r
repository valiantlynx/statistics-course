# Assuming you have already installed and loaded ggplot2 and read the data
# Install necessary packages if not already installed
if (!require(ggplot2)) install.packages("ggplot2")

# Read CSV data
df <- read.csv("./terningDroppXY.csv")

# Perform Linear Regression on the first 5 measurements
lm_first5 <- lm(Lengde ~ Dropp, data=df[1:5, ])

# Perform Linear Regression on the entire dataset
lm_full <- lm(Lengde ~ Dropp, data=df)

# Function to plot data, regression line, and residuals
plot_data <- function(df, lm_model, title) {
  ggplot(df, aes(x=Dropp, y=Lengde)) +
    geom_point() +
    geom_smooth(method="lm", se=FALSE, color="blue") +
    geom_segment(aes(xend=Dropp, yend=predict(lm_model)), linetype="dotted", color="red") +
    labs(title=title, x="Dropp", y="Lengde")
}

# Plot for the first 5 measurements
plot1 <- plot_data(df[1:5, ], lm_first5, "Linear Regression on First 5 Measurements")

# Plot for the entire dataset
plot2 <- plot_data(df, lm_full, "Linear Regression on Entire Dataset")

# Print the plots
print(plot1)
print(plot2)

# Calculate Sum of Squared Residuals and Standard Error for both models
ssr_first5 <- sum(residuals(lm_first5)^2)
se_first5 <- sqrt(ssr_first5 / lm_first5$df.residual)

ssr_full <- sum(residuals(lm_full)^2)
se_full <- sqrt(ssr_full / lm_full$df.residual)

# Print Sum of Squared Residuals and Standard Error
cat("First 5 Measurements:\n")
cat("Sum of Squared Residuals:", ssr_first5, "\n")
cat("Standard Error:", se_first5, "\n\n")

cat("Entire Dataset:\n")
cat("Sum of Squared Residuals:", ssr_full, "\n")
cat("Standard Error:", se_full, "\n")
