
def criar_lista(texto):
    # texto = texto.replace(" ", "")
    lista_valores = texto.split(" ")
    lista_final = []
    for item in lista_valores:
        lista_final.append(int(item))
    return lista_final


def comparar_listas(lista_1, lista_2):
    # tamanho_lista_1 = len(lista_1)
    # tamanho_lista_2 = len(lista_2)
    if len(lista_1) > len(lista_2):
        for i in range(0, (len(lista_1)-len(lista_2))):
            lista_2.append(0)
    elif len(lista_2) > len(lista_1):
        for i in range(0, (len(lista_2)-len(lista_1))):
            lista_1.append(0)
    return lista_1, lista_2


def somar_listas(lista_1, lista_2):
    lista_resultado = []
    if len(lista_1) == len(lista_2):
        for i in range(len(lista_1)):
            item_lista = lista_1[i] + lista_2[i]
            lista_resultado.append(item_lista)
    else:
        lista_resultado.append("Número de itens das listas é diferente.")
    return lista_resultado


arquivo_1 = open("questao_05a.txt", "r", encoding="UTF-8")
texto_1 = arquivo_1.read()
lista_1 = criar_lista(texto_1)

arquivo_2 = open("questao_05b.txt", "r", encoding="UTF-8")
texto_2 = arquivo_2.read()
lista_2 = criar_lista(texto_2)

resulatado_final = somar_listas(comparar_listas(lista_1, lista_2)[0], comparar_listas(lista_1, lista_2)[1])
print(resulatado_final)
