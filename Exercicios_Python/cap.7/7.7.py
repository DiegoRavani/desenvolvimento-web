# Faça um programa que crie um diretório chamado "temp" e, dentro desse diretório, crie também um arquivo chamado "temp.txt".

import os

nome_diretorio = "temp"

if not os.path.exists(nome_diretorio):
    os.makedirs(nome_diretorio)
    print(f"Diretório '{nome_diretorio}' criado com sucesso.")

    caminho_arquivo = os.path.join(nome_diretorio, "temp.txt")

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write("Este é um arquivo temporário.")

    print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")
else:
    print(f"O diretório '{nome_diretorio}' já existe.")

