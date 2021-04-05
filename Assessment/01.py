import psutil

def processo_pid():
    lista_pids = psutil.pids()
    lista_result = []
    for pid in lista_pids:
        try:
            processo = psutil.Process(pid)
            nome_processo = processo.name()
            msg_print = f"PID:{pid} - NOME DO PROCESSO:{nome_processo}"
            lista_result.append(msg_print)
        except:
            pass
    return lista_result

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    utilizada = round(mem.used / (1024 * 1024 * 1024), 2)
    percentual = round(mem.percent, 2)
    uso_memoria = f"Uso de Memória: {utilizada}GB usados ({percentual}%):"

    return uso_memoria


def mostra_uso_cpu():
    capacidade = psutil.cpu_percent(interval=0)
    uso_cpu = f"Uso de CPU: {capacidade:.2f}% usados"
    return uso_cpu

def imprime_informacoes():
    print("INFO PIDS")
    for item in processo_pid():
        print(item)

    print("\n")
    print(mostra_uso_memoria())
    print("\n")
    print(mostra_uso_cpu())


imprime_informacoes()
