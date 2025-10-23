# loop
# O tratamento de exceção pode ficar dentro de um loo while
# O loop é diferente
while True: 
    try:
        # menu 
        print("1 - Soma")
        print("2 - subtração")
        print("3 - multiplicação")
        print("4 - Divisão")
        print("5 - Sair do programa")
        opcao = input("Informe a opção desejada: ").strip()
        if opcao != "5":
            n1 = int(input("Informe o primeiro número: ").strip())
            n2 = int(input("Informe o segundo número: ").strip())
            match opcao:
                case "1":
                    print("Você selecionou a soma")
                    result = n1+n2
                    print(f"O resultado da soma é: {result}")
                    continue
                case "2":
                    print("Você selecionou a subtração")
                    result = n1-n2
                    print(f"O resultado da subtração é: {result}")
                    continue
                case "3":
                    print("Você selecionou a multiplicação")
                    result = n1*n2
                    print(f"O resultado da multiplicação é: {result}")
                    continue
                case "4":
                    print("Você selecionou a divisão")
                    result = n1/n2
                    print(f"O resultado da divisão é: {result}")
                    continue
                case "5":
                    print("Saindo...")
                    continue
                case _:
                    print("Opção inválida! ")
                    continue
        else:
            print("Programa encerrado! ")
        break
        # O break a lógica dele é quando o usuário quiser encerrar 
    except:
        print("Valores invalidos.")

# Lembrar de por um continue antes dos cases, isso faz com que ele volte para o menu