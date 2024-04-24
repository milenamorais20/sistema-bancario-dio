menu = '''
    MENU
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=> '''

saldo = 0
extrato = ""
valor_limite_saque = 500
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        
        valor_deposito = float(input("Insira o valor que deseja DEPOSITAR: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito}\n"
            print("Depósito realizado com sucesso")
        else:
            print("Operação inválida. Insira valor positivo")
            
    elif opcao == 's':
        
        saques_realizados = 0
        valor_saque = float(input("Insira o valor que deseja SACAR: "))
        
        if valor_saque > saldo:
            print("Operação inválida. Você não tem saldo suficiente.")
        elif numero_saques >= LIMITE_SAQUE:
            print("Operação inválida. Você excedeu o limite de saques diários. Tente amanhã.")
        elif valor_saque > valor_limite_saque:
            print("Operação inválida. O valor limite de saque é 500 reais. Tente novamente.")
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque}\n"
            numero_saques += 1
            print("Saque realizado com sucesso")
            
    elif opcao == 'e':
        print("MENU".center(20, "="))
        print(extrato if not extrato else extrato)
        print(f"Saldo:{saldo}")
        print("="*20)
        
    elif opcao == 'q':
        break
    
    else:
        print("Insira uma opção válida")