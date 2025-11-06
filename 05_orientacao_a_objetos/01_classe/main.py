# biblioteca
import os

# classe
class Pessoa:
    # atributos
    nome = "Rodrigo Campelo"
    idade = 21
    email = "rodrigo@gmail.com"

    # método = ação
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")

if __name__ == "__main__":
    # instanciar a classe (cria novo objeto)
    usuario = Pessoa()

    os.system("cls" if os.name == "nt" else "clear")

    # saída de dados
    usuario.exibir_dados()