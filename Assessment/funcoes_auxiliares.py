import os
import psutil


def listar_arquivos(pasta=os.getcwd()):
    lista_arquivos = []
    if pasta == "":
        pasta = os.getcwd()
        conteudo_pasta = os.listdir(pasta)
        for item in conteudo_pasta:
            if os.path.isfile(item):
                lista_arquivos.append(item)
        return lista_arquivos
    elif pasta:
        conteudo_pasta = os.listdir(pasta)
        for item in conteudo_pasta:
            if os.path.isfile(item):
                lista_arquivos.append(item)
        return lista_arquivos
    else:
        pasta = os.getcwd()
        conteudo_pasta = os.listdir(pasta)
        for item in conteudo_pasta:
            if os.path.isfile(item):
                lista_arquivos.append(item)
        return lista_arquivos


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    livre = round(mem.free / (1024 * 1024 * 1024), 2)
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    uso_memoria = f"Uso de Memória: {livre}GB usados (Total: {total}GB)"

    return uso_memoria


if __name__ == "__main__":
    print(listar_arquivos(""))
