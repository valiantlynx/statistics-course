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


# Function to draw vertical lines and add text annotations
drawLinesAndText <- function(mean, median, mode, std_dev, sample_std_dev, ymax) {
  list(
    geom_vline(xintercept=mean, color='red', linetype="solid", linewidth=1),
    geom_text(aes(x=mean, label="Middelverdi", y=ymax*0.9), color='red', vjust=-1.5, size=3),
    
    geom_vline(xintercept=median, color='green', linetype="solid", linewidth=1),
    geom_text(aes(x=median, label="Median", y=ymax*0.8), color='green', vjust=-1.5, size=3),
    
    geom_vline(xintercept=mode, color='blue', linetype="solid", linewidth=1),
    geom_text(aes(x=mode, label="Typetall", y=ymax*0.7), color='blue', vjust=-1.5, size=3),
    
    geom_vline(xintercept=mean - std_dev, color='orange', linetype="dashed", linewidth=1),
    geom_text(aes(x=mean - std_dev, label="Populasjonsstandardavvik", y=ymax*0.6), color='orange', vjust=-1.5, size=3),
    
    geom_vline(xintercept=mean + std_dev, color='orange', linetype="dashed", linewidth=1),
    geom_text(aes(x=mean + std_dev, label="Populasjonsstandardavvik", y=ymax*0.5), color='orange', vjust=-1.5, size=3),
    
    geom_vline(xintercept=mean - sample_std_dev, color='purple', linetype="dotted", linewidth=1),
    geom_text(aes(x=mean - sample_std_dev, label="Utvalgsstandardavvik", y=ymax*0.4), color='purple', vjust=-1.5, size=3),
    
    geom_vline(xintercept=mean + sample_std_dev, color='purple', linetype="dotted", linewidth=1),
    geom_text(aes(x=mean + sample_std_dev, label="Utvalgsstandardavvik", y=ymax*0.3), color='purple', vjust=-1.5, size=3)
  )
}

# Determine the maximum Y value for each plot
ymax_hist <- max(df$Antall)
ymax_freq <- max(df$Antall)
ymax_cumul <- max(cumulative_frequency)

# Plotting Histogram with Annotations
ggplot(df, aes(x=Midpunkt, y=Antall)) +
  geom_bar(stat="identity", position=position_dodge(), color="black") +
  labs(title="Histogram", x="Midpunkt", y="Frekvens") +
  drawLinesAndText(mean, median, mode, std_dev, sample_std_dev, ymax_hist)

# Plotting Frequency Diagram with Annotations
ggplot(df, aes(x=Midpunkt, y=Antall)) +
  geom_bar(stat="identity", position=position_dodge(), color="black") +
  labs(title="Frekvens Diagram", x="Midpunkt", y="Frekvens") +
  drawLinesAndText(mean, median, mode, std_dev, sample_std_dev, ymax_freq)

# Plotting Cumulative Frequency Diagram with Annotations using geom_step
ggplot(df, aes(x=Midpunkt, y=cumulative_frequency)) +
  geom_step(color="black") +  # Using geom_step for blocky appearance
  labs(title="Kumulativ Frekvens Diagram", x="Midpunkt", y="Kumulativ Frekvens") +
  drawLinesAndText(mean, median, mode, std_dev, sample_std_dev, ymax_cumul) +
  theme(panel.background = element_rect(fill = "lightgray"))

