
data = [164, 167, 169, 173, 174, 177, 178, 179, 179, 182, 183, 184, 188, 189, 194]

#  list of tuples to represent the intervals and their frequencies
intervals = [(150, 155), (155, 160), (160, 165), (165, 170), (170, 175), (175, 180), (180, 185), (185, 190), (190, 195), (195, 200)]
freq_list = []
for i in intervals:
    freq = len([x for x in data if x >= i[0] and x < i[1]])
    freq_list.append((i, freq))

# Next, we'll calculate the relative frequency for each interval
total = sum([x[1] for x in freq_list])
rel_freq_list = []
for i, freq in freq_list:
    rel_freq = freq / total
    rel_freq_list.append((i, freq, rel_freq))

# Finally, we'll calculate the cumulative relative frequency for each interval
cum_rel_freq_list = []
cumulative = 0
for i, freq, rel_freq in rel_freq_list:
    cumulative += rel_freq
    cum_rel_freq_list.append((i, freq, rel_freq, cumulative))

# Print the final frequency table
print("Høyde i cm\tFrekvens\tRelativ frekvens\tKumulativ relativ frekvens")
for interval, freq, rel_freq, cum_rel_freq in cum_rel_freq_list:
    print(f"{interval}\t{freq}\t{rel_freq:.3f}\t{cum_rel_freq:.3f}")

#Q1 gjennomsnitt for dataene
def gjennomsnitt(data):
    gjennomsnitt = sum(data)/len(data)
    return gjennomsnitt
   

print(f"gjennomsnitt = {gjennomsnitt(data):.3f} ") 
 
#Q2 median for dataene
def median(data):
    data.sort()
    median = len(data)//2
    if len(data)%2 != 0:
        return data[median]
    elif len(data)%2 == 0:
        return (data[median-1] + data[median])/2
print(f"median = {median(data):.3f} ")

#Q3 modus for dataene
def modus(data):
    # create a dictionary to store the frequency of each value
    frequency = {}
    for x in data:
        if x in frequency:
            frequency[x] += 1
        else:
            frequency[x] = 1
    # find the highest frequency
    max_frequency = max(frequency.values())
    # find the values that have the highest frequency
    modus = [k for k, v in frequency.items() if v == max_frequency]
    return modus

print(f"modus = {modus(data)} ")

#Q4 varianse for dataene
def variance(data):
    # calculate the mean of the data
    mean = sum(data) / len(data)
    # calculate the variance
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance

print(f"variance = {variance(data):.3f} ")



def standard_deviation(data):
    # calculate the mean of the data
    mean = sum(data) / len(data)
    # calculate the variance
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    # calculate the standard deviation
    standard_deviation = variance ** 0.5
    return standard_deviation

print(f"standard deviation = {standard_deviation(data):.3f} ")

# use matplotlib  to plot the histogram, and show the plot as well as the frequency and kumulative frequency tables. also make a frequency diagram and a kumulative frequency diagram. on the disgrams, show the mean, median and modus as vertical lines. and begge type standard avvik as vertical lines- populasjon standard avvik and utvalg standard avvik.

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# plot the histogram
plt.hist(data, bins=10, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Høyde i cm")
plt.ylabel("Frekvens")
plt.show()

# plot the frequency diagram
x = [x[0][0] for x in freq_list]
y = [x[1] for x in freq_list]
plt.bar(x, y, width=5, edgecolor="black")
plt.title("Frekvensdiagram")
plt.xlabel("Høyde i cm")
plt.ylabel("Frekvens")
plt.show()

# plot the cumulative frequency diagram
x = [x[0][0] for x in cum_rel_freq_list]
y = [x[3] for x in cum_rel_freq_list]
plt.bar(x, y, width=5, edgecolor="black")
plt.title("Kumulativt frekvensdiagram")
plt.xlabel("Høyde i cm")
plt.ylabel("Kumulativ frekvens")
plt.show()

# plot the normal distribution with the mean, median and modus as vertical lines, and the population standard deviation and sample standard deviation as vertical lines
x = np.linspace(150, 200, 100)
plt.plot(x, stats.norm.pdf(x, gjennomsnitt(data), standard_deviation(data)))
plt.axvline(gjennomsnitt(data), color="red")
plt.axvline(median(data), color="green")
plt.axvline(modus(data)[0], color="blue")
plt.axvline(gjennomsnitt(data) - standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) + standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) - standard_deviation(data) / (len(data) ** 0.5), color="purple")
plt.axvline(gjennomsnitt(data) + standard_deviation(data) / (len(data) ** 0.5), color="purple")
plt.title("Normalfordeling")
plt.xlabel("Høyde i cm")
plt.ylabel("Frekvens")
plt.show()

# plot the normal distribution with the mean, median and modus as vertical lines, and the population standard deviation and sample standard deviation as vertical lines, and the cumulative frequency diagram
x = np.linspace(150, 200, 100)
plt.plot(x, stats.norm.pdf(x, gjennomsnitt(data), standard_deviation(data)))
plt.axvline(gjennomsnitt(data), color="red")
plt.axvline(median(data), color="green")
plt.axvline(modus(data)[0], color="blue")
plt.axvline(gjennomsnitt(data) - standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) + standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) - standard_deviation(data) / (len(data) ** 0.5), color="purple")
plt.axvline(gjennomsnitt(data) + standard_deviation(data) / (len(data) ** 0.5), color="purple")
x = [x[0][0] for x in cum_rel_freq_list]
y = [x[3] for x in cum_rel_freq_list]
plt.bar(x, y, width=5, edgecolor="black")
plt.title("Kumulativt frekvensdiagram")
plt.xlabel("Høyde i cm")
plt.ylabel("Frekvens")
plt.show()

# plot the normal distribution with the mean, median and modus as vertical lines, and the population standard deviation and sample standard deviation as vertical lines, and the frequency diagram
x = np.linspace(150, 200, 100)
plt.plot(x, stats.norm.pdf(x, gjennomsnitt(data), standard_deviation(data)))
plt.axvline(gjennomsnitt(data), color="red")
plt.axvline(median(data), color="green")
plt.axvline(modus(data)[0], color="blue")
plt.axvline(gjennomsnitt(data) - standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) + standard_deviation(data), color="orange")
plt.axvline(gjennomsnitt(data) - standard_deviation(data) / (len(data) ** 0.5), color="purple")
plt.axvline(gjennomsnitt(data) + standard_deviation(data) / (len(data) ** 0.5), color="purple")
x = [x[0][0] for x in freq_list]
y = [x[1] for x in freq_list]
plt.bar(x, y, width=5, edgecolor="black")
plt.title("Frekvensdiagram")
plt.xlabel("Høyde i cm")
plt.ylabel("Frekvens")
plt.show()
