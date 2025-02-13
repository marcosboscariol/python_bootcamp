import pandas as pd
import os
import glob


def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


def carregar_dados(df: pd.DataFrame, formato_saida: list):
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv('dados.csv')
        if formato == 'parquet':
            df.to_parquet('dados.parquet')


def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


# pasta_argumento = 'aula_08/data'
# data_frame = (extrair_dados_e_consolidar(pasta_argumento))
# data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
# formato_saida = ['csv', 'parquet']
# carregar_dados(data_frame_calculado, formato_saida)
