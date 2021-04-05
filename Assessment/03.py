import os


def listar_arquivos(pasta=os.getcwd()):
    lista_arquivos = []
    if pasta:
        conteudo_pasta = os.listdir(pasta)
        for item in conteudo_pasta:
            if os.path.isfile(item):
                tamanho = os.stat(item).st_size
                arq_info = [item, tamanho]
                lista_arquivos.append(arq_info)
            arq_info = []
        filtro_tamanho = lambda arquivo: arquivo[1]
        lista_arquivos.sort(key=filtro_tamanho, reverse=True)
        return lista_arquivos
    else:
        pasta = os.getcwd()
        conteudo_pasta = os.listdir(pasta)
        for item in conteudo_pasta:
            if os.path.isfile(item):
                tamanho = os.stat(item).st_size
                arq_info = [item, tamanho]
                lista_arquivos.append(arq_info)
            arq_info = []
        filtro_tamanho = lambda arquivo: arquivo[1]
        lista_arquivos.sort(key=filtro_tamanho, reverse=True)
        return lista_arquivos


def obter_diretorio_usuario():
    diretorio_usuario = os.environ['HOMEPATH']
    print(diretorio_usuario)
    return diretorio_usuario

def exibir_resultado():
    pasta = input("Informe a pasta a ser verificada ou [ENTER] para pasta atual:")
    result_arquivos = listar_arquivos(pasta)
    if len(result_arquivos) == 0:
        print("Não existem arquivos na pasta especificada.")
    else:
        print(f"Arquivos na pasta {pasta}:")
        for arquivo in result_arquivos:
            print(f"NOME: {arquivo[0]} - TAMANHO EM DISCO: {arquivo[1]} kb")


def criar_arquivo_texto(lista):
    arquivo = open("questao_03.txt", "w", encoding="UTF-8")
    arquivo.write(f"DIRETÓRIO DO USUÁRIO: {obter_diretorio_usuario()}\n\n")
    for item in lista:
        arquivo.write(f"NOME: {item[0]} - TAMANHO EM DISCO: {item[1]} kb\n")
    arquivo.close()


criar_arquivo_texto(listar_arquivos())
# exibir_resultado()
