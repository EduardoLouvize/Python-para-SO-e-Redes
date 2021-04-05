import time
import threading


def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def fatorial_lista(lista_inteiros, fat_parc, id):
    lista_retorno = []
    if type(lista_inteiros) == list:
        for item in lista_inteiros:
            resultado = fatorial(item)
            lista_retorno.append(resultado)
    elif type(lista_inteiros) == int:
        lista_retorno.append(fatorial(lista_inteiros))
    fat_parc[id] = lista_retorno


quantidade_numeros = 5000

hora_inicio = time.time()

lista = []
for i in range(quantidade_numeros):
    lista.append(i)

num_threads = 4
result_parcial = num_threads * [0]
lista_threads = []

for i in range(num_threads):
    ini = i * int(quantidade_numeros / num_threads)
    fim = (i + 1) * int(quantidade_numeros / num_threads)
    t = threading.Thread(target=fatorial_lista, args=(lista[ini:fim], result_parcial, i))
    t.start()
    lista_threads.append(t)

for t in lista_threads:
    t.join()


resultado = [x for l in result_parcial for x in l]

hora_final = time.time()
tempo_decorrido = hora_final-hora_inicio


print("Primeiros resultados:", resultado[:5])
print(f"Tempo multithread: {tempo_decorrido}")

arq = open("08B.txt", "w")
for item in resultado:
    arq.write(f"{item}\n")
arq.close()
