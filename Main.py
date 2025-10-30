from datetime import datetime

# Lista de usuários cadastrados
usuarios = []

# Lista de contas bancárias
contas = []

# Cadastro de novo usuário
def criar_usuario():
    cpf = input("CPF (somente números): ")
    if any(u['cpf'] == cpf for u in usuarios):
        print("CPF já cadastrado.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (logradouro, número - cidade/UF): ")

    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'nascimento': nascimento,
        'endereco': endereco
    })
    print("Usuário criado com sucesso.")

# Criação de conta vinculada a um usuário existente
def criar_conta():
    cpf = input("CPF do titular da conta: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)

    if not usuario:
        print("Usuário não encontrado.")
        return

    numero_conta = len(contas) + 1
    conta = {
        'agencia': '0001',
        'numero': numero_conta,
        'usuario': usuario,
        'saldo': 0.0,
        'extrato': [],
        'limite': 500.0,
        'numero_saques': 0,
        'limite_saques': 3
    }
    contas.append(conta)
    print(f"Conta {numero_conta} criada para {usuario['nome']}.")

# Exibe todas as contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {conta['usuario']['nome']}")

# Realiza depósito (argumentos por posição)
def deposito(saldo, valor, extrato, /):
    if valor <= 0:
        print("Valor inválido para depósito.")
    else:
        saldo += valor
        extrato.append((datetime.now(), f"Depósito: +R${valor:.2f}"))
        print("Depósito realizado.")
    return saldo, extrato

# Realiza saque (argumentos por nome)
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite de saques atingido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor excede o limite por saque.")
    elif valor <= 0:
        print("Valor inválido.")
    else:
        saldo -= valor
        extrato.append((datetime.now(), f"Saque: -R${valor:.2f}"))
        numero_saques += 1
        print("Saque realizado.")
    return saldo, extrato, numero_saques

# Exibe extrato da conta (saldo por posição, extrato por nome)
def extrato_bancario(saldo, /, *, extrato):
    print("\nEXTRATO")
    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for data, descricao in extrato:
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {descricao}")
    print(f"Saldo atual: R${saldo:.2f}\n")

# Seleciona uma conta pelo número
def selecionar_conta():
    try:
        numero = int(input("Número da conta: "))
        conta = next((c for c in contas if c['numero'] == numero), None)
        if not conta:
            print("Conta não encontrada.")
        return conta
    except ValueError:
        print("Entrada inválida.")
        return None

# Menu principal
def menu():
    print("\nMENU BANCÁRIO")
    print("1. Criar usuário")
    print("2. Criar conta corrente")
    print("3. Listar contas")
    print("4. Depositar")
    print("5. Sacar")
    print("6. Ver extrato")
    print("7. Sair")

# Loop principal do sistema
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            criar_conta()
        elif opcao == '3':
            listar_contas()
        elif opcao == '4':
            conta = selecionar_conta()
            if conta:
                try:
                    valor = float(input("Valor para depósito: R$"))
                    conta['saldo'], conta['extrato'] = deposito(
                        conta['saldo'], valor, conta['extrato']
                    )
                except ValueError:
                    print("Entrada inválida.")
        elif opcao == '5':
            conta = selecionar_conta()
            if conta:
                try:
                    valor = float(input("Valor para saque: R$"))
                    conta['saldo'], conta['extrato'], conta['numero_saques'] = saque(
                        saldo=conta['saldo'],
                        valor=valor,
                        extrato=conta['extrato'],
                        limite=conta['limite'],
                        numero_saques=conta['numero_saques'],
                        limite_saques=conta['limite_saques']
                    )
                except ValueError:
                    print("Entrada inválida.")
        elif opcao == '6':
            conta = selecionar_conta()
            if conta:
                extrato_bancario(conta['saldo'], extrato=conta['extrato'])
        elif opcao == '7':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
