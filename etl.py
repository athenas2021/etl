import pandas as pd
import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
filepath = f'{CURR_DIR}\COTAHIST_A2021.TXT'

print(CURR_DIR, filepath)

'''3.2 REGISTRO - 01 - COTAÇÕES HISTÓRICAS POR PAPEL-MERCADO '''
# (2, 10) DATA DO PREGÃO FORMATO “AAAAMMDD”  N(08) 03 10 
# (10, 12) CODBDI - CÓDIGO BDI 


# Importando as informações
# Arquivo trabalhando é um .txt posicional (vamos usar o método readfwf)

# lista com posições que eu quero para cada campo
colspecs = [(2, 10), (10, 12), (12, 24), (27, 39), (56, 69), (69, 82), (82,95), (108, 121),
(152,170), (170, 188)] 

# lista com os nomes de cada campos
names = ['data_pregao', 'codbdi', 'sigla_acao', 'nome_acao', 'preco_abertura', 'preco_maximo', 'preco_minimo', 'preco_fechamento',
'qtd_negocios', 'volume_negocios' ]

# Dataframe
df = pd.read_fwf(filepath, colspecs = colspecs, names = names, skiprows =1)

# Filtragem para o lote padrão (codbdi =2)
df = df [df['codbdi']==2]
# elimina esta coluna
df = df.drop(['codbdi'], 1)
print(df)