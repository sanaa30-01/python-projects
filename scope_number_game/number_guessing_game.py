from ascii import ascii_art
import random

#welcome message and ascii art

print(ascii_art)
print("Welcome to the Number Guessing Game!")

#picking a random number from 1 to 100

chosen_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

#program for difficulty 

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if chosen_difficulty == "easy":
    attempts = 10
elif chosen_difficulty == "hard":
    attempt = 5

#game loop

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        break
    
    if guess < chosen_number:
        print("Too low.")
        print("Guess again.")
    elif guess > chosen_number:
        print("Too high.")
        print("Guess again.")
    
    attempts -= 1

    if attempts == 0:
        print("You've run out of guesses. Refresh the page to play again.")




