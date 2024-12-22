
# População normal (sigma desconhecido)
# Implementar IC 'paramétrico' para média \mu
# Implementar IC aproximado para média \mu
# Comparar IC's construídos em termos  de cobertura e tamanho

n     <- 12  
mu    <- 7  
sigma <- 1/2
gama  <- 0.95
alpha <- 1 - gama  
rep   <- 1000

ic_param <- 0
ic_aprox <- 0

param_interval <- c()
aprox_interval <- c()

for (i in 1:rep) {
  
    sample <- rnorm(n, mu, sigma)
    
    # param
    inf_lim  <- mean(sample) - qt(1 - alpha/2, df = n - 1) * sd(sample) / sqrt(n)
    sup_lim  <- mean(sample) + qt(1 - alpha/2, df = n - 1) * sd(sample) / sqrt(n)
    ic_param <- ic_param + as.numeric(inf_lim <= mu && mu <= sup_lim)
    
    param_interval <- append(param_interval, (sup_lim - inf_lim))

    # aprox
    inf_lim  <- mean(sample) - qnorm(1 - alpha/2) * sqrt((n - 1) * var(sample) / n^2)
    sup_lim  <- mean(sample) + qnorm(1 - alpha/2) * sqrt((n - 1) * var(sample) / n^2)
    ic_aprox <- ic_aprox + as.numeric(inf_lim <= mu && mu <= sup_lim) 
    
    aprox_interval <- append(aprox_interval, (sup_lim - inf_lim))
}

prob_cobert_param <- ic_param / rep;
prob_cobert_aprox <- ic_aprox / rep;

cat("Probabilidade de coberura dos IC's: \n",
    "Paramétrico: ", prob_cobert_param, "\n",
    "Aproximado: ",  prob_cobert_aprox, "\n")

cat("Tamanho IC's: \n",
    "Paramétrico: ", mean(param_interval), "\n",
    "Aproximado: ",  mean(aprox_interval), "\n")
