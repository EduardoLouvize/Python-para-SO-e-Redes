# Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’
# de Python. Dê um exemplo de cada.
import os

nome_arquivo = input("Digite o nome do arquivo: ")

executavel_com_path = os.environ['SYSTEMROOT'] + '\\System32\\notepad.exe'
os.spawnv(os.P_WAIT, executavel_com_path, [executavel_com_path, nome_arquivo])
