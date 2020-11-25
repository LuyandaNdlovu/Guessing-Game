from random import randint

num = randint(1,100)

print("This is a guessing game. \nThe computer will pick a number between 1 and 100.\nYour task is to try and guess what that number is, in as little guesses as possible. \nThe rules are simple: \n1. You have an unlimited number of guesses. \n2. Any guesses below 1 and greater than 100 are considered out of bounds.\n\n")

guesses =[0]

while  True :
    guess = int(input("What is your guess??: "))

    if 1 > guess or guess > 100 :
        print("OUT OF BOUNDS!!\nTry again.\n")
        continue

    break


while  True :
    guess = int(input("What is your guess??: "))

    if guess == num:
        print(f"Well done! You've guessed the correct number. You only guessed it in {len(guesses)} guesses.")
    break

guesses.append(guess)

if guesses[-2]:
    if abs(num - guess) < abs(num - guesses[-2]):
        print("WARMER")
    else:
        print("COLDER")

else:

    if abs(num - guess) <=10:
        print("WARM")
    else:
        print("COLD")

        


