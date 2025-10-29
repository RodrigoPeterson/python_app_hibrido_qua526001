import os

# delclaração de lista
nomes = []

# Limpeza de console
os.system("cls")

# Laço de loop
while True:
    # menu
    print("1 - Inserir novo nome")
    print("2 - Exibir lista de nomes")
    print("3 - Excluir nome na lista")
    print("4 - Sair do Programa")
    opcao = input("Informe a opção desejada: ").strip()

    
    match opcao:
        case "1":
            novo_nome = input("Informe o novo nome: ").strip().title()
            nomes.append(novo_nome)
            os.system("cls")
            print(f"Novo nome inserido com sucesso!")
            continue
        case "2":
            os.system("cls")
            print("\nLista de nomes: \n")
            for i in range(len(nomes)):
                print(f"{i} - {nomes[i]}")
            print(f"\n{'-'*40}\n")
            continue
        case "3":
            os.system("cls")
            try:
                posicao = int(input("Informe o nome a ser excuido: ").strip())
                if posicao >=0 and posicao < len(nomes):
                    del(nomes[posicao])
                    print("Nome excluído com sucesso.")
                else:
                    print("Posição enexistente.")
                    
            except Exception as e:
                print(f"Posição invalida {e}.")
            continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("opção invalida.")
            continue