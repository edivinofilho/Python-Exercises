# A frase é PALÍNDROMO?

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
inverso = ''
for letras in range(len(junta)-1, -1, -1):
    inverso += junta[letras]
if inverso == junta:
    print(f'\nO contrário de {junta} é {inverso}')
    print('Temos um PALÍNDROMO!')
else:
    print('NÃO temos um PALÍNDROMO!')
