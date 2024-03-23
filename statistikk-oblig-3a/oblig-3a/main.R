p=0.349
m=50
n=10
z = rbinom(m,n,p)/n
hist(z,breaks=seq(-0.5,n+.5,1)/n)
m=mean(z)
s=sd(z)
abline(v=m,col="green",lwd=1)
abline(v=m+c(-s,s),col="pink",lwd=1)
abline(v=p,col="blue",lwd=1)

# rbinom(30,1,p)
# rbinom(1,30,p)