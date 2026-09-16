import random
guess_count = 0
lucky_number = random.randint (1, 10)

while guess_count < 3 :
    guess = int(input("Guess a number between 1 to 10:"))
    guess_count += 1

    if guess == lucky_number:
       print("Wow you are a good guesser aren't you?")
       break
else:
    print(f"Sorry luh twan :( .The lucky number was {lucky_number}!")
