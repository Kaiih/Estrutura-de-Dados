#1- Incluir uma nova letra na pilha (não imprimir nada)
#2- Excluir a letra do topo da pilha (ou em caso de pilha vazia, imprimir "Erro")
#3- Imprimir a letra do topo da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
#4- Imprimir todas as letras da pilha (preservar a pilha, ou em caso de pilha vazia imprimir "Vazio")
#5- Excluir todas as letras da pilha (não imprimir nada)


class Pilha:
    minhaPilha = None
    topo = None

    def __init__(self):
        self.minhaPilha = []
        self.topo = str
        
    def empilhar(self, valor):
        self.topo = valor
        self.minhaPilha.append(valor)
    
    def desempilhar(self):
        if len(self.minhaPilha) != 0:
            self.minhaPilha.pop()
            if len(self.minhaPilha) != 0:
                self.topo = self.minhaPilha[-1]
                print(self.topo)
            else:
                self.topo = None
                print(self.topo)
    
    def imprimirTopo(self):
        return self.topo
        
    def imprimirTudo(self):
        for elementos in self.minhaPilha[::-1]:
            print(elementos)
        
    def excluirTudo(self):
        while len(self.minhaPilha) != 0:
            self.minhaPilha.pop()
    
def main():
    
    p1 = Pilha()
    
    while True:
        #opcao = int(input("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: "))
        #print("\n1- Empilhar\n2– Desempilhar\n3- Sair\n\nOpção: ")
        print("")
        print("1- Empilhar")
        print("2– Desempilhar")
        print("3- Imprimir topo")
        print("4- Imprimir tudo")
        print("5- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            valor = str(input("Digite uma letra: "))
            p1.empilhar(valor)
            
        elif opcao == 2:
            p1.desempilhar()
            
        elif opcao == 3:
            print(p1.imprimirTopo())
            
        elif opcao == 4:
            p1.imprimirTudo()
            
        elif opcao == 6:
            p1.excluirTudo()
    
        else:
            break
    

if __name__ == "__main__":
    main()