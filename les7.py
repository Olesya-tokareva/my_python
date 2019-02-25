total=0
while True:
    a=input('Вводите числа. Чтобы закончить, напишите:"стоп". ')
    if a.upper()=='СТОП':
        break
    else:
        if a.isdigit():
            total+=int(a)
        else:
            print('Ошибка ввода')
print(total)
