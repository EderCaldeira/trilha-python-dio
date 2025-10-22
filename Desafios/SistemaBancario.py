
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar usuário
[b] Cadastrar conta bancária
[q] Sair
=> """

saldo = 150
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0
    
nomes = []
datas_nascimento = []
cpfs = []
enderecos = []
contas_bancarias = []


def depositar(saldo, valor, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

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

    else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar():
    cpf_input = input("Informe o CPF (somente número): ")
    if cpf_input in cpfs:
        print("Já existe usuário com esse CPF!")
        return
    nome_input = input("Informe o nome completo: ")
    data_input = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco_input = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    nomes.append(nome_input)
    datas_nascimento.append(data_input)
    cpfs.append(cpf_input)
    enderecos.append(endereco_input)
    print("Usuário cadastrado com sucesso!")
        
def cadastrarContas():
    cpf_input = input("Informe o CPF do titular: ")
    if not cpf_input:
            print("Usuário não encontrado, por favor cadastre um usuário antes de criar uma conta.")
            return
        
    if cpf_input not in cpfs:
        print("CPF não encontrado, por favor verifique os dados e tente novamente.")
        return

    titular_index = cpfs.index(cpf_input)
    numero_conta = len(contas_bancarias) + 1
    contas_bancarias.append({
        "Agência": "0001",
        "Número da conta": f"{numero_conta:04d}",
        "Titular": nomes[titular_index]
        })
    print("Conta criada com sucesso!")

while True:

    opcao = input(menu).strip().lower()
        
    if opcao == "d":
        depositar(saldo, valor, extrato)
    elif opcao == "s":
        sacar( valor, extrato, limite, numero_saques, LIMITE_SAQUES)
    elif opcao == "e":
        extrato(saldo, extrato)
    elif opcao == "c":
        cadastrar()
    elif opcao == "b":
        cadastrarContas()
    elif opcao == "q":
        break
    else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


