#  a)
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = set(lst)
print(lst2)
#  б)
lst2 = []
for item in lst:
    if lst.count(item) == 1:
        lst2.append(item)
print(lst2)