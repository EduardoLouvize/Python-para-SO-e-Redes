# Escreva um programa que mostre as datas de criação e modificação de cada arquivo em um diretório.
import os
import time

conteudo_da_pasta = os.listdir(os.getcwd())
arquivos = []

for item in conteudo_da_pasta:
    if os.path.isfile(item):
        arquivos.append(item)

print(arquivos)

for arquivo in arquivos:
    print(f"Arquivo: {arquivo} | Criação: {time.ctime(os.stat(arquivo).st_ctime)} | "
          f"Modificação: {time.ctime(os.stat(arquivo).st_mtime)}")

