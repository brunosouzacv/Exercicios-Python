import math
a = float(input('Digite um ângulo:'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O valor do seno é {:.2f}.\nO valor do cosseno é {:.2f}.\nO valor da tangente é {:.2f}.'.format(sen, cos, tan))