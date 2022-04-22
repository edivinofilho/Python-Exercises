# Programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso incorreto, repita a pergunta.

sexo = str(input('Digite seu sexo [M/F]: '))
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo [M/F]: '))
print('Dado cadastrado com sucesso.')
