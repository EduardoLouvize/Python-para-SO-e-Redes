import time
import multiprocessing


def fatorial(n):
    fat = n
    for i in range(n - 1, 1, -1):
        fat = fat * i
    return fat


def fatorial_lista(lista, result_parcial, id):
    lista_retorno = []
    for item in lista:
        resultado = fatorial(item)
        lista_retorno.append(resultado)
    result_parcial[id] = lista_retorno


if __name__ == "__main__":
    quantidade_numeros = 5000
    hora_inicio = time.time()

    lista = []
    for i in range(quantidade_numeros):
        lista.append(i)

    num_processos = 4
    hora_inicio = time.time()

    with multiprocessing.Manager() as manager:
        # Cria lista na memória do SP
        lista = manager.list(lista)
        # Vetor para salvar a soma parcial de cada thread
        result_parcial = manager.list(num_processos * [0])

        lista_processos = []
        for i in range(num_processos):
            ini = i * int(quantidade_numeros / num_processos)
            fim = (i + 1) * int(quantidade_numeros / num_processos)
            p = multiprocessing.Process(target=fatorial_lista, args=(lista[ini:fim],result_parcial, i))
            p.start()
            lista_processos.append(p)

        for p in lista_processos:
            p.join()


        resultado = [x for l in result_parcial for x in l]

        hora_final = time.time()
        tempo_decorrido = hora_final - hora_inicio


        print("Primeiros resultados:", resultado[:5])
        print(f"Tempo multiprocess: {tempo_decorrido}")

        arq = open("08C.txt", "w")
        for item in resultado:
            arq.write(f"{item}\n")
        arq.close()
