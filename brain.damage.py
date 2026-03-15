my_list = [1, 2, 3]
my_new_list = ((my_list * 2)[1:5] + list((7, 8)))*4
print("Η αρχική λίστα: " + str(my_list))
print("Η λίστα με τις πράξεις: " + str(my_new_list))
print("Πλήθος των 2 απο λίστα και λίστα με πράξεις μαζί: " + str((my_list+my_new_list).count(2)))
