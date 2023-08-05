import random as rand

low = int(input("Guess from: "))
high = int(input("Guess to: "))

number = int(
    input(f"Now pick a number from {low} to {high} for the computer to guess: ")
)

guess = rand.randint(low, high)

while guess != number:
    print(f"The computer guessed {guess}")
    if guess > number:
        print("Guess was too high")
        high = guess - 1
        guess = rand.randint(low, high)
    elif guess < number:
        print("Guess was too low")
        low = guess + 1
        guess = rand.randint(low, high)

print(f"The computer guessed {guess} correctly!")
