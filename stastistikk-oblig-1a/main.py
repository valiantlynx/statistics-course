import pandas as pd
import numpy as np

# Read CSV data
df = pd.read_csv("./labanXY.csv")
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

# Plotting Histogram
plt.figure(figsize=(10, 6))
plt.bar(midpoints, frequencies, width=df['Bredde'][0], edgecolor='black')
plt.title("Histogram")
plt.xlabel("Midpunkt")
plt.ylabel("Frekvens")
# Adding vertical lines for mean, median, mode, and standard deviations
plt.axvline(mean, color='red', label='Middelverdi')
plt.axvline(median, color='green', label='Median')
plt.axvline(mode, color='blue', label='Typetall')
plt.axvline(mean - std_dev, color='orange', linestyle='--', label='Populasjons Std Avvik')
plt.axvline(mean + std_dev, color='orange', linestyle='--')
plt.axvline(mean - sample_std_dev, color='purple', linestyle=':', label='Sample Std Avvik')
plt.axvline(mean + sample_std_dev, color='purple', linestyle=':')
plt.legend()
plt.show()

# Plotting Frequency Diagram
plt.figure(figsize=(10, 6))
plt.bar(midpoints, frequencies, width=df['Bredde'][0], edgecolor='black')
plt.title("Frequency Diagram")
plt.xlabel("Midpunkt")
plt.ylabel("Frekvens")
plt.axvline(mean, color='red')
plt.axvline(median, color='green')
plt.axvline(mode, color='blue')
plt.axvline(mean - std_dev, color='orange', linestyle='--')
plt.axvline(mean + std_dev, color='orange', linestyle='--')
plt.axvline(mean - sample_std_dev, color='purple', linestyle=':')
plt.axvline(mean + sample_std_dev, color='purple', linestyle=':')
plt.show()

# Plotting Cumulative Frequency Diagram
plt.figure(figsize=(10, 6))
plt.plot(midpoints, cumulative_frequency, drawstyle='steps-post', color='black')
plt.title("Cumulative Frequency Diagram")
plt.xlabel("Midpunkt")
plt.ylabel("Kumulativ Frekvens")
plt.axvline(mean, color='red')
plt.axvline(median, color='green')
plt.axvline(mode, color='blue')
plt.axvline(mean - std_dev, color='orange', linestyle='--')
plt.axvline(mean + std_dev, color='orange', linestyle='--')
plt.axvline(mean - sample_std_dev, color='purple', linestyle=':')
plt.axvline(mean + sample_std_dev, color='purple', linestyle=':')
plt.show()
