# Escreva um programa que indique a extensão de um arquivo usando função do módulo os.path
import os

import os

arquivo = "arquivo_teste.txt"
caminho_completo = os.path.abspath(arquivo)
nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

print(f"A extensão do arquivo '{arquivo}' é '{extensao_arquivo}'")
