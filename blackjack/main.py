# Main assumptions:
# - Infinite card deck
# - Ace is 11, J, K, Q - are 10
# - But when Ace is drawn and the total goes over 21, count the Ace as 1 instead
# - Player knows only first card of dealer
# - If player has more than 21 or computer delear has blackjack, game will be immediately break and delear win

import random
from os import system
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_game_and_print_results(dealer_cards, user_cards):
    dealer_final_result = sum(dealer_cards)
    user_final_result = sum(user_cards)

    print(f"Your final hand: {user_cards}, final score: {user_final_result}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_final_result}")

    if user_final_result > 21:
        print("You went over. You loose")
    elif dealer_final_result > 21:
        print("Opponent went over. You win")
    else:
        if len(dealer_cards) == 2 and dealer_final_result == 21:
            print("Lose, opponent has Blackjack")
        elif len(user_cards) == 2 and user_final_result == 21:
            print("Win with a Blackjack")
        elif user_final_result == dealer_final_result:
            print("Draw")
        elif user_final_result < dealer_final_result:
            print("You lose")
        else:
            print("You win")   

def handle_drawn_and_get_next_card(current_cards):
   next_card = random.choice(cards)
   if next_card == 11 and sum(current_cards) + next_card > 21:
      return 1
   else:
      return next_card


def get_dealer_game():
    dealer_cards = []
    for i in range(2):
       dealer_cards.append(handle_drawn_and_get_next_card(dealer_cards))
    while sum(dealer_cards) < 16:
        dealer_cards.append(handle_drawn_and_get_next_card(dealer_cards))
    return dealer_cards

def start_the_game():
    continue_the_game = True

    dealer_cards = get_dealer_game()
    user_cards = []
    for i in range(2):
       user_cards.append(handle_drawn_and_get_next_card(user_cards))

    while continue_the_game and not sum(user_cards) >= 21:
      print(f"You cards: {user_cards}, current score: {sum(user_cards)}")
      print(f"Computer's first card: {dealer_cards[0]}")

      user_take_another_card = input("Type 'y' to get another card, type anything else to pass: ")

      if user_take_another_card != "y":
          continue_the_game = False
      else:
          user_cards.append(handle_drawn_and_get_next_card(user_cards))

    calculate_game_and_print_results(dealer_cards, user_cards)

while True:
  should_start_the_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if should_start_the_game == "y":
    system("clear|cls")
    print(logo)
    start_the_game()
  else:
     break