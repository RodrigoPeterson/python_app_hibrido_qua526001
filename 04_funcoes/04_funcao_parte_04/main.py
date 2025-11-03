# biblioteca
import os
import math
# limpa console
def limpar():
    os.system("cls")

# funções de cálculo 
def quadrado(l):
    return l**2

def retangulo(b, h):
    return b*h

def triangulo(b, h):
    return (b*h)/2

def hipotenusa(b, h):
    return math.sqrt((b**2)+(h**2))
# TODO: Crie uma nova função para calcular a hipotenusa do triângulo-retângulo.
# TODO: para calcular a raiz quadrada, importe a biblioteca "math" e use a função "sqrt()".


# algoritmo principal
limpar()

while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular Hipôtenusa")
    print("5 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    limpar()

    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            resultado = quadrado(l)
            limpar()
            print(f"Área do quadrado é {resultado}")
            continue
        case "2":
            b = float(input("Informe a base do retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do retângulo: ").strip().replace(",","."))
            resultado = retangulo(b, h)
            limpar()
            print (f"Área do retângulo: {resultado}")
            continue
        case "3":
            b = float(input("Informe a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do triângulo: ").strip().replace(",","."))
            resultado = triangulo(b, h)
            limpar()
            print (f"Área do triângulo é: {resultado}")
            continue
        case "4":
            b = float(input("Informe a base: ").strip().replace(",","."))
            h = float(input("Informe a altura: ").strip().replace(",","."))
            resultado = hipotenusa(b, h)
            limpar()
            print (f"O resultado da hipotenusa é: {resultado}")
            continue
        case "5":
            print("Programa encerrado")
            break
        case _:
            print("Opção inválida.")
            continue