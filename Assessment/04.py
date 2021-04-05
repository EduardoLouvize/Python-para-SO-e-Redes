arquivo = open("questao_04.txt", "r", encoding="UTF-8")
texto = arquivo.read().splitlines()
arquivo.close()
for i in range(len(texto)-1, -1, -1):
    texto_invertido = texto[i][::-1]
    print(texto_invertido)
