# Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo.
# A impressão não deve conter o nome do arquivo, apenas o caminho.
import os

arquivo = "arquivo_teste.txt"
caminho_completo = os.path.abspath(arquivo)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

print(f"O caminho do arquivo '{arquivo}' é '{caminho_arquivo}'")
