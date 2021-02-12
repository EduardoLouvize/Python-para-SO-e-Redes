# Escreva um programa que indique se um arquivo existe ou não. Caso exista, indique se é realmente um arquivo ou não.
import os

arquivo = "arquivo_teste.txt"
arquivo_lista = arquivo.split(".")

if os.path.exists(arquivo):
    print(f"{arquivo} existe.")
    if os.path.isfile(arquivo):
        print("É um arquivo")
    else:
        print("Existe mas não é um arquivo.")
else:
    print("Não existe.")
