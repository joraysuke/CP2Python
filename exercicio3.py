n = 123456
#soma = str(n)
soma_alg = 0
i = 0
b = n
while True:
    soma = str(b)

    if b < 10:
        break
    while i < len(soma):
        soma_alg += int(soma[i])
        i += 1
    b = soma_alg
    i = 0
    soma_alg = 0
    print(b)
print(soma_alg)
