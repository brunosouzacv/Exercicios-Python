peso = float(input('Digite seu peso em kg:'))
alt = float(input('Digite sua altura em metros:'))
imc = peso / (alt * alt)
print('O valor de seu IMC é {:.1f}.'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está em sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida')