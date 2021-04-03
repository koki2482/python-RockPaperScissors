#Import Random Module
import random

while True:
    
  #Create A Variable Named user_action and store user information
  user_action = input("Enter a choice (r, p, s): ")


  possible_actions = ["r", "p", "s"] #Create An Array With 3 Values
  computer_action = random.choice(possible_actions) # Computer Picks 1 Of The Options Randomly


  # Pring Current Status of Both players
  print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

  #Conditions To Determing Winnder
  if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
      
  elif user_action == "r":
    if computer_action == "s":
      print("rock smashes scissors! You win!")
    else:
          print("paper covers rock! You lose.")

  elif user_action == "p":
      if computer_action == "r":
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif user_action == "s":
      if computer_action == "p":
          print("Scissors cuts paper! You win!")
      else:
          print("Rock smashes scissors! You lose.")
          
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break

          