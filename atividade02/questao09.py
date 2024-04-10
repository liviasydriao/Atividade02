#Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

import pandas as pd

df = pd.read_csv('arquivo.csv')

#para filtrar valores de uma coluna com a idade de pessoas maiorees de idade:
coluna = df[df['´coluna_idade'] >= 18]