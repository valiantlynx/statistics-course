#install.packages("ggplot2")
library(ggplot2)

# Read CSV data
df <- read.csv("./labanXY.csv")

# Calculate Mean
mean <- weighted.mean(df$Midpunkt, df$Antall)

# Calculate Median
cumulative_frequency <- cumsum(df$Antall)
total_frequency <- tail(cumulative_frequency, n=1)
median_interval_index <- which(cumulative_frequency >= total_frequency / 2)[1]
median_interval_lower <- df$Lower[median_interval_index]
median_interval_upper <- df$Upper[median_interval_index]
median_interval_freq <- df$Antall[median_interval_index]
cumulative_freq_before_median <- ifelse(median_interval_index > 1, cumulative_frequency[median_interval_index - 1], 0)
median <- median_interval_lower + (total_frequency / 2 - cumulative_freq_before_median) / median_interval_freq * (median_interval_upper - median_interval_lower)

# Calculate Mode
mode <- df$Midpunkt[which.max(df$Antall)]

# Calculate Variance and Standard Deviation
mean_square <- weighted.mean(df$Midpunkt^2, df$Antall)
variance <- mean_square - mean^2
std_dev <- sqrt(variance)

# Sample Standard Deviation (assuming this is a sample)
sample_variance <- sum(df$Antall * (df$Midpunkt - mean)^2) / (total_frequency - 1)
sample_std_dev <- sqrt(sample_variance)

# Print calculated values
cat("Mean:", mean, "Median:", median, "Mode:", mode, "Variance:", variance, "Standard Deviation:", std_dev, "Sample Standard Deviation:", sample_std_dev, "\n")

# Function to draw vertical lines
drawLines <- function(mean, median, mode, std_dev, sample_std_dev) {
  list(
    geom_vline(xintercept=mean, color='red', linetype="solid", linewidth=1),
    geom_vline(xintercept=median, color='green', linetype="solid", linewidth=1),
    geom_vline(xintercept=mode, color='blue', linetype="solid", linewidth=1),
    geom_vline(xintercept=mean - std_dev, color='orange', linetype="dashed", linewidth=1),
    geom_vline(xintercept=mean + std_dev, color='orange', linetype="dashed", linewidth=1),
    geom_vline(xintercept=mean - sample_std_dev, color='purple', linetype="dotted", linewidth=1),
    geom_vline(xintercept=mean + sample_std_dev, color='purple', linetype="dotted", linewidth=1)
  )
}

# Plotting Histogram
ggplot(df, aes(x=Midpunkt, y=Antall)) +
  geom_bar(stat="identity", position=position_dodge(), color="black") +
  labs(title="Histogram", x="Midpunkt", y="Frekvens") +
  drawLines(mean, median, mode, std_dev, sample_std_dev)

# Plotting Frequency Diagram
ggplot(df, aes(x=Midpunkt, y=Antall)) +
  geom_bar(stat="identity", position=position_dodge(), color="black") +
  labs(title="Frequency Diagram", x="Midpunkt", y="Frekvens") +
  drawLines(mean, median, mode, std_dev, sample_std_dev)

# Plotting Cumulative Frequency Diagram
ggplot(df, aes(x=Midpunkt, y=cumulative_frequency)) +
  geom_line(color="black") +
  labs(title="Cumulative Frequency Diagram", x="Midpunkt", y="Kumulativ Frekvens") +
  drawLines(mean, median, mode, std_dev, sample_std_dev)

