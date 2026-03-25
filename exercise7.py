hidden_cards = [1,2,3,3,2,4,1,4]
N = 8
cards_state = ["closed", "closed", "closed", "closed", "closed", "closed", "closed", "closed"]

active_game = True
while active_game:
    card1 = int(input("Pick first card (from 0-7): "))
    while card1 < 0 or card1 > 7:
        card1 = int(input("Pick first card (from 0-7): "))
    card2 = int(input("Pick second card (from 0-7): "))
    while card2 < 0 or card2 > 7:
        card2 = int(input("Pick second card (from 0-7): "))

