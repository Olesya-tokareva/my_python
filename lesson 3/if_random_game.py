import random
n=random.randint(1,4)
p=int(input('Угадай число!'))
if p==n:
    print('Ты угадала! Это', n)
else: print('Попробуй еще раз :(')
