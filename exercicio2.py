

n = int(input('Diga o valor de quantos termos você quer somar: '))
seq1 = 0
seq2 = 1
i = 0
soma = 0

print(0)
print(1)
while i < (n-2):
    fibo = seq1 + seq2
    seq1 = seq2
    seq2 = fibo

    soma += fibo
    print(f'valor na sequencia:{fibo} e soma {soma}')

    i+= 1

numero = soma +1
print(f'O resultado final {numero}')
