## SCRIPT GERADOR DE BANCO DE DADOS

###############################
### COLOCAR A SEMENTE AQUI - NUMERO CARTAO UFRGS SEM OS ZEROS
###############################

set.seed(577787)

# tamanho do banco
n_size <- 200 # padrao
# nomes dos vendedores
c1 <- c("Andrew", "Michael", "Christopher",
        "Joshua", "Daniel", "David",
        "James", "Matthew", "Robert", "Anthony")
c2 <- c("Elizabeth", "Sarah", "Jessica",
        "Jennifer", "Ashley", "Samantha",
        "Stephanie", "Brittany", "Nicole", "Amanda")

# banco auxiliar dos vendedores
vend <- sample(c1, size = 5, replace = FALSE)
vend <- c(vend, sample(c2, size = 5, replace = FALSE))
cod <- sample(1:15, size = 10, replace = FALSE)
cod_vend <- as.data.frame(as.factor(cod), vend)

###############################
##### O banco cod.vend eh o banco auxiliar para montar o banco final do trabalho
###############################

#### FUNCAO EXTRA
rdate <- function(x,
                  min = paste0(format(Sys.Date(), "%Y"), "-01-01"),
                  max = paste0(format(Sys.Date(), "%Y"), "-12-31"),
                  sort = TRUE) {

  dates <- sample(seq(as.Date(min),
                      as.Date(max),
                      by = "day"),
                  x,
                  replace = TRUE)
  if (sort == TRUE) {
    sort(dates)
  } else {
    dates
  }
}

### INDICE PRODUTOS
prd <- c("chair", "stool", "table", "mug", "cup", "desk lamp", "floor lamp",
         "desk", "shelf", "sofa", "tea cup", "tea pot", "cutlery", "chess set",
         "lounge", " alarm clock", "phone dock", "keyboard", "side table",
         "wallet", "vase", "dog bed", "bird house", "wine holder", "skateboard",
         "calculator")
prd_n <- sample(prd, size = 6, replace = FALSE)

###############################
# banco principal

# local
local <- list(reg = sample(1:10, size = n, replace = TRUE),
              zon = sample(20:30, size = n, replace = TRUE),
              mun = sample(100:110, size = n, replace = TRUE))

var1 <- sample(c("reg","zon","mun"), size = 1)

# produto
produto <- list(cat = sample(LETTERS[1:6], size = n_size, replace = TRUE),
                ind = sample(1:6, size = n_size, replace = TRUE),
                cod = sample(1002:1007, size = n_size, replace = TRUE),
                nom = sample(prd.n, size = n_size, replace = TRUE))

var2 <- sample(c("cat", "ind", "cod", "nom"), size = 1)

# vendas
vendas <- list(und = sample(1:50, size = n_size, replace = TRUE),
               rec = sample(500:800, size = n_size, replace = TRUE),
               luc = sample(100:300, size = n_size, replace = TRUE))

var3 <- sample(c("und", "rec", "luc"), size = 1)

# datas
datas <- list(trim1 = rdate(n_size, "2020/01/01", "2020/03/30"),
              trim2 = rdate(n_size, "2020/04/01", "2020/06/30"),
              trim3 = rdate(n_size, "2020/07/01", "2020/09/30"),
              trim4 = rdate(n_size, "2020/10/01", "2020/12/30"))

var4 <- sample(c("trim1", "trim2", "trim3", "trim4"), size = 1)

# vendedor
vend_f <- sample(1:15, size = n_size, replace = TRUE)

###############################
## BANCO FINAL
dados <- data.frame(vend_f,
                    local[var1],
                    produto[var2],
                    vendas[var3],
                    datas[var4])

###############################
## BANCO AUXILIAR - cod.vend

################################
## INICIO DO CODIGO DA TAREFA ##
################################

library(dplyr)
library(lubridate)

################################
# Montagem da Amostra 

amostra <- dados[sample(nrow(dados),
                        0.4 * nrow(dados),
                        replace = FALSE), ]

################################
# Nomear vendedores

df_aux <- data.frame(vend.f = cod,
                     nome = vend)

amostra_nomes <- merge(amostra,
                       df_aux,
                       by = "vend.f",
                       all.x = TRUE)

# Replace NA's por 'Desconhecido'
amostra_nomes$nome <- ifelse(is.na(amostra_nomes$nome),
                             "Desconhecido",
                             amostra_nomes$nome)

################################

vars <- colnames(amostra)
vars <- vars[!vars %in% "rec"]

respostas <- list()

for (i in vars) {

  if (i == "trim3"){
    resum <- amostra %>%
      group_by(month(get(i))) %>%
      summarise(tot_rec = sum(rec)) %>%
      arrange(desc(tot_rec))
  } else {
    resum <- amostra %>%
      group_by(get(i)) %>%
      summarise(tot_rec = sum(rec)) %>%
      arrange(desc(tot_rec))
  }

  respostas[[paste(i, "|rec", sep = "|")]] <- resum
}

respostas[["amostra|+|nomes"]] <- amostra_nomes
View(respostas)