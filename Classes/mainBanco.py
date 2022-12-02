from Banco import SenaiBank

nome = input(f'\033[1;97mOlá\nDigite seu nome:\n')
idade = input(f'Insira sua idade:\n')
cpf = input(f'Insira seu CPF:\n\033[0;0m')

conta = SenaiBank(nome=nome, cpf=cpf, idade=idade)

# print(f'Olá {conta.nome}, você possui R${conta.saldo} em sua conta.')

while True:
    menu = input(f'\033[1;36mBEM VINDO {conta.nome}, O QUE DESEJA?\n'
                 f'[1] - Ver Saldo\n'
                 f'[2] - Sacar\n'
                 f'[3] - Depositar\n'
                 f'[4] - Transferir\n'
                 f'[5] - Ver extrato\n\nOPÇÃO: ')
    if menu == '1':
        print(f'\033[1;31mSaldo atual: {conta.extrato()} \033[1;33m- CC\033[0;0m')
        voltar = input(f'\033[1;35mVoltar ao menu inicial? [S] [N]\033[0;0m').lower()
        if voltar == 's':
            pass
        else:
            break
    if menu == '2':
        saque = float(input('\033[1;97mDigite o valor que deseja sacar:\n\033[0;0m'))
        if conta.sacar(valor_sacar=saque):
            print(f'\033[1;32mSaque efetivado com sucesso!\n\033[1;97mSaldo atual: {conta.efetivar_saque(valor_sacar=saque)} - CC\033[0;0m')
        else:
            print(f'\033[1;31mValor além do seu saldo.\n\033[1;97mSaldo atual: {conta.extrato()} \033[1;33m- CC\033[0;0m')

        voltar = input(f'\033[1;35mVoltar ao menu inicial? [S] [N]\033[0;0m').lower()
        if voltar == 's':
            pass
        else:
            break
    if menu == '3':
        deposito = float(input('\033[1;97mDigite o valor que deseja depositar:\n\033[0;0m'))
        saldoAtual = conta.depositar(valor_depositar = deposito)
        print(f'\033[1;97mSaldo atual: {saldoAtual} \033[1;33m- CC\033[0;0m')

        voltar = input(f'\033[1;35mVoltar ao menu inicial? [S] [N] \033[0;0m').lower()
        if voltar == 's':
            pass
        else:
            break
    if menu == '4':
        print(f'\033[1;97mSaldo atual: {conta.extrato()} - CC\033[0;0m')
        transferencia = float(input('\033[1;97mDigite o valor que deseja transferir:\n\033[0;0m'))
        saldoAtual = conta.transferir(valor_transf=transferencia)
        destinatario = input(f'\033[1;36m[1] - Transferência para sua Conta Poupança\n'
                             f'[2] - Tranferência para outra \n\n'
                             f'OPÇÃO: \033[0;0m')
        if destinatario == '1':
            saldoAtual = conta.transferir(valor_transf=transferencia)
            saldoP = conta.tranfP(valor_transf=transferencia)
            print(f'\033[1;97mSaldo atual: {saldoP} \033[1;33m- CP\033[0;0m')
            print(f'\033[1;97mSaldo atual: {saldoAtual} \033[1;33m- CC')

        elif destinatario == '2':
            saldoAtual = conta.transferir(valor_transf=transferencia)
            contaDest = input('\033[1;97mInsira a conta que deseja transferir:\n\033[0;0m')
            print(f'\033[1;32mTransferência realizada com sucesso!\033[0;0m')
            print(f'\033[1;97mSaldo atual: {saldoAtual} \033[1;33m- CC')

        voltar = input(f'\033[1;35mVoltar ao menu inicial? [S] [N] \033[0;0m').lower()
        if voltar == 's':
            pass
        else:
            break



