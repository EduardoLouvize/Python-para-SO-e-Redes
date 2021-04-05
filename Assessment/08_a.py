import time


def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return (fat)


def fatorial_lista(lista_inteiros):

    lista_retorno = []
    for item in lista_inteiros:
        resultado = fatorial(item)
        lista_retorno.append(resultado)
    return lista_retorno


hora_inicio = time.time()
quantidade_numeros = 5000

lista = []
for i in range(quantidade_numeros):
    lista.append(i)

resultado = fatorial_lista(lista)

hora_final = time.time()
tempo_decorrido = hora_final-hora_inicio


print("Primeiros resultados:", resultado[:5])
print(f"Tempo sequencial: {tempo_decorrido}")

arq = open("08A.txt", "w")
for item in resultado:
    arq.write(f"{item}\n")
arq.close()
