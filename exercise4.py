list1 = []
tuple1 = ()
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list1.append(i)
tuple1 = tuple(list1)
print(tuple1)