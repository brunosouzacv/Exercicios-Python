c = float(input('Digite uma temperatura em grau celsius ºC:'))
f = (c * 9/5 + 32)
k = (c + 273.15)
print('A temperatura {}ºC convertida para Fahrenheit e Kelvin será, respectivamente, {}ºF e {}K.'.format(c, f, k))