#declaração de variáveis
nome = input("Informe seu nome: ").strip().title() #elimina os espaços antes e depois da variável #.stip elimina os espaços antes e depois do str e o .title mesmo que seja feito o registro do nome em caixa alta ou tudo minúsculo ele converte tudo para as iniciais maiúsculas e o resto minúsculo.
idade = int(input("Informe sua idade: ").strip())
altura = float(input("informe sua altura: ").strip().replace(",",".")) #.replace "substitui" ou faz com que o computador aceite a virgula caso ela seja digitada, pois no computador o que separa números decimais não é a vírgua mas sim o ponto.

#saida de dados
print(f"nome do usuário: {nome}. Tipo: {type(nome)}")
print(f"idade: {idade}. Tipo: {type(idade)}")
print(f"altura: {altura}. Tipo: {type(altura)}")
