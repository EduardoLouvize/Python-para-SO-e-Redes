# Escreva um programa que mostre a quantidade de bytes (em KB) de cada arquivo em um diretório.
import os

conteudo_da_pasta = os.listdir(os.getcwd())
arquivos = []

for item in conteudo_da_pasta:
    if os.path.isfile(item):
        arquivos.append(item)

print(arquivos)

for arquivo in arquivos:
    print(f"O tamanho do arquivo {arquivo} é {round((os.stat(arquivo).st_size / 1024), 2)} ")
