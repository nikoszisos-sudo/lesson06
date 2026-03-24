array = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
array.insert(0, [0,0,0,0])
print(array)
array.append([1,1,1,1])
print(array)

for row in array:
    for element in row:
        print(element, end=" ")
    print()
