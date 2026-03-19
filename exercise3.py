N = int(input("Δώσε ένα πρώτο αριθμό: "))
while N <= 1:
    N = int(input("Προσοχή. Πρέπει να είναι μεγαλύτερος απο το 1: "))
    for i in range(N):
        if (N % N == 0 and N % 1 == 0 and N % 2 !=0 and N % (N-1) !=0) or (N == 2):
            print("Σωστά! Είναι πρώτος.")
else:
    print("Δεν είναι πρώτος.")

