class Lista:

    def __init__(self):
        self.minhaLista = []
        self.inicio = None
        self.fim = None
        
    def inserirInicio(self,dado):
        if len(self.minhaLista) == 0:
            self.fim=dado
        self.minhaLista.insert(0,dado)
        self.inicio=dado
        
    def removerInicio(self):
        if len(self.minhaLista) == 0:
            print("Erro")
        else:
            self.minhaLista.pop(0)
                
    def inserirFinal(self,dado):
        if len(self.minhaLista) == 0:
            self.inicio=dado
        self.minhaLista.append(dado)
        self.fim=dado
    
    def removerFinal(self):
        if self.minhaLista:
            self.minhaLista.pop(-1)
            if len(self.minhaLista) == 0:
                self.fim=None
                self.inicio=None
            else:
                self.fim=self.minhaLista[len(self.minhaLista)-1]
        else:
            print("Erro")
    
    def imprimirTudo(self):
        if len(self.minhaLista) == 0:
            print("Vazio")
        else:
            for elemento in self.minhaLista:
                print(elemento,end=" ")
        
    def excluirTudo(self):
        if len(self.minhaLista) == 0:
            print("Vazio")
        else:
            self.minhaLista.clear()
        
    def inserirPosicao(self):
        indice=int(input("Digite um indice: "))
        dado=str(input("Digite uma letra para inserir na lista: "))
        self.minhaLista.insert(indice,dado)
    
    def removerPosicao(self):
        indice = int(input("Digite o indice: "))
        self.minhaLista.pop(indice)

    
    def imprimirPosicao(self):
        indice = int(input("Digite o indice: "))
        print(self.minhaLista[indice])
    
def main():
    L1 = Lista()
    
    while True:
        print("")
        print("1- Inserir Inicio")
        print("2– Remover Inicio")
        print("3- Inserir Final")
        print("4- Remover Final")
        print("5- Imprimir Tudo")
        print("6- Excluir Tudo")
        print("7- Inserir na Posicao")
        print("8- Remover da Posicao")
        print("9- Imprimir da Posicao")
        print("10- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        if opcao == 1:
            dado=input("Digite um dado para inserir no início da lista: ")
            L1.inserirInicio(dado)
            
        elif opcao == 2:
            L1.removerInicio()
            
        elif opcao == 3:
            dado=input("Digite um dado para inserir no fim da lista: ")
            L1.inserirFinal(dado)
            
        elif opcao == 4:
            L1.removerFinal()
            
        elif opcao == 5:
            L1.imprimirTudo()
            
        elif opcao == 6:
            L1.excluirTudo()
            
        elif opcao == 7:
            L1.inserirPosicao()
            
        elif opcao == 8:
            L1.removerPosicao()
        
        elif opcao == 9:
            L1.imprimirPosicao()
            
        else:
            break
    

if __name__ == "__main__":
    main()