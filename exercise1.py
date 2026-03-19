my_list = []
print ("Δώσε 10 αριθμούς απο το 10 ως 20: ")
for i in range(10):
    x = int(input("Δώσε τον " + str(i+1) + "ο ακέραιο: "))
    while x < 10 or x > 20:
        x = int(input("Δώσε τον " + str(i+1) + "ο ακέραιο: "))
    my_list.append(x)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
my_list.sort()
my_tuple2 = tuple(my_list)
print(my_tuple2)
squared_list = []
for x in range(10):
    squared_list.append(my_list[x]**2)
squared_tuple = tuple(squared_list)
print(squared_tuple)
