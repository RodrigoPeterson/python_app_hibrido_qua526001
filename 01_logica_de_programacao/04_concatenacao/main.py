#declaração de variáveis
nome = "Rodrigo Campelo"
idade = 21

#concatenação de valores
#Forma 1 de executar print
print ("Boa tarde, meu nome é " + nome + " e tenho " + str(idade) + " anos.")
#forma 2
print ("Boa tarde, meu nome é", nome,"e tenho", idade, "anos.")
#forma 3
print("Boa tarde, meu nome é {} e tenho {} anos." .format(nome, idade))
#forma 4 (Forma mais usada) f-string
print(f"Boa tarde, meu nome é {nome} e tenho {idade} anos.")
