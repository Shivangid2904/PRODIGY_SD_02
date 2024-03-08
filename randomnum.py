import random

number = random.randint(1, 100)
guesses = 0

while True:
  guess_str = input("Guess a number between 1 and 100: ")
  
  try:
    guess = int(guess_str)
  except ValueError:
    print("Invalid input. Please enter an integer.")
    continue
  guesses += 1

  if guess == number:
    print("Congratulations! You guessed the number in", guesses, "attempts.")
    break
  elif guess < number:
    print("Too low, try again.")
  else:
    print("Too high, try again.")

print("The number was", number)
