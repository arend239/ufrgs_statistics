set.seed(338357) 
n <- 20
theta <- 2
gama <- 0.99
replicacoes <- 100000

a <- 1 - gama
lambda <- 1 / theta # -- lambda para a exponencial: 1/theta

contador_exp <- 0
contador_uni <- 0

for (i in 1:replicacoes) {
    # -- Exponencial
    dados_exp <- rexp(n, rate = lambda)
    soma_amostral <- sum(dados_exp)
    qinf_exp <- qchisq((1 - gama)/2, df = 2 * n)
    qsup_exp <- qchisq((1 + gama)/2, df = 2 * n)
    ic_inferior_exp <- (2 * soma_amostral) / qsup_exp
    ic_superior_exp <- (2 *soma_amostral) / qinf_exp
    if (theta >= ic_inferior_exp && theta <= ic_superior_exp) {
        contador_exp <- contador_exp + 1
    }

    # -- Uniforme
    dados_uni <- runif(n, min = 0, max = theta)
    X_max <- max(dados_uni)
    qinf_uni <- (1 - gama)/2
    qsup_uni <- (1 + gama)/2
    ic_inferior_uni <- X_max / qsup_uni^(1/n)
    ic_superior_uni <- X_max / qinf_uni^(1/n)
    if (theta >= ic_inferior_uni && theta <= ic_superior_uni) {
        contador_uni <- contador_uni + 1
    }
}

probabilidade_cobertura_exp <- contador_exp / replicacoes
probabilidade_cobertura_uni <- contador_uni / replicacoes

cat("Probabilidade de cobertura (Exponencial):", probabilidade_cobertura_exp, "\n")
cat("Probabilidade de cobertura (Uniforme):", probabilidade_cobertura_uni, "\n")
