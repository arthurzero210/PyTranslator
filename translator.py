import pandas as pd
import os

errors = pd.read_json('errors.json', typ='series')
df_errors = errors.reset_index()
df_errors.columns = ['error_name', 'Valor']

while True:
    error = input("""Hello! Describe your error so we can help you!
Put the init (ex: TypeError, SyntaxError)
    """)
    error = str(error.lower())
    result = errors.get(error, "Erro não encontrado")
    print(result)