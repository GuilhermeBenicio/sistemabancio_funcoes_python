usuarios = []
contas = []
agencia = "0001"
numero_conta = 1

def criarUsuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if(usuario['cpf'] == cpf):
            print()
            print('Conta não criada! CPF já cadastrado!!')
            return
    
    usuarios.append({
        'nome': nome, 
        'data_nascimento': data_nascimento, 
        'cpf': cpf, 
        'endereco': endereco})
    
    criarConta(nome)
    
def criarConta(nome):
        
        global numero_conta

        contas.append({
        'nome': nome, 
        'agencia': agencia,
        'numero_conta': numero_conta })

        print()
        print('Conta criada com sucesso!')
        numero_conta += 1

def listarContas():
    if not contas: 
        print("Não há contas para serem exibidas!!")
    else:
        print("CONTAS CRIADAS\n")
        for conta in contas:
            print(f"""
          Nome: {conta['nome']}
          Agência: {conta['agencia']}
          Número da Conta: {conta['numero_conta']}
          
          ========================================================================================
          """)

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")

            else:
                print("Operação falhou! O valor informado é inválido")

            return saldo, extrato, numero_saques

def deposito(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def extratoConta(saldo, /, *, extrato):
    print("\n====================== EXTRATO ====================== ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================================")

def menu():
    menu = """

    Digite a opção que você deseja:

    [c] Criar Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar Contas
    [q] Sair

    =>  """ 

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            valor = float(input("Digite aqui o valor do seu depósito: "))         
            saldo, extrato = deposito(valor, saldo, extrato)
        
        elif opcao == "s":
            valor = float(input("Digite aqui o valor do seu saque: "))
            saldo, extrato, numero_saques = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

        elif opcao == "e":
           extratoConta(saldo, extrato = extrato)
        
        elif opcao == "l":
            listarContas()
        
        elif opcao == "c":
            nome = input("Digite o seu nome: ")
            data_nascimento = input("Digite a sua data de nascimento: ")
            cpf = input("Digite o seu CPF (somente número): ")
            endereco = input("Digite o seu endereço: ")
            criarUsuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "q":
            break

        else:
            print("Operação inválida! Por favor, selecione novamente a operação desejada.")

menu()
