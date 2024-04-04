import pandas as pd
from time import sleep

def setup():
    # Carrega os dados do arquivo dados.txt em um DataFrame, 
    # cada linha no txt equivale à uma linha no excel,
    # para separar as colunas, utiliza vírgula
    dataframe = pd.read_csv('dados.txt', delimiter=',')

    # Salva o DataFrame em um arquivo Excel
    dataframe.to_excel('dados.xlsx', index=False)

    # Loopando o código à cada 1 minuto
    sleep(60)
    setup()

# Iniciando o código de fato
setup()
