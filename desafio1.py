menu = """
----------------------
        MENU        
----------------------
[d] DEPOSITAR
[s] SAQUE
[e] EXTRADO
[q] SAIR        
----------------------
"""
LIMITE_SAQUE = 3
saldo=0
saque=500
qde_saque = 0

extrato_deposito=[]
extrato_saque=[]

print(menu)

while True:
    opcao = input("DIGITE UM OPÇÃO DESEJADO DO MENU: ")

    if opcao == "d" :
        valor = float(input("DIGITE O VALOR DO DEPOSITO: "))
        
        if valor>0:
            print(f"DEPOSITO DE R$ {valor} REALIZADO COM SUCESSO!\n")
            saldo+=valor
            extrato_deposito.append(valor)

            print(f"SEU SALDO ATUAL É R$ {saldo:.2F}\n\n")
            
        else:
            print("VALOR INCORRETO\n")
        
    elif opcao == "s":
        valor_saque = float(input("DIGITE O VALOR PARA O SAQUE: "))
        
        excedeu_saldo= valor_saque>saque
        excedeu_limite =  valor_saque>saldo
        excedeu_saque = qde_saque > LIMITE_SAQUE

        if excedeu_saldo:
            print("SAQUE NÃO PODE SER REALIZADO, VALOR DESEJADO MAIOR QUE O PERMITIDO\n")
        elif valor_saque<=0:
            print("NÃO FOI POSSIVEL REALIZAR O SEU SAQUE (VALOR < OU IGUAL A 0)\n")
        elif excedeu_limite:
            print("O VALOR SOLICITADO E MAIOR QUE O SALDO EM CONTA\n")
        else:
            if excedeu_saque:
                print("VOCÊ EXCEDEU SEU LIMITE DE SAQUE DIÁRIO\n")
            else:
                extrato_saque.append(valor_saque)
                saldo-=valor_saque
                qde_saque+=1
                print("SAQUE REALIZADO COM SUCESSO\n")
                print(f"SEU SALDO ATUAL É R$ {saldo:.2F}\n\n")
    elif opcao == "e":
        print("\n-------------------EXTRATO-----------------")
        print("DEPOSITOS" if extrato_deposito else "NÃO HOUVE DEPOSITO NO MOMENTO")
        for entrada in extrato_deposito:
            print(f"R$ {entrada:.2F}")

        print("\nSAQUES" if extrato_saque else "NÃO HOUVE SAQUE NO MOMENTO")
        for saidas in extrato_saque:
            print(f"R$ {saidas:.2F}")

        print(f"SEU SALDO ATUAL É R$ {saldo:.2F}")
        print("\n---------------------FIM-------------------")
    elif opcao == "q":
        print("VOCÊ SAIU DO SISTEMA, OBRIGADO VOLTE SEMPRE")
        print()
        break
    else:
        print("OPERAÇÃO INVÁLIDA, SELECIONE UMA OPÇÃO NO MENU ANTERIOR.\n")
    

        
