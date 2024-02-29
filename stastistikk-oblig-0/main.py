import pandas as pd
import numpy as np

# Read CSV data
df = pd.read_csv("./oblig1a/labanXY.csv")
midpoints = df['Midpunkt'].values
frequencies = df['Antall'].values

# Calculate Mean
mean = np.average(midpoints, weights=frequencies)

# Calculate Median
cumulative_frequency = np.cumsum(frequencies)
total_frequency = cumulative_frequency[-1]
median_interval_index = np.searchsorted(cumulative_frequency, total_frequency / 2)
median_interval_lower = df['Lower'][median_interval_index]
median_interval_upper = df['Upper'][median_interval_index]
median_interval_freq = frequencies[median_interval_index]
cumulative_freq_before_median = cumulative_frequency[median_interval_index - 1] if median_interval_index > 0 else 0
median = median_interval_lower + (total_frequency/2 - cumulative_freq_before_median) * (median_interval_upper - median_interval_lower) / median_interval_freq

# Calculate Mode
mode = df.loc[df['Antall'].idxmax(), 'Midpunkt']

# Calculate Variance and Standard Deviation
mean_square = np.average(midpoints**2, weights=frequencies)
variance = mean_square - mean**2
std_dev = np.sqrt(variance)

# Sample Standard Deviation (assuming this is a sample)
sample_variance = sum(frequencies * (midpoints - mean)**2) / (total_frequency - 1)
sample_std_dev = np.sqrt(sample_variance)

# Print calculated values
print(f"Mean: {mean:.2f}, Median: {median:.2f}, Mode: {mode}, Variance: {variance:.2f}, Standard Deviation: {std_dev:.2f}, Sample Standard Deviation: {sample_std_dev:.2f}")


import matplotlib.pyplot as plt

class DrawLines:
    def __init__(self, mean, median, mode, std_dev, sample_std_dev):
        self.mean = mean
        self.median = median
        self.mode = mode
        self.std_dev = std_dev
        self.sample_std_dev = sample_std_dev
        
    # Adding vertical lines for mean, median, mode, and standard deviations
    def draw(self):
        plt.axvline(self.mean, color='red', label='Middelverdi')
        plt.axvline(self.median, color='green', label='Median')
        plt.axvline(self.mode, color='blue', label='Typetall')
        plt.axvline(self.mean - self.std_dev, color='orange', linestyle='--', label='Populasjons Std Avvik')
        plt.axvline(self.mean + self.std_dev, color='orange', linestyle='--')
        plt.axvline(self.mean - self.sample_std_dev, color='purple', linestyle=':', label='Sample Std Avvik')
        plt.axvline(self.mean + self.sample_std_dev, color='purple', linestyle=':')
        plt.legend()
        plt.show()

draw = DrawLines(mean, median, mode, std_dev, sample_std_dev)
# Plotting Histogram
plt.figure(figsize=(10, 6))
plt.bar(midpoints, frequencies, width=df['Bredde'][0], edgecolor='black')
plt.title("Histogram")
plt.xlabel("Midpunkt")
plt.ylabel("Frekvens")
draw.draw()


# Plotting Frequency Diagram
plt.figure(figsize=(10, 6))
plt.bar(midpoints, frequencies, width=df['Bredde'][0], edgecolor='black')
plt.title("Frequency Diagram")
plt.xlabel("Midpunkt")
plt.ylabel("Frekvens")
draw.draw()

# Plotting Cumulative Frequency Diagram
plt.figure(figsize=(10, 6))
plt.plot(midpoints, cumulative_frequency, drawstyle='steps-post', color='black')
plt.title("Cumulative Frequency Diagram")
plt.xlabel("Midpunkt")
plt.ylabel("Kumulativ Frekvens")
draw.draw()
