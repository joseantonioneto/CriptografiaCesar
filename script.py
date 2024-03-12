texto = input('Digite o texto que deseja criptografar: ')
distancia = int(input('Digite a distância que deseja usar: '))
cripto = ''

for letra in texto:
    numero = ord(letra)
    numero = numero + distancia
    letra = chr(numero)
    cripto = cripto + letra

print ('O texto criptografado é: ' + cripto)