import os
# Sobre variáveis de ambiente, responda:
# a. O que são?
# São valores que afetam o comportamento dos processos executados em um computador.
# Variáveis de ambiente fornecem parâmetros ou informações necessários para o bom funcionamento dos processos,
# por exemmlo: o local da pasta "TEMP", o nome do usuário, a data atual, etc.

# b. Como elas podem ser obtidas pelo módulo ‘os’ de Python?
print("Como elas podem ser obtidas pelo módulo ‘os’ de Python?")
variaveis_sistema_dic = os.environ
for item in variaveis_sistema_dic:
    print(f"{item}: {os.environ[item]}")
# c. Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?
print("\nComo pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?")
print(os.environ['HOMEDRIVE'])
