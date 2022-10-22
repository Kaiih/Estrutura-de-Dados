#1- Criar uma lista com números de 0 ate 10
#2- Imprimir a lista criada
#3- Imprimir o primeiro elemento
#4- Imprimir o menor elemento
#5- Imprimir o último elemento
#6- Imprimir o maior elemento
#7- Imprimir a quantidade de elementos da lista
#8- Imprimir apenas os números ímpares
#9- Imprimir a soma de dos números ímpares
#10- Imprimir a lista invertida
#11- Remover o último e primeiro elemento da lista e imprimir a lista

def main():
    
    lista = []
    impar = []
    
    for i in range(0, 11):
        lista.append(i)
        
    while True:
        print("")
        print("1- Imprimir a lista criada")
        print("2– Imprimir o primeiro elemento")
        print("3- Imprimir o menor elemento")
        print("4- Imprimir o último elemento")
        print("5- Imprimir o maior elemento")
        print("6- Imprimir a quantidade de elementos da lista")
        print("7- Imprimir apenas os números ímpares")
        print("8- Imprimir a soma de dos números ímpares")
        print("9- Imprimir a lista invertida")
        print("10-  Remover o último e primeiro elemento da lista e imprimir a lista")
        print("11- Sair")
        print("")
        print("Opção: ")
        opcao = int(input())
        
        if opcao == 1:
            print(lista)
            break
            
        elif opcao == 2:
            print(lista[0])
            break
            
        elif opcao == 3:
            print(min(lista))
            break
            
        elif opcao == 4:
            print(lista[-1])
            break
            
        elif opcao == 5:
            print(max(lista))
            break
            
        elif opcao == 6:
            print(len(lista))
            break
            
        elif opcao == 7:
            for i in (lista):
                if i % 2 != 0:
                    print(i, end=" ")
        
        elif opcao == 8:
            for i in (lista):
                if i % 2 != 0:
                    impar.append(i)
            print("Soma dos ímpares: ")
            print(sum(impar))
        
        elif opcao == 9:
            print(lista[::-1])
        
        elif opcao == 10:
            lista.remove(0)
            lista.remove(lista[-1])
            print(lista)
            
        else:
            break

if __name__ == "__main__":
    main()