#βαζω μια λιστα με 8 αριθμους, μια μεταβλητη Ν=8 και μια λιστα με 8 τιμες στρινγκ ολες με κατασταση κλειστη

hidden_cards = [1,2,3,3,2,4,1,4]
N = 8

cards_state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]

# οριζω ολο τον κωδικα μεσα σε μια boolean=true. αμυντικος προγραμματισμος
# για τα ορια μεταξυ 0 και 7 + οχι κατασταση opened + οχι 2 ιδιες καρτες
# οι καρτες θα γινουν απο closed σε temp opened.

active_game = True
found = 0
score = 0
while active_game:
    card1 = int(input("Pick first card (from 0-7): "))
    while card1 < 0 or card1 > 7 or cards_state[card1] == "opened":
        card1 = int(input("Out of bounds or card opened! Pick first card (from 0-7): "))
    card2 = int(input("Pick second card (from 0-7): "))
    while card2 < 0 or card2 > 7 or cards_state[card2] == "opened" or card2 == card1:
        card2 = int(input("Out of bounds or card opened or already opened! Pick second card (from 0-7): "))
    cards_state[card1] = "temp_opened"
    cards_state[card2] = "temp_opened"

    # για ολες τις 8 θεσεις (Ν=8) αν η θεση που εξεταζω στη λιστα cards_state
    print()
    for position in range(N):
        if cards_state[position] == "closed":
            print("_", end=" ")
        elif cards_state[position] == "opened":
            print(hidden_cards[position], end=" ")
        else:
            print(hidden_cards[position], end=" ")
    print()

#αν η πρωτη με τη δευτερη καρτα ειναι ιδιες η κατασταση γινεται ανοιχτη αλλιως κλειστη

    if hidden_cards[card1] == hidden_cards[card2]:
        cards_state[card1] = "opened"
        cards_state[card2] = "opened"
        found += 2
        score += 1
        print("Success!")
        print("Score: " + str(score))
    else:
        cards_state[card1] = "closed"
        cards_state[card2] = "closed"
        print("Failure!")

    print()
    for position in range(N):
        if cards_state[position] == "closed":
            print("_", end=" ")
        elif cards_state[position] == "opened":
            print(hidden_cards[position], end=" ")
        else:
            print(hidden_cards[position], end=" ")
    print()

    if found == N:
        print ("Bravo! Game Over! Score = " + str(score))
        active_game = False
