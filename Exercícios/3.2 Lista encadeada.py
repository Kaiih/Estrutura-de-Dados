class No:

    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior=None

class Lista:

    def __init__(self):
        self.inicio = None
        self.fim = None
        
    def inserirInicio(self, dado):
        novoNo= No(dado)
        novoNo.proximo=self.inicio
        self.inicio=novoNo

    def removerInicio(self):
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

    def inserirFinal(self, dado):
        novoNo = No(dado)
        if self.inicio is None and self.fim is None:
            self.fim = novoNo
            self.inicio = self.fim
        else:
            self.fim.proximo=novoNo
            self.fim=novoNo
    
    def removerFinal(self):
        if self.inicio is None and self.fim is None:
            print("Erro")
            return
        inicio_memorizado=self.inicio
        while self.inicio.proximo.proximo is not None and self.inicio.proximo is not None:
            self.inicio=self.inicio.proximo
        self.inicio.proximo=None
        self.inicio=inicio_memorizado

    def imprimirTudo(self):
        if self.inicio is None:
            print("Vazio")
            return
        memoria = self.inicio
        while self.inicio is not None:
            print(self.inicio.dado, end=" ")
            self.inicio=self.inicio.proximo
        self.inicio = memoria
        
    def excluirTudo(self):
        while self.inicio is not None:
            self.removerInicio()
    
    def inserirPosicao(self,posicao, dado):
        novoNo=No(dado)
        if posicao == 0:
            novoNo.proximo=self.inicio
            self.inicio=novoNo
        else:
            inicio_memorizado=self.inicio
            for i in range(posicao-1):
                self.inicio=self.inicio.proximo
                if self.inicio.proximo is None:
                    break
            novoNo.proximo=self.inicio.proximo
            self.inicio.proximo=novoNo
                
            self.inicio=inicio_memorizado
    
    def removerPosicao(self, posicao):
        inicio_memorizado=self.inicio
        if posicao == 0:
            self.inicio = self.inicio.proximo
        for i in range(posicao-1):
            self.inicio=self.inicio.proximo
            if self.inicio.proximo is None:
                break
        self.inicio.proximo= self.inicio.proximo.proximo
    
    def imprimirPosicao(self,posicao):
        if self.inicio is None and self.fim is None:
            print("Vazio")
            return 
        inicio_memorizado=self.inicio
        
        for i in range(posicao):
            self.inicio=self.inicio.proximo
        print(self.inicio.dado)
        self.inicio=inicio_memorizado

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
            dado = input("Insira um dado no ínicio: ")
            L1.inserirInicio(dado)
        elif opcao == 2:
            L1.removerInicio()
        elif opcao == 3:
            dado = input("Insira um dado no final: ")
            L1.inserirFinal(dado)
        elif opcao == 4:
            L1.removerFinal()
        elif opcao == 5:
            L1.imprimirTudo()
        elif opcao == 6:
            L1.excluirTudo()
        elif opcao == 7:
            posicao=int(input("Digite a posição: "))
            dado=input("Digite o dado: ")
            L1.inserirPosicao(posicao, dado)
        elif opcao == 8:
            posicao=int(input("Digite a posição: "))
            L1.removerPosicao(posicao)
        elif opcao == 9:
            posicao=int(input("Digite a posição: "))
            L1.imprimirPosicao(posicao)
        else:
            break
    

if __name__ == "__main__":
    main()