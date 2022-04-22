# Leia o peso de 5 pessoas, no final mostre qual foi o maior e o menor peso lido.

maior = menor = 0
for c in range(1, 6):
    print(f'{c}° Pessoa')
    peso = float(input('Digite seu peso em kg: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso registrado foi de {maior}kg')
print(f'E o menor peso registrado foi de {menor}kg')
