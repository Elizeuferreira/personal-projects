import random

magic_num = random.randint(1,100)
guess = -1

while guess != magic_num:
    guess = int(input("What is your guess? "))

    if guess < magic_num:
        print("Higher")
    elif guess > magic_num:
        print("Lower")
    else:
        print("You guessed it!")