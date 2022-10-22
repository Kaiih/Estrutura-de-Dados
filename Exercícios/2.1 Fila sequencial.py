class Fila:

    def __init__(self):
        self.minhaFila = []
        self.inicio = str
        self.fim = str

    def enfileirar(self, dado):
        if len(self.minhaFila) == 0:
            self.inicio = dado
        self.minhaFila.append(dado)
        self.fim = dado

    def desenfileirar(self):
        if len(self.minhaFila) != 0:
            self.minhaFila.pop(0)
            if len(self.minhaFila) != 0:
                self.inicio = self.minhaFila[0]
            else:
                self.inicio = None
                self.fim = None
        else:
            print("Erro")

    def imprimirInicio(self):
        if len(self.minhaFila) == 0:
            print ("Vazio")
        else:
            print(self.inicio)

    def imprimirFim(self):
        if len(self.minhaFila) == 0:
            print ("Vazio")
        else:
            print(self.fim)

    def imprimirTudo(self):
        if len(self.minhaFila) == 0:
            print ("Vazio")
        else:
            print(self.minhaFila)

    def excluirTudo(self):
        
        if len(self.minhaFila) == 0:
            print("Erro")
        
        else:
            while len(self.minhaFila) != 0:
                self.minhaFila.pop(0)
                if len(self.minhaFila) == 0:
                    self.inicio = None
                    self.fim = None
                    
def main():
    f1 = Fila()

    while True:
        print("")
        print("1- Enfileirar")
        print("2– Desenfileirar")
        print("3- Imprimir inicio")
        print("4- Imprimir fim")
        print("5- Imprimir tudo")
        print("6- Excluir tudo")
        print("7- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            dado = input("Digite um dado pra enfileirar: ")
            f1.enfileirar(dado)

        elif opcao == 2:
            f1.desenfileirar()

        elif opcao == 3:
            f1.imprimirInicio()

        elif opcao == 4:
            f1.imprimirFim()

        elif opcao == 5:
            f1.imprimirTudo()

        elif opcao == 6:
            f1.excluirTudo()

        else:
            break


if __name__ == "__main__":
    main()