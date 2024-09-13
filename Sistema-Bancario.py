def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(menu)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    
    while True:
        opcao = exibir_menu()
        
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
            
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
            
        elif opcao == "q":
            print("Saindo do sistema...")
            break
        
        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")
