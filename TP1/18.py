# Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de
# memória de paginação (swap) existem no computador.
import psutil
import time

memoria_principal = psutil.virtual_memory().total
memoria_paginacao = psutil.swap_memory().total

print(f"Memória principal: {round(memoria_principal / (1024*1024*1024), 2)} GB")
print(f"Memória de paginação: {round(memoria_paginacao / (1024*1024*1024), 2)} GB")
