menu = """
 [1] Deposito
 [2] Saque
 [3] Extrato
 [4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    
    if opcao == "1":
        valor = float(input("Infome o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é Invalido.")
    
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excendeu_saldo = valor > saldo

        excendeu_limite = valor > limite

        excendeu_saques = numero_saque  >= LIMITE_SAQUES

        if excendeu_saldo:
            print("Operação falhou! você não tem saldo suficiente.")

        elif excendeu_limite:
            print("Operação falhou!o valor de saque excende o limite.")

        elif excendeu_saques:
            print("Operação falhou!o Número máximo de saques excendido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque +=1

        else:
            print("Operação falhou! o valor Informado é inválido.")

    
    elif opcao == "3":
        print("\n################ EXTRATO ################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("###########################################")
    
    elif opcao == "4":
        break

    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada.")
