my_list = []
print ("Δώσε 10 αριθμούς απο το 10 ως 20: ")
for i in range(1, 11, 1):
    x = int(input("Δώσε τον " + str(i) + "ο ακέραιο: "))
    while x < 10 or x > 20:
        x = int(input("Δώσε τον " + str(i) + "ο ακέραιο: "))
    my_list.append(x)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
my_tuple2 = tuple(my_list)
print(my_tuple2.sort)