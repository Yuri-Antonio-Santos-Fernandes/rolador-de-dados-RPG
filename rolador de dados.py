import random
import os

def limpar():
    os.system('cls')


while True:
    print("selecione um dado: ")
    print("D4\nD6\nD8\nD10\nD12\nD20\nD100\npara sair digite -sair-\npara limpar a tela digite -limpar-\n---------------------------------")

    tipo = input().strip().upper()

    if tipo == "D4":
        print("valor rodado: ",random.randint(1,4),"\n--------------------------\n")

    elif tipo == "D6":
        print("valor rodado: ",random.randint(1,6),"\n--------------------------\n")
    
    elif tipo == "D8":
        print("valor rodado: ",random.randint(1,8),"\n--------------------------\n")
    
    elif tipo == "D10":
        print("valor rodado: ",random.randint(1,10),"\n-------------------------\n")
    
    elif tipo == "D12":
        print("valor rodado: ",random.randint(1,12),"\n-------------------------\n")
    
    elif tipo == "D20":
        print("valor rodado: ",random.randint(1,20),"\n-------------------------\n")
    
    elif tipo == "D100":
        print("valor rodado: ",random.randint(1,100),"\n------------------------\n")

    elif tipo == "sair":
        print("encerrando programa...")
        break

    elif tipo == "LIMPAR":
        limpar()
