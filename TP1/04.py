# Que função do módulo ‘os’ de Python é usada para obter o caminho absoluto de um diretório com caminho relativo?
# Dê um exemplo.

# A função é os.path.abspath()

import os

# Diretório atual
print(os.path.abspath("."))
# Diretório "pai"
print(os.path.abspath(".."))
# Um diretório dentro do diretório atual
print(os.path.abspath("diretorio_teste"))
