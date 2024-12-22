n           <- 16
rep         <- 1000 
mu          <- c(0,1)
alpha       <- 0.05
var         <- 1
val_critico <- qnorm(alpha, mu[1], var/sqrt(n), lower.tail = F)
  
cont_0 <- 0 
cont_1 <- 0 

for (i in 1:rep){
  
  sample <- rnorm(n, mu[1], var)
  cont_0 <- cont_0 + as.numeric(mean(sample) > val_critico)
  
  sample <- rnorm(n, mu[2], var)  
  cont_1 <- cont_1 + as.numeric(mean(sample) > val_critico)  
}

cat("Erro Tipo I (alpha) estimado:", cont_0 / rep, "\n")
cat("Poder do teste estimado:", cont_1 / rep, "\n")