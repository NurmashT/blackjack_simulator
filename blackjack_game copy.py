import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    def deal_card():
        card = random.choice(cards)
        return card

    user_cards = []
    comp_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    
    def calc_score(list_of_cards):
        score = sum(list_of_cards)
        for i in range(2):
            if list_of_cards[i] == 11 and score > 21:
                list_of_cards[i] = 1
                score = sum(list_of_cards)
        if score == 21 and len(list_of_cards) == 2:
            score = 0 # 0 represents a blackjack ==> 21
        return score

    user_score = calc_score(user_cards)
    comp_score = calc_score(comp_cards)

    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_choice == "y":
        print(logo)
        should_continue = True
    else:
        should_continue = False
    while should_continue:
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {comp_cards[0]}")
        print(comp_cards)
        
        if user_score == 0 and comp_score == 0:
            should_continue = False
            print("Draw.")
        elif user_score == 0:
            should_continue = False
            print("You have a Blackjack. You win!")
        elif comp_score == 0:
            should_continue = False
            print("Computer has a Blackjack. You lose.")
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
        
        while hit == "y":
            user_cards.append(deal_card())
            user_score = calc_score(user_cards)
            if user_score > 21:
                should_continue = False
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
                print("You went over. You lose.")
                hit = ""
            elif user_score == 0 and comp_score == 0:
                should_continue = False
                print("Draw.")
                hit = ""
            elif user_score == 0:
                should_continue = False
                print("You have a Blackjack. You win!")
                hit = ""
            elif comp_score == 0:
                should_continue = False
                print("Computer has a Blackjack. You lose.")
                hit = ""
            else:
                print(f"   Your cards: {user_cards}, current score: {user_score}")
                print(f"   Computer's first card: {comp_cards[0]}")
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
        if hit == "n":
            while comp_score < 17:
                comp_cards.append(deal_card())
                comp_score = sum(comp_cards)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
            if comp_score > 21:
                print("Computer went over. You win!")
            if comp_score > user_score:
                print("You lose.")
            elif comp_score == user_score:
                print("Draw.")
            else:
                print("You win!")
            should_continue = False
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        os.system("clear")
        blackjack()
blackjack()