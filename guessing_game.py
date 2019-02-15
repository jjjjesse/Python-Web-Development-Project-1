"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

from random import randint

def validate_input(prompt):
    try:
      output = int(input(prompt))
      
      if (output <= 10 and output >= 1):
        return output
      else:
        return validate_input("Number must be inbetween 1 and 10\nGuess again:   ")
    except:
       return validate_input("Please enter a valid number:   ")

def guess_number(solution):
  guess = validate_input("\nGuess a number between 1 and 10:   ")
  guess_count = 0
  
  
  while(True):
    guess_count += 1
    if (guess == solution):
      break
    elif(guess > solution):
      guess = validate_input("It's lower, try again:   ")
    elif (guess < solution):
      guess = validate_input("It's higher, try again:   ")
  print("You got it! It took you {} tries".format(guess_count))
  return guess_count

def play_again():
  again = input("Would you like to play again? (y/n):   ")
  while(True): 
    if (again == 'y'):
      return True
    if (again == 'n'):
      return False
    else:
      again = input("Please enter 'y' or 'n':   ")
      
      
  
  

def start_game():
  print(
'''
-------------------------------------
         ~ Welcome to the ~
N U M B E R  G U E S S I N G  G A M E
-------------------------------------
'''
  )
  highscore = 0
  while(True):
    if (highscore != 0):
        print("The current highscore is: ", highscore)
    solution = randint(1, 10)
    
    guess_count = guess_number(solution)
    
    if (guess_count < highscore or highscore == 0):
      highscore = guess_count
      print("You've made a new high score!")
    if (not play_again()):
      break
  print("Thank you for playing! Goodbye")
        


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
