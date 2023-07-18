print('\033[1;34;40mSeja Bem Vindo a Sorveteria do Vitor Renan!\033[m')
print('-'*35, 'Cardápio', '-'*36, '|',
      '\n| Nº de Bolas | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |\n'
      '|      1      |         R$ 6,00        |       R$ 7,00      |       R$ 8,00       | \n'
      '|      2      |        R$ 10,00        |      R$ 12,00      |       R$ 14,00      |\n'
      '|      3      |        R$ 14,00        |      R$ 17,00      |       R$ 20,00      |\n'
      '|', '-'*34, 'Cardápio', '-'*35, '|')

total_a_pagar = 0  # Variável para armazenar o valor total a ser pago

while True:
    s = str(input('\nEscolha o sabor desejado: ')).strip().lower()
    if s not in ['tr', 'pr', 'es']:
        print('Sabor inválido. Tente novamente, por favor!')
        continue
    qt = int(input('\nEscolha a quantidade de bolas desejadas: '))
    if qt not in [1, 2, 3]:
        print('Quantidade inválida. Tente novamente, por favor!')
    else:
        if s == 'tr' or s == 'sabor tradicional':
            valor_sabor = 4*(qt-1) + 6
        elif s == 'pr' or s == 'sabor premium':
            valor_sabor = 5*(qt-1) + 7
        else:
            valor_sabor = 6*(qt-1) + 8

        total_a_pagar += valor_sabor  # Adiciona o valor do sabor escolhido ao total a pagar

    des = str(input('Deseja mais algum sorvete? Digite sim ou não: ')).strip().lower()
    if des != 'sim' and des != 's':
        break

print(f'O valor total a ser pago foi de: R$ {total_a_pagar}')
