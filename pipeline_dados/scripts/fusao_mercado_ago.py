import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv ='data_raw/dados_empresaB.csv'

# Extract
print('-------------------------------------------------------- EXTRAINDO DADOS -------------------------------------------------------- ')
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'\033[1;40mNome das colunas da Empresa A:\033[m \033[4;1;35m{dados_empresaA.nome_colunas}\033[m')
print(f'\033[1;40mQuantidade de linhas presentes nos arquivos da empresa A:\033[m \033[4;1;35m{dados_empresaA.qtd_linhas} - Linhas\033[m')

print()

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'\033[1;40mNome das colunas da Empresa B: \033[m \033[4;1;35m{dados_empresaB.nome_colunas}\033[m')
print(f'\033[1;40mQuantidade de linhas presentes nos arquivos da empresa B: \033[m \033[4;1;35m{dados_empresaB.qtd_linhas} - Linhas\033[m')

#Transform:
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
print()

print('-------------------------------------------------------- TRANSFORMANDO OS DADOS -------------------------------------------------------- ')
dados_empresaB.rename_columns(key_mapping)
print(f'\033[1;40mNovos nomes das colunas da Empresa B: \033[m \033[4;1;35m{dados_empresaB.nome_colunas}\033[m')

print()

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f'\033[1;40mDados unidos das empresas A e B: \033[m \033[4;1;35m{dados_fusao.nome_colunas}\033[m')

print(f'\033[1;40mQuantidade de linhas dos dados unidos: \033[m \033[4;1;35m{dados_fusao.qtd_linhas} - Linhas\033[m')

#Load
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)


   