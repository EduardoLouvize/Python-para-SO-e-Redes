
import subprocess
import os


def cria_abre_arquivo_txt(nome_arquivo):
    if f"{nome_arquivo}.txt" not in os.listdir():
        arq = open(f"{nome_arquivo}.txt", "w")
        arq.close()
        subprocess.Popen(["notepad", nome_arquivo])
    else:
        subprocess.Popen(["notepad", nome_arquivo])


arquivo = input("Informe o nome do arquivo de texto SEM a extensão:")
cria_abre_arquivo_txt(arquivo)
