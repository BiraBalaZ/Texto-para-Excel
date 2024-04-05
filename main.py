import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('origem', help='Digite a origem dos dados')
parser.add_argument('destino', help='Digite o destino dos dados')
args = parser.parse_args()

def setup():
    '''Docstring'''
    try:
        dataframe = pd.read_csv(args.origem, delimiter=',')
    except FileNotFoundError as exc:
        raise FileNotFoundError(f'Arquivo {args.origem} não encontrado.') from exc
    except UnicodeDecodeError as exc:
        raise Exception(f'Arquivo {args.origem} é inválido.') from exc

    # Salva o DataFrame em um arquivo Excel
    dataframe.to_excel(args.destino, index=False)

    print('\033[32mDados transferidos com sucesso!\033[m')

if __name__ == "__main__":
    setup()
