import random
n = int(input('Введите количество случайных элементов в списке: '))
my_list = []
for el in range(n):
    my_list.append(random.randint(-100, 100))
print(my_list)