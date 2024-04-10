#Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd
df = pd.read_csv('arquivo.csv')

# Verifica se há valores ausentes em todo o DataFrame
df.isna()
# Verifica se há valores ausentes em uma coluna específica
df['Nome_da_Coluna'].isna()

# Preenche todos os valores ausentes com um valor específico
df.fillna(valor)

# Remove linhas com pelo menos um valor ausente
df.dropna()
# Remove colunas com pelo menos um valor ausente
df.dropna(axis=1)




