menu = """
    [d]depositar 
    [s]Sacar f
    [e]Extrato 
    [q]Sair

"""



saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    op = input(menu)

    if op == "d":
        print('Deposito')
        deposito = int(input(" ditite o valor que deseja depositar. R$  "))
        print('deposito realizado com sucesso!')
        
        if deposito > 0:
            saldo += deposito 
            extrato += f"deposito: R$ {deposito:.2f}"
        else:
            print('valor de deposito invalido , tente novamente')

    elif op == "s":
        print('Saque')
        if saldo > deposito:
            print('Não ha saldo sufuciente . ')
        elif deposito > limite:
            print('Limite exedido ')
        elif numero_saque > LIMITE_SAQUE:
            print('Limite de saque exedido< tente novamente outro dia. ')
        elif deposito > 0:
            saldo += deposito
            extrato += f'Saque: R$ {deposito:.2f}'
            numero_saque += 1
        else:
            print('valor invalido , tente novamente. ')

    elif op == "e":
        print('Extrato')
        print(f"Saldo: R$ {saldo:.2f} ")

    elif op == 'q':
        break
    else:
        print('Opção,invalida')


        

