import random
number_to_guess = random.randint(1,9)
guess = int(input("Guess a number between 1 and 9:"))
if guess < number_to_guess:
    print ("Your guess was too low.")
elif guess > number_to_guess:
    print ("Your guess was too high.")
else:
    print ("Your guess was correct!")