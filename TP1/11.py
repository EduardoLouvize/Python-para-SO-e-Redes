# Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo, usando o módulo ‘os’,
# de bloco de notas (notepad) para abri-lo.
import os

nome_arquivo = input("Digite o nome do arquivo: ")

executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe'
os.spawnv(os.P_WAIT, executavel_com_path, [executavel_com_path, nome_arquivo])

