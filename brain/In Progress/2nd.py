#first test of rps bot

import random

def results(num, number):
    #find the difference in the two numbers
    difference = num - number
    #if/elif statement
    if difference == 0:
        ties += 1
        print("TIE!")
        #call restart
        #restart()
    elif difference % 3 == 1:
        ties += 1
        print("I'm sorry! You lost :(")
        #call restart
        #restart()
    elif difference % 3 == 2:
        wins += 1
        print("Congratulations! You won :)")
        #call restart
        #restart()

def computer_number():
  #get a random number in the range of 1 through 3
  num = random.randrange(1,4)
  #if/elif statement
  if num == 1:
    print("Computer chooses rock")
  elif num == 2:
    print("Computer chooses paper")
  elif num == 3:
    print("Computer chooses scissors")
  #return the number
  return num

def user_guess():
  #get the user's guess
  guess = raw_input("Choose 'rock', 'paper', or 'scissors' by typing that word. ")
  if is_valid_guess(guess):
    #if/elif statement
    #assign 1 to rock
    if guess == 'rock':
      number = 1
      #assign 2 to paper
    elif guess == 'paper':
      number = 2
    #assign 3 to scissors
    elif guess == 'scissors':
      number = 3
    print "user chooses " + guess
    return number
  else:
      print('That response is invalid.')
      user_guess()

def is_valid_guess(guess):
    
  if guess == 'rock' or guess == 'paper' or guess == 'scissors':
    status = True
  else:
    status = False
  return status

def restart():
  answer = raw_input("Would you like to play again? Enter 'y' for yes or \
  'n' for no: ")
  #if/elif statement
  if answer == 'y':
      main()
  elif answer == 'n':
      print("Goodbye!")
  else:
      print("Please enter only 'y' or 'n'!")
      #call restart
      restart()

def main():
  #intro message
  ties = 0
  wins = 0
  losses = 0
  print("Let's play 'Rock, Paper, Scissors'!")
  
  user_choice = user_guess()
  computer_choice = computer_number()
  #print str(user_choice) + " " + str(computer_choice)
  results(computer_choice, user_choice)
  restart()

main()
