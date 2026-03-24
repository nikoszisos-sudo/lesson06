array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
array.insert(0, [0,0,0,0])

for row in array:
    for element in row:
        print(element, end=" ")
    print()

for row in array:
    row.append(1)
    for element in row:
        print(element, end=" ")
    print()

for row in array:
    row.insert(0, 99)
    for element in row:
        print(element, end=" ")
    print()
