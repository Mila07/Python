fruits = ['Яблоко', 'Банан', 'Киви', 'Виноград', 'Груша',]
last_name = len(fruits)
i = 0
for i in range(last_name):

    print(str(i + 1) + '.' + '{: >10}'.format(fruits[i]))