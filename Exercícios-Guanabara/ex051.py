# Leia o primeiro termo de uma Progressão Aritimética (P.A.) e a sua razão. Mostre os 10 primeiros termos

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
print(f'{primeiro}', end=' → ')
for c in range(1, 10):
    primeiro += razao
    print(f'{primeiro}', end=' → ')
print('FIM')
