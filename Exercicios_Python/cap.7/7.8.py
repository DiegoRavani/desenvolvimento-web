# Crie um programa que exclua o diretório criado no exercício anterior com todo o seu conteúdo (cuidado para não excluir a pasta errada).

import os
import shutil

nome_diretorio = "temp"

if os.path.exists(nome_diretorio):
    shutil.rmtree(nome_diretorio)
    print(f"Diretório '{nome_diretorio}'foi excluído com sucesso.")
else:
    print(f"O diretório '{nome_diretorio}' não existe.")

