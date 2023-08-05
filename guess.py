import random as rand


a = int(input("Guess from: "))
b = int(input("Guess to: "))
num = rand.randint(a, b)

while True:
    guess = int(input("Guess number: "))
    if guess == num:
        print("YOU GUESSED IT!!")
        break
    elif guess > num:
        print("too high")
    elif guess < num:
        print("too low")

