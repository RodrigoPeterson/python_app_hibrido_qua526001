import os

usuario = {
    'nome': "Rodrigo Peterson",
    'nascimento': "08/08/2004",
    'email': "rodrigo@gmail.com",
    'telefone': "0827384793",
    'endereço': "QI"

}

os.system("cls")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")
