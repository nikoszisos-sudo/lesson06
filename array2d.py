array = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

for i in range(0, rows):
    array.append([])
    for j in range(0, cols):
        element = int(input("Enter element for  " + str(i) + " row and " + str(j) + " column: "))
        array[i].append(element)
print(array)
