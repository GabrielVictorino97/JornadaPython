#Passo a Passo
# Passo 1: Importar a Base de Dados
import pandas

tabela = pandas.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
# Passo 2: Visualizar a Base de Dados
#display(tabela)

# Passo 3: Corrigir as cagadas da base de dados
#display(tabela.info())
tabela = tabela.dropna()
#display(tabela.info())
# Passo 4: Primeira Análise do cancelamento dos clientes (Qual a % de clientes que cancelou)
# Passo 5: Análise a causa de cancelamento de clientes

# Passo 4: Primeira Análise do cancelamento dos clientes (Qual a % de clientes que cancelou)
#display(tabela["cancelou"].value_counts())
#display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

#display(tabela["duracao_contrato"].value_counts())
#display(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.1%}".format))

#agrupamento
agrupamento = tabela.groupby("duracao_contrato").mean(numeric_only=True)
#display(agrupamento)

#todos os clientes do contrato mensal cancelaram
# sugestão: oferecer desconto nos contratos anuais/trimestrais

tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
# display(tabela["cancelou"].value_counts())
# display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise a causa de cancelamento de clientes
# criar gráficos para fazer análise
import plotly.express as px

#cria o grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x="idade", color="cancelou")

#exibe o grafico
    grafico.show()