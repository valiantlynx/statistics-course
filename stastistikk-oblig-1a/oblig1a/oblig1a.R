# Leser inn data
laban <- read.csv("labanXY.csv")

# Erstatter NA verdier i 'Antall' med 0
laban$Antall[is.na(laban$Antall)] <- 0

# Beregner kumulativ frekvens
laban$CumulativeFrequency <- cumsum(laban$Antall)

# Beregner statistiske mål
meanValue <- mean(laban$Midpunkt, na.rm = TRUE)
medianValue <- median(laban$Midpunkt, na.rm = TRUE)
modeValue <- as.numeric(names(sort(table(laban$Midpunkt), decreasing = TRUE)[1]))
sdValue <- sd(laban$Midpunkt, na.rm = TRUE)


# Lager et 'barplot' og lagrer returverdien for å få søyleposisjonene
bp <- barplot(laban$Antall, names.arg = laban$Midpunkt, 
              main = "Histogram of 'Antall'", xlab = "Midpunkt", ylab = "Frekvens", 
              col = "lightblue", border = "blue")

# Finner x-posisjonene for mean, median, mode og standardavvik
mean_xpos <- meanValue
median_xpos <- medianValue
mode_xpos <- modeValue
sd_neg_xpos <- meanValue - sdValue
sd_pos_xpos <- meanValue + sdValue

# Tegner linjer for statistiske mål
abline(v = mean_xpos, col = "red", lwd = 2)
abline(v = median_xpos, col = "blue", lwd = 2)
abline(v = mode_xpos, col = "purple", lwd = 2)
abline(v = sd_neg_xpos, col = "green", lwd = 2)
abline(v = sd_pos_xpos, col = "green", lwd = 2)

# Legger til tekstetiketter
text(mean_xpos, 0, "Mean", pos = 3, col = "red")
text(median_xpos, 0, "Median", pos = 3, col = "blue")
text(mode_xpos, 0, "Mode", pos = 3, col = "purple")
text(sd_neg_xpos, 0, "-SD", pos = 3, col = "green")
text(sd_pos_xpos, 0, "+SD", pos = 3, col = "green")

# Lager kumulativt frekvensdiagram
plot(laban$Midpunkt, laban$CumulativeFrequency, type = "o", 
     main = "Kumulativt Frekvensdiagram", xlab = "Midpunkt", ylab = "Kumulativ Frekvens")
