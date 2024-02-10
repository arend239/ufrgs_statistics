## TRABALHO JULIA

# carrega pacotes

using Random
using Faker
using CSV
using DataFrames
using Dates

# configura para portugues
Faker.language("pt-BR")

# inicializa matriz de dados
dados = DataFrame([[],[],[],[],[],[]], ["nome", "estado","data","dia","unid","valor"])

#############################
#############################
# SEMENTE A SER MODIFICADA
Faker.seed(577787)
#############################
#############################

# ciclo de criacao do dataframe
for _ in 1:300
    nome = Faker.first_name()
    estado = Faker.state_abbr()
    temp = Faker.date_time_between("-20y","now","d-m-Y")
    data = Date(temp,"d-m-y")
    dia = Dates.dayname(data)
    unid = rand(15:40)
    valor = unid * rand(5:20)
    push!(dados, (nome, estado,data,dia,unid,valor))
end

dados

## A PARTIR DAQUI INICIA O CODIGO DE VOCES

ans = Dict()

cols = Dict("dia"    => "valor",
            "estado" => "valor",
            "nome"   => "unid") 
            
for (a,b) in cols

    ans[b * "_" * a] = combine(groupby(dados, Symbol(a)), Symbol(b) => sum)
    sort!(ans[b * "_" * a], Symbol(b * "_sum"), rev=true)

    if a == "nome"
        ans[b * "_" * a] = filter(b * "_sum" => i -> i > 35, ans[b * "_" * a])
    end
end

ans["dados_add_cols"] = insertcols(dados, :int_mes => month.(dados.data), 
                                          :chr_mes => monthabbr.(month.(dados.data)), 
                                          :tempo   => Dates.value.(Dates.today.() - Dates.Date.(dados.data)))

for i in ans

    println(i)
end