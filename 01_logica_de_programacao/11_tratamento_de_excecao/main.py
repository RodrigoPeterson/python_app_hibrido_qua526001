# tratamento de exceção
try:
    # entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())
    altura = float(input("Informe sua altura: ").strip().replace(",","."))

    # saida de dados
    print(f"Nome: {nome}")
    print(f"idade: {idade}")
    print(f"altura: {altura}")
except:
    print("infelizmente o programa não pode ser executado.")
