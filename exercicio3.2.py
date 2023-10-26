n = 141846
while n > 9:
    sd = sum(int(i) for i in str (n))
    n = sd

print(sd)

j1 = input('Jogador 1, par ou impar: ')

if j1 =='par':
    j2='impar'
else:
    j2='par'

nj1 = int(input('Qual número jogado: '))
nj2 = sd
resultado = nj1 = nj2

if resultado%2 == 0:
    a = 'par'
else:
    a = 'impar'

if j1==a:
    print('jogador 1 venceu!')
else:
    print('jogador 1 perdeu.')
