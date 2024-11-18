class ListaAcose():
    def __init__(self):
        self.contatos ={}
    def adicionar(self, nome, numero):
        nome = input("Insira o seu nome: ")
        numero = input("Insira o numero: ")
        self.nome = nome
        self.numero = numero
        self.contatos[nome] = numero     
    def mostrar_lista(self):
        for nome, numero in self.contatos.items():
                    print(f'{nome}: {numero}')
    def remover(self, nome):
        nome = input("Insira o nome do contato que deseja exluir: ")
        self.nome = nome
        if self.nome in self.contatos: 
            del self.contatos[nome]
            print(f'Contato {nome} excluido.')
        else:
            print(f'O contato{nome} não foi encontrado.')
    def buscar(self, nome):
        nome = input("Insira o nome que deseja buscar: ")
        self. nome = nome
        if self.nome in self.contatos:
            print(f'{self.nome}: {self.contatos[nome]}')
        else:
            print(f'O contato {nome} não foi encontrado.')
    def menu(self):
        while True:

            print("\n1. Adicionar/Atualizar Contato \n2. Visualizar Contatos \n3. Buscar Contato \n4. Excluir Contato \n5. Sair \n")

            print("Escolha uma opção (1-6): \n")

            pergunta = input("Escolha uma opção de 1 a 5: ")

            if pergunta == "1":
                contatos.adicionar('','')


            elif pergunta == "2":
                contatos.mostrar_lista()

            elif pergunta == "3":
                contatos.buscar('')

            elif pergunta == "4":
                contatos.remover('')


            elif pergunta == "5":
                print("Saindo do programa")
                break

            else:
                print("Opção invalida, escolha de um 1-5")


contatos = ListaAcose()
contatos.menu()
