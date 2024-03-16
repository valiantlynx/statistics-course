library(dplyr)
library(stringr) 
files = dir(path="Seigmann-filer")
idx = grepl("Laban", files, fixed=TRUE)
Laban = files[idx]
labanData = read.csv(file=paste("Seigmann-filer/",Laban[1],sep=""))
n = length(Laban)
for (k in 2:n) {
  newLabanData = read.csv(file=paste("Seigmann-filer/",Laban[k],sep=""))
  colnames(newLabanData) = str_to_title(colnames(newLabanData))
  #print(newLabanData)
  labanData = rbind(labanData,newLabanData)
}
labanData[is.na(labanData$Antall),"Antall"]=0
# Studentene får klare utdfordringen med å merge rader med samme intervallgrenser selv. :-)
