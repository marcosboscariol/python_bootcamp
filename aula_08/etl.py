import pandas as pd
import os
import glob

pasta = 'aula_08\data'


def extrair_dados(pasta: str) -> pd.DataFrame:

    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
