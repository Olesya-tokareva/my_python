k=int(input('До скольки знаков округлять? '))
import math
def pi_number(k):
    return f'{round(math.pi,k)}'
print(pi_number(k))
