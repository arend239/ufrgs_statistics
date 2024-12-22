mu=5
sd=47
n=15
Xbarra<-c()
S2<-c()
for(i in 1:1000){
  X<-rnorm(n,mu,sd)
  Xbarra[i]<-mean(X)
  S2[i]<-var(X)
  
}

plot(Xbarra,S2)
plot(S2,Xbarra)
abline(h=mu)

plot(density(x)) #density() densidade empírica

plot(density(Xbarra))


curve(dchisq(x, df = 10), from = 0, to = 40)#densidade teórica 
