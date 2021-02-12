import os
# https://docs.python.org/3.9/library/os.html

print("Sistema operacional:", os.name.upper())
print("\nNome do usuário:", os.getlogin())
print("\nVariáveis de ambiente:", os.environ)
print("\nDisco default:", os.environ['HOMEDRIVE'])
print("\nDiretório do usuário:", os.environ['HOMEPATH'])
print("\nDiretório corrente:", os.getcwd())
print("\nPID do processo:", os.getpid())
