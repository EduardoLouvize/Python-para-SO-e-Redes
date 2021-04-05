arq1 = open("08A.txt", "r")
arq1_linhas = arq1.read().splitlines()

arq2 = open("08B.txt", "r")
arq2_linhas = arq2.read().splitlines()

arq3 = open("08C.txt", "r")
arq3_linhas = arq3.read().splitlines()

if (len(arq1_linhas) != len(arq2_linhas)) and (len(arq1_linhas) != len(arq3_linhas)):
    print(f"arq_1 tem {len(arq1_linhas)} linhas")
    print(f"arq_2 tem {len(arq2_linhas)} linhas")
    print(f"arq_3 tem {len(arq3_linhas)} linhas")
else:
    for i in range(len(arq1_linhas)):
        print(i, end=" ")
        if (arq1_linhas[i] == arq2_linhas[i]) and (arq1_linhas[i] == arq3_linhas[i]):
            print("passou")
        else:
            print(f"***linha {i} diferente***")
            print("*************************************************************************************************************************")
            break
