import math

my_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for item in my_list:
    if item > 0 and math.sqrt(item) % 1 == 0:
        new_list.append(int(math.sqrt(item)))
print(new_list)