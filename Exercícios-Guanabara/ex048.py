# A soma entre os números ímpares, multiplos de 3, no intervalo de 1 até 500
soma = 0
multiplos = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        multiplos += 1
print(f'A soma dos {multiplos} números impares, múltiplos de três, neste intervalo é de {soma}.')
