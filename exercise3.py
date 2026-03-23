N = int(input("Δώσε ένα πρώτο αριθμό: "))
while N <= 1:
    N = int(input("Προσοχή. Πρέπει να είναι μεγαλύτερος απο το 1: "))
for i in range(2, N):
    if N % i == 0:
     print("Δεν είναι πρώτος.")
     break
else:
    print("Είναι πρώτος.")

