# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar base de dados de pdorutos
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o cadastro para todos os produtos

# install pandas 
# pip install pandas numpy openpyxl

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)