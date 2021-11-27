import pandas as pd
import os



'''3.2 REGISTRO - 01 - COTAÇÕES HISTÓRICAS POR PAPEL-MERCADO '''
# (2, 10) DATA DO PREGÃO FORMATO “AAAAMMDD”  N(08) 03 10 
# (10, 12) CODBDI - CÓDIGO BDI 

''' *Extract* '''
# Importando as informações
# Arquivo trabalhando é um .txt posicional (vamos usar o método readfwf)

def read_files(path, name_file, year_date, type_file):
    _file = f'{path}{name_file}{year_date}.{type_file}'
    # lista com posições que eu quero para cada campo
    colspecs = [(2, 10), (10, 12), (12, 24), (27, 39), (56, 69), (69, 82), (82,95), (108, 121),
    (152,170), (170, 188)] 

    # lista com os nomes de cada campos
    names = ['data_pregao', 'codbdi', 'sigla_acao', 'nome_acao', 'preco_abertura', 'preco_maximo', 'preco_minimo', 'preco_fechamento',
    'qtd_negocios', 'volume_negocios' ]

    # Dataframe
    df = pd.read_fwf(_file, colspecs = colspecs, names = names, skiprows =1)
    return df

def filter_stocks(df):
    # Filtragem para o lote padrão (codbdi =2)
    df = df [df['codbdi']==2]
    # elimina esta coluna
    df = df.drop(['codbdi'], 1)
    return df


''' *Transform* '''
def parse_date(df):
    # Ajuste no campo data
    df['data_pregao'] = pd.to_datetime(df['data_pregao'], format='%Y%m%d')
    return df 


def parse_values(df):
    # Ajuste dos campos numéricos (campos decimais, 2 casas após ponto)
    df['preco_abertura'] = (df['preco_abertura'] / 100).astype(float)
    df['preco_maximo'] = (df['preco_maximo'] / 100).astype(float)
    df['preco_minimo'] = (df['preco_minimo'] / 100).astype(float)
    df['preco_fechamento'] = (df['preco_fechamento'] / 100).astype(float)
    return df


# Função para juntar arquivos de vários anos em um único arquivo já formatado
def concat_files(path, name_file, year_date, type_file, final_file):
    for i, y in enumerate(year_date):

        df = read_files(path, name_file, y, type_file)
        df = filter_stocks(df)
        df = parse_date(df)
        df = parse_values(df)

        if i==0:
            df_final = df
        else:
            df_final = pd.concat([df_final], df)
    ''' *Load*'''
    df_final.to_csv(f'{path}//{final_file}', index=False)


# Execução
year_date = ['2021']
path = f'{os.path.dirname(os.path.realpath(__file__))}\\'
name_file = 'COTAHIST_A'
type_file = 'TXT'    
final_file = 'bovespa_teste_tudo.csv'
concat_files(path, name_file, year_date, type_file, final_file)
