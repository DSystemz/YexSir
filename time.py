import time
horario = time.ctime()
a = horario
frmt = a[11:16]
print(frmt)
hs = str(input('Digite o horário (H:M) ==> '))
if frmt == hs:
    print('Ok! Deu certo!')
else:
    print('Ops, algo deu errado.')