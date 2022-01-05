m = float(input('Digite uma distância em metros:'))
cm = m*100
mm = m*1000
km = m/1000
dm = m/10
um = m/1000000
nm = m/1000000000
print('A distância em metros é {}.\nEm centímetros é {}.\nEm milímetros é {}.\nEm quilômetros é {}.\nEm decímetros é {}.\nEm micrômetro é {}.\nEm nanômetro é {}.'.format(m, cm, mm, km, dm, um, nm))
