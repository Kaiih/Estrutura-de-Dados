class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
    
class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def enfileirar(self, dado):
        novoNo = No(dado)
        if self.inicio is None and self.fim is None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            self.fim=novoNo
    
    def desenfileirar(self):
        if self.inicio is None:
            print("Erro")
        else:
            auxiliarDado=self.inicio.dado
            auxiliarReferencia=self.inicio.proximo
            if auxiliarReferencia is None:
                self.inicio=None
                self.fim=None
            else:
                self.inicio=auxiliarReferencia
    
    def imprimirInicio(self):
        if self.inicio is None:
            print("Vazio")
        else:
            print(self.inicio.dado)
    
    def imprimirFim(self):
        if self.inicio is None:
            print("Vazio")
        else:
            print(self.fim.dado)
    
    def imprimirTudo(self):
        aux=self.inicio
        while self.inicio is not None:
            print(self.inicio.dado,end=" ")
            self.inicio=self.inicio.proximo
        self.inicio=aux
        print("\n")
    
    def excluirTudo(self):
        while self.inicio is not None:
            self.inicio=self.inicio.proxima
            if self.inicio is None:
                self.inicio = None
                self.fim=None
    
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
            f1.enfileirar(input("Digite uma letra:"))
        
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