# Importando bibliotecas
import numpy as np
import pandas as pd
import os
pd.options.display.max_columns = 150

def pre_process():
    # Lendo o CSV com os dados
    samples_path = os.path.abspath("src/data/samples/")
    data_set = pd.read_csv(f"{samples_path}/data-final.csv", sep='\t')

    # Removendo valores ausentes
    print("Conjunto de dados: ", data_set.shape)
    print("Número de participantes: ", len(data_set))
    print("Existem valores ausentes? ", data_set.isnull().values.any())
    print("Quantos valores faltantes? ", data_set.isnull().values.sum())
    data_set.dropna(inplace=True)
    print("Número de participantes após excluir linhas com valores ausentes: ", len(data_set))

    start_rows = len(data_set)
    data_set = data_set.replace(0, np.nan).dropna(axis=0).reset_index(drop=True)
    remove_rows = start_rows - len(data_set)

    # Define os labels positivos
    positively_keyed = [
        'EXT1', 'EXT3', 'EXT5', 'EXT7', 'EXT9',                             #5 extroversão
        'EST1', 'EST3', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',    #8 neuroticismo                            
        'AGR2', 'AGR4', 'AGR6', 'AGR8', 'AGR9', 'AGR10',                    #6 Compatibilidade
        'CSN1', 'CSN3', 'CSN5', 'CSN7', 'CSN9', 'CSN10',                    #6 Responsabilidade
        'OPN1', 'OPN3', 'OPN5', 'OPN7', 'OPN8', 'OPN9', 'OPN10'             #7 Abertura à experiência
    ]

    # Define os labels negativos
    negatively_keyed = [
        'EXT2', 'EXT4', 'EXT6', 'EXT8', 'EXT10',    #5 extroversão
        'EST2', 'EST4',                             #2 neuroticismo
        'AGR1', 'AGR3', 'AGR5', 'AGR7',             #4 Compatibilidade
        'CSN2', 'CSN4', 'CSN6', 'CSN8',             #4 Responsabilidade
        'OPN2', 'OPN4', 'OPN6'                      #3 Abertura à experiência
    ]

    # Subtraindo 6 de cada item negativo, para termos uma direção dos dados
    data_set.loc[:, negatively_keyed] = 6 - data_set.loc[:, negatively_keyed]

    # Definindo e ordenando as colunas
    columns = positively_keyed + negatively_keyed
    data_set = data_set[sorted(columns)]

    # Definindo as labels a serem usadas a seguir
    personality_traits = ["EXT", "AGR", "CSN", "EST", "OPN"]

    # Soma os valores correspondentes a cada personalidade listada acima, para cada uma das linhas, 
    # e divide por 10, que é a quantia de perguntas respondidas para aquele traço de personalidade
    personality_traits_columns = []
    for trait in personality_traits:
        personality_traits_columns = sorted([col for col in data_set.columns if trait in col and '_E' not in col])
        data_set[trait] = data_set[personality_traits_columns].sum(axis=1).div(10)

    # Soma o total da pontuação das personalidades
    data_set["SUM"] = data_set[personality_traits].sum(axis=1)

    # Calcula a porcentagem de cada traço da personalidade
    for trait in personality_traits:
        data_set[trait + "_PER"] = data_set[trait].mul(100).div(data_set["SUM"])

    personality_traits_final = ["EXT_PER", "AGR_PER", "CSN_PER", "EST_PER", "OPN_PER"]

    y = data_set[personality_traits_final]
    X = data_set[sorted(columns)]
    # print(y)
    # print(X)

    return X, y

def get_x(data_set):
    # Removendo valores ausentes
    print("Conjunto de dados: ", data_set.shape)
    print("Número de participantes: ", len(data_set))
    print("Existem valores ausentes? ", data_set.isnull().values.any())
    print("Quantos valores faltantes? ", data_set.isnull().values.sum())
    data_set.dropna(inplace=True)
    print("Número de participantes após excluir linhas com valores ausentes: ", len(data_set))

    start_rows = len(data_set)
    data_set = data_set.replace(0, np.nan).dropna(axis=0).reset_index(drop=True)
    remove_rows = start_rows - len(data_set)

    # Define os labels positivos
    positively_keyed = [
        'EXT1', 'EXT3', 'EXT5', 'EXT7', 'EXT9',                             #5 extroversão
        'EST1', 'EST3', 'EST5', 'EST6', 'EST7', 'EST8', 'EST9', 'EST10',    #8 neuroticismo                            
        'AGR2', 'AGR4', 'AGR6', 'AGR8', 'AGR9', 'AGR10',                    #6 Compatibilidade
        'CSN1', 'CSN3', 'CSN5', 'CSN7', 'CSN9', 'CSN10',                    #6 Responsabilidade
        'OPN1', 'OPN3', 'OPN5', 'OPN7', 'OPN8', 'OPN9', 'OPN10'             #7 Abertura à experiência
    ]

    # Define os labels negativos
    negatively_keyed = [
        'EXT2', 'EXT4', 'EXT6', 'EXT8', 'EXT10',    #5 extroversão
        'EST2', 'EST4',                             #2 neuroticismo
        'AGR1', 'AGR3', 'AGR5', 'AGR7',             #4 Compatibilidade
        'CSN2', 'CSN4', 'CSN6', 'CSN8',             #4 Responsabilidade
        'OPN2', 'OPN4', 'OPN6'                      #3 Abertura à experiência
    ]

    # Subtraindo 6 de cada item negativo, para termos uma direção dos dados
    data_set.loc[:, negatively_keyed] = 6 - data_set.loc[:, negatively_keyed]

    # Definindo e ordenando as colunas
    columns = positively_keyed + negatively_keyed
    data_set = data_set[sorted(columns)]

    # Definindo as labels a serem usadas a seguir
    personality_traits = ["EXT", "AGR", "CSN", "EST", "OPN"]

    # Soma os valores correspondentes a cada personalidade listada acima, para cada uma das linhas, 
    # e divide por 10, que é a quantia de perguntas respondidas para aquele traço de personalidade
    personality_traits_columns = []
    for trait in personality_traits:
        personality_traits_columns = sorted([col for col in data_set.columns if trait in col and '_E' not in col])
        data_set[trait] = data_set[personality_traits_columns].sum(axis=1).div(10)

    X = data_set[sorted(columns)]
    # print(y)
    # print(X)

    return X