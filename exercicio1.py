user = input('Digite um usuário para cadastro: ')
passwd = input('Digite a senha para o usuário: ')

print(
'''
Os exames disponíveis na ala são:
Exame A | 120 min | R$ 500
Exame B | 500 min | R$ 300
'''
)

print('''
Temos as seguintes opções:
1 - Agendar um exame 
2 - Remover um exame a
3 - Encerrar o sistema
''')
tempo_tot = 0
custo_tot = 0
qntd = 0

while True:
    opcao = input('Digite o que você deseja (1, 2 ou 3): ')
    if opcao == '1' or opcao == '2':
        exame = input('Qual exame você deseja escolher: ')

        if exame =='A':
            custo = 500
            tempo = 120
        elif exame =='B':
            custo = 300
            tempo = 600

    if opcao == '1':
        if tempo_tot+tempo <= 8*60:
            tempo_tot += tempo
            custo_tot += custo
            qntd += 1
            print('Exame adicionado com sucesso!')
            print(f'O tempo total ds exames é: {tempo_tot}')
        else:
            print('Não possível adicionar mais exames!')
        #agendamento

    elif opcao == '2':
        user_check = input('Digite o usuário cadastrado: ')
        passwd_check = input('Digite a senha cadastrada: ')

        if user_check == user and passwd_check == passwd:
            print('Usuário e senha válidos')
            tempo_tot -= tempo
            custo_tot -= custo
            qntd -= 1
        else:
            print('Usuário e senha inválidos')
        #remocao

    elif opcao == '3':
        print('Encerrando o sistema!')
        break
    else:
        print('Opção inválida')

print(f'O custo total dos exames é: {custo_tot}')
print(f'O tempo total ds exames é: {tempo_tot}')
print(f'A quantidade total dos exames é: {qntd}')
