#Guessing game

secret = 7

guess = int(input("Guess the number: "))

while guess != secret:

    if guess > secret:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Guess again: "))

print("Correct!")