hidden_cards = [1,2,3,3,2,4,1,4]
N = 8
cards_state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]

active_game = True
while active_game:
    card1 = int(input("Pick first card (from 0-7): "))
    while card1 < 0 or card1 > 7 or cards_state[card1] == "opened":
        card1 = int(input("Out of bounds or card opened! Pick first card (from 0-7): "))
    card2 = int(input("Pick second card (from 0-7): "))
    while card2 < 0 or card2 > 7 or cards_state[card2] == "opened" or card2 == card1:
        card2 = int(input("Out of bounds or card opened or already opened! Pick second card (from 0-7): "))
    cards_state[card1] = "temp_opened"
    cards_state[card2] = "temp_opened"

    for position in range(N):
        if cards_state[position] == "closed":
            print("_", end=" ")
        elif cards_state[position] == "opened":
            print(hidden_cards[position], end=" ")
        else:
            print(hidden_cards[position], end=" ")


    active_game = False