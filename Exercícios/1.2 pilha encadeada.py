# 1- Incluir uma nova letra na pilha (não imprimir nada)
# 2- Excluir a letra do topo da pilha (ou em caso de pilha vazia, imprimir "Erro")
# 3- Imprimir a letra do topo da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
# 4- Imprimir todas as letras da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
# 5- Excluir todas as letras da pilha (não imprimir nada)


class No:

    def __init__(self, dado):
        self.dado = dado
        self.anterior = None


class Pilha:

    def __init__(self):
        self.minhaPilha = None
        self.topo = None


    def empilhar(self, dado):
        self.topo = dado
        novoNo = No(dado)
        if self.minhaPilha is None:
            self.minhaPilha = novoNo
        else:
            novoNo.anterior = self.minhaPilha
            self.minhaPilha = novoNo

    def desempilhar(self):
        if self.minhaPilha is None:
            print("Erro")
        else:
            self.minhaPilha = self.minhaPilha.anterior
            if self.minhaPilha is None:
                self.topo = None
            else:
                self.topo = self.minhaPilha.dado

    def imprimirTopo(self):
        if self.topo is None:
            print("Vazio")
        else:
            print("Dado do topo: {}" .format(self.topo))

    def imprimirTudo(self):
        if self.minhaPilha is None:
            print("Vazio")
        else:
            auxiliar = Pilha()
            auxiliar = self.minhaPilha
            while auxiliar is not None:
                print(auxiliar.dado)
                auxiliar = auxiliar.anterior

    def excluirTudo(self):
        if self.minhaPilha is None:
            print("vazia ")
        else:
            while self.minhaPilha is not None:
                self.minhaPilha = self.minhaPilha.anterior
            if self.minhaPilha is None:
                self.topo = None

def main():
    p1 = Pilha()

    while True:
        # opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        # print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2– Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Excluir tudo")
        print("5- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            p1.empilhar(input("Digite uma letra: "))
    
        elif opcao == 2:
            p1.desempilhar()
        elif opcao == 3:
           p1.imprimirTopo()
        elif opcao == 4:
            p1.imprimirTudo()
        elif opcao == 5:
            p1.excluirTudo()
        else:
            break


if __name__ == "__main__":
    main()
