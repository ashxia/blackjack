import random
from art import logo
from replit import clear


def deal_card():
  # returns a random card from the deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  choice = random.choice(cards)
  return choice


def calculate_score(list):
  #a function to calculate score for a given list
  total = sum(list)
  if total == 21:
    return 0
  if total > 21 and 11 in list:
    list.remove(11)
    list.append(1)
  return total


def compare(user_score, computer_score):
#function to compare scores
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

play = True
def play_game():
  #print logo
  print(logo)
  #create an empty list for user cards andy computer cards
  user_cards = []
  computer_cards = []

  #distribut cards to players by randomly picking from a deck of cards
  for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())

  #print user and computer choice to give the chance for the user to decide



  #a loop to ask the user if they need more cards
  game_over = False
  while not game_over:
    #calculate scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your cards are {user_cards}")
    print(f"the computer cards are {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score>21:
      game_over = True
    else:
      contin = input("would you like to have another card?")
      if contin == "y":
        user_cards.append(deal_card())
      else:
        game_over = True

  #loop to give the computer cards while <17
  while computer_score !=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    


  result = compare(user_score, computer_score)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
play = True
while input("do you wanna play a game of black jack? please press 'y' for yes or 'n' for no") == "y":
    clear() 
    play_game() 


