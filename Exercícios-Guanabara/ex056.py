# Programa que leia o nome, idade e sexo de 4 pessoas:
# Depois mostre: A média de idade do grupo, o nome do homem mais velho e quantas mulheres abaixo de 20 anos.

idadeHvelho = soma = contM20 = 0
nomeHvelho = ''
for c in range(1, 5):
    print(f'\n{c}° PESSOA')
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    soma += idade
    if c == 1 and sexo == 'M':
        idadeHvelho = idade
        nomeHvelho = nome
    elif c != 1 and sexo == 'M':
        if idade > idadeHvelho:
            idadeHvelho = idade
            nomeHvelho = nome
    elif sexo == 'F' and idade < 20:
        contM20 += 1
media = soma / 4
print(f'\nA média de idade do grupo é {media:.0f} anos')
print(f'O nome do homem mais velho do grupo é o {nomeHvelho}. Ele tem {idadeHvelho} anos de idade.')
print(f'E temos neste grupo {contM20} mulher(es) abaixo de 20 anos.')
